import os
import shutil

# Ask user for the folder to clean up
target_folder = input("Enter the path of the folder to reorganize: ").strip()

# Validate the path
if not os.path.isdir(target_folder):
    print("❌ Error: The provided path is not a valid folder.")
    exit()

# Loop through all subfolders
for root, dirs, files in os.walk(target_folder, topdown=False):
    if root == target_folder:
        continue  # Skip the main folder itself

    for file in files:
        file_path = os.path.join(root, file)
        new_path = os.path.join(target_folder, file)

        # Avoid overwriting files with the same name
        if os.path.exists(new_path):
            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(new_path):
                new_path = os.path.join(target_folder, f"{base}_{counter}{ext}")
                counter += 1

        # Move the file
        shutil.move(file_path, new_path)
        print(f"Moved: {file_path} → {new_path}")

    # Remove empty folder
    try:
        os.rmdir(root)
        print(f"Deleted empty folder: {root}")
    except OSError:
        pass  # Ignore if the folder is not empty

print("✅ All files moved successfully!")
