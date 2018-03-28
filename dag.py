#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3, codecs
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__, static_folder="/home/melanoya/1/static")

conn = sqlite3.connect('dag_locatives.db')



def db_insert():
	c = conn.cursor() # создала точку соприкосновения с базой

	c.execute('''CREATE TABLE andi (id, rus_ex, andi_ex, marker, loc, orient, postposition)''') # создали пустой лист с колонками
	andi = open('andi.csv', 'r')
	for line in andi:
		line = line.strip()
		idd, rus_ex, andi_ex, marker, loc, orient, postposition = line.split(',')
		c.execute(u'''INSERT INTO andi VALUES (?, ?, ?, ?, ?, ?, ?)''', (idd, rus_ex, andi_ex, marker, loc, orient, postposition))

	c.execute('''CREATE TABLE location (id, loc)''') # создали пустой лист с колонками
	location = open('location.csv', 'r')
	for line in location:
		line = line.strip()
		idd, loc = line.split(',')
		c.execute(u'''INSERT INTO location VALUES (?, ?)''', (idd, loc))

	c.execute('''CREATE TABLE orientation (id, orient)''') # создали пустой лист с колонками
	orientation = open('orientation.csv', 'r')
	for line in orientation:
		line = line.strip()
		idd, orient = line.split(',')
		c.execute(u'''INSERT INTO orientation VALUES (?, ?)''', (idd, orient))

	conn.commit()
	conn.close()

# db_insert()


def poisk(word):
   conn = sqlite3.connect('dag_locatives.db')
   c = conn.cursor()
   constr = u''
   c.execute('SELECT andi_ex FROM andi WHERE loc=?', (word,))
   for i in c.fetchone():
       constr += i
   return constr

# print(poisk('SUB'))

# @app.route('/')
# def form():
# 	if request.form:
# 		conn = sqlite3.connect('dag_locatives.db')
# 		c = conn.cursor()
# 		word = u''
# 		word = request.args['word']
# 		c.execute('SELECT andi_ex FROM andi WHERE loc=?', word)
# 		for constr in c.fetchone():
# 			return render_template('results.html', constr = constr, word = word)
# 	else:
# 		return render_template('landing-page.html')

@app.route('/')
def form():
	if request.args:
		construct = poisk(request.args['word'])
		arr = request.args['word']
		return render_template('results.html', array = construct, word = arr)
	else:
		return render_template('landing-page.html')
        

app.run(debug = True) 