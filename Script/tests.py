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
	
	# Ouverture du html pour parsingd
	file = open('temp.html', 'r')
	contents = file.read()
	soup = BeautifulSoup(contents, 'html.parser')

	debut = 0
	titreLivre = False

	#print(soup.prettify())

	for data in soup.find_all():
		if data.name == "font":
			if data.attrs['size'] == '5' or data.attrs['size'] == '4':
				if debut >1:
					if not titreLivre:
						print("Titre livre")
						print(data.getText())
						titreLivre = True
					else:
						print("Titre liminaire")
						print(data.getText())
						titreLivre = False
				else:
					debut += 1
			elif data.attrs['size'] == '3' and titreLivre:
				if data.children != None:
					for child in data.children:
						print(child.name)



			#print(data.attrs['size'])
			#print(data.contents[0])
			#if data.children != None:
			#	for child in data.children:
			#		if child.name != None:
			#			print(child.getText())
			#			print(child.name)



telechargerVersets("75")
