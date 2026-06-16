import os
from huggingface_hub import HfApi

# 1. Ensure HF_TOKEN is set in the environment
token = os.environ.get("HF_TOKEN")
if not token:
    print("❌ ERROR: HF_TOKEN environment variable not found.")
    print("Please run this script with: HF_TOKEN=your_token python3 push_to_hf.py")
    exit(1)

api = HfApi()
repo_id = "qurancn/China-Halal-Restaurant"

print(f"Pushing dataset to {repo_id}...")

try:
    # 2. Create the dataset repo if it doesn't exist
    api.create_repo(repo_id=repo_id, repo_type="dataset", private=False, exist_ok=True)
    
    # 3. Upload the entire hf_dataset_ready directory to the root of the dataset repo
    api.upload_folder(
        folder_path="/Users/goodday/Documents/qurancn/final_fix 2/China-Halal-Restaurant/hf_dataset_ready",
        repo_id=repo_id,
        repo_type="dataset",
        commit_message="Release v1.0.0: High-quality structure with Parquet partitions"
    )
    print(f"✅ Successfully pushed high-quality structured dataset to Hugging Face!")
    print(f"Check it out at: https://huggingface.co/datasets/{repo_id}")
except Exception as e:
    print(f"❌ Failed to push dataset: {e}")
