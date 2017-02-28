import requests
from utils.DBUtils import DBUtils
# https://wiki.teamfortress.com/wiki/WebAPI/GetHeroes

url ="http://api.steampowered.com/IDOTA2Match_570/GetMatchDetails/v1"
key ="?key=<key>"
params = "&language=zh_cn"
matchid = "&match_id=3024796243L"


r = requests.get(url+key+params+matchid)
# r = requests.get(url+key)
rj = r.json()
print rj
results = rj['result']

# for res in results:
for (k,v) in results.items():
    print k+" : "+str(v)