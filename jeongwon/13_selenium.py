from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://naver.com")

elem = browser.find_element(By.ID, "query")

elem.send_keys("나도코딩")

elem.send_keys(Keys.ENTER)

elem = browser.find_elements(By.TAG_NAME, "a")

for e in elem:
    e.get_attribute("href")


browser.get("http://daum.net")

elem = browser.find_element(By.ID, "q")

elem.send_keys("나도코딩")

elem = browser.find_element(By.XPATH, "//*[@id='daumSearch']/fieldset/div/div/button[2]")
elem.click()

browser.close() # 현재 탭만 닫기
browser.quit() # 모든 탭 닫기