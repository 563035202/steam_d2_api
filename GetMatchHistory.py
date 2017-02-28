'''
 @Time    : 2017-2-28 21:22
 @Author  : Moses
 @File    : GetMatchHistory.py
'''

import requests
from utils.DBUtils import DBUtils
# https://wiki.teamfortress.com/wiki/WebAPI/GetHeroes

url ="http://api.steampowered.com/IDOTA2Match_570/GetMatchHistory/v1"
key ="?key=<key>"
params = "&language=zh_cn"
matchid = "&account_id=247189748"


r = requests.get(url+key+params+matchid)
rj = r.json()
print rj
results = rj['result']

