import re
import requests
import html5lib
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"}
def extractUrl(url):
    """
    Method takes in one parameter 'url'
    Checks the validity of the Amazon URL and shortens it into a more manageable string.
    """
    if url.find('www.amazon.com') != -1:
        index = url.find('/dp')
        if index != -1:
            index2 = index +14
            url = 'https://www.amazon.com' + url[index:index2]
        else:
            index = url.find('/gp')
            if index != -1:
                index2 = index + 22
                url = "https://www.amazon.com" + url[index:index2]
            else:
                url = None
    else:
        url = None
    return url

def convertPrice(price):
    """
    Method takes in the product's price as a string with currency symbol and converts
     it into a float value using simple Regex
    """
    converted_price = float(re.sub(r"[^\d.]", "", price))
    return converted_price


def getProductDetails(url):
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"}
    details = {'name': '', 'price': 0, 'deal': True, 'url': ''}
    _url = extractUrl(url)
    if _url == '':
        details = None
    else: 
        page = requests.get(url, headers = headers)
        soup = BeautifulSoup(page.content, 'html5lib')
        title = soup.find(id="productTitle")
        price = soup.find(id="priceblock_dealprice")

        # if item is not on sale, look for alternate ID for price
        if price is None:
            price = soup.find(id="priceblock_saleprice")
            details['deal'] = False
        print(title, price)
        # Check for availability and add data into dictionary
        if title is not None and price is not None:
            details['name'] = title.get_text().strip()
            details['price'] = convertPrice(price.get_text())
            details['url'] = _url
        else:
            details = None

    return details

print(getProductDetails('https://www.amazon.com/SideTrak-Freestanding-Anti-Glare-Kickstand-Compatible/dp/B08D1TYR4G/ref=sr_1_4?dchild=1&keywords=sidetrak&qid=1603053905&sr=8-4'))
