import csv
from playwright.async_api import async_playwright, expect
from bs4 import BeautifulSoup
import asyncio
from env_s import path_hrefs

"""Это парсер табличных товаров родительского парсера"""
async def mosis(page):
    html = await page.content()
    soup = await souper(html)
    return soup
async def new_named(soup):
    named = soup.find('h1', attrs={'class': 'product-details__name'})
    if named != None:
        named = named.text
    return named
async def dFeat(soup):
    detf = soup.find_all('div', attrs={'class': 'product-details__features'})
    # if detf != None:
    #     detf = detf.text
    return detf
async def dmaterial(soup):
    material = soup.find('div', attrs={'class': "product-family-details__materials-description"})
    material = material.text if material != None else '—'
    return material
async def dver(soup):
    ver = soup.find('div', attrs={'class': "-materials-description--version"})
    ver = ver.text if ver is not None else '—'
    return ver
async def dCcater(soup):
    table_wert = soup.find('div', attrs={'class': 'category-texts__table'})
    items = table_wert.find_all('div', attrs={'class', 'category-texts__cell -product'})
    lister = {}
    for di in items:
        text = di.find('div', attrs={'class': 'category-texts__cell-text'}).text
        head = di.find('span', attrs={'class': 'category-texts__cell-headline-backgroundcolor--norelem'}).text
        lister[head] = text
    return lister
async def desTable(soup):
    table = soup.find('div', attrs={'class': 'nlm-category-texts'})
    # for ell in table:
    #     print(ell.text)
    return
async def cat_bul_points(soup):
    html_ul = soup.find('div', attrs={'nlm-category-bullet-points'})
    find_all_li = html_ul.find_all('li')
    k = ''
    for el in find_all_li:
        k += el.text
        k += ' '
    return k
async def doich_items(soup, page,url):
    url = url
    three = url.replace('https://norelem.de/en', '')
    title = soup.find('title').text.strip()
    articul = soup.find('div', attrs={'class': 'family-number product-family-details__family-number'}).text
    named = await new_named(soup)
    price = soup.find('span', attrs={'class': 'product-price__net-price'}).text
    material = await dmaterial(soup)
    product_details = ''.join([df.text for df in await dFeat(soup)])
    version = await dver(soup)
    images = await imager(soup, d='-i')
    table = '—'
    category_texts = await dCcater(soup)
    descript_table = await desTable(soup)
    category_bullet_points = await cat_bul_points(soup)

    parse_itog = {
        'url': url,
        'three_product': three,
        'title': title,
        'articul': articul,
        'named': named,
        'price': price,
        'material': material,
        'version': version,
        'images': images,
        'table': table,
        'product_details': product_details,
        'category_table_text': category_texts,
        'category_bullet_points': category_bullet_points,
        'descript_table': descript_table
    }
    return parse_itog
async def parseTable_hrefs(context, urls_three, writer):
    for urls in urls_three:
        page = await context.new_page()
        await page.goto(url=urls, timeout=0)
        await navigation(page)
        items = await doich_items(await mosis(page), page, urls)
        writer.writerow([
                items['url'],
                items['three_product'],
                items['title'],
                items['articul'],
                items['named'],
                items['price'],
                items['material'],
                items['version'],
                items['images'],
                items['table'],
                items['product_details'],
                items['category_table_text'],
                items['category_bullet_points'],
                items['descript_table']
        ])
        await page.close()

