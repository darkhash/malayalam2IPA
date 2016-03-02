# -*- coding: utf-8 -*-
#!/bin/python
import sys
class IPAMap:
	consonants= ['ക','ഖ','ഗ','ഘ','ങ','ച','ഛ','ജ','ഝ','ഞ','ട','ഠ','ഡ','ഢ','ണ','ത','ഥ','ദ','ധ','ന','പ','ഫ','ബ','ഭ','മ','യ','ര','റ','ല','ള' 'ഴ','വ','ശ','ഷ','സ','ഹ']
	#conuni=[x  for x in consonants]
	matraa= ['ാ','െ','േ','ി','ീ','ൊ','ോ','ു','ൂ','ൃ','ൈ','ൗ','ൌ','്','﻿ം','ഃ']
	#maarauni=[x  for x in matraa]
	charDict = {'ബ' :'b','ഭ' :'bʱ','ച' :'t͡ʃ','ഛ' :'t͡ʃʰ','ശ' :'ʃ','ഡ' :'ɖ','ഢ' :'ɖʱ','ഗ' :'g','ഘ' :'ɡʱ','ഹ' :'h','ജ' :'ɟ','ഝ' :'ɟʱ','ക' :'k','ഖ' :'kʰ','ള' :'ɭ','ഴ' :'ɻ','മ':'m','ങ' :'ŋ','ഞ' :'ɲ','പ' :'p','റ' :'r','ര' :'ɾ','ഷ' :'ʂ','സ' :'s','ത' :'t̪','യ' :'j','വ' :'ʋ','ന' :'n̪','ന' :'n','അ' :'a','ാ' :'aː','ആ' :'aː','െ' :'e','എ' :'e','േ' :'eː','ഏ' :'eː','ി' :'i','ഇ' :'i','ീ' :'iː','ഈ' :'iː','ൊ' :'o','ഒ' :'o','ോ' :'oː','ഓ' :'oː','ു' :'u','ഉ' :'u','ൂ' :'uː','ഊ' :'uː','ൃ' :'r̥','ഋ' :'r̥','ൈ' :'ai̯','ഐ' :'ai̯','ൗ' :'au̯','ൌ' :'au̯','ഔ' :'au̯','ല' :'l', '്' :'#', 'ട' :'ʈ', 'ണ' :'ŋ' }
	ipalist =[]
	charCount = 0;
	def __init__(self, string):
		self.string = string
	
	def splitString(self):
		charlist = [char for char in  self.string.decode("utf-8") ]
		self.charCount = len(charlist)
		for index,char in enumerate(charlist):
			print "dsfasdf==>", index+1, char
			if (char.encode("utf-8") in self.consonants) and ( (index+1 < self.charCount) and (charlist[index+1] not in self.matraa)):
				print "3------------>", char, self.charDict.get(char.encode("utf-8"),'#'), 'ə'
				self.ipalist.append(self.charDict.get(char.encode("utf-8"),'#'))
				self.ipalist.append('ə')
			elif char.encode("utf-8") in self.consonants and index+1 == self.charCount:
				print "2---->", char, self.charDict.get(char.encode("utf-8"),'#'), 'ə'
				self.ipalist.append(self.charDict.get(char.encode("utf-8"),'#'))
				self.ipalist.append('ə')
			else:
				print char, self.charDict.get(char.encode("utf-8"),'#')
				self.ipalist.append(self.charDict.get(char.encode("utf-8"),'#'))
		
		print "result---->", "".join(self.ipalist)


if(len(sys.argv) < 2):
	print 'Usage: python '+sys.argv[0] +' string'
	sys.exit(1)

map = IPAMap(sys.argv[1])
map.splitString()
