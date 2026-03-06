---
name: publish
description: Publish a deck by exporting it to HTML, committing, and pushing to the repo. Use when the user asks to publish a deck.
---

# Publish

Export the specified deck to HTML, commit, and push.

## Steps

1. Export the deck to HTML in the deck's directory:

```bash
marp decks/<deck-name>/<deck-name>.md --output decks/<deck-name>/<deck-name>.html
```

2. Add a link to the new deck in `index.html` following the existing format.

3. Stage all files: deck.html, images, index.html

4. Commit with message: `Publish <deck-name>`

5. Push to remote.
