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
a = input("시작? : ")

data = []
page = 1
check = True;
while check:
    url = "https://everytime.kr/hotarticle/p/"+str(page)
    driver.get(url)
    time.sleep(2)
    # Parse the HTML of the page
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # Get the posts
    posts = soup.find_all('article')

    for post in posts:
        a_tag = post.find('a')
        if a_tag == None:
            check = False
            break
        href = "https://everytime.kr"+a_tag['href']
        driver.get(href)
        time.sleep(2)
        html2 = driver.page_source
        soup2 = BeautifulSoup(html2, 'html.parser')
        try:
            title = soup2.find('h2').text
            content = soup2.find('p',{'class': 'large'}).text
            comment_count = soup2.find('li', {'title': '댓글'}).text
            like_count = soup2.find('li', {'title': '공감'}).text
            scrap_count = soup2.find('li', {'title': '스크랩'}).text
            comments_all = soup2.find('div', {'class':'comments'})
            comments_all = soup2.find('div', {'class': 'comments'})
            comments_large = comments_all.find_all('p', {'class': 'large'})
            comments = [comment.text for comment in comments_large]

            post_data = [title, content, comment_count, like_count, scrap_count] + comments
            data.append(post_data)

            # Save the data to a CSV file
            with open('everytime_hotarticle.csv', 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Title', 'Content', 'Number of Comments', 'Number of Likes', 'Number of Scraps', 'Comments'])
                writer.writerows(data)
        except:
            print(href)

    page += 1
    if page == 50:
        break

# Loop over each post



driver.quit()
