import re
import os
from datetime import datetime

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

def parser(folder, start_date, end_date):
    
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    url = "https://www.okx.com/help/section/announcements-latest-announcements"

    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox") 
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--disable-dev-shm-usage") 

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    page = driver.page_source

    soup = BeautifulSoup(page, 'html.parser')

    try:
        number_of_pages = int(soup.find_all('a', class_='okui-pagination-item okui-pagination-item-link')[-1].text.strip())
    except:
        number_of_pages = 1


    folder_path = os.path.join(os.getcwd(), folder)

    if not os.path.exists(folder_path):
        os.makedirs(folder)

    for page_number in range(1, number_of_pages + 1):

        if page_number == 1:
            url_current_page = url
        else:
            url_current_page = url + '/page/' + str(page_number)

        driver.get(url_current_page)
        page = driver.page_source
        soup = BeautifulSoup(page, 'html.parser')

        dates_html = soup.find_all('span', attrs={'class': '', 'data-testid': 'DateDisplay'})

        date_format = '%b %d, %Y'
        expression = r'(\w+ \d{1,2}, \d{4})'
        dates = [datetime.strptime(re.search(expression, date.text).group(1), date_format) for date in dates_html]

        page_dates_start = dates[0]
        page_dates_end = dates[-1]

        for i, date_html in enumerate(dates_html):

            if page_dates_end > start_date:
                break

            news_date = dates[i]

            if start_date <= news_date <= end_date:

                driver.get('https://www.okx.com' + date_html.find_parent('a')['href'])
                html_content = driver.page_source
                soup = BeautifulSoup(html_content, 'html.parser')

                for script in soup.find_all('script'):
                    script.decompose()
                cleaned_html = str(soup)

                name = date_html.find_parent('a').find('div', class_='index_title__iTmos index_articleTitle__ys7G7').text
                file_path  = folder_path + '/' + str(news_date.date()) + ' ' + name + '.html'
                
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(cleaned_html)
        

        if page_dates_start < end_date:
            break
