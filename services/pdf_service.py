# === This service module handles PDF generation for LakshyaClasses ===
# It includes functions to:
# 1. Convert Markdown or HTML content into a styled PDF
# 2. Save the PDF to a specified location for student access
# This is useful for exporting notes, worksheets, and submissions.

import pdfkit
import os
import logging

# === PDF configuration ===
PDF_OPTIONS = {
    'page-size': 'A4',
    'encoding': 'UTF-8',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'no-outline': None
}

# === Function: Convert HTML string to PDF ===
def html_to_pdf(html_content, output_path):
    try:
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        pdfkit.from_string(html_content, output_path, options=PDF_OPTIONS)
        logging.info(f"✅ PDF generated at: {output_path}")
        return True
    except Exception as e:
        logging.error(f"❌ Error generating PDF: {e}")
        return False

# === Function: Convert Markdown file to PDF ===
def markdown_to_pdf(md_path, output_path, renderer):
    try:
        html_content = renderer(md_path)
        return html_to_pdf(html_content, output_path)
    except Exception as e:
        logging.error(f"❌ Error converting Markdown to PDF: {e}")
        return False
