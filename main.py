from flask import Flask, request, redirect, render_template
import cgi
import re

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too


@app.route('/', methods=['POST'])
def welcome():
    name_var = request.form['name']
    pw_var = request.form['password']
    pw_var2 = request.form['password2']
    email_var = request.form['email']


    error = ""
    error2 = ""
    error3 = ""
    email_error = ""

 # username data validation  
    if len(name_var)<3 or len(name_var)>20 or (not name_var) or (name_var.strip() == '') or (not(name_var.isdigit()) and not(name_var.isalpha())):
        error = "That is not a valid username"
       
        
# password data validation         
    if len(pw_var)<3 or len(pw_var)>20 or (not pw_var) or (pw_var.strip() == '') or (not(pw_var.isdigit()) and not(pw_var.isalpha())):
        error2 = "That's not a valid password"
       

# verify password data validation            
    if pw_var != pw_var2 or len(pw_var2)<3 or len(pw_var2)>20 or (not pw_var2) or (pw_var2.strip() == '') or (not(pw_var2.isdigit()) and not(pw_var2.isalpha())):
        error3 = "The passwords do not match"

# validate email is correct
    if len(email_var)>0:
        if len(email_var)<3 or len(email_var)>20 or '@' not in(email_var) or '.' not in(email_var) or re.search('\s', email_var):
            email_error = "That is not a valid email" 
    if((not email_var) or (email_var.strip=='')):
        email_var = ''  

# If everything is fine then this renders the welcome form
      
    if not error and not error2 and not error3 and not email_error:
        return render_template('welcome.html', name=name_var,password=pw_var,password2=pw_var2,email=email_var)
     
# This keeps user on the sign in to correct any errors
    else:
        return render_template('edit.html',name=name_var,password=pw_var,password2=pw_var2,email=email_var, error=error, error2=error2, error3=error3, email_error=email_error)

            

@app.route('/')
def index():
    
    
    return render_template('edit.html')
    


app.run()