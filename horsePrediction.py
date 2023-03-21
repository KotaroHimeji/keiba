# 足立くんによるお馬さん予測シミュレーション

import math
import datetime
import re
import time
import locale
import tkinter as tk    # for making Desktop Application
import numpy as np      # for array calculation
import sympy as sp      # for mathematical operation
import openpyxl         # to use Excel from python
import django           # for making Web system
import requests         # to download HTML data
from bs4 import BeautifulSoup   # to extract HTML data
import PySimpleGUI as sg        # to choose date in calendarwith under one



url = 'https://race.netkeiba.com/top/?rf=footer'
res = requests.get(url)
res.encoding = res.apparent_encoding
#print(res.text)
soup = BeautifulSoup(res.content, "html.parser")
#elems = soup.find_all(href=re.compile("news.yahoo.co.jp/pickup"))
#print(elems)
elems = soup.find_all("th")
#print(elems)
#print(len(elems))
place = []
for elem in elems:
    if elem.contents[0] in ['札幌','函館','福島','新潟','東京','中山','中京','京都','阪神','小倉']:
        place.append(elem.contents[0])
print(place)


dt = datetime.date.today()
print(dt)
###########カレンダーから日付選択############
layout = [[sg.InputText(key='-date-'),
                sg.CalendarButton('日付選択', key='-button_calendar-',
                close_when_date_chosen=False,
                target='-date-', format="%Y-%m-%d")],
           [sg.Button('終了')]]

window = sg.Window('レースの日付',layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, '終了'):
        break

window.close()
#########################################
dt = datetime.datetime(2022, 10, 23)
print(dt.strftime('%a'))
if (dt.strftime('%a') == 'Sun') or (dt.strftime('%a') == 'Sat') : #土日の中央競馬
    dt = dt.strftime('%Y%m%d')
    print(dt)
    url2 = 'https://race.netkeiba.com/top/race_list_sub.html?kaisai_date=' + dt + '&current_group=10' + dt + '#racelist_top_a'
    res2 = requests.get(url2)
    res2.encoding = res2.apparent_encoding
    soup2 = BeautifulSoup(res2.content, "html.parser")
#elems2 = soup2.find_all("span")
    elems2 = soup2.find_all("span", class_="ItemTitle")
    print(elems2)
    Race = []
    for elem2 in elems2:
        Race.append(elem2.contents[0])

    raceNum = (len(Race))
    Race = np.array(Race).reshape(int(raceNum/12),12)
    print(Race)
    print(Race[0,10])


else : #平日の地方競馬
    dt = dt.strftime('%Y%m%d')
    print(dt)
    url2 = 'https://race.netkeiba.com/top/race_list_sub.html?kaisai_date=' + dt + '&current_group=10' + dt + '#racelist_top_a'
    res2 = requests.get(url2)
    res2.encoding = res2.apparent_encoding
    soup2 = BeautifulSoup(res2.content, "html.parser")
#elems2 = soup2.find_all("span")
    elems2 = soup2.find_all("span", class_="ItemTitle")
    print(elems2)
    Race = []
    for elem2 in elems2:
        Race.append(elem2.contents[0])
    print(Race)

#「出馬表」から中央競馬の情報
#「地方競馬」から地方競馬の情報


# coded by K Himeji
