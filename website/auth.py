from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Admin
from werkzeug.security import generate_password_hash, check_password_hash
from . import db  # means from __init__.py import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
    # you need image, item ,date of report,description,categorty
    if request.method == 'POST':

        email = request.form.get('Aemaik')
        password = request.form.get('APassword')

        Admin = User.query.filter_by(email=email).first()
        if Admin:
            if Admin.password == password:
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", Admin=current_user)


# admin uploadarea
@auth.route('/adminupload', methods=['POST'])
def adminupload():
    if request.method == 'POST':
        image = request.form.get('image')
        item = request.form.get('item')
        date = request.form.get('date')
        description = request.form.get('description')
        itemcategory = request.form.get('category')
        # imglink = (need to upload to s3 bucket ,then retrieve html)
        db.insert_details(imglink, item, date, description, itemcategory)

        return redirect(url_for('views.home'))
        

            # Convert this into upload script based on image item data description category
       
    elif  image not in request.image:
        flash('You need to upload an image', category='error')
    elif len(item) <=1 :
        flash('The name of the item  be greater than 1 character.', category='error')
    elif not request.form.get(date):
        flash('You need to add a date', category='error')
    elif len(description) < 7:
        flash('description neeeds to be mroethan 7 charecters', category='error')
    elif not request.form.get(itemcategory):
        flash('the item needs to be assignedt a  category .', category='error')


            

    return render_template("adminupload.html", user=current_user)




@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# need to modift further, have to include id for whythey subscribed
@auth.route('/subscribe', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        Sname = request.form.get('name')
        type = request.form.get('type')
        category = request.form.get('category')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif '@mymail.nyp.edu.sg' not in email:
            flash('Email must be assigned to @mymail.nyp.edu.sg', category='error')
        elif len(Sname) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')

      
        else:
            new_user = User(email=email, Sname=name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("subscribe.html")
