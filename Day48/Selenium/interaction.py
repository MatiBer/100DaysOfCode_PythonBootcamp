from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
# chrome_driver_path = ""
driver = webdriver.Chrome(options=chrome_options)

driver.get("http://secure-retreat-92358.herokuapp.com/")

# number_of_articles = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(number_of_articles.text)
# number_of_articles.click()

# all_portals = driver.find_element("All portals")
# all_portals.click()

# search_button = driver.find_element(by=By.ID, value="Search Wikipedia [alt-shift-f]")
# search_button.click()
# search = driver.find_element(by=By.CSS_SELECTOR, value="search")
# search.send_keys("Python")

first_name = driver.find_element(by=By.NAME, value="fName")
first_name.send_keys("Mati")
last_name = driver.find_element(by=By.NAME, value="lName")
last_name.send_keys("Ber")
email = driver.find_element(by=By.NAME, value="email")
email.send_keys("MatiBer@email.com")

submit = driver.find_element(by=By.CSS_SELECTOR, value="form button")
submit.click()

# driver.quit()