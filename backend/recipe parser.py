
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient
import urllib3
urllib3.disable_warnings()
headers = {'Accept-Encoding': 'identity',
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
           }
db = MongoClient('167.172.165.25')
url = 'https://eda.ru/recepty/osnovnye-blyuda/russkaya-kuhnya?page=1'


form = {
    "region": "",
    "name": "",
    "photo": "",
    "type": "",
    "ingredients": {},
    "description": "",
    "_id": 0
}
# name : quantity
page_counter = 1


defined = [20, 10, 10, 10, 15, 10]
types = ["osnovnye-blyuda", "zavtraki", "zakuski", "vypechka-deserty", "salaty", "sup"]

regions = ['Русская кухня', 'Итальянская кухня', 'Японская кухня', 'Мексиканская кухня',
           'Китайская кухня', "Французская кухня", "Армянская кухня", 'Испанская кухня']

kitchen = ["russkaya-kuhnya", "italyanskaya-kuhnya", "yaponskaya-kuhnya", "meksikanskaya-kuhnya",
           "kitayskaya-kuhnya","francuzskaya-kuhnya", "armyanskaya-kuhnya", "ispanskaya-kuhnya"]


for ss, g in enumerate(regions):
    for sss, sl in enumerate(defined):
        f = 0
        for k in range((sl // 14) + 2):
            print(k)
            url = 'https://eda.ru/recepty/{0}/{1}?page={2}'.format(kitchen[ss], types[sss], str(k))
            r = requests.get(url, headers=headers, verify=False)
            soup = BeautifulSoup(r.content, 'lxml')
            for i in soup.findAll("h3", class_="horizontal-tile__item-title item-title"):
                url = "https://eda.ru/" + i.find('a')['href']
                form['name'] = " ".join(i.find("span").text.split()).replace('.', ' ')
                form['region'] = g
                form['type'] = types[sss]
                if f == sl:
                    break
                r = requests.get(url, headers=headers, verify=False)
                soup2 = BeautifulSoup(r.content, 'lxml')

                form['photo'] = soup2.find('div', class_='recipe__print-cover').find('img')['src']

                for m in soup2.find('div', class_='ingredients-list').findAll('p', class_="content-item"):
                    temp = " ".join(m.text.split()).replace('.', ' ').split()
                    if 'по' in temp and 'вкусу' in temp:
                        form["ingredients"][' '.join(temp[:-2])] = ' '.join(temp[-2:])
                    else:
                        for z in range(len(temp)):
                            try:
                                test = int(temp[z])
                                form["ingredients"][' '.join(temp[:-(len(temp)-z)])] = ' '.join(temp[-(len(temp)-z):])
                            except ValueError:
                                pass

                temp2 = []
                for pm in soup2.find_all('div', class_='instruction__wrap'):
                    temp2.append(' '.join(pm.find('span').text.split()))
                form["description"] = '\n'.join(temp2)
                form['_id'] += 1
                f += 1
                post_id = db.data.recipes.insert_one(form)
                print(post_id.inserted_id)
                form["ingredients"] = dict()
    print("cycle done")


