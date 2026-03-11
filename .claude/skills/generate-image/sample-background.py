#!/usr/bin/env python3
"""Sample the background color of an image from its corner pixels."""

import click
from PIL import Image


@click.command()
@click.argument("image_path")
def main(image_path: str) -> None:
    """Sample the background color of an image by averaging its four corners."""
    img = Image.open(image_path).convert("RGB")

    w, h = img.size
    s = 20  # sample block size

    regions = [
        (0, 0, s, s),                     # top-left
        (w - s, 0, w, s),                 # top-right
        (0, h - s, s, h),                 # bottom-left
        (w - s, h - s, w, h),             # bottom-right
        (w // 2 - s // 2, 0, w // 2 + s // 2, s),          # top-center
        (w // 2 - s // 2, h - s, w // 2 + s // 2, h),      # bottom-center
        (0, h // 2 - s // 2, s, h // 2 + s // 2),          # left-center
        (w - s, h // 2 - s // 2, w, h // 2 + s // 2),      # right-center
    ]

    rs, gs, bs = [], [], []
    for box in regions:
        for r, g, b in img.crop(box).get_flattened_data():
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
