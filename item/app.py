from flask import Flask, render_template, flash, redirect, request
import pymysql
import boto3, botocore 
from werkzeug.utils import secure_filename


app = Flask(__name__)

app.config['SECRET_KEY'] = 'ABCDEFU'
app.config['S3_BUCKET']= "ethansimagebucket"
app.config['S3_KEY'] = "ASIA3D5AHGW33TT6YJGF"
app.config['S3_SECRET']= "1tdcANi99q3I8yLRsGOLVoJ7AVcgQcEWCyEDzJzT"
app.config['Session_token']= "FwoGZXIvYXdzEAcaDKN6EOdNNtZegqQmQyLDATK8TblLzfDS9q6TfZf4PQWPsBcIxsdzSOem6vFbKt91nxQTlYyozW5wscpwXEREmV6vX+4by50Gez4FdTD8TfjnmRZsMzD1SqiiL8f48agd3wQ935IhTYOPWbb/EsQwScef8bVCGz17zX0KCaaAWa0DTbZG0Fbk39V0qvUasUQ382F8U9W8hNoY7fZ+c5etoVIondorpTP0QpOfZlDvoTR5SaeFlFXvRWShjNzxszBlk3xvgb7zP+hU3yxIMV2xok9J3SiX0MifBjItC4qft1vfI5NTKESF20CqICG8YlSA4006WvsgB59s7Jfzc16MpuTmozN2KFuJ"
app.config['S3_LOCATION']= 'http://{}.s3.amazonaws.com/'.format(app.config['S3_BUCKET']) 

s3_client = boto3.client('s3',
   aws_access_key_id= app.config['S3_KEY'],
   aws_secret_access_key= app.config['S3_SECRET'],
   aws_session_token= app.config['Session_token']
 )
db = pymysql.connect(host='assignmentdatabase.co7landwei8p.us-east-1.rds.amazonaws.com',
                             port=3306,
                             user='admin',
                             password='Password',
                             database='lostfound',
                             autocommit='true')

categories = ["Electronics", "Sports", "Toy", "Education", "Clothes"]
@app.route('/')
def home():
    sql_query = "select * from lostitem"
    with db.cursor() as cursor:
        cursor.execute(sql_query)
        data = cursor.fetchall()
    # print(data)
    return render_template("index.html", your_data=data)

@app.route('/subscribe')
def subscribe():
    return render_template("subscribe.html")

@app.route('/adminupload',methods = ["POST","GET"])
def adminupload():
    if request.method == 'POST':
        if 'image' in request.files:
            image = request.files['image']
           
            image.filename = secure_filename(image.filename)
            imglink = upload_file_to_s3(image, app.config["S3_BUCKET"])
            print(imglink)
            item = request.form.get('item')
            date = request.form.get('date')
            description = request.form.get('description')
            itemcategory = request.form.get('category')
            my_insert = "INSERT INTO  lostitem ( `imgLink`, `Item`, `DateOfReport`, `Description`, `Category`)VALUES(%s,%s,%s,%s,%s)"
            cursor = db.cursor()
            cursor.execute(my_insert,(imglink, item, date, description, itemcategory))
            db.commit()    
        else:
             flash ("No image key in request.files")
    return render_template("adminupload.html" ,category = categories)
def upload_file_to_s3(file, bucket_name, acl="public-read"):
    try:
        s3_client.upload_fileobj(
            file,  bucket_name, file.filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type    
            }
        )
    except Exception as e:
        print("Something Happened: ", e)
        return e
    return ( app.config["S3_LOCATION"] + file.filename)
if __name__=='__main__':
    app.run(host="localhost", port=4001, debug=True)
