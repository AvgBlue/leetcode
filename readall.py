import os

# Path to your frontend root folder (update this!)
FRONTEND_DIR = r"C:\Projects\GitHub\ReadBuddy\frontend\ReadBuddy"  # ⬅️ Change this

# Output text file
OUTPUT_FILE = "frontend_files.txt"

# File types we care about
RELEVANT_EXTENSIONS = {".xaml", ".cs", ".resx"}

# Folders to ignore
IGNORED_FOLDERS = {"bin", "obj", ".vs", ".git", "__pycache__"}


def is_relevant_file(filename):
    return os.path.splitext(filename)[1] in RELEVANT_EXTENSIONS


def list_and_dump_files(directory):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as out_file:
        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in IGNORED_FOLDERS]
            for file in files:
                if is_relevant_file(file):
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, FRONTEND_DIR)
                    out_file.write(f"=== {rel_path} ===\n")
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            out_file.write(f.read())
                    except UnicodeDecodeError:
                        out_file.write("[Could not decode file as UTF-8]")
                    out_file.write("\n\n")


if __name__ == "__main__":
    list_and_dump_files(FRONTEND_DIR)
    print(f"✅ All relevant frontend files saved to '{OUTPUT_FILE}'")
