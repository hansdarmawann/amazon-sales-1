import kagglehub
import shutil
from pathlib import Path

# 1. Download dataset terbaru ke cache KaggleHub
path = kagglehub.dataset_download("rohiteng/amazon-sales-dataset")
print("Path (cache):", path)

# 2. Tentukan folder project dan tujuan /datasets
project_root = Path(__file__).resolve().parent
target_dir = project_root / "datasets"

# 3. Buat folder datasets jika belum ada
target_dir.mkdir(exist_ok=True)

# 4. Copy semua isi dari cache ke /datasets
source_dir = Path(path)
for item in source_dir.iterdir():
    dest = target_dir / item.name
    if item.is_dir():
        if dest.exists():
            shutil.rmtree(dest)  # hapus folder lama dulu
        shutil.copytree(item, dest)
    else:
        shutil.copy2(item, dest)

print(f"✅ Dataset copied to: {target_dir}")

# 5. Hapus folder cache KaggleHub tempat download
try:
    shutil.rmtree(source_dir)
    print(f"🧹 Cache deleted: {source_dir}")
except Exception as e:
    print(f"⚠️ Failed to delete cache: {e}")