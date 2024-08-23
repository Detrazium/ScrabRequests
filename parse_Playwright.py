import csv
from playwright.async_api import async_playwright, expect
from bs4 import BeautifulSoup
import asyncio
from env_s import path_hrefs

async def souper(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup
async def scroll(page):
    # base = await page.get_by_role('div', name='.tabbody')
    # await expect(base).to_be_visible()
    # await base.scroll_into_view_if_needed()
    await page.mouse.wheel(delta_y=100, delta_x=0)
async def click_naw(page):
    await page.locator('#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
    return 'nice'
async def navigation(page):
    """рописать способ прогрузки таблицы до того как скрипт попытается ее найти"""
    try:
        s = await click_naw(page)
    except:
        s = 'nice'
    ll = 0
    while s=='nice':
        ll += 1
        if ll != 10:
            await scroll(page)
        if ll >= 10:
            return


async def get_named_(soup):
    named = soup.find('h1', attrs={'class': 'product-family-details__heading'})
    if named != None:
        named = named.text
    return named
async def product_image(soup):
    hrefCore = 'https://norelem.de/'
    source = soup.find('a', attrs={'class': 'product-variants__drawing-image'})
    picture = source.find('picture').find('img').get('src')
    img_href = hrefCore+picture
    return img_href
async def imager(soup):
    images = soup.select('div.slider')
    k = []
    for el in images:
        for el1 in el.find_all('img'):
            k.append("https://norelem.de/"+el1.get('src'))
    img_picture_plan = await product_image(soup)
    k.append(img_picture_plan)
    return k

async def parse_table(soup):
    tablearea = soup.find('div', attrs={'class': 'product-table__scroll-wrapper'})
    table = tablearea.find('table', attrs={'class': 'product-table__list'})
    return table
ll = 0
async def itemir(soup, url):
    global ll
    url = url
    title = soup.find('title').text.strip()
    articul = soup.find('div', attrs={'class': 'family-number product-family-details__family-number'}).text
    named = await get_named_(soup)
    price = soup.find('span', attrs={'class': 'product-price__net-price'}).text
    material = soup.find('div', attrs={'class': "product-family-details__materials-description"})
    material = material.text if material != None else '—'
    version = soup.find('div', attrs={'class': "-materials-description--version"})
    version = version.text if version != None else '—'
    images = await imager(soup)
    table = await parse_table(soup)

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
    ll += 1
    print(ll, '|', parse_itog['url'])
    return parse_itog

async def get_parse_items(page, url):
    await navigation(page)
    html = await page.content()
    soup = await souper(html)
    items = await itemir(soup, url)
    return items

async  def async_worker(context, path_hrefs_folder, num):
    with open(path_hrefs_folder, 'r', encoding='utf=8') as hand:
        hand = hand.readlines()
        with open(f'data/pages_parseSource__{num}__.csv', 'w', encoding='utf=8', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([
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
            for url in hand:
                urld = url[5:].replace('\n', '').split('|| ')
                ww = 'https'+ urld[0]
                page = await context.new_page()
                await page.goto(url = ww, timeout=0)
                itog = await get_parse_items(page, url)
                await asyncio.sleep(4)
                await page.close()
                writer.writerow([
                    itog['url'],
                    itog['title'],
                    itog['articul'],
                    itog['named'],
                    itog['price'],
                    itog['material'],
                    itog['version'],
                    itog['images'],
                    itog['table']
                ])

async def taskerser(context, path_hrefs):
    async with asyncio.TaskGroup() as tg:
        for hrefer, num in zip(path_hrefs, range(10)):
            tasks = tg.create_task(async_worker(context, hrefer, num))

async def main(path_hrefs):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        await taskerser(context, path_hrefs)

asyncio.run(main(path_hrefs))