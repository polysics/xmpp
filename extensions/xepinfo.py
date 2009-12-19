# File: xepinfo.py
# Version: 0.2
# Description: xepinfo class
# Last Modified: 2009
# Author: Tobias Markmann (tm@ayena.de)

## LICENSE ##
#
# Copyright (c) 1999 - 2009 XMPP Standards Foundation
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
## END LICENSE ##

from xml.dom.minidom import parse,parseString,Document,getDOMImplementation

def getText(nodelist):
    thisText = ""
    for node in nodelist:
        if node.nodeType == node.TEXT_NODE:
            thisText = thisText + node.data
    return thisText

class XEPInfo:
	def __init__(self, filename):
		thexep = parse(filename)
		xepNode = (thexep.getElementsByTagName("xep")[0])
		headerNode = (xepNode.getElementsByTagName("header")[0])
		titleNode = (headerNode.getElementsByTagName("title")[0])
		self.title = getText(titleNode.childNodes)
		self.nr = getText((headerNode.getElementsByTagName("number")[0]).childNodes)
		abstractNode = (headerNode.getElementsByTagName("abstract")[0])
		abstract = getText(abstractNode.childNodes)
		statusNode = (headerNode.getElementsByTagName("status")[0])
		self.status = getText(statusNode.childNodes)
		self.type = getText((headerNode.getElementsByTagName("type")[0]).childNodes)
		revNode = (headerNode.getElementsByTagName("revision")[0])
		version = getText((revNode.getElementsByTagName("version")[0]).childNodes)
		self.date = getText((revNode.getElementsByTagName("date")[0]).childNodes)
		self.authors = []
		print len(headerNode.getElementsByTagName("author"))
		print headerNode.getElementsByTagName("author")
		for author in headerNode.getElementsByTagName("author"):
			print getText((author.getElementsByTagName("firstname")[0]).childNodes),
			print getText((author.getElementsByTagName("surname")[0]).childNodes)
			
	def getNr(self):
		return self.nr
	
	def getTitle(self):
		return self.title
	
	def getStatus(self):
		return self.status
	
	def getType(self):
		return self.type
	
	def getDate(self):
		return self.date
	