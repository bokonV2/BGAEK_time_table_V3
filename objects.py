import json
from utils import getLinks, getTable


load = [["q","Загрузка..."]]

class Links():
    li = [load, load]

    def __init__(self):
        # self.getAll()
        pass

    def getAll(self):
        self.li[0] = getLinks("http://bgaek.by/category/расписание/buh-otdel/")
        self.li[1] = getLinks("http://bgaek.by/category/расписание/stroi-otdel/")
        print("GET "*100)

class Otdel(object):
    li = ["Бухгалтерское отделение","Строительное отделение"]

    def __init__(self):
        with open("settings.json", "r", encoding="utf-8") as f:
            jsn = json.load(f)
        self.otdel = jsn['otdel']

    def set(self, id):
        self.otdel = id
        with open("settings.json", "w", encoding="utf-8") as f:
            f.write(json.dumps({"otdel":id}))
