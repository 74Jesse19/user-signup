from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

def data_validation(info):
    if (not info) or (info.strip() == ''): 
        return "yes"
    else:
        return "no"

    


@app.route('/welcome', methods=['POST'])
def welcome():
    name_var = request.form['name']
    pw_var = request.form['password']
    pw_var2 = request.form['password2']

    error = ""
    if len(name_var)<3 or len(name_var)>20:
        error = "That is not a valid username"
        return redirect("/?error=" + error)


        
    if not(name_var.isdigit()) and not(name_var.isalpha()):
        error = "That is not a valid username"
        return redirect("/?error=" + error)
    if (not name_var) or (name_var.strip() == ''):
        error = "That is not a valid username"
        return redirect("/?error=" + error)

    else: 
        encoded_error = request.args.get("error")
        encoded_error2 = request.args.get("error") 
        encoded_error3 = request.args.get("error")  
        return render_template('welcome.html',name=name_var,password=pw_var, password2=pw_var2, error=encoded_error, error2=encoded_error2, error3=encoded_error3)

    if len(pw_var)<3 or len(pw_var)>20:
        error2 = "That's not a valid password"
        return redirect("/?error=" + error2)
    if not(pw_var.isdigit()) and not(pw_var.isalpha()):
        error2 = "That's not a valid password"
        return redirect("/?error=" + error2)
    if (not pw_var) or (pw_var.strip() == ''):
        error2 = "That's not a valid password"
        return redirect("/?error=" + error2)
    else: 
        encoded_error = request.args.get("error")
        encoded_error2 = request.args.get("error") 
        encoded_error3 = request.args.get("error")  
        return render_template('welcome.html',name=name_var,password=pw_var, password2=pw_var2, error=encoded_error, error2=encoded_error2, error3=encoded_error3)

    if len(pw_var2)<3 or len(pw_var2)>20:
        error3 = "That's not a valid password"
        return redirect("/?error=" + error3)
    if not(pw_var2.isdigit()) and not(pw_var2.isalpha()):
        error3 = "That's not a valid password"
        return redirect("/?error=" + error3)
    if (not pw_var2) or (pw_var2.strip() == ''):
        error3 = "That's not a valid password"
        return redirect("/?error=" + error3)



    else: 
        encoded_error = request.args.get("error")
        encoded_error2 = request.args.get("error") 
        encoded_error3 = request.args.get("error")  
        return render_template('welcome.html',name=name_var,password=pw_var, password2=pw_var2, error=encoded_error, error2=encoded_error2, error3=encoded_error3)    
    
    
    """if (not name_var) or (name_var.strip() == ''):
        
        return redirect("/?error=" + error)
    elif (not pw_var) or (pw_var.strip() == ''):
            error = "That is not a valid password"
            return redirect("/?error=" + error)
    elif (not pw2_var) or (pw_var2.strip() == ''):
            error = "Please validate password"
            return redirect("/?error=" + error)    

    
    else:
        encoded_error = request.args.get("error") 
        return render_template('welcome.html',name=name_var,password=pw_var, password2=pw_var2, error=encoded_error and cgi.escape(encoded_error, quote=True))
"""
        
    
    
     
    
@app.route('/')
def index():
    encoded_error = request.args.get("error") 
    return render_template('edit.html', error=encoded_error and cgi.escape(encoded_error, quote=True))
    


app.run()