---
name: generate-deck
description: Generate a complete Marp slide deck end-to-end. Use when the user asks to generate, create, or build a new deck from a topic.
---

# Generate Deck

Create a complete Marp slide deck from a topic through a multi-step pipeline.

## Usage

The user provides a topic. Follow all steps in order.

## Step 1 — Generate Draft Slides

Create 10 slides in Marp markdown format in a new deck directory under `decks/`:

- Slide 1: Title slide with `<!-- _class: title -->` and `<!-- _paginate: false -->`
- Slides 2–9: Content slides with bullet points, tables, or quotes
- Slide 10: Closing slide with `<!-- _class: closing -->` and `<!-- _paginate: false -->`

Use the whale-communication deck as a reference for structure and style. Start with a neutral theme (default Marp theme, no custom colors yet).

```
decks/<deck-name>/<deck-name>.md
```

Render with `marp --watch` and give the user a clickable `file://` link to the HTML.

## Step 2 — Human Review

Ask the user to review the draft. Wait for their feedback on content, structure, and tone. Present a clickable file:// link to the rendered HTML.

## Step 3 — Update Draft

Apply the user's feedback to the slides. Re-render and confirm changes with the user.

## Step 4 — Verify Content

Use the **verify** skill to research all factual claims in the deck. Fix false claims and add citation comments for true ones. Show the user a summary of what changed.

## Step 5 — Apply Theme Colors

Choose a color palette that fits the deck topic. Apply it as a Marp `style` block in the frontmatter, following the pattern in the whale-communication deck:

- CSS variables for background, foreground, highlight, and dimmed colors
- Styled `section`, `h1`, `h2`, `h3`, `strong`, `a`, `li`, `table`, `th`, `td`
- Special classes: `title`, `light`, `closing`

Re-render and confirm the theme looks good.

## Step 6 — Generate Images

Use the **generate-image** skill to create 4 images:

1. A title image for slide 1
2. Three content images for slides that would benefit most from visuals

Save images in the deck directory. Use descriptive filenames.

## Step 7 — Integrate Images and Adjust Theming

For each generated image:

1. Use the **sample-background** tool to check the image's background color
2. If the background is close to white (light/pale):
   - Use the **remove-background** tool to make it transparent
   - Add the image to the slide with no background color change
3. If the background is not close to white:
   - Use the sampled color to set the slide's background: `<!-- _backgroundColor: #hexcolor -->`
   - Add `<!-- _class: light -->` if the background is light, adjusting text colors for readability
   - Add the image as `![bg right:40% fit](image.png)` or similar layout

Re-render and verify images look good on their slides.

## Step 8 — Final Review

Ask the user to do a final review of the complete deck. Apply any last changes.

## Step 9 — Publish

Use the **publish** skill to export the deck to HTML, commit, and push.
