#!/usr/bin/python

#FastWebOpener 1.0

import os
import json


pathToApplications =  "/Applications"

def getLinks():

	links = [];
	with open('favoriteList') as json_file:
		data = json.load(json_file)
		for p in data['keywords']:
			links.append(p)
		return links


def openLinks():
	
	linksString = ""
	for link in links:
		linksString = linksString + " %s" % (link)
		
	os.system("cd /Applications && open Google\ Chrome.app/ --args --new-window -a  %s" % (linksString))

links = getLinks()
openLinks()

