import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument("--ignore-ssl-errors=yes")
chrome_options.add_argument("--ignore-certificate-errors")


chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.missionbay.sandiegounified.org/staff/staff_directories/classroom_teacher_directory")


# ALL THE FUNCTIONS
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


parent_element = driver.find_element(By.CSS_SELECTOR,'[class="pageContent"]')

table_tag= parent_element.find_elements(By.CSS_SELECTOR,'table')
tr_elements= parent_element.find_elements(By.CSS_SELECTOR,'tr')

# LA JOLLA

teacher_details = []

# iterating through the tr tags ( extracting name, email, etc)

for tr_element in tr_elements:
    td_elements = tr_element.find_elements(By.CSS_SELECTOR, 'td')

    if len(td_elements) <= 5:  
        # Extract the name, email, and phone number
        try:

            name = td_elements[0].text
            print(name)
            department = td_elements[1].text
            print(department)
            phone_extension= td_elements[2].text
            print(phone_extension)
            email_address1 = td_elements[3].text
            print(email_address1,"em")

            

            #  here we are directly taking the path of the element from the inspect of the website ( for the school name )
            school_name_xpath='/html/body/form/div[3]/div[3]/div/div[2]/a/div[1]'
            school_name_element = driver.find_element(By.XPATH, school_name_xpath)
            school_name = school_name_element.text
                
            teacher_details.append([name, email_address1,department,phone_extension,school_name]) 
            print(teacher_details)
        # Add the teacher details to the list
        except:
            continue
               
with open('staff_data_missionbay.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['name','email_address','deprtment','phone_extension','school_name'])
    writer.writerows(teacher_details)