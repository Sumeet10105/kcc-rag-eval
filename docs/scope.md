# Scope: Evaluated RAG over a messy corpus (Kisan Credit Card)

Status: draft v1, 2026-10-03
Rule for this file: every TODO marked "(you)" needs your own words. Do not leave a TODO in the final version.

---

## 1. Problem

TODO (you): 2 sentences.
Start with: "A farmer who relies on ______ may ______."
Think about outdated blog posts, bank rumours, and what a wrong eligibility or interest answer costs.

## 2. Corpus

- Scheme: Kisan Credit Card (KCC).
- First document: the myScheme KCC page (saved in `data/raw/`, with the date saved in the file name).
- Target size for the first pass: 8-12 documents.
- Document groups (tick when collected and logged in `data/sources.csv`):

| Group | Document | Status |
|---|---|---|
| myScheme summary | myScheme KCC page | [x] saved |
| Official | RBI circular, Modified Interest Subvention Scheme FY 2025-26 | [ ] |
| Official | RBI circular, Modified Interest Subvention Scheme FY 2026-27 | [ ] not yet located |
| Official | Original or master KCC scheme guidelines | [ ] not yet located |
| Bank | Public KCC page of one bank | [ ] |
| Bank | Public KCC page of a second bank | [ ] |
| Secondary | One news article or explainer (non-authoritative) | [ ] |
| Other | TODO (you): anything else you find | [ ] |

- Every document gets a recorded publication date and a date accessed.
- Raw files stay untouched in `data/raw/`. Check each site's terms before publishing any raw file; publish the manifest and download notes instead if unsure.

## 3. User (draft, confirm or change)

A farmer asking short questions in simple English.
TODO (you): confirm, or change it to one more specific person.

## 4. Question types in scope

| # | Type | Example question | Why it matters for a farmer |
|---|---|---|---|
| 1 | Direct lookup | "Do I have to give my land papers as proof for the loan?" | Documents and eligibility are the most common questions. |
| 2 | Not in the documents, or possibly outdated | "If I cannot repay because of a disaster, will they extend the date or give any compensation?" | Wrong or outdated answers do the most harm here. Correct behaviour is "not found in these documents" or a date warning. |
| 3 | List extraction | "What can I use KCC money for?" | A farmer needs the complete list, not part of it. |

Note on type 3: reworded from "how many uses other than farming" because a count depends on how you count, and "use" is ambiguous (purposes of the loan vs ways to use the card).

### Out of scope for now

- Other schemes
- Languages other than English
- Personalised calculations such as "how much loan will I get?"
- Bank-specific procedures

Revisit after Milestone 3.

## 5. What a good answer looks like

TODO (you): rank these from most to least important for KCC, with one line of reasoning for your top choice.

1. ______
2. ______
3. ______
4. ______
5. ______

Properties: correct, grounded in the documents, cited, complete enough to act on, says "not found" when unsure.

Reasoning: TODO (you)

## 6. Ground-truth rule

Sources are ranked:

1. Newest official government or RBI document
2. Older official documents
3. myScheme summary
4. Bank and third-party pages

When documents disagree, the highest-ranked, most recent official document defines the expected answer.
Every document in the corpus has its date recorded.
If the corpus has nothing newer, the system answers from what it has, states the document date, and notes that rules may have changed.

Reason: outdated information can cause real harm to a farmer.

## 7. Non-goals

- Not a replacement for a bank officer
- Not a production service
- Not legal or financial advice

TODO (you): add one more, if you have one.

## 8. Constraints

- Time: about 18 hours per week.
- LLM access: free only. Local model: Qwen 1.5B. Free API provider: to be decided. Check limits in your own console, not in blog posts.
- Hardware: 16 GB RAM, NVIDIA RTX 3050 with 6 GB, about 100 GB free disk.
- Plan: embeddings local; local model for development runs; free API for final evaluation and judging, using a different model as judge than the one that writes answers.
- Numeric quality targets: none yet. Set them after the baseline in Milestone 3.

## 9. Open questions

- Which free API provider? (decide in Milestone 3)
- Does the FY 2026-27 interest subvention circular exist yet, and what does it say?
- TODO (you): anything else you are unsure about.