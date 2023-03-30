from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
from selenium.webdriver.common.action_chains import ActionChains

# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'C:/Users/박준성/Desktop/NEXT/NEXT_assignment/Session5/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

# 실행할 웹페이지 불러오기 (네이버 영화)
driver.get("https://movie.naver.com/")

# 영화랭킹 버튼 클릭
rankbtn = driver.find_element(By.XPATH,'//*[@id="scrollbar"]/div[1]/div/div/ul/li[3]/a')
rankbtn.click()
# rankbtn.implicitly_wait(time_to_wait=10)

#1위부터 20위 가져오기
for i in range(2,12):
    titles = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a").text
    print(i-1, titles)
    
for i in range(13,23):
    titles = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[{i}]/td[2]/div/a").text
    print(i-2, titles)
    
    
#각 페이지 클릭
chartbtn1 = driver.find_element(By.XPATH,f"/html/body/div/div[4]/div/div/div/div/div[1]/table/tbody/tr[2]/td[2]/div/a")
chartbtn1.click()
time.sleep(3)

genre = driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[1]/p/span[1]")
director = driver.find_element(By.XPATH,'/html/body/div/div[4]/div[2]/div[1]/div[2]/div[1]/dl/dd[2]/p/a')
rating = driver.find_element(By.XPATH,"/html/body/div/div[4]/div[2]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/div/em")
print(genre, director, rating)

