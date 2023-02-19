import pymysql
db = pymysql.connect(host='assignmentdatabase.co7landwei8p.us-east-1.rds.amazonaws.com',
                             port=3306,
                             user='admin',
                             password='Password',
                             database='lostfound'
                              )
                           

cursor = db.cursor()
img= "https://ethansimagebucket.s3.amazonaws.com/image/tshirt.jpeg"  
item = "Tshrt"
date = "2023-02-05"
des="Tshirt worn,xxl"
category = "Clothes"

my_insert ="INSERT INTO  lostitem ( `imgLink`, `Item`, `DateOfReport`, `Description`, `Category`)VALUES(%s,%s,%s,%s,%s)"
cursor.execute(my_insert, (img,item,date,des,category))
sql_query = "select * from lostitem"
db.commit()

cursor.execute(sql_query)

print("Total number of rows in table: ", cursor.fetchall())


