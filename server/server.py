from operator import ior
from flask import Flask, render_template, json, request, redirect, flash, session;
import datetime;
from datetime import date;
from dateutil.relativedelta import *;
from flask_sqlalchemy import SQLAlchemy;
from sqlalchemy import desc;

app=Flask(__name__)
db=SQLAlchemy(app)

# members api route


def connect_to_db(app):
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
  # instantiate db
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
    user_email = db.Column(db.String)
    tip_id = db.Column(db.Integer)

    def __repr__(self):
        return f"<user_email={self.user_email} tip_id={self.tip_id}>"

class Times(db.Model):
    """time table"""

    __tablename__ = "times"
    
    id=db.Column(db.Integer, primary_key=True)
    date=db.Column(db.Date)
    user_email = db.Column(db.String)
    wake=db.Column(db.Time)
    sleep=db.Column(db.Time)
    hours=db.Column(db.Integer)

    def __repr__(self):
        return f"date={self.date} user_email={self.user_email} wake={self.wake} sleep={self.sleep} hours={self.hours}"+"|"


class Notes(db.Model):
    """notes table"""

    __tablename__ = "notes"
    
    id=db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String)
    note=db.Column(db.String)

    def __repr__(self):
        return f"<user_id={self.user_email} note={self.note}>"

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

  db.session.add_all([one, two, three, four, five, six,seven, eight, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty, twenty_one, twenty_two, twenty_three, twenty_four, twenty_five, twenty_six, twenty_seven, twenty_eight, twenty_nine, thirty, thirty_one, thirty_two, thirty_three, thirty_four, thirty_five, thirty_six, thirty_seven, thirty_eight, thirty_nine, forty, forty_one, forty_two, forty_three, forty_four, forty_five, forty_six, forty_seven, forty_eight, forty_nine, fifty, fifty_one, fifty_two, fifty_three, fifty_four, fifty_five, fifty_six, fifty_seven, fifty_eight, fifty_nine, sixty])
  
  db.session.commit()


def load_tips():
  tip1=Tips(tip="Relaxation Exercises: Breathing, Visualization, Progressive Muscle Relaxation, Biofeedback", source="The Sleep Foundation", link="https://www.sleepfoundation.org/sleep-hygiene/relaxation-exercises-to-help-fall-asleep")
  tip2=Tips(tip="Melatonin: Jetlag, Shifting Schedule, Side Effects, Dosage", source="The Sleep Foundation", link="https://www.sleepfoundation.org/melatonin")
  tip3=Tips(tip="Sleep Apnea: Definition, AHI, Measurement, Home Tests", source="The Sleep Foundation", link="https://www.sleepfoundation.org/sleep-apnea/ahi")
  tip4=Tips(tip="Weighted Blankets: 9 Options, Care, Costs, FAQ", source="The Sleep Foundation", link="https://www.sleepfoundation.org/best-weighted-blankets")
  tip5=Tips(tip="Diseases Linked with Sleep Health: Diabetes, CardioVascular Disease, Obesity, Depression", source="The CDC", link="https://www.cdc.gov/sleep/about_sleep/chronic_disease.html")
  tip6=Tips(tip="Snoring: Causes, Remedies, Devices", source="American Sleep Association", link="https://www.sleepassociation.org/sleep-disorders/snoring/what-causes-snoring/")
  tip7=Tips(tip="Sleep Hygeine: General tips, Schedule, Activites, Food, Environment", source="American Sleep Association", link="https://www.sleepassociation.org/about-sleep/sleep-hygiene-tips/sleep-hygiene/")
  tip8=Tips(tip="Insomnia: Definition, Psychiatric Issues, Physical Issues, Medications, Lifestyle", source="American Sleep Association", link="https://www.sleepassociation.org/sleep-disorders/insomnia/insomnia-causes/")
  tip9=Tips(tip="Nightmares: Nightmares or Night Terrors, Frequency, Treatment", source="American Sleep Association", link="https://www.sleepassociation.org/sleep-disorders/night-terrors/nightmares/")
  tip10=Tips(tip="Circadian Rhythm: Types, Treatments, Research, FAQ", source="American Sleep Association", link="https://www.sleepassociation.org/sleep-disorders/circadian-rhythm/")
  tip11=Tips(tip="Sleep and Fatigue: Sleep Pressure, Circadian Rhythm, Light, Fatigue", source="CDC", link="https://www.cdc.gov/niosh/emres/longhourstraining/sleepfatigue.html")
  tip12=Tips(tip="Naps: Benefits, Drawbacks, Tips", source="The Mayo Clinic", link="https://www.mayoclinic.org/healthy-lifestyle/adult-health/in-depth/napping/art-20048319")
  db.session.add_all([tip1, tip2,tip3, tip4,tip5,tip6,tip7, tip8, tip9, tip10,tip11, tip12])
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

  user_details=User(username=name,email=email, password=password, city=city,birthday=birthday)
  db.session.add(user_details)
  db.session.commit()

  return {"message": "user added"}


