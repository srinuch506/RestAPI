from flask import Flask,render_template,redirect,url_for,request,session
app=Flask(__name__)
app.secret_key='secretkey123'
@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/register',methods=['GET','POST'])
def register(): 
    if request.method=='POST':
        name=request.form['name']
        email=request.form['email']
        password=request.form['pass']
        cpassword=request.form['cpass']
        if password==cpassword:
            data={'Name':name,'Email':email,'password':password}
            print(data)
            session['user']=data
            return redirect(url_for('login'))
        else:
            return 'Password Mismatch'
    else:
        return render_template('register.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        data=session.get('user')
        email=request.form['email']
        password=request.form['pass']
        if email==data['Email'] and password==data['password']:
            return 'Login Success'
        else:
            return 'Invalid credentials'
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)
