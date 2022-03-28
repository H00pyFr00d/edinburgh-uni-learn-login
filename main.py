from getUserInfo import read_contents

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get("https://www.ease.ed.ac.uk/cosign.cgi?cosign-eucsCosign-www.myed.ed.ac.uk&https://www.myed.ed.ac.uk/uPortal/Login?refUrl=%2Fmyed-progressive%2F")

data = read_contents()
username = data[0]
password = data[1]

# enter username and proceed
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"login\")]"))).send_keys(username)
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"submit\")]"))).click()

# enter password and log in
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"password\")]"))).send_keys(password)
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"submit\")]"))).click()
