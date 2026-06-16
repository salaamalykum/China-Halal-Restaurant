---
license: mit
language:
- zh
size_categories:
- n<1K
task_categories:
- question-answering
- text-generation
- text-retrieval
- token-classification
tags:
- halal
- chinese-muslim
- restaurant
- halal-food
- rag
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
  - split: validation
    path: data/validation-*
  - split: test
    path: data/test-*
---

# China Halal Restaurant Dataset (RAG Optimized)

This is a rigorously formatted Chinese Halal Restaurant corpus containing 201 authentic articles and travel guides.
It is explicitly optimized for Retrieval-Augmented Generation (RAG) and pure text indexing.

## Dataset Features
- **Zero-Noise Markdown**: All BBCode, HTML, and escaped characters have been parsed into strict Markdown.
- **Rich Metadata**: Every chunk includes `author`, `pub_date`, `word_count`, and `topics`.
- **Pre-split**: 80/10/10 Train/Validation/Test splits.
- **High-Performance Parquet**: Encoded with `row_group_size=1024` and `write_page_index=True` for instant Hugging Face Data Viewer rendering.
