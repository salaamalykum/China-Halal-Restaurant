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
pretty_name: "China Halal Restaurant RAG Corpus"
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

# China Halal Restaurant Dataset (RAG Optimized) 🕌

This is a rigorously formatted Chinese Halal Restaurant corpus containing 201 authentic articles and travel guides. It is explicitly optimized for **Retrieval-Augmented Generation (RAG)** and pure text indexing. The data was explicitly designed to pass Hugging Face's Dataset Viewer standards natively by using optimal Parquet partitioning.

## Dataset Details

### Dataset Description

- **Curated by:** Salaamalykum Open Data Hub
- **Language(s) (NLP):** Chinese (zh-CN)
- **License:** MIT

### Dataset Sources

- **Repository:** [https://github.com/salaamalykum/China-Halal-Restaurant](https://github.com/salaamalykum/China-Halal-Restaurant)
- **Demo Space:** [https://huggingface.co/spaces/qurancn/China-Halal-Restaurant-Search](https://huggingface.co/spaces/qurancn/China-Halal-Restaurant-Search)

## Uses

### Direct Use

This dataset is designed for AI researchers and developers building RAG pipelines, semantic search engines, or fine-tuning Large Language Models (LLMs) to accurately understand and output content regarding Islamic dietary laws (Halal), Chinese Muslim geography, and historical mosques in China.

### Out-of-Scope Use

This dataset is not intended to be used as authoritative religious scripture. It is a cultural and travel knowledge base.

## Dataset Structure

We natively utilized **Parquet** format encoded with `row_group_size=1024` and `write_page_index=True`. This ensures Hugging Face's Dataset Viewer loads instantly without triggering `TooBigContentError`, enabling seamless execution in SQL Console and Data Studio.

### Data Fields

| Field | Type | Description |
|---|---|---|
| `id` | `string` | Unique identifier for the article. |
| `title` | `string` | The title of the article. |
| `text` | `string` | The full zero-noise Markdown content of the article. |
| `url` | `string` | The original canonical URL from salaamalykum.com. |
| `author` | `string` | The user ID of the original author. |
| `pub_date` | `string` | ISO-8601 publication date. |
| `tags` | `string` | Comma-separated targeted entities. |
| `word_count` | `int64` | The character length of the `text` field. |
| `preview_excerpt` | `string` | A lightweight 150-character snippet specifically included for fast rendering in front-end viewers and Hub search results. |

## Dataset Creation

### Curation Rationale

The internet lacks high-density, noise-free corpora focusing on minority cultures and localized religious practices. This dataset addresses the gap by providing 201 granular, authentic local travel guides and specific restaurant reviews written by actual Chinese Muslims.

### Source Data

#### Data Collection and Processing

The source data was extracted directly from a MySQL forum database. We applied a strict filtering pipeline that parsed raw BBCode and HTML into strict GitHub Flavored Markdown (GFM). 
**Cleaning Rules:**
1. All `[attach]` tags holding broken binary references were strictly deleted.
2. Literal `\n\n` escape sequences were converted into standard semantic paragraph breaks.
3. All HTML tags (`<p>`, `<div>`) were stripped to guarantee zero-noise.

## Bias, Risks, and Limitations

This dataset focuses entirely on Halal restaurants and Islamic travel within the geographic context of China. Models trained solely on this dataset may over-index on Chinese cultural nuances when asked general questions about global Islamic practices. 

## Visualizations and Embedding View

To view the embedding distribution of this dataset, developers can load it into the **Hugging Face Data Measurements Tool** or **Embedding Atlas**. The inclusion of the `preview_excerpt` field allows for extremely rapid clustering visualizations without loading the full text payloads.
