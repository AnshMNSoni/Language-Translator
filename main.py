from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pyautogui


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)


text = input('⬇️  Enter you text here ⬇️\n')
print('\n')
lang = input('In which Language, Do you want to translate: ').capitalize()


driver = webdriver.Chrome(options=chrome_options)
driver.get(url='https://quillbot.com/translate')


input_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'translate-input-box'))
)
input_box.send_keys(text)


into_lang = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[3]/section[1]/div/div/div/section/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div/div[4]/div/div/div/div/div/div/button'))
)
into_lang.click()


search = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'search-items'))
)
search.send_keys(lang)

pyautogui.moveTo(852, 438, duration=1)
pyautogui.leftClick()

translate = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[3]/section[1]/div/div/div/section/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div[1]/div[1]/div/div[2]/div/div/div/div[2]/div/span/button/span[1]"))
)
translate.click()