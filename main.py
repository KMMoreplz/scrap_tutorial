import time
import os
import datetime
from art import *
from getpass import getpass

from bs4 import BeautifulSoup
from locale import atof, setlocale, LC_NUMERIC, atoi
import io
import json
import csv
import requests
import random
from time import sleep
import locale
import sys

art_1=text2art("ABC",font='block')
print(art_1)
url="https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters"
headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.124 YaBrowser/22.9.3.886 Yowser/2.5 Safari/537.36"
}
req = requests.get(url, headers=headers)
srcc = req.text
#print(srcc)
setlocale(LC_NUMERIC, '')
path = "blank/а283хе126_Новый_отчет_мм_2022-10-15_16-28-24.html"
with io.open(path, encoding='utf-8') as file:
    src = file.read()
# print(src)
soup = BeautifulSoup(src, "lxml")
# title =soup.title
# print(title)
page_all = soup.find_all("tr")
# print(page_all)
# for item in page_all:
#   print(item.text)


car_number = soup.find("tr", class_="unit_name")
car_number = car_number.text
# find car number^^^

fileName = f"result_{car_number.strip()}.txt"
#print(fileName)

fileOne=open(fileName, 'w')
fileOne.write(f"Номер машины:  {car_number}\n")



startOfTrip = soup.find_all("td", class_="dt data_col0_1")



endOfTrip = soup.find_all("td", class_="data_col0_2")
#for item in endOfTrip:
    #print(item.text)

tripLength = soup.find_all("td", class_="data_col0_3")
#for item in tripLength:
    #print(item.text)

allTimeInTrip = soup.find_all("td", class_="data_col0_4")
#for item in allTimeInTrip:
    #print(item.text)

allStayStopTime = soup.find_all("td", class_="data_col0_5")
#for item in allStayStopTime:
    #print(item.text)

# ----------------------------------------------------------

for i in range(len(tripLength)):
    tripLength[i] = tripLength[i].text.replace("км", "")
#print(itemSum)
#-----------------------------------------------------------


#regNumber----tripLength----allTimeInTrip----Stay(>5m)--Stop

dataTime = datetime.datetime.strptime(startOfTrip[1].text.split(" ")[0],'%Y-%m-%d')

dataCount = 0
dataSet = []
for i in range(2, len(startOfTrip)):
    if datetime.datetime.strptime(startOfTrip[i].text.split(" ")[0], '%Y-%m-%d').date() == dataTime.date():
        dataCount += 1
        #print(startOfTrip[i].text)
    else:
        #print("step")
        dataTime = datetime.datetime.strptime(startOfTrip[i].text.split(" ")[0], '%Y-%m-%d')

        dataSet.append(dataCount)
        dataCount = 0

saversaver=0
for i in range(len(dataSet)):
    saversaver+=dataSet[i]

dataSet.append(len(startOfTrip)-saversaver-10)

#print(dataSet)
dataSaver = 0
date_time_str = '00:05:00'
date_time_str1 = '00:04:00'
stayTime = datetime.datetime.strptime(date_time_str, '%H:%M:%S')
stayTime2 = datetime.datetime.strptime(date_time_str1, '%H:%M:%S')
saver = 0
dataSet[0]=dataSet[0]-1
for item in range(len(dataSet)):
    dataSet[item]=dataSet[item]+1
dataSet[9]= dataSet[9] - 1
#print(dataSet)
for i in range(len(dataSet)):
    itemSum = 0

    for j in range(2 + saver, dataSet[i] + saver+2):
        itemSum += atof(tripLength[j])
        #print(itemSum)
    saver += dataSet[i]
    fileOne.write(str(itemSum) + " " + startOfTrip[saver-dataSet[i]+2].text + " "+ str(saver) + '\n')
    itemSum = 0






        #if (datetime.datetime.strptime(startOfTrip[j].text.split(" ")[0], '%Y-%m-%d').time<datetime.datetime.strptime(startOfTrip[j+1].text.split(" ")[0], '%Y-%m-%d').time)&(
        #        datetime.datetime.strptime(startOfTrip[j].text.split(" ")[0], '%Y-%m-%d').date()==datetime.datetime.strptime(startOfTrip[j+1].text.split(" ")[0], '%Y-%m-%d').date()):
       #     print(1)






fileOne.close()
#for i in range(len(startOfTrip)):






# преобр км
# for i in range(len(startOfTrip)):
#    print(tripLength[i].text,endOfTrip[i].text)
