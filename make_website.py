
import string 

def MakeWebsite():
	li  = [] ;
	for i in string.digits:
		for j in string.digits:
			for k in string.ascii_lowercase:
				for l in string.ascii_lowercase:
					for m in string.ascii_lowercase:
						li.append('http://www.' + i + j + k + l + m +'.com/')
	return li

if __name__ == '__main__':
	pass
				

