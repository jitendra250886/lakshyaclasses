import os

# Define the content files to be created inside each chapter folder
content_files = ["NOTES.md", "EXERCISES.md", "DIAGRAMS.md"]

def create_content_files(base_path):
    for root, dirs, files in os.walk(base_path):
        # Only target chapter folders (e.g., CHAPTER-01-...)
        if os.path.basename(root).startswith("CHAPTER-"):
            for filename in content_files:
                file_path = os.path.join(root, filename)
                if not os.path.exists(file_path):
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(f"# {filename.replace('.md', '')}\n\n")
                        f.write("<!-- Add your content here -->\n")
                    print(f"Created: {file_path}")

# Example usage
base_directory = r"C:\Users\nxa16254\OneDrive - NXP\lakshyaclasses\content"
create_content_files(base_directory)