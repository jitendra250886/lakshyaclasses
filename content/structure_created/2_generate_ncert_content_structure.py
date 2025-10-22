"""
This script generates the full NCERT-based content folder structure for LakshyaClasses.
It creates folders for LKG, UKG, and Class 1 to Class 12.
Each class includes relevant NCERT subjects.
Each subject folder contains:
  - notes.md
  - worksheet1.md
  - worksheet1.pdf
"""

import os

# === Base content folder ===
BASE_DIR = "content"

# === Class labels ===
classes = ["LKG", "UKG"] + [f"class{i}" for i in range(1, 13)]

# === NCERT subjects per class ===
ncert_subjects = {
    "LKG": ["english", "math", "environment"],
    "UKG": ["english", "math", "environment"],
    "class1": ["english", "math", "evs"],
    "class2": ["english", "math", "evs"],
    "class3": ["english", "math", "evs"],
    "class4": ["english", "math", "evs"],
    "class5": ["english", "math", "evs"],
    "class6": ["english", "math", "science", "social_science", "hindi", "sanskrit"],
    "class7": ["english", "math", "science", "social_science", "hindi", "sanskrit"],
    "class8": ["english", "math", "science", "social_science", "hindi", "sanskrit"],
    "class9": ["english", "math", "science", "social_science", "hindi", "sanskrit"],
    "class10": ["english", "math", "science", "social_science", "hindi", "sanskrit"],
    "class11": ["english", "math", "physics", "chemistry", "biology", "economics", "accountancy", "business_studies", "history", "political_science", "geography", "sociology", "psychology", "hindi"],
    "class12": ["english", "math", "physics", "chemistry", "biology", "economics", "accountancy", "business_studies", "history", "political_science", "geography", "sociology", "psychology", "hindi"]
}

# === Files to create in each subject folder ===
files = ["notes.md", "worksheet1.md", "worksheet1.pdf"]

# === Create folder structure ===
for class_name in classes:
    subjects = ncert_subjects.get(class_name, [])
    for subject in subjects:
        subject_path = os.path.join(BASE_DIR, class_name, subject)
        os.makedirs(subject_path, exist_ok=True)

        for filename in files:
            file_path = os.path.join(subject_path, filename)

            # Create placeholder content for .md files
            if filename.endswith(".md"):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"# {class_name.upper()} - {subject.replace('_', ' ').title()} - {filename}\n\n")
                    f.write("This is a placeholder for educational content.\n")

            # Create empty .pdf file
            elif filename.endswith(".pdf"):
                with open(file_path, "wb") as f:
                    f.write(b"%PDF-1.4\n% Placeholder PDF\n")

print("✅ NCERT-based content folder structure generated successfully.")

"""
🧠 What This Script Covers:
All NCERT subjects from LKG to Class 12
Creates Markdown and PDF placeholders for each subject
Uses clean naming and reproducible structure
Ready for integration with your content blueprint and dashboard

Let me know if you want:
To add quiz.md or submission.md files
To auto-fill notes with NCERT chapter titles
To generate a dashboard preview of this structure
Want me to bundle this into your admin panel for one-click regeneration?

"""