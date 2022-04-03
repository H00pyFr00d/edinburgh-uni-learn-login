from subprocess import CREATE_NO_WINDOW

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import os

# Change Chrome options to stop window closing when program terminates and to remove automation header
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

# prepare drivers and set options
driver_path = ChromeDriverManager().install()

chrome_service = Service(driver_path)
chrome_service.creationflags = CREATE_NO_WINDOW

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Navigate to MyEd
driver.get("https://www.ease.ed.ac.uk/cosign.cgi?cosign-eucsCosign-www.myed.ed.ac.uk&https://www.myed.ed.ac.uk/uPortal/Login?refUrl=%2Fmyed-progressive%2F")

# Get user info from .txt file
with open(os.getcwd() + "\\userinfo.txt", "r") as f:
    data = f.read().splitlines()
    f.close()

username = data[0]
password = data[1]

# Enter username and proceed
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"login\")]"))).send_keys(username)
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"submit\")]"))).click()

# Enter password and log in
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"password\")]"))).send_keys(
    password)
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"submit\")]"))).click()
