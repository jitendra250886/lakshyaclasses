import os
import requests

# List of Class 7 NCERT textbook PDF URLs
pdf_urls = [
    # Science
    "https://ncert.nic.in/textbook/pdf/gesc101.pdf",
    "https://ncert.nic.in/textbook/pdf/gesc102.pdf",
    "https://ncert.nic.in/textbook/pdf/gesc103.pdf",
    # Maths
    "https://ncert.nic.in/textbook/pdf/gemh101.pdf",
    "https://ncert.nic.in/textbook/pdf/gemh102.pdf",
    # English Honeycomb
    "https://ncert.nic.in/textbook/pdf/geen101.pdf",
    "https://ncert.nic.in/textbook/pdf/geen102.pdf",
    # English An Alien Hand
    "https://ncert.nic.in/textbook/pdf/geen201.pdf",
    "https://ncert.nic.in/textbook/pdf/geen202.pdf",
    # Hindi Vasant
    "https://ncert.nic.in/textbook/pdf/ghvs101.pdf",
    # Hindi Durva
    "https://ncert.nic.in/textbook/pdf/ghdu101.pdf",
    # Social Science - History
    "https://ncert.nic.in/textbook/pdf/gess101.pdf",
    # Social Science - Geography
    "https://ncert.nic.in/textbook/pdf/gess201.pdf",
    # Social Science - Civics
    "https://ncert.nic.in/textbook/pdf/gess301.pdf",
    # Sanskrit
    "https://ncert.nic.in/textbook/pdf/gsks101.pdf",
    # Urdu
    "https://ncert.nic.in/textbook/pdf/gurd101.pdf"
]

# Folder to save PDFs
folder_name = "NCERT_Class7_PDFs"
os.makedirs(folder_name, exist_ok=True)

# Download each PDF
for url in pdf_urls:
    file_name = url.split("/")[-1]
    file_path = os.path.join(folder_name, file_name)
    response = requests.get(url)
    if response.status_code == 200:
        with open(file_path, "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {file_name}")
    else:
        print(f"Failed to download: {file_name}")
