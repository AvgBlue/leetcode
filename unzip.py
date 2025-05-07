import zipfile
import os

def unzip_all_in_folder(folder_path):
    # Make sure the folder exists
    if not os.path.isdir(folder_path):
        print(f"Folder '{folder_path}' does not exist.")
        return

    # Go through each file in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.zip'):
            zip_path = os.path.join(folder_path, filename)
            extract_folder = os.path.join(folder_path, os.path.splitext(filename)[0])

            print(f"Unzipping '{filename}' to '{extract_folder}'...")

            # Extract the zip file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_folder)

    print("All zip files have been extracted.")

# Example usage
if __name__ == "__main__":
    folder = input("Enter the folder path containing zip files: ").strip()
    unzip_all_in_folder(folder)
