---
name: verify
description: Research slide content for factual accuracy using web search. Fix false claims and add citations for true ones.
---

# Verify

Fact-check the content of a Marp slide deck by researching each claim.

## Steps

1. Read the deck and extract every factual claim (statistics, dates, names, scientific facts, quotes, etc.)

2. For each claim, use **WebSearch** to verify it. Search for the specific fact, not the slide topic generally.

3. For each claim, determine one of:
   - **True** — add a citation as a markdown comment next to the claim: `<!-- Source: [Title](URL) -->`
   - **False or outdated** — update the claim with correct information and add a citation
   - **Unverifiable** — flag it with `<!-- UNVERIFIED -->` so the user can review

4. Present a summary to the user showing what was verified, what was corrected, and what remains unverified.
