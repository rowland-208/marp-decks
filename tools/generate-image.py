#!/usr/bin/env python3
"""Generate images for Marp decks using OpenRouter's image generation API."""

import base64
import json
import os
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import Request, urlopen

import click
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

OPENROUTER_API_URL = os.environ.get("OPENROUTER_API_URL", "https://openrouter.ai/api/v1/chat/completions")
DEFAULT_MODEL = os.environ.get("OPENROUTER_IMAGE_GEN_MODEL", "google/gemini-3.1-flash-image-preview")


def generate_image(prompt: str, output_path: str) -> None:
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        raise click.ClickException("OPENROUTER_API_KEY environment variable is not set.")

    payload = {
        "model": DEFAULT_MODEL,
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    }
                ],
            }
        ],
    }

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    req = Request(
        OPENROUTER_API_URL,
        data=json.dumps(payload).encode(),
        headers=headers,
        method="POST",
    )

    click.echo(f"Generating image with {DEFAULT_MODEL}...")
    try:
        with urlopen(req, timeout=120) as resp:
            result = json.loads(resp.read().decode())
    except HTTPError as e:
        body = e.read().decode()
        raise click.ClickException(f"API error ({e.code}): {body}")

    content_parts = result["choices"][0]["message"]["content"]
    if isinstance(content_parts, str):
        raise click.ClickException(
            f"Model returned text instead of an image. Try refining your prompt.\nResponse: {content_parts}"
        )

    image_data = None
    for part in content_parts:
        if part.get("type") == "image_url":
            data_url = part["image_url"]["url"]
            _, encoded = data_url.split(",", 1)
            image_data = base64.b64decode(encoded)
            break

    if not image_data:
        raise click.ClickException(
            f"No image found in API response.\nResponse: {json.dumps(result, indent=2)}"
        )

    out = Path(output_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(image_data)
    click.echo(f"Saved image to {out}")


@click.command()
@click.argument("output")
@click.argument("prompt")
def main(output: str, prompt: str) -> None:
    """Generate images for Marp decks via OpenRouter."""
    generate_image(prompt, output)


if __name__ == "__main__":
    main()
