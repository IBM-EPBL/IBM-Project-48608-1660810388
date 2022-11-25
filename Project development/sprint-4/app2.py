from flask import Flask, render_template, url_for, request, session,redirect,render_template
import ibm_db

import sendgrid
from sendgrid import Mail, Email, To, Content

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=slq71777;PWD=cL33RyWPd5XPtDx9;","","")
print(conn)

app = Flask(__name__)
app.secret_key = 'HIII'

@app.route("/")
def homepage():
   return render_template("homepage.html")

@app.route('/signin')
def signin():
   return render_template('signin.html')

@app.route('/signup')
def signup():
   return render_template('signup.html')

@app.route("/card")
def card():
   return render_template("card.html")

@app.route('/item1')
def item1():
   return render_template('item1.html')

@app.route('/item2')
def item2():
   return render_template('item2.html')

@app.route('/item3')
def item3():
   return render_template('item3.html')

@app.route('/item4')
def item4():
   return render_template('item4.html')

@app.route('/item5')
def item5():
   return render_template('item5.html')

@app.route('/item6')
def item6():
   return render_template('item6.html')

@app.route('/item7')
def item7():
   return render_template('item7.html')

@app.route('/item8')
def item8():
   return render_template('item8.html')

@app.route('/item9')
def item9():
   return render_template('item9.html')

@app.route('/item10')
def item10():
   return render_template('item10.html')

@app.route('/item11')
def item11():
   return render_template('item11.html')

@app.route('/item12')
def item12():
   return render_template('item12.html')

@app.route('/item13')
def item13():
   return render_template('item13.html')

@app.route('/item14')
def item14():
   return render_template('item14.html')

@app.route('/item15')
def item15():
   return render_template('item15.html')

@app.route('/item16')
def item16():
   return render_template('item16.html')

@app.route('/item17')
def item17():
   return render_template('item17.html')

@app.route('/item18')
def item18():
   return render_template('item18.html')

@app.route('/item19')
def item19():
   return render_template('item19.html')

@app.route('/item20')
def item20():
   return render_template('item20.html')

@app.route('/item21')
def ites21():
   return render_template('/item21.html')


@app.route('/Dont have an account ?')
def go():
   return render_template('signup.html')

@app.route('/back')
def back():
   return render_template('signin.html')

@app.route('/data',methods = ['POST', 'GET'])
def data():
   if request.method == 'POST':
         
         name = request.form['name']          
         email = request.form['email']
         password = request.form['password']

         sql = "SELECT * FROM login WHERE email=?"
         stmt = ibm_db.prepare(conn, sql)
         ibm_db.bind_param(stmt,1,email)
         ibm_db.execute(stmt)
         account = ibm_db.fetch_assoc(stmt)
         


         if account:
           return redirect("signup")
           
         else:
          insert_sql = "INSERT INTO login VALUES (?,?,?)"
          prep_stmt = ibm_db.prepare(conn, insert_sql)
          ibm_db.bind_param(prep_stmt,1,name)
          ibm_db.bind_param(prep_stmt,2,email)
          ibm_db.bind_param(prep_stmt,3,password)
          ibm_db.execute(prep_stmt)
        

   return redirect("/signin")
         
'''         con = sql.connect("login.db")
         cur=con.cursor()
         cur.execute("INSERT INTO login (name,email,password) VALUES (?,?,?)",(name,email,password))
         con.commit()
         flash("Register successfully","success")   
      except:
        flash("Error in insert operation")
      finally:
        return redirect("signup")
        con.close()'''

@app.route('/login',methods = [ 'GET', 'POST'])  
def login():
    if request.method == 'POST':
        name = request.form['email']
        password = request.form['password']

        sql = "SELECT * FROM login WHERE email = ? AND password = ?"
        stmt = ibm_db.prepare(conn, sql)

        ibm_db.bind_param(stmt,1,name)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['email'] = name
            
    return render_template("./card")
   


'''      con = sql.connect("login.db")
      con.row_factory = sql.Row
      cur = con.cursor()
      cur.execute("SELECT * from login where email=? and password=?",(name,password))
      data = cur.fetchone()

      if data:
         session["mail"] = data["email"]
         session["password"] = data["password"]
         return redirect("retail")
      else:
         flash("Username and Password Mismatch","danger")
   return redirect("/") ''' 



if __name__ == '__main__':
   app.run(debug = True)