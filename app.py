from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb
app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='123456'
app.config['MYSQL_DB']='mark'

mysql=MySQL(app)
@app.route('/')
def home():
	return render_template("home.html")

@app.route('/login', methods=['GET','POST'])
def login():
	if request.method=='POST':
		d=request.form
		email=d['email']
		password=d['password']
		conn = MySQLdb.connect(host="localhost", user = "root", passwd = "123456", db = "mark")
		cur = conn.cursor()
		cur.execute("select * from test")
		conn.commit()
		r=cur.fetchall()
		k=list(r)
		c=0
		print(k)
		for i in k:
			if i[0]==email:
				if i[1]==password:
					c=c+1
		if c>=1:
			return redirect("/test")
		else:
			return render_template("loginerror.html")
	return render_template("login.html")
@app.route('/signup',methods=['GET','POST'])
def signup():
	if request.method=='POST':
		val=request.form
		username=val['username']
		email=val['Email']
		password=val['password']
		password2=val['retype-password']
		c1=0
		if password==password2:
			c1=c1+1
			#conn=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="mark")
		else:
			return "<h1> password and retype-password not matching..........!</h1>"
		if c1==1:
			conn=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="mark")
			cur=conn.cursor()
			cur.execute("select*from test")
			conn.commit()
			r=cur.fetchall()
			k=list(r)
			c2=0
			for i in k:
				if email in i:
					c2=1
		if c2==1:
			return render_template("signuperror.htmlx")
		else:
			conn=MySQLdb.connect(host="localhost",user="root",passwd="123456",db="mark")
			cur=conn.cursor()
			cur.execute("INSERT  INTO test(email,password) VALUES(%s,%s)",(email,password))
			conn.commit()
			return "done-it"
	return render_template("signup.html")
@app.route('/test', methods=['GET','POST'])
def t():
	ans=[]
	if request.method=='POST':
		mark=0
		d1=request.form
		name=d1['email1']
		for i in range(1,30):
			a=d1[str(i)]
			ans.append(a)
		print(ans)
		ans1=["c","c","b","b","b","a","c","a","a","c","a","d","c","b","c","a","c","d","c","b","b","a","a","c","c","b","c","b","a","b"]
		for j in range(len(ans1)-1):
			if ans[j]==ans1[j]:
				mark=mark+1
		m=str(mark)
		conn = MySQLdb.connect(host="localhost", user = "root", passwd = "123456", db = "mark")
		cur = conn.cursor()
		cur.execute("INSERT INTO marks	(name,mark) VALUES(%s, %s)",(name,m))
		conn.commit()
		print(m)
		ur=2
		return render_template("pro.html",m=m)

	return render_template("newqp.html")
if __name__ == '__main__':
	app.run(host='0.0.0.0')
