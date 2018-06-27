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
	check_result()
	for i in make_website.MakeWebsite():
		try:
			if judge.Judge(i):
				output.OutPut('result',i)
			else :
				print(i)

		finally:
			print(i)
