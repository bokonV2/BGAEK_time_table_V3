import requests
from bs4 import BeautifulSoup

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.167 YaBrowser/22.7.4.957 Yowser/2.5 Safari/537.36'}

bels=[
    ("#","1ч  к 08:20 до 09:05"),
    ("#","2ч  к 09:15 до 10:00"),
    ("#","3ч  к 10:10 до 10:55"),
    ("#","4ч  к 11:05 до 11:50"),
    ("#","5ч  к 12:30 до 13:15"),
    ("#","6ч  к 13:25 до 14:10"),
    ("#","7ч  к 14:20 до 15:05"),
    ("#","8ч  к 15:15 до 16:00"),
    ("#","выходные:"),
    ("#","5ч  к 12:10 до 12:55"),
    ("#","6ч  к 13:05 до 13:50"),
    ("#","7ч  к 14:00 до 14:45"),
    ("#","8ч  к 14:55 до 15:40"),
]

def getLinks(url):
    re = requests.get(url, timeout=10, headers=headers)
    soup = BeautifulSoup(re.text)
    titleUrls = soup.findAll("h2", class_="entry-title")
    urls = []
    for id, obj in enumerate(titleUrls):
        obj = obj.find("a", href=True)
        urls.append((f"/table/{id}", obj.text, obj["href"]))
    return urls

def getTable(url):
    re = requests.get(url, timeout=10, headers=headers)
    soup = BeautifulSoup(re.text)
    obj = soup.find("table")
    return obj
