#!/usr/bin/python

#FastWebOpener 1.0

import os
import json
import argparse


parser = argparse.ArgumentParser(description = "---------------- \n FastWebOpener Script \n open your bookmark list INSTANTLY")

parser.add_argument("--name",'-n', action = 'store', type = str, help = "Specify the name of the custom list to open", default = "sites")



pathToApplications =  "/Applications"

def getLinks():

	links = [];
	with open('favoriteList') as json_file:
		data = json.load(json_file)
		for l in data['lists']:
			if l['name'] == args.name:
				for site in l['keywords']:
					links.append(site)
		return links


def openLinks():
	
	linksString = ""
	for link in links:
		linksString = linksString + " %s" % (link)
		
	os.system("cd /Applications && open Google\ Chrome.app/ --args --new-window -a  %s" % (linksString))


args = parser.parse_args()
links = getLinks()
openLinks()

