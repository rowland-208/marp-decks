#!/usr/bin/env python3
"""Sample the background color of an image from its corner pixels."""

import click
from PIL import Image


@click.command()
@click.argument("image_path")
def main(image_path: str) -> None:
    """Sample the background color of an image by averaging its four corners."""
    img = Image.open(image_path).convert("RGB")

    corners = [
        (0, 0),
        (img.width - 1, 0),
        (0, img.height - 1),
        (img.width - 1, img.height - 1),
    ]

    rs, gs, bs = [], [], []
    for x, y in corners:
        r, g, b = img.getpixel((x, y))
        rs.append(r)
        gs.append(g)
        bs.append(b)

    avg_r = sum(rs) // len(rs)
    avg_g = sum(gs) // len(gs)
    avg_b = sum(bs) // len(bs)

    hex_color = f"#{avg_r:02x}{avg_g:02x}{avg_b:02x}"
    click.echo(hex_color)


if __name__ == "__main__":
    main()
