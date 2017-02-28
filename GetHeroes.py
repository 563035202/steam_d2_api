'''
 @Time    : 2017-2-28 21:18
 @Author  : Moses
 @File    : GetHeroes.py
'''

import requests
from utils.DBUtils import DBUtils
# https://wiki.teamfortress.com/wiki/WebAPI/GetHeroes
url ="http://api.steampowered.com/IEconDOTA2_570/GetHeroes/v1"
key ="?key=<key>"
params = "&language=zh_cn"

r = requests.get(url+key+params)
rj = r.json()

heros = rj['result']['heroes']
dbutils = DBUtils()
for h in heros:
    localized_name = h['localized_name']
    name = h['name']
    id = h['id']
    dbutils.insertHeros([localized_name, name, id])
dbutils.close()





