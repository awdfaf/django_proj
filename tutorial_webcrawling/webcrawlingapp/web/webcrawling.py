from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WebCrawing:
    # 웹드라이버 변수
    driver = ""
    
    # 생성자
    def __init__(self,url):
        self.url = url
    
    # 웹크롤링 데이터 조회
    def getData(self):
        file_path = "c:/ChromeDriver_exe/chrome_109_driver.exe"
        driver = webdriver.Chrome(file_path)
        # url = "http://www.melon.com/chart/index.htm"
        driver.get(self.url)

        titles = driver.find_elements(By.CSS_SELECTOR,
                                     "tr div.ellipsis.rank01 > span > a")[0:10]
        singers = driver.find_elements(By.CSS_SELECTOR,
                                     "tr div.ellipsis.rank02 > a")[0:10]
        melon_list = []
        rank = 0
        for title, singer in zip(titles, singers):
            rank+=1

            dict = {'no':rank,'title':title.text,'singer':singer.text}
            melon_list.append(dict)
            dict = {}
        self.driver = driver
        return melon_list
    
    # 웹 드라이버 종료
    def webdriver_quit(self):
        time.sleep(3)
        self.driver.quit()