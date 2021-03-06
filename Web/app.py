#!/usr/bin/python


from flask import Flask,request,url_for,redirect,render_template,flash, send_from_directory
import os
import jinja2
import json
import datetime
from werkzeug.utils import secure_filename
from pathlib import Path
import platform
import requests


def big_main(fin):

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
	
	return  tyl1(surn) + tyl2(name) + tyl3(int(date), int(month), int(year), gender)


def temp12(fin):
	name = fin["name"]
	surn = fin["surname"]
	gender = fin["gender"]
	dob = fin["dob"]
	out ="Name       :   " + name + "<br>"
	out+="Surnname   :   " + surn + "<br>"
	out+="Gender     :   " + gender + "<br>"
	out+="DoB        :   " + dob + "<br>
	"
	
	return out


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
	

#---------------


app = Flask(__name__, static_url_path='')
if platform.system() == 'Windows':
	UPLOAD_FOLDER = Path(__file__).parent.joinpath('uploads')
else:
	UPLOAD_FOLDER = r'uploads'




@app.route('/')
def homepage():
	return render_template('upload.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
	if request.method == 'POST':
		data = request.form.to_dict(flat= True)
		
		output=big_main(data)
		output2=temp12(data)
		outputhead="<head><html style=\"width:100vw\"><style> html{background-color:#222;color:#eee; align-text:center; padding-top:25%; font-size:45;}</style></head><body style=\"width:100vw\"><div class=container style=\"text-align:center;\">"
		outputtail="</div></body></html>"
		
		return outputhead + output2 + "<br><br>CodiceFiscae for above information is :<br>" + output  + outputtail






	
if __name__=='__main__':
	app.run(host='0.0.0.0', port=80, debug=True)
