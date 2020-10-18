import requests
from bs4 import BeautifulSoup

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15"}
def extract_url(url):
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
