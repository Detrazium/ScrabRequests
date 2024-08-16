import requests

cookie = {
    'anonymous-consents': '%5B%5D',
    'cookie-notification': 'NOT_ACCEPTED',
    'CookieConsent': '{stamp:%27VAC52xJALuXO4pVb85zbJ+TGAmnZpQHe3zeJwX2b9LekW6wqJHfmCg==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:7%2Cutc:1723721271645%2Cregion:%27ru%27}',
    '_gcl_au': '1.1.2069399862.1723721279',
    'leaderboardBanner': 'visited',
    'lastViewedProducts_N_3000_10_10_de': 'agid.2133|agid.2245|agid.21541|agid.3663|agid.22589|agid.15160|agid.22644',
    'lastViewedProductsTimestamp_N_3000_10_10_de': '8/15/24|#3:47:48#PM#GMT',
    'JSESSIONID': '9BB8C94AB70357E5E8FF288429653E41.accstorefront-5bf9879c96-78n9b',
    'ROUTE': '.accstorefront-5bf9879c96-78n9b',
    '_clck': 'r8oig6%7C2%7Cfod%7C0%7C1688',
    '_clsk': '1xgz5vd%7C1723788840035%7C2%7C1%7Ct.clarity.ms%2Fcollect',
    '_uetsid': '6e1dd1105af911ef9032dd17a32a802e',
    '_uetvid': '6e1dfb105af911efa40cd565ee808165',
}
header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'anonymous-consents=%5B%5D; cookie-notification=NOT_ACCEPTED; CookieConsent={stamp:%27VAC52xJALuXO4pVb85zbJ+TGAmnZpQHe3zeJwX2b9LekW6wqJHfmCg==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:7%2Cutc:1723721271645%2Cregion:%27ru%27}; _gcl_au=1.1.2069399862.1723721279; leaderboardBanner=visited; lastViewedProducts_N_3000_10_10_de=agid.2133|agid.2245|agid.21541|agid.3663|agid.22589|agid.15160|agid.22644; lastViewedProductsTimestamp_N_3000_10_10_de=8/15/24|#3:47:48#PM#GMT; JSESSIONID=9BB8C94AB70357E5E8FF288429653E41.accstorefront-5bf9879c96-78n9b; ROUTE=.accstorefront-5bf9879c96-78n9b; _clck=r8oig6%7C2%7Cfod%7C0%7C1688; _clsk=1xgz5vd%7C1723788840035%7C2%7C1%7Ct.clarity.ms%2Fcollect; _uetsid=6e1dd1105af911ef9032dd17a32a802e; _uetvid=6e1dfb105af911efa40cd565ee808165',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24.7", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

cookies = {
    'anonymous-consents': '%5B%5D',
    'cookie-notification': 'NOT_ACCEPTED',
    'CookieConsent': '{stamp:%27VAC52xJALuXO4pVb85zbJ+TGAmnZpQHe3zeJwX2b9LekW6wqJHfmCg==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:7%2Cutc:1723721271645%2Cregion:%27ru%27}',
    '_gcl_au': '1.1.2069399862.1723721279',
    'leaderboardBanner': 'visited',
    'lastViewedProducts_N_3000_10_10_de': 'agid.2133|agid.2245|agid.21541|agid.3663|agid.22589|agid.15160|agid.22644',
    'JSESSIONID': '9BB8C94AB70357E5E8FF288429653E41.accstorefront-5bf9879c96-78n9b',
    'ROUTE': '.accstorefront-5bf9879c96-78n9b',
    '_clck': 'r8oig6%7C2%7Cfod%7C0%7C1688',
    'lastViewedProductsTimestamp_N_3000_10_10_de': '8/16/24|#6:52:00#AM#GMT',
    '_uetsid': '6e1dd1105af911ef9032dd17a32a802e',
    '_uetvid': '6e1dfb105af911efa40cd565ee808165',
    '_clsk': '1nj2ix2%7C1723795810049%7C1%7C1%7Ct.clarity.ms%2Fcollect',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'ru,en;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    # 'Cookie': 'anonymous-consents=%5B%5D; cookie-notification=NOT_ACCEPTED; CookieConsent={stamp:%27VAC52xJALuXO4pVb85zbJ+TGAmnZpQHe3zeJwX2b9LekW6wqJHfmCg==%27%2Cnecessary:true%2Cpreferences:true%2Cstatistics:true%2Cmarketing:true%2Cmethod:%27explicit%27%2Cver:7%2Cutc:1723721271645%2Cregion:%27ru%27}; _gcl_au=1.1.2069399862.1723721279; leaderboardBanner=visited; lastViewedProducts_N_3000_10_10_de=agid.2133|agid.2245|agid.21541|agid.3663|agid.22589|agid.15160|agid.22644; JSESSIONID=9BB8C94AB70357E5E8FF288429653E41.accstorefront-5bf9879c96-78n9b; ROUTE=.accstorefront-5bf9879c96-78n9b; _clck=r8oig6%7C2%7Cfod%7C0%7C1688; lastViewedProductsTimestamp_N_3000_10_10_de=8/16/24|#6:52:00#AM#GMT; _uetsid=6e1dd1105af911ef9032dd17a32a802e; _uetvid=6e1dfb105af911efa40cd565ee808165; _clsk=1nj2ix2%7C1723795810049%7C1%7C1%7Ct.clarity.ms%2Fcollect',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 YaBrowser/24.7.0.0 Safari/537.36',
    'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "YaBrowser";v="24.7", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
# response = requests.get(
#     'https://norelem.de/en/Product-overview/Flexible-standard-component-system/c/21089',
#     cookies=cookies,
#     headers=headers,
# )
#
# print(response)
# print(response.status_code)
