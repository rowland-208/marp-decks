---
name: generate-image
description: Generate an image using OpenRouter. Use this whenever the user asks to generate, create, or make an image.
---

# Generate Image

Run the generate-image tool located in this skill directory.

```bash
uv run --with-requirements .claude/skills/generate-image/requirements.txt .claude/skills/generate-image/generate-image.py <output-path> "<prompt>"
```

## Background Removal

If the user asks to remove the background from a generated image, use the remove-background tool. It uses Pillow's floodfill from the four corners to replace white (or near-white) pixels with transparency.

```bash
uv run --with-requirements .claude/skills/generate-image/requirements.txt .claude/skills/generate-image/remove-background.py <image-path>
```

Options:
- `--thresh N` — Color distance threshold for floodfill (default: 40). Increase for off-white backgrounds.
- `-o, --output PATH` — Save to a different file instead of overwriting the input.

## Background Color Sampling

If the user wants to match a slide background to an image's background color, use the sample-background tool. It averages the four corner pixels and returns a hex color.

```bash
uv run --with-requirements .claude/skills/generate-image/requirements.txt .claude/skills/generate-image/sample-background.py <image-path>
```

This outputs a hex color like `#f8f9f5`. Use it to set the Marp slide background with `<!-- _backgroundColor: #f8f9f5 -->` so the image blends seamlessly into the slide.
