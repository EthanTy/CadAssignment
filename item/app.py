from flask import Flask, render_template, flash, redirect, request
import pymysql
import boto3

db = pymysql.connect(host='assignmentdatabase.co7landwei8p.us-east-1.rds.amazonaws.com',
                             port=3306,
                             user='admin',
                             password='Password',
                             database='lostfound',
                             autocommit='true')
app = Flask(__name__)

categories = ["Electronics", "Sports", "Toy", "Education", "Clothes"]
@app.route('/')
def home():
    
    sql_query = "select * from lostitem"
    with db.cursor() as cursor:
        cursor.execute(sql_query)
        data = cursor.fetchall()
    print(data)
    return render_template("index.html", your_data=data)


@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")


@app.route('/adminupload',methods = ["POST","GET"])
def adminupload():

    if request.method == 'POST':
        image = "https://ethansimagebucket.s3.amazonaws.com/image/tshirt.jpeg"
        # request.form.get('image')
        item = request.form.get('item')
        date = request.form.get('date')
        description = request.form.get('description')
        itemcategory = request.form.get('category')
        # imglink = (need to upload to s3 bucket ,then retrieve html)
        my_insert = "INSERT INTO  lostitem ( `imgLink`, `Item`, `DateOfReport`, `Description`, `Category`)VALUES(%s,%s,%s,%s,%s)"
        cursor = db.cursor()
        cursor.execute(my_insert, (image, item, date, description, itemcategory))
        db.commit()
        # if len(item) <=1 :
        #     flash('The name of the item  be greater than 1 character.', category='error')
        # elif not request.form.get(date):
        #     flash('You need to add a date', category='error')
        # elif len(description) < 7:
        #     flash('description neeeds to be mroethan 7 charecters', category='error')
        # elif not request.form.get(itemcategory):
        #     flash('the item needs to be assignedt a  category .', category='error')
        # else:
        # return redirect(url_for('views.home'))

            # Convert this into upload script based on image item data description category

    # elif  image not in request.image:
    #     flash('You need to upload an image', category='error')
    return render_template("adminupload.html" ,category = categories)

if __name__=='__main__':
    app.run(host="localhost", port=4001, debug=True)
