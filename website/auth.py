from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean = True )

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up',methods =['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # Checks for the inputs meet certain criteria
        if len(email) < 4:
            flash('Email must be greater than 4 characters.',category='input_error')
        elif len(firstName) < 2:
            flash('First name must be greater than 2 characters.',category='input_error')
        elif password1 != password2:
            flash('Passwords does not match',category='input_error')
        elif len(password1) < 7:
            flash('Passwords must be greater than 7 characters',category='input_error')
        else:
            # add user to database
            flash('Account created!',category='success')

    return render_template("sign_up.html")