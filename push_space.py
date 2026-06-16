import os
from huggingface_hub import HfApi

# 1. Ensure HF_TOKEN is set in the environment
token = os.environ.get("HF_TOKEN")
if not token:
    print("❌ ERROR: HF_TOKEN environment variable not found.")
    print("Please run this script with: HF_TOKEN=your_token python3 push_space.py")
    exit(1)

api = HfApi()
repo_id = "qurancn/China-Halal-Restaurant-Search"

print(f"Creating and pushing Space to {repo_id}...")

try:
    # 2. Create the space repo if it doesn't exist
    api.create_repo(repo_id=repo_id, repo_type="space", space_sdk="gradio", private=False, exist_ok=True)
    
    # 3. Upload the hf_space directory
    api.upload_folder(
        folder_path="/Users/goodday/Documents/qurancn/final_fix 2/China-Halal-Restaurant/hf_space",
        repo_id=repo_id,
        repo_type="space",
        commit_message="Initial deploy of Search Space"
    )
    print(f"✅ Successfully pushed Gradio Search Space to Hugging Face!")
    print(f"Check it out at: https://huggingface.co/spaces/{repo_id}")
except Exception as e:
    print(f"❌ Failed to push space: {e}")