@app.route("/login", methods=["POST"])
def login():
  predetails=(json.loads(request.data))
  details=predetails["login"]
  email=details["email"]
  password=details["password"]

  user=User.query.filter_by(email=email).first()
  dbpassword=user.password
  answer=False
  age=0

  if dbpassword==password:
    birthday=user.birthday.date()
    today=date.today()
    agediff=relativedelta(today,birthday)
    age=agediff.years
    answer=True
    city=user.city

  return{"authenticate": answer, "age": age, "city":city}


# @app.route("/profile")
# def profile():
#   return{"members":["hi"]}


# @app.route("/members")
# def members():
#   return{"members":["member1","member2","member3"]}

@app.route("/graph", methods=["POST"])
def graph():
  details=(json.loads(request.data))
  email=details["email"]
  age=details["age"]


  # user=User.query.filter_by(email=email).first()
  times=Age.query.filter_by(age=age).first()
  
  recorded_data=Times.query.order_by(Times.date.desc()).filter_by(user_email=email).limit(7).all()
  dates=[date.today(),date.today(),date.today(),date.today(),date.today(),date.today(),date.today()]
  hours_total=[0,0,0,0,0,0,0]
  
  for data_point in recorded_data:
    edited=data_point.date
    dates.insert(0,edited)
    dates.pop()

  for hours_point in recorded_data:
    hours_total.insert(0,hours_point.hours)
    hours_total.pop()

  # if len(dates) == 0:
  #   dates=[date.today(),date.today(),date.today(),date.today(),date.today(),date.today(),date.today()]
  # if len(hours_total)==0:
    # hours_total=[0,0,0,0,0,0,0]
  return{"hours":[f"{times.hours_low}",f"{times.hours_high}"], "dates": dates, "slept_hours": hours_total}

@app.route("/backhistory", methods=["POST"])
def backhistory():
  details=(json.loads(request.data))
  email=details["data"]["email"]

  user=User.query.filter_by(email=email).first()
  age=date.today().year-user.birthday.year 
  times=Age.query.filter_by(age=age).first()

  counted=details["data"]["count"]
  recorded_data=Times.query.order_by(Times.date.desc()).filter_by(user_email=email).offset(counted).limit(7).all()
  
  dates=[]
  for data_point in recorded_data:
    edited=data_point.date
    dates.insert(0,edited)
  
  hours_total=[]
  for hours_point in recorded_data:
    hours_total.insert(0, hours_point.hours)

  if len(dates)==6:
    dates.extend(date.today())
    hours_total.extend(0)

  if len(dates)==5:
    dates.extend((date.today(),date.today()))
    hours_total.extend((0,0))
  
  if len(dates)==4:
    dates.extend((date.today(),date.today(),date.today()))
    hours_total.extend((0,0,0))

  if len(dates)==3:
    dates.extend((date.today(),date.today(),date.today(),date.today()))
    hours_total.extend((0,0,0,0))

  if len(dates)==2:
    dates.extend((date.today(),date.today(),date.today(),date.today(),date.today()))
    hours_total.extend((0,0,0,0,0))

  if len(dates)==1:
    dates.extend((date.today(),date.today(),date.today(),date.today(),date.today(),date.today()))
    hours_total.extend((0,0,0,0,0,0))

  if len(dates)==0:
    dates.extend((date.today(),date.today(),date.today(),date.today(),date.today(),date.today(),date.today()))
    hours_total.extend((0,0,0,0,0,0,0))

  return{"hours":[f"{times.hours_low}",f"{times.hours_high}"],"dates": dates, "slept_hours": hours_total}

