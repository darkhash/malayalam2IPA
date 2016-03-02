# -*- coding: utf-8 -*-
#!/bin/python
import sys
class IPAMap:
	consonants= ['ക','ഖ','ഗ','ഘ','ങ','ച','ഛ','ജ','ഝ','ഞ','ട','ഠ','ഡ','ഢ','ണ','ത','ഥ','ദ','ധ','ന','പ','ഫ','ബ','ഭ','മ','യ','ര','റ','ല','ള' 'ഴ','വ','ശ','ഷ','സ','ഹ']
	conuni=[x.decode("utf-8") for x in consonants]
	matraa= ['ാ','െ','േ','ി','ീ','ൊ','ോ','ു','ൂ','ൃ','ൈ','ൗ','ൌ']
	maarauni=[x.decode("utf-8") for x in matraa]
	charDict = {'ബ'.decode("utf-8"):'b','ഭ'.decode("utf-8"):'bʱ','ച'.decode("utf-8"):'t͡ʃ','ഛ'.decode("utf-8"):'t͡ʃʰ','ശ'.decode("utf-8"):'ʃ','ഡ'.decode("utf-8"):'ɖ','ഢ'.decode("utf-8"):'ɖʱ','ഗ'.decode("utf-8"):'g','ഘ'.decode("utf-8"):'ɡʱ','ഹ'.decode("utf-8"):'h','ജ'.decode("utf-8"):'ɟ','ഝ'.decode("utf-8"):'ɟʱ','ക'.decode("utf-8"):'k','ഖ'.decode("utf-8"):'kʰ','ള'.decode("utf-8"):'ɭ','ഴ'.decode("utf-8"):'ɻ','മ'.decode("utf-8"):'m','ങ'.decode("utf-8"):'ŋ','ഞ'.decode("utf-8"):'ɲ','പ'.decode("utf-8"):'p','റ'.decode("utf-8"):'r','ര'.decode("utf-8"):'ɾ','ഷ'.decode("utf-8"):'ʂ','സ'.decode("utf-8"):'s','ത'.decode("utf-8"):'t̪','യ'.decode("utf-8"):'j','വ'.decode("utf-8"):'ʋ','ന'.decode("utf-8"):'n̪','ന'.decode("utf-8"):'n','അ'.decode("utf-8"):'a','ാ'.decode("utf-8"):'aː','ആ'.decode("utf-8"):'aː','െ'.decode("utf-8"):'e','എ'.decode("utf-8"):'e','േ'.decode("utf-8"):'eː','ഏ'.decode("utf-8"):'eː','ി'.decode("utf-8"):'i','ഇ'.decode("utf-8"):'i','ീ'.decode("utf-8"):'iː','ഈ'.decode("utf-8"):'iː','ൊ'.decode("utf-8"):'o','ഒ'.decode("utf-8"):'o','ോ'.decode("utf-8"):'oː','ഓ'.decode("utf-8"):'oː','ു'.decode("utf-8"):'u','ഉ'.decode("utf-8"):'u','ൂ'.decode("utf-8"):'uː','ഊ'.decode("utf-8"):'uː','ൃ'.decode("utf-8"):'r̥','ഋ'.decode("utf-8"):'r̥','ൈ'.decode("utf-8"):'ai̯','ഐ'.decode("utf-8"):'ai̯','ൗ'.decode("utf-8"):'au̯','ൌ'.decode("utf-8"):'au̯','ഔ'.decode("utf-8"):'au̯','ല'.decode("utf-8"):'l'}
	ipalist =[]
	charCount = 0;
	def __init__(self, string):
		self.string = string
	
	def splitString(self):
		charlist = [char for char in self.string.decode("utf-8")]
		self.charCount = len(charlist)
		for char in charlist:
			print "dsfasdf==>", charlist.index(char)+1
			if char in self.conuni and (charlist.index(char)+1 < self.charCount and charlist[charlist.index(char)+1] not in self.maarauni):
				print char, self.charDict[char], 'ə'
				self.ipalist.append(self.charDict[char])
				self.ipalist.append('ə')
			elif char in self.conuni and charlist.index(char)+1 == self.charCount:
				print char, self.charDict[char], 'ə'
				self.ipalist.append(self.charDict[char])
				self.ipalist.append('ə')
			else:
				print char, self.charDict[char]
				self.ipalist.append(self.charDict[char])
		print self.ipalist


if(len(sys.argv) < 2):
	print "Usage: sys.argv[0] string"

map = IPAMap(sys.argv[1])
map.splitString()
