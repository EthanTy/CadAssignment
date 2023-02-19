from flask import Blueprint ,render_template
from sqlalchemy import schema
views = Blueprint('views', __name__)
data = {
        ("image/bear.jpeg", 'Softbear', 'stuffedbear', '22/12/22','Toy'),
        ("image/chess.jpg", 'Chess Set', 'Chess pieces for chess set', '10/12/22','Education'),
        ("image/tshirt.jpeg", 'Smartphone','Smartphone products','10/12/22','Clothes'),
        ("image/phones.jpeg", 'Smartphone','Smartphone products','10/12/22','Electronics'),
        ("image/rugby.jpeg", 'RugbyBall','Sportsball, used for rugby','05/12/22','Sports'),
        ("image/tenis.jpg", 'Tenis Racket','Tenis Racket, used for Tenis','05/01/23','Sports'),
        ("image/kricket.jpg", 'KriketRacket','Giant Bat used for Kriket','05/12/22','Sports')
        
    }
@views.route('/')
def home():
    categories = ("Electronics","Sports","Toy","Education","Clothes")
    
    # print data.items()  {{ url_for('static', filename='image/nanyang_polytechnic_logo.png') }}
    
    return render_template("index.html" , your_data= data ,category=categories )

@views.route('/subscribe')    
def subscribe():
    return render_template("subscribe.html")

@views.route('/admin')    
def admin():
    return render_template("admin.html")

