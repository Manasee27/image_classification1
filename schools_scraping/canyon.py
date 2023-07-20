import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--ignore-ssl-errors=yes")
chrome_options.add_argument("--ignore-certificate-errors")


chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.lajollahigh.sandiegounified.org/academics/staff_list")

def check_for_p_tag(td_element):
    """
    Check if there is a <p> tag inside the given <td> tag.

    Args:
        td_element (WebElement): The <td> tag to check.

    Returns:
        bool: True if there is a <p> tag inside the <td> tag, False otherwise.
    """
    td_p = td_element.find_elements(By.CSS_SELECTOR, 'p')

    if td_p:
        return True
    else:
        return False


wait = WebDriverWait(driver, 20)
parent_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '[class="row"]')))
print("lolllllollll")

div_elements = parent_element.find_element(By.CSS_SELECTOR, 'div[class="person"]')
# tr_elements= parent_element.find_elements(By.CSS_SELECTOR,'tr')
print(div_elements,"hey")
# LA JOLLA

teacher_details = []

# iterating through the tr tags ( extracting name, email, etc)

 
       # Extract the name, email, and phone number
for div_element in div_elements:
    print(div_element,"hello")
    try:

        name_desig = div_elements[0]
        name= name_desig.find_element(By.CSS_SELECTOR, 'a').text.strip()
        designation= name_desig[1].text
        print(name, designation)
                
        phone_email = div_elements[1]
        phone=phone_email.find_element(By.CSS_SELECTOR, 'a').text.strip()
        email=phone_email[1]
        print(email, phone)

                # email = div_elements[2].find_element(By.CSS_SELECTOR, 'a')
        print("emmmmmmmmmm")
                

                #  here we are directly taking the path of the element from the inspect of the website ( for the school name )
        school_name_xpath='/html/body/div[1]/div[2]/div[2]/div[3]/div/div/div[2]/div[1]/div[1]'
        school_name_element = driver.find_element(By.XPATH, school_name_xpath)
        school_name = school_name_element.text
                    
        teacher_details.append([name, email, designation,phone,school_name]) 
        print(teacher_details)
            # Add the teacher details to the list
    except:
        continue
               
with open('staff_data_canyon.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['name','email_address','designation','phone','school_name'])
    writer.writerows(teacher_details)

