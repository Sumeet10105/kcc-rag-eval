# KCC-RAG: An evaluated RAG system over messy government documents

A question-answering system for farmers about the **Kisan Credit Card (KCC)** scheme in India. It answers from real, inconsistent government documents, cites its sources, and says "not found" when the documents do not contain the answer. The main goal of the project is not the chatbot itself but **measuring how good it is** and showing what actually improves it.

**Status:** in progress. Milestone 0 (scope) is being finalised and Milestone 1 (corpus collection and audit) is starting. No results yet.

Author: TODO (you)

---

## Why this project

Government scheme information is spread across official circulars, ministry portals, bank pages, summaries and blogs. These sources are often inconsistent and sometimes outdated. A wrong or outdated answer about eligibility, interest or limits can cost a farmer real money. A system that answers from these documents must therefore be tested, not just demonstrated.

## What is being built

A Retrieval-Augmented Generation (RAG) pipeline:

1. **Collect** real KCC documents (official circulars, scheme summaries, bank pages)
2. **Prepare** them (parse, clean, split into chunks, attach metadata such as source and date)
3. **Retrieve** the passages most relevant to a question
4. **Generate** an answer from those passages only, with citations
5. **Evaluate** retrieval and answers separately against a hand-written test set

## Corpus

- Scheme: Kisan Credit Card
- Document groups: official (RBI and government), myScheme summary, bank pages, secondary explainers
- Every document is logged in [`data/sources.csv`](data/sources.csv) with its URL, publisher, publication date, date accessed and authority level
- Raw files are not published in this repository. Check each source's terms before reusing the originals.

### Ground-truth rule

When documents disagree, the newest official government or RBI document defines the expected answer. The ranking, in order: newest official document, older official documents, myScheme summary, bank and third-party pages. If the corpus contains nothing newer, the system answers from what it has, states the document date and notes that rules may have changed. Full details are in [`docs/scope.md`](docs/scope.md).

## Evaluation plan

- A hand-written test set with questions of several types: direct lookup, questions not answerable from the documents or possibly outdated, and list questions
- Retrieval measured separately from answer quality
- Controlled experiments, changing one thing at a time (for example chunk size, retrieval method, model size)
- Failure analysis with a taxonomy of why answers go wrong

## Results

None yet. This section will hold the results table once the baseline and experiments exist.

## Repository structure

```
data/
  raw/            untouched downloads (not committed)
  processed/      cleaned text and chunks
  sources.csv     manifest of every document
docs/
  scope.md        scope, question types, ground-truth rule, constraints
  audit.md        corpus audit notes
src/              pipeline code
eval/             test set and evaluation results
outputs/          results of runs
```

## Roadmap

- [ ] Milestone 0: scope
- [ ] Milestone 1: corpus collection and audit
- [ ] Milestone 2: ingestion and chunking
- [ ] Milestone 3: baseline RAG
- [ ] Milestone 4: test set
- [ ] Milestone 5: evaluation harness
- [ ] Milestone 6: experiments
- [ ] Milestone 7: failure analysis
- [ ] Milestone 8: simple interface
- [ ] Milestone 9: write-up

## Setup

TODO: added when the baseline runs (Milestone 3).

## Disclaimer

This is a learning and portfolio project. It is not financial, legal or banking advice, and it is not a substitute for a bank officer. Source documents may be outdated or may differ between banks.