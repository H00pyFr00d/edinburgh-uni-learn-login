import os
from tkinter import *

import keyring
from requests.exceptions import ConnectionError
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

global username, password


def set_username(usr, main):
    global username
    username = usr
    main.destroy()


def set_password(pwd, main):
    global password
    password = pwd
    main.destroy()


def get_username():
    # Creates a tkinter frame
    main = Tk()
    main.title("Please enter your student number (e.g. s2000000)")

    Label(main, text='Username')

    username_box = Entry(main, width=50)
    username_box.grid(row=0, column=1, padx=5)
    username_box.focus_set()

    confirm = Button(main, text="Enter", command=lambda: set_username(username_box.get(), main))
    confirm.grid(row=1, column=1, padx=5, pady=5)

    main.mainloop()


def get_password(usr):
    # Creates a tkinter frame
    main = Tk()
    main.title("Password not found for " + usr)

    Label(main, text='Password').grid(row=0)

    password_box = Entry(main, width=50)
    password_box.grid(row=0, column=1, padx=5)
    password_box.focus_set()

    confirm = Button(main, text="Enter", command=lambda: set_password(password_box.get(), main))
    confirm.grid(row=1, column=1, padx=5, pady=5)

    main.mainloop()


try:
    with open(os.getcwd() + "\\userinfo.txt", "r") as f:
        username = f.read().splitlines()[0]
        f.close()
except(FileNotFoundError, IndexError):
    with open(os.getcwd() + "\\userinfo.txt", "w") as f:
        while True:
            get_username()
            try:
                if (len(username) == 8) & (username[0] == "s"):
                    f.write(username)
                    break
            except IndexError:
                pass
        f.close()

if keyring.get_password("MyEd", username) is None:
    get_password(username)
    keyring.set_password("MyEd", username, password)

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

try:
    driver = webdriver.Chrome(ChromeDriverManager(log_level=0).install(), options=chrome_options)
    driver.get("https://www.ease.ed.ac.uk/cosign.cgi?cosign-eucsCosign-www.myed.ed.ac.uk&https://www.myed.ed.ac.uk/uPortal/Login?refUrl=%2Fmyed-progressive%2F")
except ConnectionError:
    print("Cannot connect to the internet.")

# enter username and proceed
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"login\")]"))).send_keys(
    username)
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"submit\")]"))).click()

# enter password and log in
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"password\")]"))).send_keys(keyring.get_password("MyEd", username))
WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.XPATH, "//*[(@id = \"submit\")]"))).click()

# if we ended up at this page again we've got a wrong user or password
if not driver.current_url.find("https://www.myed.ed.ac.uk/myed-progressive/#/"):
    print("Username or password is incorrect, please check the userinfo.txt and run the program again.")
    keyring.delete_password("MyEd", username)
