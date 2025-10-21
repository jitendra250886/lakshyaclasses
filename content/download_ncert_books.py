import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Setup Chrome options
chrome_options = Options()
# chrome_options.add_argument("--headless")  # Uncomment to run in background
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Setup WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 30)

# Load NCERT page
driver.get("https://ncert.nic.in/textbook.php")
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Wait for dropdowns
selects = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "select")))
if len(selects) < 3:
    print("❌ Not enough dropdowns found.")
    driver.quit()
    exit()

# Identify dropdowns
class_select = Select(selects[0])
subject_select = Select(selects[1])
book_select = Select(selects[2])

class_options = [opt.get_attribute("value") for opt in class_select.options if opt.get_attribute("value")]

for class_value in class_options:
    class_select.select_by_value(class_value)
    time.sleep(2)

    # Refresh subject dropdown
    # Wait until subject dropdown has more than 1 option
    
    # Retry loop to wait for subject dropdown to update
    for attempt in range(5):
        try:
            subject_element = driver.find_element(By.ID, "subject")
            subject_select = Select(subject_element)
            subject_options = [opt.get_attribute("value") for opt in subject_select.options if opt.get_attribute("value")]
            if len(subject_options) > 1:
                break
            else:
                print(f"Waiting for subject dropdown to populate... Attempt {attempt + 1}")
                time.sleep(2)
        except Exception as e:
            print(f"Error accessing subject dropdown: {e}")
            time.sleep(2)
    else:
        print(f"Subject dropdown failed to load for class {class_value}. Skipping.")
        continue

    subject_options = [opt.get_attribute("value") for opt in subject_select.options if opt.get_attribute("value")]

    for subject_value in subject_options:
        if subject_value not in subject_options:
            print(f"Subject '{subject_value}' not found for class '{class_value}'. Skipping.")
            continue

        subject_select.select_by_value(subject_value)
        time.sleep(2)

        # Refresh book dropdown
        wait.until(EC.presence_of_element_located((By.ID, "book")))
        book_select = Select(driver.find_element(By.ID, "book"))
        book_options = [opt.get_attribute("value") for opt in book_select.options if opt.get_attribute("value")]

        for book_value in book_options:
            if book_value not in book_options:
                print(f"Book '{book_value}' not found. Skipping.")
                continue

            book_select.select_by_value(book_value)
            time.sleep(2)

            driver.find_element(By.NAME, "button").click()
            time.sleep(3)

            folder_path = os.path.join("ncert_books", f"Class_{class_value}", f"Subject_{subject_value}", f"Book_{book_value}")
            os.makedirs(folder_path, exist_ok=True)

            try:
                download_all = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Download All")))
                download_all.click()
                time.sleep(2)

                download_links = driver.find_elements(By.XPATH, "//a[contains(@href, '.pdf') or contains(@href, '.zip') or contains(@href, '.srt')]")

                for link in download_links:
                    file_url = link.get_attribute("href")
                    file_name = link.text.strip().replace(" ", "_")
                    file_path = os.path.join(folder_path, file_name)

                    response = requests.get(file_url)
                    with open(file_path, "wb") as f:
                        f.write(response.content)
                    print(f"✅ Downloaded: {file_path}")

            except Exception as e:
                print(f"❌ Could not download files for Class {class_value}, Subject {subject_value}, Book {book_value}: {e}")

            # Go back and re-select dropdowns
            driver.get("https://ncert.nic.in/textbook.php")
            wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
            selects = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, "select")))
            class_select = Select(selects[0])
            subject_select = Select(selects[1])
            book_select = Select(selects[2])
            class_select.select_by_value(class_value)
            subject_select.select_by_value(subject_value)

# Close browser
driver.quit()
print("🎉 All available files have been downloaded and organized.")