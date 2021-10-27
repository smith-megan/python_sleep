from flask import Flask, render_template, json, request, redirect, flash, session;
import datetime;
from datetime import date;
# from werkzeug import check_password_hash;
# check_password_hash;
from flask_sqlalchemy import SQLAlchemy;
# from seed import load_age;

app=Flask(__name__)
db=SQLAlchemy(app)

# members api route


def connect_to_db(app):
  app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:HelloG1T@localhost:5432/lunardb'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
  # instantiate db]
  db.app=app
  db.init_app(app)

# db models
class Age(db.Model):
    """Age and hours table."""

    __tablename__ = "age"

    age = db.Column(db.Integer, primary_key=True)
    hours_low = db.Column(db.Integer)
    hours_high=db.Column(db.Integer)

    def __repr__(self):
        return f"<age={self.age} hours_low={self.hours_low} hours_high={self.hours_high}>"

class Tips(db.Model):
    """tips table."""

    __tablename__ = "tips"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tip=db.Column(db.String(300))
    source=db.Column(db.String(300))
    link=db.Column(db.String(100))
    
    def __repr__(self):
        return f"<id={self.id} tip={self.tip} source={self.source} link={self.link}>"

class User_tips(db.Model):
    """connections between users and tips table."""

    __tablename__ = "user_tips"

    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    tip_id = db.Column(db.Integer)

    def __repr__(self):
        return f"<user_id={self.user_id} tip_id={self.tip_id}>"

class Times(db.Model):
    """time table"""

    __tablename__ = "times"
    
    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    date_id = db.Column(db.Integer)
    date=db.Column(db.Date)
    morning=db.Column(db.Date)
    night=db.Column(db.Date)
    week_id=db.Column(db.Integer)

    def __repr__(self):
        return f"user_id={self.user_id} date_id={self.date_id} date={self.date} morning={self.morning} night={self.night} week_id={self.week_id}"


class Notes(db.Model):
    """notes table"""

    __tablename__ = "notes"
    
    id=db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    week_id = db.Column(db.Integer)
    note=db.Column(db.String)

    def __repr__(self):
        return f"<user_id={self.user_id} week_id={self.week_id} note={self.note}>"

class User(db.Model):
    """user table"""

    __tablename__ = "user"
    
    id=db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    email=db.Column(db.String)
    city=db.Column(db.String)
    birthday=db.Column(db.DateTime)
    

    def __repr__(self):
        return f"<username={self.username} password={self.password} email={self.email} city={self.city} birthday={self.birthday}>"


def load_age():
  one = Age(age=1, hours_low=11, hours_high=14)
  two = Age(age=2, hours_low=11, hours_high=14)
  three = Age(age=3, hours_low=10, hours_high=13)
  four = Age(age=4, hours_low=10, hours_high=13)
  five = Age(age=5, hours_low=10, hours_high=13)
  six = Age(age=6, hours_low=6, hours_high=12)
  seven = Age(age=7, hours_low=6, hours_high=12)
  eight = Age(age=8, hours_low=6, hours_high=12)
  nine = Age(age=9, hours_low=6, hours_high=12)
  ten = Age(age=10, hours_low=6, hours_high=12)
  eleven = Age(age=11, hours_low=6, hours_high=12)
  twelve = Age(age=12, hours_low=6, hours_high=12)
  thirteen = Age(age=13, hours_low=8, hours_high=10)
  fourteen = Age(age=14, hours_low=8, hours_high=10)
  fifteen = Age(age=15, hours_low=8, hours_high=10)
  sixteen = Age(age=16, hours_low=8, hours_high=10)
  seventeen = Age(age=17, hours_low=8, hours_high=10)
  eighteen = Age(age=18, hours_low=8, hours_high=10)
  nineteen = Age(age=19, hours_low=7, hours_high=12)
  twenty = Age(age=20, hours_low=7, hours_high=9)
  twenty_one = Age(age=21, hours_low=7, hours_high=9)
  twenty_two = Age(age=22, hours_low=7, hours_high=9)
  twenty_three = Age(age=23, hours_low=7, hours_high=9)
  twenty_four = Age(age=24, hours_low=7, hours_high=9)
  twenty_five = Age(age=25, hours_low=7, hours_high=9)
  twenty_six = Age(age=26, hours_low=7, hours_high=9)
  twenty_seven = Age(age=27, hours_low=7, hours_high=9)
  twenty_eight = Age(age=28, hours_low=7, hours_high=9)
  twenty_nine = Age(age=29, hours_low=7, hours_high=9)
  thirty = Age(age=30, hours_low=7, hours_high=9)
  thirty_one = Age(age=31, hours_low=7, hours_high=9)
  thirty_two = Age(age=32, hours_low=7, hours_high=9)
  thirty_three = Age(age=33, hours_low=7, hours_high=9)
  thirty_four = Age(age=34, hours_low=7, hours_high=9)
  thirty_five = Age(age=35, hours_low=7, hours_high=9)
  thirty_six = Age(age=36, hours_low=7, hours_high=9)
  thirty_seven = Age(age=37, hours_low=7, hours_high=9)
  thirty_eight = Age(age=38, hours_low=7, hours_high=9)
  thirty_nine = Age(age=39, hours_low=7, hours_high=9)
  forty = Age(age=40, hours_low=7, hours_high=9)
  forty_one = Age(age=41, hours_low=7, hours_high=9)
  forty_two = Age(age=42, hours_low=7, hours_high=9)
  forty_three = Age(age=43, hours_low=7, hours_high=9)
  forty_four = Age(age=44, hours_low=7, hours_high=9)
  forty_five = Age(age=45, hours_low=7, hours_high=9)
  forty_six = Age(age=46, hours_low=7, hours_high=9)
  forty_seven = Age(age=47, hours_low=7, hours_high=9)
  forty_eight = Age(age=48, hours_low=7, hours_high=9)
  forty_nine = Age(age=49, hours_low=7, hours_high=9)
  fifty = Age(age=50, hours_low=7, hours_high=9)
  fifty_one = Age(age=51, hours_low=7, hours_high=9)  
  fifty_two = Age(age=52, hours_low=7, hours_high=9)
  fifty_three = Age(age=53, hours_low=7, hours_high=9)
  fifty_four = Age(age=54, hours_low=7, hours_high=9)
  fifty_five = Age(age=55, hours_low=7, hours_high=9)
  fifty_six = Age(age=56, hours_low=7, hours_high=9)
  fifty_seven = Age(age=57, hours_low=7, hours_high=9)
  fifty_eight = Age(age=58, hours_low=7, hours_high=9)
  fifty_nine = Age(age=59, hours_low=7, hours_high=9)
  sixty = Age(age=60, hours_low=7, hours_high=9)

  # We need to add to the session or it won't ever be stored
  db.session.add_all([one, two, three, four, five, six,seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twenty_one, twenty_two, twenty_three, twenty_four, twenty_five, twenty_six, twenty_seven, twenty_eight, twenty_nine, thirty, thirty_one, thirty_two, thirty_three, thirty_four, thirty_five, thirty_six, thirty_seven, thirty_eight, thirty_nine, forty, forty_one, forty_two, forty_three, forty_four, forty_five, forty_six, forty_seven, forty_eight, forty_nine, fifty, fifty_one, fifty_two, fifty_three, fifty_four, fifty_five, fifty_six, fifty_seven, fifty_eight, fifty_nine, sixty])
  
  # Once we're done, we should commit our work
  db.session.commit()


