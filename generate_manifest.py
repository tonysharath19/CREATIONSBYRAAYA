import os, json

# Define base folder relative to this script
BASE_DIR = "TEMPLATES"

# Function to build nested manifest
def build_manifest(path, base_path):
    manifest = {}
    for root, dirs, files in os.walk(path):
        # Get relative path from base
        rel_path = os.path.relpath(root, base_path)
        if rel_path == ".":
            current = manifest
        else:
            # Navigate to the correct nested dict
            parts = rel_path.split(os.sep)
            current = manifest
            for part in parts:
                part_title = part.replace("-", " ").title()
                if part_title not in current:
                    current[part_title] = {}
                current = current[part_title]
        
        # Add files to current level
        image_files = [
            f"TEMPLATES/{os.path.relpath(os.path.join(root, file), base_path).replace(os.sep, '/')}"
            for file in sorted(files)
            if file.lower().endswith((".jpg", ".png", ".jpeg"))
        ]
        if image_files:
            current["files"] = image_files
    return manifest

# Build the manifest
manifest = build_manifest(BASE_DIR, BASE_DIR)

# Write output as JS file
with open("imageManifest.js", "w", encoding="utf-8") as f:
    f.write("const imageManifest = ")
    json.dump(manifest, f, indent=2)
    f.write(";")
    
print("✅ imageManifest.js generated successfully!")
