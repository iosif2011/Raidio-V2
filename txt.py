import os
import json

def clean_filenames_and_export(folder_path, output_file="songs.txt"):
    result = []

    # Walk through all folders and files
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            old_path = os.path.join(root, file)

            # Split filename and extension
            name, ext = os.path.splitext(file)

            # Remove ONLY the suffix if it exists at the end
            if name.endswith("_spotdown.org"):
                new_name = name.replace("_spotdown.org", "")
            else:
                new_name = name

            new_file = new_name + ext
            new_path = os.path.join(root, new_file)

            # Rename if needed
            if old_path != new_path:
                os.rename(old_path, new_path)

            # Convert to relative path with forward slashes
            rel_path = os.path.relpath(new_path, folder_path)
            rel_path = rel_path.replace("\\", "/")

            result.append(rel_path)

    # Sort for cleaner output
    result.sort()

    # Format like your example
    formatted = [f"{path}" for path in result]

    # Save as JSON-style txt
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("[\n")
        for i, item in enumerate(formatted):
            comma = "," if i < len(formatted) - 1 else ""
            f.write(f'  "{item}"{comma}\n')
        f.write("]")

    print(f"Done. Renamed files and saved list to {output_file}")


# ==== USAGE ====
folder_path = input("Enter folder path: ").strip()
clean_filenames_and_export(folder_path)