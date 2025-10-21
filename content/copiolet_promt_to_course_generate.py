import os
from pathlib import Path

# Define input and output directories
input_dir = Path("generated_prompts")
output_base = Path("Course1to12")

# Ensure output base directory exists
output_base.mkdir(parents=True, exist_ok=True)

# Simulated Copilot interaction (replace this with actual API call)
def generate_course_content(prompt_text):
    # Placeholder for actual Copilot response
    return f"# Course Content Generated\n\n{prompt_text}\n\n<!-- End of Course Content -->"

# Process each .md file in the input directory
for md_file in input_dir.glob("*.md"):
    with open(md_file, "r", encoding="utf-8") as f:
        prompt_text = f.read()

    # Extract metadata from filename: class7_maths_06_the-triangle-and-its-properties.md
    parts = md_file.stem.split("_")
    class_part = parts[0]  # e.g., class7
    subject = parts[1]     # e.g., maths
    chapter_index = parts[2]  # e.g., 06
    chapter_slug = "_".join(parts[3:])  # e.g., the-triangle-and-its-properties

    # Format output path
    class_dir = output_base / class_part.capitalize() / subject.lower()
    class_dir.mkdir(parents=True, exist_ok=True)

    output_file = class_dir / f"_{chapter_slug}_Course.md"

    # Generate course content
    course_md = generate_course_content(prompt_text)

    # Save the output
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(course_md)

print("✅ Course Markdown files generated and saved in Course1to12 directory.")