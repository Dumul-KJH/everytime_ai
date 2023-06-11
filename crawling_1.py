from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from bs4 import BeautifulSoup
import time
import subprocess
import csv

subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\chrometemp"') # 디버거 크롬 구동


option = Options()
option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
try:
    driver = webdriver.Chrome(options=option)
except:
    chromedriver_autoinstaller.install(True)
    driver = webdriver.Chrome(options=option)

driver.implicitly_wait(2)
# URL for Everytime's Best articles
url = "https://everytime.kr/bestarticle"
driver.get(url)
a = input("시작? : ")

data = []

# Parse the HTML of the page
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
title = soup.find('h2').text
content = soup.find('p',{'class': 'large'}).text
comment_count = soup.find('li', {'title': '댓글'}).text
like_count = soup.find('li', {'title': '공감'}).text
scrap_count = soup.find('li', {'title': '스크랩'}).text
comments_all = soup.find('div', {'class':'comments'})
comments_all = soup.find('div', {'class': 'comments'})
comments_large = comments_all.find_all('p', {'class': 'large'})
comments = [comment.text for comment in comments_large]

post_data = [title, content, comment_count, like_count, scrap_count] + comments
data.append(post_data)

# Save the data to a CSV file
with open('ex2.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Title', 'Content', 'Number of Comments', 'Number of Likes', 'Number of Scraps', 'Comments'])
    writer.writerows(data)


# Loop over each post



driver.quit()
