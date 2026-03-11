#!/usr/bin/env python3
"""Remove the background from an image using floodfill from the corners."""

import click
from PIL import Image, ImageDraw


@click.command()
@click.argument("image_path")
@click.option("--thresh", default=40, help="Color distance threshold for floodfill (default: 40).")
@click.option("--output", "-o", default=None, help="Output path. Defaults to overwriting the input file.")
def main(image_path: str, thresh: int, output: str) -> None:
    """Remove white background from an image via corner floodfill."""
    img = Image.open(image_path).convert("RGBA")

    corners = [
        (0, 0),
        (img.width - 1, 0),
        (0, img.height - 1),
        (img.width - 1, img.height - 1),
    ]
    for seed in corners:
        ImageDraw.floodfill(img, seed, (0, 0, 0, 0), thresh=thresh)

    out = output or image_path
    img.save(out)
    click.echo(f"Background removed. Saved to {out}")


if __name__ == "__main__":
    main()
