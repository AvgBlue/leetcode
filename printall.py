import os


def save_all_file_contents(root_dir: str, output_file: str) -> None:
    with open(output_file, "w", encoding="utf-8") as out:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                try:
                    with open(full_path, "r", encoding="utf-8") as file:
                        content = file.read()
                    out.write(f"Filename: {full_path}\n")
                    out.write("Content:\n")
                    out.write(content)
                    out.write("\n" + "=" * 80 + "\n\n")
                except Exception as e:
                    out.write(f"Could not read {full_path}: {e}\n\n")


# Example usage:
# Replace 'your_directory_path_here' with the path you want to scan
# Replace 'output.txt' with the desired output filename
save_all_file_contents(
    r"C:\Users\4646d\source\repos\WPFTutorial23UsingViewModelsinMVVM\WPFTutorial23UsingViewModelsinMVVM",
    r"C:\Projects\GitHub\leetcode\all.txt",
)
