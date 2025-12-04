import os
import kagglehub
from pathlib import Path

# folder datasets di project yang sama
project_root = Path(__file__).resolve().parent.parent
target_dir = project_root / "datasets"
target_dir.mkdir(exist_ok=True)

os.environ["KAGGLEHUB_CACHE"] = str(target_dir)

path = kagglehub.dataset_download("rohiteng/amazon-sales-dataset")

print("Path to dataset files:", path)