@app.route("/register", methods=["POST"])
def register():
  details=(json.loads(request.data))

  #todo
  #  if details["user_details"]["email"] doesn't already exist in the database, add in

  name=details["user_details"]["name"]
  email=details["user_details"]["email"]
  password=details["user_details"]["password"]
  city=details["user_details"]["city"]
  birthday=details["user_details"]["birthday"]
  today=date.today()
  print(today)

  print(name,email,password,city,birthday)

  user_details=User(username=name,email=email, password=password, city=city,birthday=birthday)
  db.session.add(user_details)
  db.session.commit()

  return {"message": "success"}


@app.route("/login", methods=["POST"])
def login():
  details=(json.loads(request.data))
  email=details["email"]
  # password=request.args.get("password")
  # print(email)
  user=User.query.filter_by(email=email).first()
  # print(user.birthday)
  date=user.birthday
  # print(date.year)


   # if user.email == email and check_password_hash(user.password, password):
  #   session['logged_in_user_id']=user.id
  #   logged_in_user_id=user.id

  # if 'logged_in_user_id' in session.keys():
  #   user=User.query.get(logged_in_user_id)
  #   flash(f"Logged in user with email: {user.email}")

  # else:
  #   flash("incorrect email/password.")
  #   return redirect("/login")

  return{"birthyear":f"{date.year}"}
  # {redirect: ("/profile")}


@app.route("/profile")
def profile():
  return{"members":["hi"]}


@app.route("/members")
def members():
  return{"members":["member1","member2","member3"]}

@app.route("/graph", methods=["POST"])
def graph():
  details=(json.loads(request.data))
  email=details["email"]
  user=User.query.filter_by(email=email).first()
  age=date.today().year-user.birthday.year
  # print(age)
  
  times=Age.query.filter_by(age=age).first()
  # print(times)
  # print(times.hours_low)
  return{"hours":[f"{times.hours_low}",f"{times.hours_high}"]}


@app.route("/data", methods=["POST"])
def data():
  details=(json.loads(request.data))
  sleep=details["data"]
  print(details)
  print(sleep)

  return{"mess":"age"}

@app.route("/notes", methods=["POST"])
def day():
  noted=(json.loads(request.data))
  print(noted["note"])
  note=Notes(user_id=3,week_id=3, note=noted["note"])
  db.session.add(note)
  db.session.commit()
  return{"response":"note saved"}

if __name__=="__main__":
  connect_to_db(app)
  print("connected to db")
  db.create_all()
  print("created dbs")
  app.run(debug=True)