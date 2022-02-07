import requests
from bs4 import BeautifulSoup


def getLinks(url):
    re = requests.get(url, timeout=10)
    soup = BeautifulSoup(re.text, "lxml")
    titleUrls = soup.findAll("h2", class_="entry-title")
    urls = []
    for id, obj in enumerate(titleUrls):
        obj = obj.find("a", href=True)
        urls.append((id, obj.text, obj["href"]))
    return urls

def getTable(url):
    re = requests.get(url, timeout=10)
    soup = BeautifulSoup(re.text, "lxml")
    obj = soup.find("table")
    return obj
