from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
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
    time.sleep(0.3)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    return soup
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
    return k

def parse_table(soup):
    table = soup.find('table', attrs={'class': 'hover-v'})
    for el in table:
        print(el.find('th'))
    return
def get_itemir(soup, url):
    # url = url
    # title = soup.find('title').text.strip()
    # articul = soup.find('div', attrs={'class': 'family-number product-family-details__family-number'}).text
    # named = get_named_(soup)
    # price = soup.find('span', attrs={'class': 'product-price__net-price'}).text
    # price_discount = None
    # material = soup.find('div', attrs={'class':"product-family-details__materials-description"}).text
    # images = imager(soup)
    product_drawing = None
    table = parse_table(soup)



def parser(url):
    soup = souper(url)
    get_itemir(soup, url)

def start():
    with open('all_urls.txt', 'r', encoding='utf=8') as file:
        lines = file.readlines()
        i = 1
        for line in lines:
            s = line.replace('\n', '')
            print(i, ' |:| ', s)
            parser(s)
            i+=1
start()

