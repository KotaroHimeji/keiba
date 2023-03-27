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


# net競馬ホームページからwebスクレイピングを実行する
# 32行目までtyuou, chihou 以外必要ないかも
url = 'https://race.netkeiba.com/top/?rf=footer'
res = requests.get(url)
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.content, "html.parser")
elems = soup.find_all("th")
print(elems)
place = []
tyuou = ['札幌','函館','福島','新潟','東京','中山','中京','京都','阪神','小倉']
chihou = {"帯広":65, "門別":30, "盛岡":35, "水沢":36,"浦和":42,"船橋":43, "大井":44, "川崎":45,
 "金沢":46, "笠松":47,"名古屋":48, "姫路":51, "園田":25, "高知":54, "佐賀":55}
for elem in elems:
    if elem.contents[0] in ['札幌','函館','福島','新潟','東京','中山','中京','京都','阪神','小倉']:
        place.append(elem.contents[0])
print(place)

# カレンダーから日付選択
layout = [[sg.InputText(key='-date-'),
                sg.CalendarButton('日付選択', key='-button_calendar-',
                close_when_date_chosen=False,
                target='-date-', format="%Y%m%d")],
           [sg.Button('終了')]]

window = sg.Window('レースの日付',layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, '終了'):
        break

window.close()
#########################################
dt_str = values['-date-']
dt = datetime.datetime.strptime(dt_str, '%Y%m%d')
print(dt)
if (dt.strftime('%a') == 'Sun') or (dt.strftime('%a') == 'Sat') : #土日の中央競馬
    url2 = 'https://race.netkeiba.com/top/race_list_sub.html?kaisai_date=' + dt_str + '&current_group=10' + dt_str + '#racelist_top_a'
    print(url2)
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
    url2 = 'https://nar.netkeiba.com/top/?kaisai_date=' + dt_str
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
