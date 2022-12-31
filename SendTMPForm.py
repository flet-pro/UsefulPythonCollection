from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from datetime import date
import random
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv('FORM_URL')
tmp_id = os.getenv('TMP_ID')
date_id = os.getenv('DATE_ID')
mail_add = os.getenv('YOUR_EMAIL')
mail_pass = os.getenv('YOUR_PASS')


def random_tmp():
    temp = round(36.0 + random.normalvariate(0, 0.3), 1)
    return str(temp)


def get_date(year=None, month=None, day=None):
    dt = date.today()
    if year:
        dt.replace(year)
    if month:
        dt.replace(month)
    if day:
        dt.replace(day)
    return str(dt)


def generate_url(m_url, tmp_, date_):
    tmp_add = f"&entry.{tmp_}={random_tmp()}"
    date_add = f"&entry.{date_}={get_date()}"
    opt = f"?usp=pp_url{tmp_add}{date_add}"
    n_url = m_url + opt
    return n_url


options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--window-size=1200,1000')
options.add_argument('--lang=ja-JP')

driver = webdriver.Chrome(options=options)

driver.get(generate_url(url, tmp_id, date_id))


def login(m_add, m_pass):
    time.sleep(5)
    mail = driver.find_element(By.NAME, "identifier")
    m_button = driver.find_element(By.CSS_SELECTOR,
                                   ".JnOM6e.TrZEUc.rDisVe")

    mail.clear()
    ActionChains(driver) \
        .send_keys_to_element(mail, m_add) \
        .click(m_button) \
        .perform()

    time.sleep(10)

    password = driver.find_element(By.NAME, "Passwd")
    p_button = driver.find_element(By.CSS_SELECTOR,
                                   ".JnOM6e.TrZEUc.rDisVe")

    password.clear()
    ActionChains(driver) \
        .send_keys_to_element(password, m_pass) \
        .click(p_button) \
        .perform()

    time.sleep(7)


login(mail_add, mail_pass)

send_btn = driver.find_element(By.CSS_SELECTOR, ".uArJ5e.UQuaGc.Y5sE8d.VkkpIf.QvWxOd")

send_btn.click()

time.sleep(10)

driver.quit()
