###################### Import Module ###########################                        
import json , sys , hashlib , os , time , marshal
###################### COLOR ###################################                      
if sys.platform in ["linux","linux2"]:
	W = "\033[0m"
        G = '\033[32;1m'
        R = '\033[31;1m'
else:
	W = ''
	G = ''
	R = ''
	
####################### Exception  ###############################                   
try:
	import requests
except ImportError:
	print ' '
	print "[!] Can't import module 'requests'\n"
	sys.exit()
###################### Set Default encoding ######################                   
reload (sys)
sys . setdefaultencoding ( 'utf8' )
####################### Declare Array  ###########################      	      	 
jml = []
jmlgetdata = []
n = []
####################### LOGIN FACEBOOK ###########################
def get(data):
	global fb 
	print '[*] Please wait.... \n'
	try:
		r = requests.get('https://api.facebook.com/restserver.php',params=data)
		a = json.loads(r.text)
		fb = a['access_token']
		print '[*] You are login successfully :) '
		#call summary friend and phone numer 
		getdata()
		#call export phone number
		phone()		
		sys.exit()
	except KeyError:
		print '[!] You are login Failed please Check your connection / email or password '
		cek = raw_input('[?] Are you sure you want to continue [Y/N] ')
		if cek.lower() != 'y':
			print '[!] Exiting program !!'
			sys.exit()
		id()
	except requests.exceptions.ConnectionError:
		print '[!] Login Failed try again'
		print '[!] Connection error !!!'
		id()
def id():
	fb = ''
	print  '[*] login to your facebook account         ';id = raw_input('[?] Username : ');pwd = raw_input('[?] Password : ');API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
        x.update(sig)

	data.update({'sig':x.hexdigest()})
        get(data)
################### FETCHING PHONE NUMBER ##########################
def phone():
	global fb	
	cek = raw_input('[?] Do you want export all phone number  [Y/N] ')
	if cek.lower() != 'y':
		print '[!] Exiting program !!'
		sys.exit()	
	print "[*] fetching all phone list of friend facebook"
	print '[*] start\n'
	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+fb)
		a = json.loads(r.text)
		out = open('data.txt','w')							
		for i in a['data']:
			x = requests.get("https://graph.facebook.com/"+i['id']+"?access_token="+fb)
			z = json.loads(x.text)
				
			try:
				head = z['mobile_phone'][0:4]
				
				if  z['mobile_phone'][0:3]  == '+66': #country code thai 
					print '[*] '+ z['mobile_phone'][0:5]  + "xnxx#" + z['mobile_phone'].replace('+66' , "0")[0:3]+'xnxx'
					out.write(z['mobile_phone'] + "#" + z['mobile_phone'].replace('+66' , "0")+'#'+z['birthday'].replace('/','-')+'#'+z['id'] +'\n')
				elif z['mobile_phone'][0:3]  == '+91':#country code india 
					print '[*] '+  z['mobile_phone'][0:5]  + "xnxx#" + z['mobile_phone'].replace('+91' , "0")[0:3]+'xnxx'
					out.write(z['mobile_phone'] + "#" + z['mobile_phone'].replace('+91' , "")+'#'+z['birthday'].replace('/','-')+'#'+z['id'] +'\n')
				elif z['mobile_phone'][0:3]  == '+82':#country code south korea 
					print '[*] '+  z['mobile_phone'][0:5]  + "xnxx#" + z['mobile_phone'].replace('+82' , "0")[0:3]+'xnxx'
					out.write(z['mobile_phone'] + "#" + z['mobile_phone'].replace('+82' , "0")+'#'+z['birthday'].replace('/','-')+'#'+z['id']+'\n')
				elif z['mobile_phone'][0:3]  == '+60':#country code Malaysia 
					print '[*] '+  z['mobile_phone'][0:5]  + "xnxx#" + z['mobile_phone'].replace('+60' , "0")[0:3]+'xnxx'
					out.write(z['mobile_phone'] + "#" + z['mobile_phone'].replace('+60' , "0")+'#'+z['birthday'].replace('/','-')+'#'+z['id']+'\n')	
				elif z['mobile_phone'][0:4]  == '+855': #country code khmer 
					print '[*] '+  z['mobile_phone'][0:6]  + "xnxx#" + z['mobile_phone'].replace('+855' , "0")[0:3]+'xnxx'
					out.write(z['mobile_phone'] + "#" + z['mobile_phone'].replace('+855' , "0")+'#'+z['birthday'].replace('/','-')+'#'+z['id']+ '\n')
				else:	#country code remix 5555
					print '[*] '+  z['mobile_phone'][0:6]  + "xnxx#" + z['mobile_phone'].replace(head , "0")[0:3]+'xnxx'
					out.write(z['mobile_phone'] + "#" + z['mobile_phone'].replace(head, "0") +'#'+z['birthday'].replace('/','-')+'#'+z['id']+ '\n')
					
			except KeyError:
				pass
		out.close()
		print '[*] done'
		print "[*] all phone list of facebook successfuly retrieved"
		print '[*] file saved directorie : data.txt'
		sys.exit()
	except KeyboardInterrupt:
		print '\r[!] Stopped'
		sys.exit()
	except KeyError:
		print "[!] failed to fetch all phone numbers"
		sys.exit()
	except (requests.exceptions.ConnectionError , requests.exceptions.ChunkedEncodingError):
		print '[!] Connection Error'
		print '[!] Stopped'
		sys.exit()

###########################  Get Data  ################################                         
def getdata():
	global a , fb
	try:
		r = requests.get('https://graph.facebook.com/me/friends?access_token='+fb)
		a = json.loads(r.text)
	except KeyError:
		print '[!] Your connection expired to facebook again'
		id()
	except requests.exceptions.ConnectionError:
		print '[!] Connection Error'
		print '[!] Stopped'
		id()
	for i in a['data']:
		jml.append(i['id'])	
		print '\r[*] fetching %s data from friends'%(len(jml)),;sys.stdout.flush();time.sleep(0.0001)
	print '\r[*] '+str(len(jml))+' data of friends successfully retrieved'
########################################################################
if __name__ == '__main__':
	id()	
