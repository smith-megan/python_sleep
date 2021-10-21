from flask import Flask, render_template, json, request;
from flask_sqlalchemy import SQLAlchemy;

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
    age_avg_hours = db.Column(db.Integer)

    def __repr__(self):
        return f"<age={self.age} age_avg_hours={self.age_avg_hours}>"

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
    birthday=db.Column(db.Date)
    

    def __repr__(self):
        return f"<username={self.username} password={self.password} email={self.email} city={self.city} birthday={self.birthday}>"


@app.route("/members")
def members():
  return{"members":["member1","member2","member3"]}

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