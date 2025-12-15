import os, json

# Define base folder relative to this script
BASE_DIR = "VIDEO-TEMPLATES"

# Dictionary to hold all images by category and tier
manifest = {}

for category in os.listdir(BASE_DIR):
    category_path = os.path.join(BASE_DIR, category)
    if not os.path.isdir(category_path):
        continue

    manifest[category.replace("-", " ").title()] = {}

    for tier in ["VIDEOS"]:
        tier_path = os.path.join(category_path, tier)
        if not os.path.isdir(tier_path):
            continue

        # Collect only video files (mp4, mkv, mov)
        videos = [
            f"./{BASE_DIR}/{category}/{tier}/{file}"
            for file in sorted(os.listdir(tier_path))
            if file.lower().endswith((".mp4", ".mkv", ".mov"))
        ]
        manifest[category.replace("-", " ").title()][tier.title()] = videos

# Write output as JS file
with open("videoManifest.js", "w", encoding="utf-8") as f:
    f.write("const videoManifest = ")
    json.dump(manifest, f, indent=2)
    f.write(";")
    
print("✅ videoManifest.js generated successfully!")
