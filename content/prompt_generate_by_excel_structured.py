
from pathlib import Path
import pandas as pd

# Define the Excel file path
excel_path = Path("./1_EXEL_DATA_SHEET_generated/NCERT_Classes.xlsx")

# Load the Excel file
xl = pd.ExcelFile(excel_path, engine='openpyxl')

# Prompt template
prompt_template = """# {chapter_index}. {chapter_title}

You are a subject-matter expert creating structured notes for Class {class_no} - {subject}.

## Chapter Overview
- Title: {chapter_title}
- Class: {class_no}
- Subject: {subject}
- Language: English
- Depth: Standard school level

## Sources
- NCERT PDF: https://ncert.nic.in/textbook/pdf/{subject_slug[0]}esc{class_no:02}{chapter_index:02}.pdf
- Byju's: https://byjus.com/ncert-solutions-class-{class_no}-{subject_slug}/chapter-{chapter_index}-{chapter_title_slug}/
- YouTube: https://www.youtube.com/results?search_query={chapter_title_slug}+class+{class_no}+{subject_slug}

## Content
(Write detailed explanation here)
"""

# Create base output directory
output_dir = Path("./2_prompt_generate_by_exel/generated_prompts_exel")
output_dir.mkdir(parents=True, exist_ok=True)

# Process each worksheet
for sheet_name in xl.sheet_names:
    df = xl.parse(sheet_name)
    class_no = int(sheet_name.split()[-1])
    class_dir = output_dir / f"Class_{class_no:02d}"

    for _, row in df.iterrows():
        subject = row['Subject']
        chapter_index = int(str(row['Chapter_Index']).split('-')[1]) if '-' in str(row['Chapter_Index']) else 0
        chapter_title = str(row['Chapter_Index']).replace(f'CHAPTER-{chapter_index:02d}-', '').replace('-', ' ').title()

        # Generate slugs
        chapter_title_slug = chapter_title.lower().replace(' ', '-').replace("'", "")
        subject_slug = subject.lower().replace(' ', '-')

        # Fill the prompt
        prompt = prompt_template.format(
            class_no=class_no,
            subject=subject,
            chapter_index=chapter_index,
            chapter_title=chapter_title,
            chapter_title_slug=chapter_title_slug,
            subject_slug=subject_slug
        )

        # Create subject folder
        subject_dir = class_dir / subject_slug
        subject_dir.mkdir(parents=True, exist_ok=True)

        # Save to .md file
        filename = f"{chapter_index:02d}_{chapter_title_slug}.md"
        with open(subject_dir / filename, "w", encoding="utf-8") as f:
            f.write(prompt)

print("✅ Prompts generated in structured folders: Class → Subject → Chapter")
