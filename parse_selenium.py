from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def get_driver():
    options = Options()
    options.add_argument('headless')
    options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    driver = webdriver.Chrome(options=options)
    return driver
def souper(url):
    print(1, " |:| ", url)
    driver = get_driver()
    driver.get(url)
    time.sleep(0.1)
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
def img_pict(soup):
    img = soup.select('section.acc-tab__content')
    # print(img)
    for el in img:
        print(el.find('img'))
    # print('https://norelem.de/'+img)
    return
def get_itemir(soup, url):
    # url = url
    # title = soup.find('title').text.strip()
    # articul = soup.find('div', attrs={'class': 'family-number product-family-details__family-number'}).text
    # named = get_named_(soup)
    # price = soup.find('span', attrs={'class': 'product-price__net-price'}).text
    # price_discount = None
    # images = imager(soup)
    image_picture = img_pict(soup)
    # material = soup.find('div', attrs={'class':"product-family-details__materials-description"}).text
    print(image_picture)

def parser(url):
    soup = souper(url)
    get_itemir(soup, url)

def start():
    with open('all_urls.txt', 'r', encoding='utf=8') as file:
        lines = file.readlines()
        for line in lines:
            parser(line.replace('\n', ''))
start()