"""Родительский парсер"""
ll = 0
async def souper(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup
async def scroll(page):
    await page.mouse.wheel(delta_y=100, delta_x=0)

async def click_naw(page):
    if await page.query_selector('#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll') is not None:
        await page.locator('#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
    return 'nice'
async def navigation(page):
    try:
        s = await click_naw(page)
    except:
        s = 'nice'
    ll = 0
    while s == 'nice':
        ll += 1
        if ll != 20:
            await scroll(page)
        if ll >= 20:
            return 'lol'


async def get_named_(soup):
    named = soup.find('h1', attrs={'class': 'product-family-details__heading'})
    if named != None:
        named = named.text
    return named
async def product_image(soup, d = None):
    hrefCore = 'https://norelem.de/'
    if d == '-i':
        source = soup.find_all('a', attrs={'class': 'product-drawings-component'})
        imL = []
        for ims in source:
            pic = ims.find('picture').find('img').get('src')
            img = hrefCore+pic
            imL.append(img)
        return imL
    source = soup.find('a', attrs={'class': 'product-variants__drawing-image'})
    picture = source.find('picture').find('img').get('src')
    img_href = hrefCore+picture
    return img_href
async def imager(soup, d = None):
    images = soup.select('div.slider')
    k = []
    for el in images:
        for el1 in el.find_all('img'):
            k.append("https://norelem.de/"+el1.get('src'))
    if d == '-i':
        img_pic_plan = await product_image(soup, d ='-i')
        for ell in img_pic_plan:
            k.append(ell)
        return k
    else:
        img_picture_plan = await product_image(soup)
        k.append(img_picture_plan)
        return k

async def parse_table(soup):
    tablearea = soup.find('div', attrs={'class': 'product-table__scroll-wrapper'})
    table = tablearea.find('table', attrs={'class': 'product-table__list'})
    return table

async def product_versions(page):
    versions  = await page.query_selector_all('a.product-table__code')
    lst = []
    for ele in versions:
        href = 'https://norelem.de/en' + await ele.get_attribute('href')
        lst.append(href)
        # print(href)

    return lst

async def itemir(soup, url, page):
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

    products_list_versions = await product_versions(page)

    parse_itog = {
        'url': url,
        'three_product': url.replace('https://norelem.de/en', ''),
        'title': title,
        'articul': articul,
        'named': named,
        'price': price,
        'material': material,
        'version': version,
        'images': images,
        'table': table
    }
    # ll += 1
    # print(ll, '|', parse_itog['url'])
    return parse_itog, products_list_versions

async def get_parse_items(page, url):
    # global ll
    # ll += 1
    # print(ll, '|', url)
    li = await navigation(page)
    await page.wait_for_timeout(10)
    if li == 'lol':
        await page.wait_for_selector('a.product-variants__drawing-image')
        await page.wait_for_selector('div.product-table__scroll-wrapper')
        await page.wait_for_selector('table.product-table__list')
        html = await page.content()
        soup = await souper(html)
        items, veris = await itemir(soup, url, page)
        return items, veris

async  def async_worker(context, path_hrefs_folder, num):
    with open(path_hrefs_folder, 'r', encoding='utf=8') as hand:
        hand = hand.readlines()
        with open(f'data/pages_parseSource__{num}__.csv', 'w', encoding='utf=8', newline='') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerow([
                'url',
                'three_product',
                'title',
                'articul',
                'named',
                'price',
                'material',
                'version',
                'images',
                'table',
                'product_details',
                'category_table_text',
                'category_bullet_points',
                'descript_table'
            ])
            for url in hand:
                urld = url[5:].replace('\n', '').split('|| ')
                ww = 'https'+ urld[0]
                page = await context.new_page()
                await page.goto(url = ww, timeout=0)
                itog, versis = await get_parse_items(page, url)
                # await asyncio.sleep(4)
                await page.close()
                writer.writerow([
                    itog['url'],
                    itog['three_product'],
                    itog['title'],
                    itog['articul'],
                    itog['named'],
                    itog['price'],
                    itog['material'],
                    itog['version'],
                    itog['images'],
                    itog['table'],
                    '—',
                    '—',
                    '—',
                    '—'
                ])
                await parseTable_hrefs(context, versis, writer)


async def taskerser(context, path_hrefs):
    async with asyncio.TaskGroup() as tg:
        for hrefer, num in zip(path_hrefs, range(10)):
            tasks = tg.create_task(async_worker(context, hrefer, num))

async def mainE(path_hrefs):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        await taskerser(context, path_hrefs)

def start_parse():
    asyncio.run(mainE(path_hrefs))
def main():
    start_parse()

if __name__ == '__main__':
    main()