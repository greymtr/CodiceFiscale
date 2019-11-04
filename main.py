#!/usr/bin/python3

import json
import fileinput

def big_main():

	i1=""

	for stdin in fileinput.input():
		i1+=stdin
		pass
	  
	   
	i1=i1.replace(",\n\t",", ").replace("\n","")
	#print(i1)


	#totaljson="fiscalCode(ajifjshkahskjln()ssjkdjskjd()jdkfajlkjlfksa)"

	totaljson=i1

	fiscal="fiscalCode("
	indexOfFiscal=totaljson.find(fiscal)


	relevantjson=totaljson[indexOfFiscal+len(fiscal):]
	relevantjson=relevantjson[:-1]
	#	print(relevantjson)

	#relevantjson='{"name":"Matt" ,"surname":"Edabit" ,"gender":"M" ,"dob":"1/1/1900"}'

	fin=json.loads(relevantjson)


	#print(f1)


	name = fin["name"]
	surn = fin["surname"]
	gender = fin["gender"]
	dob = fin["dob"]

	#Making changes to fit with other methods
	
	name=name.lower()

	properdob = dob.split("/")

	date=properdob[0]
	month=properdob[1]
	year=properdob[2]
	
	#print("TYL1 : " + tyl1(surn) + "--")
	#print("TYL2 : " + tyl2(name) + "--")
	#print("TYL3 : " + tyl3(int(date), int(month), int(year), gender) + "--")
	"""
	print("name   : " + name )
	print("date   : " + date)
	print("month  : " + month)
	print("year   : " + year)
	"""
	
	print("TYL : " + tyl1(surn) + tyl2(name) + tyl3(int(date), int(month), int(year), gender) )


def tyl1(sname):
	
	consonants='bcdfghjklmnpqrstvwxyz'
	count=0
	sname=sname.lower()
	cons=""
	for x in sname:
		if x in consonants:
			count+=1
			cons=(cons+x)
			
	vowel='aeiou'
	v=''
	for y in sname:
		if y in vowel:
			v=(v+y)
	code=""
	letters=0
	for z in sname:
		letters+=1
	if(letters<3):
		code=(cons+v+'X')
	elif(count>=3):
		code=cons[:3]
	elif(count<3):
		code=(cons+v[:(3-count)])
	code=code.upper()
	return code


def tyl2(str):

	vowels = 0
	consonant = 0
	specialChar = 0
	digit = 0
	v = ""
	c = ""
	c2 = ""


	for i in range(0, len(str)):  
		
		ch = str[i]  

	

		if (ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u'): 
			vowels += 1
			v=v+ch
		else: 
			consonant += 1
			c=c+ch

	if(consonant == 3):
		c2 = c
	elif(consonant>3):
		c2=c[0]+c[2]+c[3]

	elif(len(str)<3):
		t="xxx"
		c2=c+v+t
		c2=c2[:3]
	elif(consonant<3):
		c2=c+v
		c2=c2[:3]
	
	
	return c2.upper()


def tyl3(d,m,y,gender):
	a=str(d)
	b=str(m)
	c=str(y)
	f=c[2:4]
	first = f

	if gender=='M':
		if(d<10):
			code=('0'+a)
		else:
			code=(a)
	else:
		temp=(40+d)
		code=str(temp)
	last = code
	Dict={1:'A',2:'B',3:'C',4:'D',5:'E',6:'H',7:'L',8:'M',9:'P',10:'R',11:'S',12:'T'}
	letter=Dict[m]
	mid=Dict[m]
	final = first+mid+last
	
	
	return final
	
big_main()

