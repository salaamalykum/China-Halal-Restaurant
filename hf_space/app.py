import gradio as gr
from datasets import load_dataset
import pandas as pd

# Load dataset
dataset = load_dataset("qurancn/China-Halal-Restaurant", split="train")
df = pd.DataFrame(dataset)

def search_articles(query):
    if not query:
        return df[['title', 'preview_excerpt', 'word_count']].head(10)
    
    mask = df['title'].str.contains(query, case=False, na=False) | df['text'].str.contains(query, case=False, na=False)
    results = df[mask]
    return results[['title', 'preview_excerpt', 'word_count']].head(15)

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🕌 China Halal Restaurant Knowledge Base")
    gr.Markdown("Search through 201 authentic articles and travel guides for Chinese Muslims. This Space demonstrates the [qurancn/China-Halal-Restaurant](https://huggingface.co/datasets/qurancn/China-Halal-Restaurant) dataset.")
    
    with gr.Row():
        search_box = gr.Textbox(label="Search Keywords (e.g., 北京, 拉面, 烤肉)", placeholder="Enter keyword...")
        search_button = gr.Button("Search")
        
    results_table = gr.Dataframe(headers=["Title", "Excerpt", "Word Count"], interactive=False)
    
    search_button.click(fn=search_articles, inputs=search_box, outputs=results_table)
    search_box.submit(fn=search_articles, inputs=search_box, outputs=results_table)
    
    demo.load(fn=search_articles, inputs=gr.State(""), outputs=results_table)

demo.launch()
