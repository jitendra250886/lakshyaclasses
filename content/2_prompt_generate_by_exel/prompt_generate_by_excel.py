# set LAKSHYA_PATH=G:\My Drive\lakshyaclasses
# python prompt_generate_by_excel.py

import pandas as pd
from pathlib import Path
import os

# Get project root from environment variable
project_root = Path(os.environ["LAKSHYA_PATH"])

# Build full path to the Excel file
excel_path = project_root / "content" / "1_EXEL_DATA_SHEET_generated" / "NCERT_Classes.xlsx"
print("exel_path", excel_path)

# Load the Excel file
xl = pd.ExcelFile(excel_path, engine='openpyxl')

# Generalized prompt template
prompt_template = '''class_no={class_no}
subject='{subject}'
chapter_index={chapter_index}
chapter_title='{chapter_title}'
language='English'
depth='Standard school level'
chapter_title_slug='{chapter_title_slug}'
subject_slug='{subject_slug}'

You are a subject-matter expert and instructional designer for the CBSE/NCERT curriculum, creating **professionally structured, student- and teacher-ready notes** for the **lakshyaclasses** website in clean, well-formatted **Markdown**.

=== PROJECT CONTEXT ===  
- Board: CBSE  
- Curriculum Reference: NCERT (latest edition)  
- Platform: lakshyaclasses (high-quality, exam-focused educational content)  
- Audience: Class {class_no} students and teachers  
- Language: English  
- Depth: Standard school level  
- Tone: Clear, engaging, exam-relevant, and professional  
- Diagrams: Automatically identify and extract from NCERT PDF, Byju's website, and YouTube video

=== SOURCES TO USE ===  
- NCERT PDF: https://www.ncert.nic.in/textbook/pdf/{subject_slug[0]}esc{class_no:02}{chapter_index:02}.pdf  
- Byju's Explanation: https://byjus.com/ncert-solutions-class-{class_no}-{subject_slug}/chapter-{chapter_index}-{chapter_title_slug}/  
- YouTube Video: https://www.youtube.com/results?search_query={chapter_title_slug}+class+{class_no}+{subject_slug}

=== SCOPE ===  
- Class {class_no} → {subject} → Chapter: “{chapter_title}”  
- Align strictly with the official NCERT chapter structure and learning objectives  
- Paraphrase content; do **not** copy NCERT text verbatim  
- Focus only on **chapter concepts** (no questions, no worksheets)  
- Include all key concepts, definitions, processes, examples, and simple numericals (if applicable)  
- Suggest where diagrams should be inserted (e.g., photosynthesis process, stomata structure, etc.)  
- Ensure content is suitable for both **students** (easy to understand) and **teachers** (ready to teach)

=== OUTPUT FORMAT (STRICT) ===  
Return a single Markdown document with this exact structure:

---
title: "{chapter_title}"  
class: "{class_no}"  
subject: "{subject}"  
board: "CBSE"  
source_alignment: "Aligned to NCERT (latest)"  
language: "English"  
level: "Standard school level"  
tags: ["NCERT class notes", "NCERT", "CBSE", "{subject}", "Class {class_no}", "{chapter_title_slug}"]  
slug: "{class_no}-{subject_slug}-{chapter_index}-{chapter_title_slug}"  
version: "1.0"  
---

# {chapter_index}. {chapter_title}

> **Learning Outcomes (NCERT-aligned)**  
> • Bullet the measurable outcomes, mapping loosely to Bloom’s levels (Remember→Create).

## Chapter Snapshot  
- **Key Terms:** (comma-separated list)  
- **Prerequisites:** (what students should know)  
- **Real-life Connections:** (2–3)

## Concept Map (Diagram)  
<!-- Diagram will be extracted from sources. Placeholder below. -->  
**[Insert Diagram: Concept Map of {chapter_title}]**

## {chapter_index}.1 [First Section Title]  
(Detailed explanation with examples and subpoints)

## {chapter_index}.2 [Second Section Title]  
(Detailed explanation with examples and subpoints)

## Activities and Experiments  
- (List of hands-on activities or experiments from the chapter)

## Summary  
(Concise recap of the chapter concepts only)
'''

# Create output directory
output_dir = Path("generated_prompts_exel")
output_dir.mkdir(exist_ok=True)

# Process each worksheet
for sheet_name in xl.sheet_names:
    df = xl.parse(sheet_name)
    class_no = int(sheet_name.split()[-1])  # Extract class number from sheet name

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

        # Save to .md file
        filename = f"class{class_no}_{subject_slug}_{chapter_index:02d}_{chapter_title_slug}.md"
        with open(output_dir / filename, "w", encoding="utf-8") as f:
            f.write(prompt)

print("✅ Prompts generated for all chapters across classes 1 to 12.")