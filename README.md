# BibCleaner Pro

A robust, brace-aware BibTeX deduplication tool for scientific workflows.  
BibCleaner Pro removes duplicate bibliography entries based on DOI, title, or URL and generates a complete audit log for transparent, reproducible deduplication.

This tool is designed for researchers, LaTeX users, and anyone working with larger `.bib` files originating from mixed sources such as arXiv, DBLP, publishers, reference managers, or automated extraction tools.

---

## Key Features

- **Brace-aware BibTeX parsing**  
  Parses entries using a structural brace counter instead of brittle regex-only splitting.  
  Handles nested braces, line breaks, and unusual formatting reliably.

- **Multi-level duplicate detection**  
  Duplicate keys are detected in the following priority order:
  1. DOI  
  2. Title  
  3. URL  

- **Deterministic output**  
  Deduplication produces the same output on every run when the input is identical.

- **Audit log**  
  Deletes are written to `dedupe.log` with:
  - full BibTeX entry removed,
  - the deduplication key,
  - decision rationale.

- **Minimal setup**  
  Pure Python, no dependencies, works as a drop-in script.

---

## When to Use This Tool

Use BibCleaner Pro if you work with:

- manually curated `.bib` files that tend to accumulate duplicates  
- large bibliographies generated from diverse sources  
- automated crawlers or extraction pipelines (arXiv → BibTeX, DBLP → BibTeX, Zotero → BibTeX, etc.)  
- RAG or NLP pipelines generating BibTeX metadata from PDFs  
- academic writing workflows requiring a consistent and clean reference base  

This tool intentionally **does not modify content**, only identifies and removes semantically duplicate entries.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/katharinaheller/bibcleaner-pro.git
cd bibcleaner-pro
