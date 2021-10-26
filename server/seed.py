# import datetime
from sqlalchemy import func

from server import Age, connect_to_db, db, app

def load_age():
  # six = Age(age=6, hours_low=9, hours_high=12)
  seven = Age(age=7, hours_low=9, hours_high=12)


  # We need to add to the session or it won't ever be stored
  db.session.add(seven)
  
  # Once we're done, we should commit our work
  db.session.commit()