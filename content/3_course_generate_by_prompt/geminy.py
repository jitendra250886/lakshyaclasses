#!/usr/bin/env python3
# gemini_md_writer.py

import argparse
import os
import sys
from datetime import datetime

from google import genai
from google.genai import types

def read_text_from_file(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_text_to_file(path: str, text: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def main():
    parser = argparse.ArgumentParser(
        description="Send a prompt to Google Gemini and save the response as a Markdown (.md) file."
    )
    parser.add_argument("--prompt", type=str, help="Prompt text.")
    parser.add_argument("--prompt-file", type=str, help="Path to a text file containing the prompt.")
    parser.add_argument("--out", type=str, default=f"./gemini_output_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                        help="Output Markdown file path. Default: ./gemini_output_<timestamp>.md")
    parser.add_argument("--model", type=str, default="gemini-2.5-flash",
                        help="Gemini model ID (e.g., gemini-2.5-flash, gemini-2.5-pro)")
    parser.add_argument("--temperature", type=float, default=0.4, help="Creativity (0.0 to 2.0).")
    parser.add_argument("--max-tokens", type=int, default=4096, help="Max output tokens.")
    parser.add_argument("--system", type=str, default=(
        "You are an education content writer for middle-school students in India. "
        "Always respond in clean, GitHub-Flavored Markdown with headings, lists, tables if useful, "
        "and include a short summary at the end."
    ), help="System instruction (how the model should behave).")
    parser.add_argument("--api-key", type=str, default=None,
                        help="(Optional) API key. If not provided, reads GEMINI_API_KEY env var.")
    args = parser.parse_args()

    # Get prompt
    if args.prompt_file:
        prompt = read_text_from_file(args.prompt_file)
    elif args.prompt:
        prompt = args.prompt
    else:
        # Read from stdin
        if sys.stdin.isatty():
            print("Enter/Paste your prompt. Press Ctrl-D (Linux/macOS) or Ctrl-Z then Enter (Windows) to end.")
        prompt = sys.stdin.read().strip()

    if not prompt:
        print("Error: No prompt provided. Use --prompt, --prompt-file, or pipe via stdin.", file=sys.stderr)
        sys.exit(1)

    # Get API key
    api_key = args.api_key or os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("Error: API key not found. Set GEMINI_API_KEY env var or pass --api-key.", file=sys.stderr)
        sys.exit(2)

    # Create client
    client = genai.Client(api_key=api_key)  # Gemini Developer API mode. [4](https://pypi.org/project/google-genai/)

    # Build config:
    # - Use system_instruction to enforce Markdown style & tone (officially supported in GenerateContentConfig).
    # - response_mime_type as 'text/markdown' is commonly used; you can also omit it and rely on system instruction.
    config = types.GenerateContentConfig(
        system_instruction=args.system,                 # system instruction support shown in docs
        temperature=args.temperature,
        max_output_tokens=args.max_tokens,
        response_mime_type="text/markdown"
    )

    try:
        resp = client.models.generate_content(
            model=args.model,
            contents=prompt,
            config=config
        )
        # The SDK exposes the primary text as .text
        md = resp.text or ""
        if not md.strip():
            # Fallback to the raw object text if needed
            md = str(resp)
    except Exception as e:
        print(f"Generation failed: {e}", file=sys.stderr)
        sys.exit(3)

    write_text_to_file(args.out, md)
    print(f"✅ Markdown saved to: {args.out}")

if __name__ == "__main__":
    main()



"""
python gemini_md_writer.py --prompt-file prompts/class7_heat.txt --out ./notes/Class7_Science_Heat.md


type prompts\class7_heat.txt | python gemini_md_writer.py --out .\notes\Class7_Science_Heat.md   # Windows
cat prompts/class7_heat.txt | python gemini_md_writer.py --out ./notes/Class7_Science_Heat.md    # macOS/Linux
``


"""