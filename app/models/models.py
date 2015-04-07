from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bear@localhost/models'
db = SQLAlchemy(app)

# # -------------------------------------
# # Many to many table, FunRuns to Themes
# # -------------------------------------
# funRuns_themes = db.Table('funRuns_themes', 
#     db.Column('funrun_id', db.Integer, db.ForeignKey('funruns.id')),
#     db.Column('theme_id', db.Integer, db.ForeignKey('themes.id'))
# )

# # -----------------------------------------
# # Many to many table, FunRuns to Challenges
# # -----------------------------------------
# funRuns_challenges = db.Table('funRuns_challenges', 
#     db.Column('funrun_id', db.Integer, db.ForeignKey('funruns.id')),
#     db.Column('challenge_id', db.Integer, db.ForeignKey('challenges.id'))
# )

# # ----------------------------------------
# # Many to many table, Themes to Challenges
# # ----------------------------------------
# themes_challenges = db.Table('themes_challenges', 
#     db.Column('theme_id', db.Integer, db.ForeignKey('themes.id')),
#     db.Column('challenge_id', db.Integer, db.ForeignKey('challenges.id'))
# )

# -------------
# FunRuns Table 
# -------------
class FunRun(db.Model):
    __tablename__ = 'funruns'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    address= db.Column(db.String(300), unique=True)
    date = db.Column(db.String(20), unique=False)
    distance = db.Column(db.String(20), unique=False) 
    price = db.Column(db.String(250), unique=False)
    hosts = db.Column(db.String(80), unique=False)
    sponsors =db.Column(db.String(300), unique=False)
    charities = db.Column(db.String(300), unique=False)
    website = db.Column(db.String(300), unique=False)
    description =db.Column(db.String(600), unique=False)
    map_url = db.Column(db.String(350), unique=False)
    
    # Fun Runs & Locations are many to one
    location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
    
    # Fun Runs & Themes are many to many
   # funRuns_themes = db.relationship('themes', secondary = funRuns_themes, backref = db.backref('funruns'))
    # Fun Runs & Challenges are many to many
    # funRuns_challenges = db.relationship('challenges', secondary = funRuns_challenges, backref = db.backref('funruns'))

    def __init__(self, id, name, address, date, distance, price, hosts, sponsors, charities, website, description, map_url, location_id):
        self.id = id
        self.name = name
        self.address = address
        self.date = date 
        self.distance = distance
        self.price = price 
        self.hosts = hosts
        self.sponsors = sponsors
        self.charities = charities
        self.website = website
        self.description = description 
        self.map_url = map_url
        self.location_id = location_id


    def __repr__(self):
        return '<Id %r>' % self.id


# ------------
# Themes table
# ------------ 
# class Theme(db.Model):
#     __tablename__ = 'themes'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=False)
#     buzzwords= db.Column(db.String(300), unique=False)
#     description = db.Column(db.String(600), unique=False)
    
#     # Themes & Challenges are many to many
#    # themes_challenges = db.relationship('challenges', secondary = themes_challenges, backref = db.backref('themes'))
#     # Fun Runs & Themes are many to many (see FunRun)

#     def __init__(self, id, name, address, date):
#         self.id = id
#         self.name = name
#         self.buzzwords = buzzwords
#         self.description = description
#     def __repr__(self):
#         return '<Id %r>' % self.id

# # ----------------
# # Challenges table
# # ----------------
# class Challenge(db.Model):
#     __tablename__ = 'challenges'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=False)
#     flavors= db.Column(db.String(300), unique=False)
#     description = db.Column(db.String(600), unique=False)

#     # Themes & Challenges are many to many (see Theme)
#     # Fun Runs & Challenges are many to many (see FunRun)

#     def __init__(self, id, name, flavors, description):
#         self.id = id
#         self.name = name
#         self.flavors = flavors
#         self.description = description 

#     def __repr__(self):
#         return '<Id %r>' % self.id

# --------------
# Location table
# --------------
class Location(db.Model):
    __tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(80), unique=False)
    winter_avgTemp = db.Column(db.Integer, unique=False)
    spring_avgTemp = db.Column(db.Integer, unique=False)
    summer_avgTemp = db.Column(db.Integer, unique=False)
    fall_avgTemp = db.Column(db.Integer, unique=False)
    winter_avgHumidity = db.Column(db.Integer, unique=False)
    spring_avgHumidity = db.Column(db.Integer, unique=False)
    summer_avgHumidity = db.Column(db.Integer, unique=False)
    fall_avgHumidity = db.Column(db.Integer, unique=False)
    altitude = db.Column(db.Integer, unique=False)
    annual_rainfall = db.Column(db.Integer, unique=False)
    landmarks = db.Column(db.String(350), unique=False)
    
    # Locations & Fun Runs are one to many
    #funruns = db.relationship('FunRun', backref=db.backref('locations'))
    
    def __init__(self, id, city, winter_avgTemp, spring_avgTemp, summer_avgTemp, fall_avgTemp, winter_avgHumidity, spring_avgHumidity, summer_avgHumidity, 
                fall_avgHumidity, altitude, annual_rainfall, landmarks):
        self.id = id
        self.city = city
        self.winter_avgTemp = winter_avgTemp
        self.spring_avgTemp = spring_avgTemp
        self.summer_avgTemp = summer_avgTemp
        self.fall_avgTemp = fall_avgTemp
        self.winter_avgHumidity = winter_avgHumidity
        self.spring_avgHumidity = spring_avgHumidity
        self.summer_avgHumidity = summer_avgHumidity
        self.fall_avgHumidity = fall_avgHumidity
        self.altitude = altitude 
        self.annual_rainfall = annual_rainfall
        self.landmarks = landmarks
        #self.funruns = funruns

    def __repr__(self):
        return '<Id %r>' % self.id



db.drop_all()
db.session.commit()

# db.create_all()
# db.session.commit()
# frun1 = FunRun(0, 'name', 'addr', 'date', 'dist', 'price', 'hosts', 'spons', 'charit', 'web', 'desc', 'map')
# loc1 = Location(0, 'blah', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'LANDMARK', [frun1])
# db.session.add(loc1)
# db.session.add(frun1)
# print("whatjkalsdjfkla;sjdfkl;asdf\n\n\n")

# db.session.commit()