import csv

import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from env_s import PATH


def get_driver():
    options = Options()
    options.add_argument('headless')
    options.binary_location = PATH
    driver = webdriver.Chrome(options=options)
    return driver

def souper(url):
    driver = get_driver()
    driver.get(url)

    clic_button_cookie_bot(driver)
    time.sleep(4)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup, driver
def clic_button_cookie_bot(driver):
    driver.find_element(By.ID, 'CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
    driver.execute_script("window.scrollBy(0, 500)")
def get_named_(soup):
    named = soup.find('h1', attrs={'class': 'product-family-details__heading'})
    if named != None:
        named = named.text
    return named
def imager(soup):
    images = soup.select('div.slider')
    k = []
    for el in images:
        for el1 in el.find_all('img'):
            k.append("https://norelem.de/"+el1.get('src'))
    img_picture_plan = product_image(soup)
    k.append(img_picture_plan)
    return k
def product_image(soup):
    hrefCore = 'https://norelem.de/'
    source = soup.find('a', attrs={'class': 'product-variants__drawing-image'})
    picture = source.find('picture').find('img').get('src')
    img_href = hrefCore+picture
    return img_href

def parse_table(soup, driver):
    tablearea = soup.find('div', attrs={'class': 'product-table__scroll-wrapper'})
    table = tablearea.find('table', attrs={'class': 'product-table__list'})

    thead = table.find('thead')
    headers = thead.find_all('th')

    matrix = []
    matrics_row = []
    for el in headers[:-3]:
        if el.text == 'AvailabilityPrice':
            matrics_row.append('Availability_Price')
            continue
        if el.text != 'CAD':
            matrics_row.append(el.text.replace('No.', ''))
    matrix.append(matrics_row)

    tbody = table.find('tbody')
    bodys = tbody.find_all('tr', attrs={'data-index': str})
    for Tt in bodys:
        if Tt.get('data-index') == None:
            bodys.remove(Tt)

    element = driver.find_elements(By.CLASS_NAME, 'product-table__code')

    for el, code in zip(bodys, element):
        matrics_row = []
        rows = el.find_all('td', attrs={'class': 'product-table__cell'})
        matrics_row.append(code.text)
        for row_el in rows[1:-3]:
            if row_el.text != '':
                matrics_row.append(row_el.text)
        matrix.append(matrics_row)
    return matrix
def get_itemir(soup, url, driver):
    url = url
    title = soup.find('title').text.strip()
    articul = soup.find('div', attrs={'class': 'family-number product-family-details__family-number'}).text
    named = get_named_(soup)
    price = soup.find('span', attrs={'class': 'product-price__net-price'}).text

    material = soup.find('div', attrs={'class':"product-family-details__materials-description"})
    material = material.text if material != None else '—'

    version = soup.find('div', attrs={'class': "-materials-description--version"})
    version = version.text if version != None else '—'

    images = imager(soup)
    table = parse_table(soup, driver)

    parse_itog = {
        'url': url,
        'title': title,
        'articul': articul,
        'named': named,
        'price': price,
        'material': material,
        'version': version,
        'images': images,
        'table': table
    }
    return parse_itog


def parser(url):
    soup, driver = souper(url)
    parse_page = get_itemir(soup, url, driver)
    return parse_page

def start():
    with open('all_urls.txt', 'r', encoding='utf=8') as file:
        lines = file.readlines()
        i = 0
        with open('data/pages_parse.csv', 'w', encoding='utf=8', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([
                '№',
                'url',
                'title',
                'articul',
                'named',
                'price',
                'material',
                'version',
                'images',
                'table'
            ])
            for line in lines:
                s = line.replace('\n', '')
                if '/c/' not in s and '/p/agid.' in s:

                    i += 1
                    print(i, ' |:| ', s)
                    t1 = time.time()
                    parse_page = parser(s)
                    parse_page['№'] = i

                    writer.writerow([
                        parse_page['№'],
                        parse_page['url'],
                        parse_page['title'],
                        parse_page['articul'],
                        parse_page['named'],
                        parse_page['price'],
                        parse_page['material'],
                        parse_page['version'],
                        parse_page['images'],
                        parse_page['table']
                    ])

                    t2 = time.time()
                    print(t2 - t1)
def main():
    start()

if __name__ == '__main__':
    main()

