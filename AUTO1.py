import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.auto1.com/en/our-cars")
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/aside/form/div/ul/li[6]/div").click()
if driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/aside/form/div/ul/li[6]").get_attribute('class') == "checked":
    print "BMW filter selected"
else:
    print "BMW filter not selected"
    print "FAIL"
    driver.quit()
    sys.exit()

try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "loading-ticker")))
    print "looking for loading ticker"
finally:
    print "content loading"
try:
    wait = WebDriverWait(driver, 10)
    wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "loading-ticker")))
    print "waiting for content to be loaded"
finally:
    print "content loaded"

all_cars_are_bmw = True

for elem in driver.find_elements_by_class_name("car-name-top"):
    if "bmw" not in elem.get_attribute("innerHTML").lower():
        all_cars_are_bmw = False

if all_cars_are_bmw:
    print "all cars are bmw"
else:
    print "some cars are not bmw"
    print "FAIL"
    driver.quit()
    sys.exit()

all_cars_have_images = True

for elem in driver.find_elements_by_class_name("car-img"):
    for e in elem.find_elements_by_tag_name("img"):
        if e.get_attribute("src") == "":
            all_cars_have_images = False

if all_cars_have_images:
    print "all cars have images"
else:
    print "some cars do not have images"
    print "FAIL"
    driver.quit()
    sys.exit()

all_cars_have_all_attributes = True

for elem in driver.find_elements_by_class_name("car-info"):
    for e in elem.find_elements_by_tag_name("td"):
        if e.get_attribute("innerHTML") == "":
            all_cars_have_all_attributes = False

if all_cars_have_all_attributes:
    print "all cars have all attributes"
else:
    print "some cars have empty attributes"
    print "FAIL"
    driver.quit()
    sys.exit()

print "PASS" 
driver.quit()
