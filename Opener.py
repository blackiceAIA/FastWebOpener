#!/usr/bin/python

#FastWebOpener 1.0

import os



pathToApplications =  "/Applications"

def getLinks():

	
	
	favoriteList_file = open('favoriteList', 'r')
	bookmarks = favoriteList_file.readlines()

	for bookmark in bookmarks:
		print(bookmark)
	return bookmarks


def openLinks():
	
	linksString = ""
	for link in links:
		linksString = linksString + "'%s' " % (link)
		
	os.system("cd /Applications && open Google\ Chrome.app/ --args --new-window -a  %s" % (linksString))

links = getLinks()
openLinks()


