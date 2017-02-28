'''
 @Time    : 2017-2-28 21:20
 @Author  : Moses
 @File    : GetLeagueListing.py
'''

import requests
from utils.DBUtils import DBUtils
# https://wiki.teamfortress.com/wiki/WebAPI/GetLeagueListing
url ="http://api.steampowered.com/IDOTA2Match_570/GetLeagueListing/v1"
# url ="http://api.steampowered.com/IDOTA2Match_<ID>/GetLeagueListing/v1/"
key ="?key=<key>"
params = "&language=zh_cn"

r = requests.get(url+key+params)
rj = r.json()

leagues = rj['result']['leagues']
dbutils = DBUtils()
for l in leagues:
    league_name = l['name']
    league_id = l['leagueid']
    tournament_url = l['tournament_url']
    itemdef =  l['itemdef']
    description =  l['description']
    dbutils.insertLeagues([league_name, league_id, tournament_url, itemdef, description])
dbutils.close()





