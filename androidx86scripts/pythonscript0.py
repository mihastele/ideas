import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the download to complete
download_dir = os.path.expanduser("~") + "/Downloads"
filename = "android-x86_64-9.0-r2.iso"

# Set up the Selenium driver
driver = webdriver.Chrome()
driver.get("https://www.fosshub.com/Android-x86.html")

# Wait for the page to load
wait = WebDriverWait(driver, -1)
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-download=true]")))

# Find the download link for the Android image
android_link = None
for link in driver.find_elements(By.CSS_SELECTOR, "a[data-download=true]"):
    if "android" in link.get_attribute("href"):
        android_link = link
        break

# Click the download link for the Android image
if android_link is not None:
    android_link.click()

    time.sleep(5)  # Wait for the download to start


    ### Lock until download
    download_dir = os.path.expanduser("~") + "/Downloads"
    filename_prefix = "android-x86_64-9.0-r2.iso"
    filename_suffix = ".crdownload"

    for filename in os.listdir(download_dir):
        while filename.startswith(filename_prefix) and filename.endswith(filename_suffix):
            time.sleep(5)
            break
        
else:
    print("Could not find download link for Android image")


wait = WebDriverWait(driver, 300)
wait.until(lambda driver: any(filename in f for f in os.listdir(download_dir)))

# Close the browser
driver.quit()