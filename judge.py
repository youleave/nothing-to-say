import requests	
url = 'http://www.812dd.com/'

keyword = ["尤物","欧美","巨乳","激情","色情"]

def Judge(s):
	for i in keyword :
		if i in s :
			return True;
	return False

 
	
def test():
	r = requests.get(url,timeout=3)
	print(r.url)
	print(r.encoding)
	r.encoding = "utf-8"
	print(r.encoding)
	# print(r.text)
	print(r.status_code)
	print(r.raise_for_status())
	print(r.headers)
	# print(type(r.headers))
	print(Judge(r.text))	

def Get_Html(myUrl):
	try:
		r = requests.get(myUrl,timeout = 3)
		r.encoding = 'utf-8'
		if Judge(r.text):
			return r.url
		else:
			return None
	except BaseException:
		print(r.raise_for_status())

	else:
		print(myUrl + " is ok ! ")


if __name__ == '__main__':
	Get_Html(url)
	# test()