#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import os
import requests
import time
import make_website
import output
import judge

def check_result():
	if 'result' in os.listdir(os.getcwd()) :
		print ("result is already created!")
	else:
		f = open("result",'w');
		print ("a new result is created!")

if __name__ == '__main__':
	fo = open("log","w")
	check_result()
	for i in make_website.MakeWebsite():
		fo.write(i+'\n')
		try:
			s = judge.Get_Html(i)
			if s :
				print("already find " + s + "  \n")
				output.OutPut(s)
		except BaseException:
			pass