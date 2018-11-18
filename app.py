from flask import Flask, render_template, request
from data import Sample
app=Flask(__name__)
getsample = Sample()

@app.route('/about')
def samp():
    return render_template('about.html',mysample=getsample)

@app.route('/')    
def home():
    return render_template('home.html')
@app.route('/contactus')    
def con():
    return render_template('contactus.html')

@app.route('/result',methods=['GET','POST'])
def result():
    if(request.method=='POST'):
        getName=request.form['name']
        getaddress=request.form['address']
        getpass=request.form['pno']
        gettime=request.form['btime']
        getfair=request.form['fairport']
        getstair=request.form['tairport']
        getseat=request.form['seat']
        
    return render_template('result.html',n=getName,r=getaddress,s=getpass,c=gettime,s1=getfair,s1m=getstair,s1t=getseat)





if(__name__=='__main__'):
    app.run(debug=True)
