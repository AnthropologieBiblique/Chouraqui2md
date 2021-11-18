#!/usr/bin/env python3
import os
import csv
import markdownify
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import re
import fileinput

def telechargerVersets(livre):
	try:
	    url = "https://nachouraqui.tripod.com/id"+livre+'.htm'
	    print(url)
	    headers = {}
	    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
	    req = urllib.request.Request(url, headers = headers)
	    resp = urllib.request.urlopen(req)
	    respData = resp.read().decode('windows-1252')
	    saveFile = open('temp.html','w')
	    saveFile.write(str(respData))
	    saveFile.close()
	except Exception as e:
	    print(str(e))
	
	# Ouverture du html pour parsing
	file = open('temp.html', 'r')
	contents = file.read()
	soup = BeautifulSoup(contents, 'html.parser')

	tag = 0
	chapitre = re.compile("Chapitre ([0-9]{1,3}).")
	verset = re.compile(r"([0-9]{1,3}).\s*(.*)")
	liminaire = True

	#print(soup.prettify())

	for data in soup.find_all():
		if data.name == "font":
			if data.attrs['size'] == '4':
				print(tag)
				print(data.getText())
		tag +=1



			#print(data.attrs['size'])
			#print(data.contents[0])
			#if data.children != None:
			#	for child in data.children:
			#		if child.name != None:
			#			print(child.getText())
			#			print(child.name)



telechargerVersets("71")
