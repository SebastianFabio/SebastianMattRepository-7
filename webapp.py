from flask import Flask, request, render_template, flash
from markupsafe import Markup
from flask import redirect
from flask import session
import os
import time
app = Flask(__name__)

# In order to use "sessions",you need a "secret key".
# This is something random you generate.  
# For more info see: https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY

app.secret_key=os.environ["SECRET_KEY"];

@app.route('/')
def renderMain():
    return render_template('home.html')

@app.route('/startOver')
def startOver():
    session.clear() #clears variable values and creates a new session
    return redirect('/') # url_for('renderMain') could be replaced with '/'

@app.route('/page1')
def renderPage1():
    session["start_time"] = time.time()
    return render_template('page1.html')

@app.route('/page2',methods=['GET','POST'])
def renderPage2():
    if "answerOne" not in session:
        session["answerOne"]=request.form['andes1']    
    return render_template('page2.html')

@app.route('/page3',methods=['GET','POST'])
def renderPage3():
    if "answerTwo" not in session:
        session["answerTwo"]=request.form['danube1']    
    return render_template('page3.html')
    
@app.route('/results', methods=['GET','POST'])
def renderPage4():
    if "answerThree" not in session:
        session["answerThree"]=request.form['tashkent1'] 
    scoreValue=get_score()
    session["end_time"] = time.time()
    time_taken = session["end_time"] - session["start_time"]
    return render_template('results.html', finalScore=scoreValue, time_taken=time_taken)

def get_score():
    scoreVal=0
    if session["answerOne"]=="Argentina" and "answerOne" in session:
        scoreVal+=1
    if session["answerTwo"]=="Bulgaria" and "answerTwo" in session:
        scoreVal+=1
    if session["answerThree"]=="Uzbekistan" and "answerThree" in session:
        scoreVal+=1
    return scoreVal
if __name__=="__main__":
    app.run(debug=False)