@app.route("/data", methods=["POST"])
def data():
  details=(json.loads(request.data))
  sleep=details["data"]

  email=sleep["email"]
  s1 = sleep["wake"]
  s2 = sleep["sleep"]

  hours1, minutes1 = map(int, s1.split(':'))
  hours2, minutes2 = map(int, s2.split(':'))
  if hours2 < hours1:
    print(hours1, ":hours1", hours2,":hours2", "choice1")
    t_a = datetime.datetime(2021, 10, 24, hours1, minutes1)
    t_b = datetime.datetime(2021, 10, 24, hours2, minutes2)

    difference=t_a-t_b
    hours=difference.total_seconds()/60**2
  elif hours2 > hours1:
    print(hours1, ":hours1", hours2,":hours2", "choice2")
    t_a = datetime.datetime(2021, 10, 25, hours1, minutes1)
    t_b = datetime.datetime(2021, 10, 24, hours2, minutes2)

    difference=t_a-t_b
    hours=difference.total_seconds()/60**2
  # now = datetime.datetime.now()
  # datetime.datetime(2020, 11, 3, 22, 57, 12, 300437)
  # yesterday = datetime.datetime(2020, 11, 3, 22, 57, 12, 300437)
  # diff = now - yesterday
  # '11:15:49' # for example
  # FMT = '%H:%M:%S'
  # tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
  
  # hours=sleep['sleep']-sleep['wake']
  print(hours, 'these are the hours being recorded')
  data=Times(date=sleep['date'], user_email=email, wake=sleep['wake'],sleep=sleep['sleep'], hours=hours)
  if not Times.query.filter_by(date=sleep["date"], user_email=email).first():
    db.session.add(data)
    db.session.commit()
  else:
    db.session.query(Times).filter(Times.date == sleep["date"]).update({"wake": sleep['wake'], "sleep": sleep['sleep'], "hours": hours})
    db.session.commit()
  return{"mess":"age"}

@app.route("/notes", methods=["POST"])
def day():
  noted=(json.loads(request.data))
  note=Notes(user_email=noted["email"], note=noted["note"])
  db.session.add(note)
  db.session.commit()
  return{"message":"success"}

@app.route("/notes/<user_email>", methods=["GET"])
def day_get(user_email):
  
  notes=Notes.query.filter_by(user_email=user_email).all()
  notes_info=[]
  for line in notes:
    notes_info.extend([line.note, line.id])
  return{"notes": notes_info}

@app.route("/notes/<user_email>/<id>", methods=["DELETE"])
def note_delete(user_email=None, id=None):
  notes=Notes.query.filter_by(user_email=user_email, id=id).delete()
  db.session.commit()
  return{"note": "note deleted"}


@app.route("/tips/<user_email>/<id>", methods=["DELETE"])
def tip_delete(user_email=None, id=None):
  tips=User_tips.query.filter_by(user_email=user_email, tip_id=id).delete()
  db.session.commit()
  return{"notes": "tip deleted"}

@app.route("/tips", methods=["GET"])
def tips():
  request=Tips.query.all()
  tips=[]
  for line in request:
    tips.append([line.tip, line.source, line.link, line.id])
  return {"tips":tips}


@app.route("/savedtip", methods=["POST"])
def save_tips():
  pre_saved_tip=(json.loads(request.data))
  saved_tips=pre_saved_tip["data"]

  tip=User_tips(user_email=saved_tips["user_email"],tip_id=saved_tips["tip_id"])
  db.session.add(tip)
  db.session.commit()
  return {"tips":"tip saved"}


@app.route("/dashboardtip/<user_email>", methods=["GET"])
def show_tips(user_email):
  # user_email=request.query_string.decode()
  # id=request.args['id'] /// if you want to pass as a query string

  tipped=User_tips.query.filter_by(user_email=user_email).all()
  tips_array=[]
  for line in tipped:
    tipdetails=Tips.query.filter_by(id=line.tip_id).first()
    tips_array.append([tipdetails.tip, tipdetails.link, tipdetails.id])
  return {"tips":tips_array}

if __name__=="__main__":
  connect_to_db(app)
  print("connected to db")
  db.create_all()
  print("created dbs")
  app.run(debug=True)