#!/usr/bin/python

#FastWebOpener 1.0

import os
import json
import argparse


parser = argparse.ArgumentParser(description = "---------------- \n FastWebOpener Script \n open your bookmark list INSTANTLY")

parser.add_argument("--name",'-n', action = 'store', type = str, help = "Specify the name of the custom list to open", default = "sites")

parser.add_argument("--incognito",'-i', action = 'store_true', help = "Launch the broswer in private mode", default = False)



pathToApplications =  "/Applications"

def getLinks():

	links = [];
	with open('favoriteList') as json_file:
		data = json.load(json_file)
		for l in data['lists']:
			if l['name'] == listName:
				for site in l['keywords']:
					links.append(site)
		return links


def openLinks():
	
	linksString = ""
	for link in links:
		linksString = linksString + " %s" % (link)
	
	if incognito == True:
		os.system("cd /Applications && open Google\ Chrome.app/ --args --incognito --new-window -a  %s" % (linksString))	
	else:
		os.system("cd /Applications && open Google\ Chrome.app/ --args --new-window -a  %s" % (linksString))


args = parser.parse_args()
incognito = args.incognito
listName = args.name

links = getLinks()
openLinks()

