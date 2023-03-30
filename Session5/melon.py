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

# 실행할 웹페이지 불러오기 (멜론 차트)
driver.get("https://www.melon.com/index.htm")

# 멜론 차트 버튼 클릭
chartbtn = driver.find_element(By.XPATH, '//*[@id="gnb_menu"]/ul[1]/li[1]/a/span[2]')
chartbtn.click()
time.sleep(3)

# 1위곡명 가져오기
#first = driver.find_element(By.XPATH, '//*[@id="lst50"]/td[6]/div/div/div[1]/span/a').text
#print(first)
time.sleep(3)

# 1위부터 20위까지 가져오기
#for i in range(1,21):
#    titles = driver.find_element(By.XPATH,f"/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a").text
#    print(titles)

# 스크롤 내리기
#driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN)
#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")


# 실시간 급상승 가수 가져오기
rank_now = driver.find_element(By.XPATH,'//*[@id="gnb"]/div[2]')
ActionChains(driver).move_to_element(rank_now).perform()

for i in range(1,11):
    ranklist =  driver.find_element(By.XPATH,f"//html/body/div/div[2]/div/div[1]/div[2]/div/ol/li[{i}]/a").text
    print(ranklist)

# 곡의 장르 가져오기
#chartbtn = driver.find_element(By.XPATH, '//*[@id="lst50"]/td[4]/div/a/span')
#chartbtn.click()
#titles = driver.find_element(By.XPATH, '//*[@id="conts"]/div[2]/div/div[2]/div[2]/dl/dd[2]').text
#print(titles)

# 좋아하는 가수의 곡명 10개
#favorite = favorite.find_element(By.XPATH,'//*[@id="frm_searchArtist"]/div/table/tbody/tr[1]/td[3]/div/div/a[2]')
#favorite.click()
#titles = driver.find_element(By.XPATH, '//*[@id="frm_searchArtist"]/div/table/tbody/tr[1]/td[3]/div/div/a[2]')
#print(titles)



# 순위, 곡명, 가수명 가져오기
for i in range(1,51):
    rank = i
    song = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[1]/span/a').text
    singer = driver.find_element(By.XPATH, f'/html/body/div/div[3]/div/div/div[3]/form/div/table/tbody/tr[{i}]/td[6]/div/div/div[2]/a').text
    print(rank, song, singer)

# csv 파일로 변환
