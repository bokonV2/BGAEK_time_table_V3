import requests
from bs4 import BeautifulSoup


bels=[
    ("q","1ч  к 08:20 до 09:05"),
    ("q","2ч  к 09:20 до 10:05"),
    ("q","3ч  к 10:20 до 11:05"),
    ("q","4ч  к 11:20 до 12:05"),
    ("q","5ч  к 12:45 до 13:30"),
    ("q","6ч  к 13:45 до 14:30"),
    ("q","7ч  к 14:45 до 15:30"),
    ("q","8ч  к 15:45 до 16:30"),
    ("q","9ч  к 16:45 до 17:30"),
    ("q","10ч к 17:45 до 18:30"),
    ("q","выходные:"),
    ("q","5ч  к 12:25 до 13:10"),
    ("q","6ч  к 13:25 до 14:10"),
    ("q","7ч  к 14:25 до 15:10"),
    ("q","8ч  к 15:25 до 16:10"),
    ("q","9ч  к 16:25 до 17:10"),
    ("q","10ч к 17:25 до 18:10"),
]

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
