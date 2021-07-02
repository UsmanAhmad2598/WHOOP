#Web Scraper Using Selenium and Beautiful Soup
#Author: Usman Ahmad

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import xlsxwriter
from bs4 import BeautifulSoup


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(3)
driver.get("https://www.colgate.edu/about/directory")

#Sign into the page
signButton = driver.find_element_by_xpath("/html/body/div[2]/header/div[1]/div/nav/div[3]/nav/ul/li[4]/a")
signButton.click()

#Enter Username
user = driver.find_element_by_xpath('.//*[@id="username"]')
user.clear()
user.send_keys("uahmad@colgate.edu")

#Enter Password
password = driver.find_element_by_xpath('.//*[@id="password"]')
password.clear()
password.send_keys("*") #Password hidden

#Click Login
loginButton = driver.find_element_by_id("submit")
loginButton.click()

#Choose student from the drop down Menu
selectElement = Select(driver.find_element_by_id("edit-directory-roles"))
selectElement.select_by_visible_text("Student")

#Click browse
wait = WebDriverWait(driver,10)
browseButton = wait.until(EC.element_to_be_clickable((By.XPATH, './/*[@id="edit-submit-directory-search"]')))
time.sleep(2)
browseButton.click()
time.sleep(5)


fileCount = 1

#Click next until last page is reached
while True:
    time.sleep(3)
    # Make HTML File
    nameOfFile = "File " + str(fileCount) + ".html" 
    with open(nameOfFile, "w") as f:
        f.write(driver.page_source)
        f.close()
    
    fileCount+=1
    
    address = '//a[@title="Go to next page"]'
    # Go To Next Page
    wait = WebDriverWait(driver,10)
    time.sleep(3)
    try:
        nextButton = wait.until(EC.element_to_be_clickable((By.XPATH, address)))
        #nextButton = driver.find_element_by_xpath((address))
        nextButton.location_once_scrolled_into_view
        time.sleep(5)
        nextButton.click()
    except:
        break
    
print("File Count: ", fileCount)


#Go through all the HTML files and put all the data into Excel
workbook = xlsxwriter.Workbook("Email Addresses.xlsx")
worksheet = workbook.add_worksheet()
row = col = 1
index = 1
while index <=fileCount:
    fileName = "File " + str(index) + ".html" 
    with open(fileName, 'r') as html_file:
        soup = BeautifulSoup(html_file, 'lxml')
        for emailTag in soup.find_all('a',class_="directory-member__contact-method label-icon label-icon--email" ):
            email = emailTag.find('span')
            emailAddress = email.text
            worksheet.write(row,col, emailAddress)
            row+=1
    index +=1
workbook.close()

print("All Done")

driver.close()







