# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options

# options = Options()
# # options.add_argument("--headless=new")  # Optional: comment out for now
# options.add_argument("--no-sandbox")
# options.add_argument("--disable-dev-shm-usage")
# options.add_argument("--disable-gpu")
# options.add_argument("--remote-debugging-port=9222")
# options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# service = Service(r"C:\tools\chromedriver\chromedriver.exe")
# driver = webdriver.Chrome(service=service, options=options)

# driver.get("https://byjus.com/cbse-notes/cbse-class-7-science-notes-chapter-1-nutrition-in-plants/")
# #driver.get("https://edurev.in/t/407611/Exploring-Substances-Acidic--Basic-and-Neutral-Class-7-Notes-Science-Chapter-2")
# html = driver.page_source

# with open("edurev_chapter2.html", "w", encoding="utf-8") as f:
#     f.write(html)

# driver.quit()
# print("✅ Page saved")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
# Comment out headless for now
# options.add_argument("--headless=new")

# Stability flags
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")

# Optional: explicitly set Chrome binary
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Use direct path to ChromeDriver
service = Service(r"C:\tools\chromedriver\chromedriver.exe")

# Launch browser
driver = webdriver.Chrome(service=service, options=options)

# Navigate and wait
driver.get("https://www.google.com")
time.sleep(5)

print("✅ Chrome launched and navigated successfully")
driver.quit()
