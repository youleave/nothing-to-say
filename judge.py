import requests
url = 'https://www.812dd.com/'

li = ['sex']

def update_doc():
	ff = open("doc",'r')
	st = ff.read()
	li = st.split(' ')

def Judge(url):
	s = requests.get(url)
	for i in li :
		if i in s :
			return True;
	return False

if __name__ == '__main__':
	r = requests.get(url)
	# ttt = str(r.text,'utf-8')
	print (r.text)	
