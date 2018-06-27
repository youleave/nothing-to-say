

import time
import os

def get_time():
	return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

def OutPut(filename,str_list):
	f = open(filename,'a+')
	print('OutPut is ok!')
	f.write(get_time() + '\t' +str_list+'\n')
	f.close();
