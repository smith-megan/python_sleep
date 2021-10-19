from flask import Flask, render_template;
import psycopg2;

# connect to db
con=psycopg2.connect(
  host="localhost",
  database="lunardb",
  user="postgres",
  password="HelloG1T"
)

# cursor
cur=con.cursor()

#insert
cur.execute("INSERT INTO age(age, avg_age_hours) values (%s, %s)", (30, 9))

# execute query
cur.execute("SELECT * FROM age")
rows=cur.fetchall()

for r in rows:
  print(f"id {r[0]} name {r[1]}")


# commit changes
con.commit()
# close cursor
cur.close()

app=Flask(__name__, template_folder="../sleep/build")

# members api route

@app.route("/members")
def members():
  return{"members":["member1","member2","member3"]}


# @app.route("/")
# def index():
#   return{render_template("index.html")}

if __name__=="__main__":
  app.run(debug=True)

# close the connection db
con.close()