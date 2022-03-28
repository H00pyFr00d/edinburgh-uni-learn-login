from getUserInfo import read_contents

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://www.learn.ed.ac.uk/")

data = read_contents()
username = data[0]
password = data[1]

# click login button
driver.find_element(By.XPATH, "//*[contains(concat( \" \", @class, \" \" ), concat( \" \", \"easelogin-bt\", \" \" ))]").click()

# enter username and proceed
driver.find_element(By.XPATH, "//*[(@id = \"login\")]").send_keys(username)
driver.find_element(By.XPATH, "//*[(@id = \"submit\")]").click()

# enter password and log in
driver.find_element(By.XPATH, "//*[(@id = \"password\")]").send_keys(password)
driver.find_element(By.XPATH, "//*[(@id = \"submit\")]").click()
