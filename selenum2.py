# this code is dedicates to all the school websites where the staff repo is in a table format

import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument("--ignore-ssl-errors=yes")
chrome_options.add_argument("--ignore-certificate-errors")


chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://patrickhenryhs.net/directory")

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

    if len(td_elements) >= 3:  
        # Extract the name, email, and phone number
        name = td_elements[0].find_element(By.CSS_SELECTOR, 'p').text.strip()
        email = td_elements[1].find_element(By.CSS_SELECTOR, 'p').text.strip()
        phone_no = td_elements[2].find_element(By.CSS_SELECTOR, 'p').text.strip()

        # Add the teacher details to the list
        teacher_details.append([name, email, phone_no])    

    # for td_element in td_elements:
    #     td_p = td_element.find_elements(By.CSS_SELECTOR, 'p')

        # for p_element in td_p:
        #     # we need to strip the string; the "mailto" part
        #     try:
        #         a_element = p_element.find_element(By.CSS_SELECTOR, 'a')
        #         print(a_element.get_attribute('href'))
        #     except:
        #         print(p_element.text)

with open('staff_data_yajolla.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['email','phone_no','name'])
    writer.writerows(teacher_details)

# LA JOLLA and CLAIREMONT

# def diffparent_function(parent_element):
#     table_tag= parent_element.find_elements(By.CSS_SELECTOR,'table')
#     tr_elements= parent_element.find_elements(By.CSS_SELECTOR,'tr')


#     for tr_element in tr_elements:
            
#             td_elements = tr_element.find_elements(By.CSS_SELECTOR, 'td')

#             for td_element in td_elements:
#                 print("...")    
#                 try:
                    
#                     if check_for_p_tag(td_element):
#                         # this block is for websites where we find p tag

#                         td_p = td_element.find_elements(By.CSS_SELECTOR, 'p')
#                         for p_element in td_p:
#                             # we need to strip the string; the "mailto" part
#                             try:
#                                 a_element = p_element.find_element(By.CSS_SELECTOR, 'a')
#                                 print(a_element.get_attribute('href'))
#                             except:
#                                 print(p_element.text, "hi")  
#                     else:
#                         # this block is for websites where we find p tag
#                         print(td_element.text)
                        
                        
#                 except:
#                     print("There is an error.")








# LA JOLLA, CLAIRE, MISSIONBAY,HENRY                 
# def diffparent_function(parent_element):
#     table_tag= parent_element.find_elements(By.CSS_SELECTOR,'table')
#     tr_elements= parent_element.find_elements(By.CSS_SELECTOR,'tr')

#     with open('staff_data_la_jolla.csv', 'w', newline='') as csvfile:
#         writer = csv.writer(csvfile, delimiter=',')
#         writer.writerow(['school_name', 'designation','department','email','phone_no','name'])

#         staff_data = []
#         for tr_element in tr_elements:
                
#                 td_elements = tr_element.find_elements(By.CSS_SELECTOR, 'td')

#                 for td_element in td_elements:
#                     try:
                        
#                         if check_for_p_tag(td_element):
#                             # this block is for websites where we find p tag

#                             td_p = td_element.find_elements(By.CSS_SELECTOR, 'p')
#                             for p_element in td_p:
#                                 # we need to strip the string; the "mailto" part
#                                 try:
#                                     a_element = p_element.find_element(By.CSS_SELECTOR, 'a')
#                                     email = a_element.get_attribute('href').split(':')[1]
#                                     name = p_element.text
#                                     department = td_elements[1].text
#                                     staff_data.append({'name': name, 'email': email, 'department': department})
#                                     writer.writerow([name,"none",department,email,"none", name])
#                                 except:
#                                     print(p_element.text, "hi")  
#                         else:
#                             # this block is for websites where we find p tag
#                             print("london")
#                             name = td_element.text
#                             email = td_elements[1].text
#                             department = td_elements[2].text
#                             staff_data.append({'name': name, 'email': email, 'department': department})
#                             writer.writerow([name,"none",department,email,"none", name])
                            
#                     except:
#                         print("There is an error.")
                    
#     return staff_data
# parent_element = driver.find_element(By.CSS_SELECTOR,'[class="pageContent"]')
# diffparent_function(parent_element)





