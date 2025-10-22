from pathlib import Path
import os

# Placeholder AI function to simulate response generation
def generate_response(prompt: str) -> str:
    return f"# AI Generated Content\n\nThis is a simulated response for the prompt:\n\n{prompt[:200]}..."

# Get project root from environment variable
project_root = Path(os.environ["LAKSHYA_PATH"])

# Correct input and output paths
input_base = project_root / "content" / "2_prompt_generate_by_exel" / "generated_courses_exel"
output_base = project_root / "content" / "3_course_generate_by_prompt" / "generated_courses_exel"

print("input_base: ", input_base)
print("output_base:", output_base)


# Traverse the input directory structure
for class_dir in input_base.iterdir():
    if class_dir.is_dir():
        print(f"\n Processing class: {class_dir.name}")
        for subject_dir in class_dir.iterdir():
            if subject_dir.is_dir():
                print(f" Subject: {subject_dir.name}")
                for prompt_file in subject_dir.glob("*.md"):
                    print(f"     Reading file: {prompt_file.name}")
                    try:
                        with open(prompt_file, "r", encoding="utf-8") as f:
                            prompt = f.read()

                        response = generate_response(prompt)

                        relative_path = prompt_file.relative_to(input_base)
                        output_path = output_base / relative_path
                        output_path.parent.mkdir(parents=True, exist_ok=True)

                        with open(output_path, "w", encoding="utf-8") as f:
                            f.write(response)

                        print(f"    Saved output to: {output_path}")
                    except Exception as e:
                        print(f"    Error processing {prompt_file.name}: {e}")

print("\nAll prompts processed and responses saved in structured output folder.")
