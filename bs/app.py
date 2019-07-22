import mysql.connector

from flask import Flask,render_template,url_for
from flask import *

import json

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/typecount',methods=['POST'])
def tyecount():
	conn = mysql.connector.connect(host='192.168.52.130', user='root', password='root', db='bs')
	cur = conn.cursor()
	sql = 'SELECT type,count FROM typecount'
	cur.execute(sql)
	u = cur.fetchall()
	jsonData={}
	xdays = []
	yvalues = []
	for data in u:
		xdays.append(data[0])
		yvalues.append(data[1])
	print(xdays)
	print(yvalues)
	jsonData['xdays']=xdays
	jsonData['yvalues'] = yvalues
	j = json.dumps(jsonData)
	cur.close()
	conn.close()
	return(j)
@app.route('/yearcount',methods=['POST'])
def yearcount():
	conn = mysql.connector.connect(host='192.168.52.130', user='root', password='root', db='bs')
	cur = conn.cursor()
	sql = 'SELECT year,count FROM yearcount ORDER BY year'
	cur.execute(sql)
	u = cur.fetchall()
	jsonData={}
	xdays = []
	yvalues = []
	for data in u:
		xdays.append(data[0])
		yvalues.append(data[1])
	print(xdays)
	print(yvalues)
	jsonData['xdays']=xdays
	jsonData['yvalues'] = yvalues
	j = json.dumps(jsonData)
	cur.close()
	conn.close()
	return(j)

@app.route('/rate')
def rate():
	return render_template('rate.html')

@app.route('/shichang',methods=['POST'])
def shi_chang():
	conn = mysql.connector.connect(host='192.168.52.130', user='root', password='root', db='bs')
	cur = conn.cursor()
	sql = 'SELECT score,shichang FROM moviedata '
	cur.execute(sql)
	u = cur.fetchall()
	jsonData = {}
	xdays = []
	yvalues = []
	for data in u:
		xdays.append(data[0])
		yvalues.append(data[1])
	print(xdays)
	print(yvalues)
	jsonData['xdays']=xdays
	jsonData['yvalues'] = yvalues
	j = json.dumps(jsonData)
	cur.close()
	conn.close()
	return(j)
@app.route('/yearscore',methods=['POST'])
def year_score():
	conn = mysql.connector.connect(host='192.168.52.130', user='root', password='root', db='bs')
	cur = conn.cursor()
	sql = 'SELECT score,time FROM moviedata'
	cur.execute(sql)
	u = cur.fetchall()
	jsonData = {}
	xdays = []
	yvalues = []
	for data in u:
		xdays.append(data[0])
		yvalues.append(data[1])
	print(xdays)
	print(yvalues)
	jsonData['xdays']=xdays
	jsonData['yvalues'] = yvalues
	j = json.dumps(jsonData)
	cur.close()
	conn.close()
	return(j)
@app.route('/renshu',methods=['POST'])
def renshu_score():
	conn = mysql.connector.connect(host='192.168.52.130', user='root', password='root', db='bs')
	cur = conn.cursor()
	sql = 'SELECT score,disum FROM moviedata'
	cur.execute(sql)
	u = cur.fetchall()
	jsonData = {}
	xdays = []
	yvalues = []
	for data in u:
		xdays.append(data[0])
		yvalues.append(data[1])
	print(xdays)
	print(yvalues)
	jsonData['xdays']=xdays
	jsonData['yvalues'] = yvalues
	j = json.dumps(jsonData)
	cur.close()
	conn.close()
	return(j)

@app.route('/diqucount',methods=['POST'])
def diqu_count():
	conn = mysql.connector.connect(host='192.168.52.130', user='root', password='root', db='bs')
	cur = conn.cursor()
	sql = 'SELECT diqu,count FROM diqucount'
	cur.execute(sql)
	u = cur.fetchall()
	jsonData = {}
	xdays = []
	yvalues = []
	for data in u:
		xdays.append(data[0])
		yvalues.append(data[1])
	print(xdays)
	print(yvalues)
	jsonData['xdays']=xdays
	jsonData['yvalues'] = yvalues
	j = json.dumps(jsonData)
	cur.close()
	conn.close()
	return(j)

@app.route('/yingyong')
def ying():
	return render_template('yingyong.html')

@app.route('/keyword',methods=['POST'])
def keyword():
	data = request.form
	print(data)
	conn = mysql.connector.connect(host='192.168.52.130', user='root', password='root', db='bs')
	cur = conn.cursor()
	sql=("select * from douban_movie_clean where title like '%%%s%%' order by rate desc" % (data['keyword']))
	print(sql)
	cur.execute(sql)
	movies =cur.fetchall()
	j = json.dumps({"movies": movies})

	print(j)
	cur.close()
	conn.close()
	return (j)

if __name__ == '__main__':
    app.run(debug=True)
