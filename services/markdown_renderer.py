# === This service module handles Markdown rendering for LakshyaClasses ===
# It includes functions to:
# 1. Read a Markdown (.md) file from disk
# 2. Convert its content into styled HTML using Python-Markdown
# 3. Return the HTML string for use in templates or PDF generation
# This allows dynamic previewing of notes, worksheets, and submissions.

import markdown
import os
import logging

# === Function: Render Markdown file to HTML string ===
def render_markdown(md_path):
    try:
        if not os.path.exists(md_path):
            raise FileNotFoundError(f"Markdown file not found: {md_path}")

        with open(md_path, "r", encoding="utf-8") as f:
            md_content = f.read()

        html = markdown.markdown(
            md_content,
            extensions=['extra', 'tables', 'toc'],
            output_format='html5'
        )

        return html

    except FileNotFoundError as fnf_error:
        logging.warning(f"📄 Missing Markdown file: {fnf_error}")
        return "<p>Markdown file not found.</p>"

    except Exception as e:
        logging.error(f"❌ Error rendering Markdown: {e}")
        return "<p>Error loading content.</p>"
