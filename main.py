import os
import requests
from difflib import SequenceMatcher
from bs4 import BeautifulSoup

ts_list = os.listdir(path='./work')


src = 'ド級編隊エグゼロス　EPISODE 06「新たな同居人（？）」'
trg = 'ド級編隊エグゼロス'
    
r = SequenceMatcher(None, src, trg).ratio()
print(r)

r = SequenceMatcher(None, 'あいうえお', 'あいうえお').ratio()
print(r)


params = (
    ('cat', '1'),
)

response = requests.get('https://cal.syoboi.jp/list', params=params)
if response.status_code != 200:
    exit(1)
soup    = BeautifulSoup(response.text, 'html.parser')
title_list   = soup.find(id='TitleList')
trs = title_list.find_all('tr')

rows = []
for tr in trs:

    title      = tr.find(class_='title')
    firstStart = tr.find(class_='firstStart')
    firstEnd   = tr.find(class_='firstEnd')
    tid        = tr.find(class_='tid')
    lastUpdate = tr.find(class_='lastUpdate')
    
    if title is not None:
        title = title.text
    if firstStart is not None:
        firstStart = firstStart.text
    if firstEnd is not None:
        firstEnd = firstEnd.text
    if tid is not None:
        tid = tid.text
    if lastUpdate is not None:
        lastUpdate = lastUpdate.text

    rows.append([title, firstStart, firstEnd, tid, lastUpdate])
        
for r in rows:
    print(r)
    
        
                       
