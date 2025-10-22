#!/usr/bin/env python3
"""
Lakshyaclasses — Prompt → Markdown Course Generator (Gemini)

Reads Markdown prompt files from:
  {LAKSHYA_PATH}/content/2_prompt_generate_by_exel/generated_courses_exel/<Class>/<Subject>/*.md

Sends each prompt to Google Gemini and writes Markdown responses to:
  {LAKSHYA_PATH}/content/3_course_generate_by_prompt/generated_courses_exel/<Class>/<Subject>/*.md

ENV VARS:
  LAKSHYA_PATH      -> absolute path to your lakshyaclasses project root (required)
  GEMINI_API_KEY    -> your Gemini API key from Google AI Studio (required)
  GEMINI_MODEL      -> model id (optional; default: gemini-2.5-flash)
  GEMINI_TEMPERATURE (optional; default 0.4)
  GEMINI_MAX_OUTPUT_TOKENS (optional; default 6144)
"""

from __future__ import annotations

import os
import sys
import time
from pathlib import Path
from typing import Optional

from google import genai
from google.genai import types


# ---------- Configuration ----------

# Required project root
try:
    PROJECT_ROOT = Path(os.environ["LAKSHYA_PATH"])
except KeyError as e:
    raise SystemExit("ERROR: LAKSHYA_PATH is not set. Please set it to your project root.") from e

# Input/Output base paths (unchanged from your structure)
INPUT_BASE = PROJECT_ROOT / "content" / "2_prompt_generate_by_exel" / "generated_courses_exel"
OUTPUT_BASE = PROJECT_ROOT / "content" / "3_course_generate_by_prompt" / "generated_courses_exel"

# Gemini config
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
MODEL_ID = os.environ.get("GEMINI_MODEL", "gemini-2.5-flash")  # switch to 'gemini-2.5-pro' if needed

SYSTEM_INSTRUCTION = (
    "You are an education content writer for lakshyaclasses. "
    "Always return clean GitHub‑Flavored Markdown with proper # headings, lists, tables if useful, "
    "and add a short '## Summary' section at the end. "
    "Respond in the SAME LANGUAGE as the prompt (e.g., Hindi if the prompt is in Hindi)."
)
TEMPERATURE = float(os.environ.get("GEMINI_TEMPERATURE", "0.4"))
MAX_OUTPUT_TOKENS = int(os.environ.get("GEMINI_MAX_OUTPUT_TOKENS", "6144"))

# Retry policy for transient errors (429/5xx)
MAX_ATTEMPTS = 3
BACKOFF_SECS = 2.0


# ---------- Gemini client setup ----------

def _make_client() -> genai.Client:
    if not GEMINI_API_KEY:
        raise SystemExit("ERROR: GEMINI_API_KEY is not set. Create a key in Google AI Studio and export it.")
    # Official client for the Gemini Developer API (auto-uses the API key)  # noqa: E501
    return genai.Client(api_key=GEMINI_API_KEY)

CLIENT: genai.Client = _make_client()

# IMPORTANT:
# Do NOT set response_mime_type="text/markdown" (not supported by the API).
# Use system instructions to enforce Markdown formatting.  # noqa: E501
# Allowed response MIME types are text/plain, application/json, application/xml, application/yaml, text/x.enum
# (we omit response_mime_type here so free-form Markdown text is returned).  # noqa: E501

GEN_CONFIG = types.GenerateContentConfig(
    system_instruction=SYSTEM_INSTRUCTION,
    temperature=TEMPERATURE,
    max_output_tokens=MAX_OUTPUT_TOKENS,
)


# ---------- Core generation functions ----------

def generate_markdown(prompt: str) -> str:
    """
    Send a single prompt string to Gemini and return Markdown text.
    """
    resp = CLIENT.models.generate_content(
        model=MODEL_ID,
        contents=prompt,
        config=GEN_CONFIG
    )
    md = resp.text or ""
    if not md.strip():
        md = str(resp)
    return md


def is_transient_error(err: Exception) -> bool:
    """Return True for errors worth retrying (429/5xx), False otherwise (e.g., 400)."""
    msg = str(err)
    # crude but practical detection
    if "429" in msg or " 5" in msg or "UNAVAILABLE" in msg or "DEADLINE_EXCEEDED" in msg:
        return True
    if "INVALID_ARGUMENT" in msg or " 400 " in msg:
        return False
    # default: don't retry
    return False


def generate_markdown_with_retry(prompt: str) -> str:
    """
    Wrapper with exponential backoff for transient errors only.
    """
    last_err: Optional[Exception] = None
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            return generate_markdown(prompt)
        except Exception as e:
            if not is_transient_error(e) or attempt == MAX_ATTEMPTS:
                raise
            sleep_for = BACKOFF_SECS * attempt
            print(f"      Transient error ({e}). Retrying in {sleep_for:.1f}s [{attempt}/{MAX_ATTEMPTS}]...")
            time.sleep(sleep_for)
            last_err = e
    if last_err:
        raise last_err
    raise RuntimeError("Unknown error during generation.")


# ---------- Main traversal ----------

def main() -> None:
    print("Input base: ", INPUT_BASE)
    print("Output base:", OUTPUT_BASE)
    print("Model:", MODEL_ID)

    if not INPUT_BASE.exists():
        raise SystemExit(f"ERROR: Input path does not exist: {INPUT_BASE}")

    # Traverse: Class -> Subject -> *.md prompts
    for class_dir in sorted(INPUT_BASE.iterdir()):
        if not class_dir.is_dir():
            continue
        print(f"\nProcessing class: {class_dir.name}")

        for subject_dir in sorted(class_dir.iterdir()):
            if not subject_dir.is_dir():
                continue
            print(f"  Subject: {subject_dir.name}")

            md_files = sorted(subject_dir.glob("*.md"))
            if not md_files:
                print("    (No .md prompt files found)")
                continue

            for prompt_file in md_files:
                print(f"    Reading file: {prompt_file.name}")
                try:
                    with open(prompt_file, "r", encoding="utf-8") as f:
                        prompt = f.read().strip()

                    if not prompt:
                        print(f"    Skipped (empty prompt): {prompt_file.name}")
                        continue

                    # Call Gemini (with retry for transient errors)
                    response_md = generate_markdown_with_retry(prompt)

                    # Mirror the relative path into the output tree
                    relative_path = prompt_file.relative_to(INPUT_BASE)
                    output_path = OUTPUT_BASE / relative_path
                    output_path.parent.mkdir(parents=True, exist_ok=True)

                    with open(output_path, "w", encoding="utf-8") as f:
                        f.write(response_md)

                    print(f"    Saved output to: {output_path}")

                except Exception as e:
                    print(f"    Error processing {prompt_file.name}: {e}")

    print("\nAll prompts processed and responses saved in structured output folder.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted by user.")
        sys.exit(130)
