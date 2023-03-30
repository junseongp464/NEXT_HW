from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import csv


# 디버깅 모드
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_driver = 'C:/Users/박준성/Desktop/NEXT/NEXT_assignment/Session5/chromedriver.exe'
driver = webdriver.Chrome(chrome_driver, options= chrome_options)

#csv 생성
file = open('movie2.csv', mode="w", newline='')
writer = csv.writer(file)
writer.writerow(["영화", "감독", "평점 개수", "리뷰 개수"])

# 실행할 웹페이지 불러오기
driver.get("https://movie.naver.com/movie/bi/mi/basic.naver?code=189000")

#제목, 감독, 평점 + 리뷰 개수
title = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/h3/a').text
director = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[2]/div[1]/dl/dd[2]/p/a').text
rating = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[2]/div[1]/div/span/em').text
review = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[4]/div[5]/div[2]/div[3]/strong/em').text
print(title, director, rating, review)

writer.writerow([title, director, rating, review])
file.close()