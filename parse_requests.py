import requests
from bs4 import BeautifulSoup
from env_s import headers, cookies



def Gsoup(url):
    response = requests.get(
        url,
        cookies=cookies,
        headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup
def get_items(soup):
    Title = soup.find('title')
    page_card = soup.select('div.product-family-page')
    for el in page_card:
        print(el.find('div.product-family-details'))
    print(Title.text)
    # print(page_card)
def parser(url):
    soup = Gsoup(url)
    get_items(soup)
def forerhrefs():
    with open('all_hrefs_url/all_urls.txt', 'r', encoding='utf=8') as file:
        lines = file.readlines()
        for line in lines:
            parser(line.replace('\n', ''))


def start():
    forerhrefs()
if __name__ == '__main__':
    start()