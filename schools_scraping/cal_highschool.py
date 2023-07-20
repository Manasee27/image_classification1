import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument("--ignore-ssl-errors=yes")
chrome_options.add_argument("--ignore-certificate-errors")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://chs.wuhsd.org/apps/staff/")
parent_element = driver.find_element(
    By.CSS_SELECTOR, '[class="list"]'
)
# Find the <li> tags within the parent element
# by_tag_name = By.TAG_NAME("li")
# li_tags = driver.find_elements(by_tag_name)
li_tags = parent_element.find_elements(By.CSS_SELECTOR, '[class="staff"]')
# create a csv with 3 columns
with open("staff_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(["name", "designation", "email"])
    for li_tag in li_tags:
        # Get the name
        name = li_tag.find_element(By.CSS_SELECTOR, '[class="name"]')
        # get designation
        try:
            designation = li_tag.find_element(
                By.CSS_SELECTOR, '[class="user-position user-data"]'
            )
            designation_text = designation.get_attribute("textContent")
            email = li_tag.find_element(By.CSS_SELECTOR, '[class="email"]')
            email_address = email.get_attribute("href")
            print(name.text, designation_text, email_address)
            writer.writerow([email_address, designation_text, name.text])
        except:
            email = li_tag.find_element(By.CSS_SELECTOR, '[class="email"]')
            email_address = email.get_attribute("href")
            print(name.text, "No designation found!")
            writer.writerow(["No designation", name.text, email_address])
csvfile.close()
