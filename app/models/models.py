from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bear@localhost/models'
db = SQLAlchemy(app)

# -------------------------------------
# Many to many table, FunRuns to Themes
# -------------------------------------
funRun_theme = db.Table('funRuns_themes', 
    db.Column('funrun_id', db.Integer, db.ForeignKey('funrun.id')),
    db.Column('theme_id', db.Integer, db.ForeignKey('theme.id'))
)

# -----------------------------------------
# Many to many table, FunRuns to Challenges
# -----------------------------------------
funRun_challenge = db.Table('funRuns_challenges', 
    db.Column('funrun_id', db.Integer, db.ForeignKey('funrun.id')),
    db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id'))
)

# ----------------------------------------
# Many to many table, Themes to Challenges
# ----------------------------------------
theme_challenge = db.Table('theme_challenge', 
    db.Column('theme_id', db.Integer, db.ForeignKey('theme.id')),
    db.Column('challenge_id', db.Integer, db.ForeignKey('challenge.id'))
)

# -------------
# FunRuns Table 
# -------------
class FunRun(db.Model):
    __tablename__ = 'funrun'
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
    video_url = db.Column(db.String(350), unique=False)
    fb_url = db.Column(db.String(350), unique=False)
    short = db.Column(db.String(250), unique=False)
    quote_1 = db.Column(db.String(250), unique=False)
    quote_2 = db.Column(db.String(250), unique=False)
    quote_3 = db.Column(db.String(250), unique=False)
    landing_img = db.Column(db.String(350), unique=False)
    img_1 = db.Column(db.String(350), unique=False)
    img_2 = db.Column(db.String(350), unique=False)
    img_3 = db.Column(db.String(350), unique=False)
    
    # Fun Runs & Locations are many to one
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))
    
    # Fun Runs & Themes are many to many
    funRun_theme = db.relationship('Theme', secondary = funRun_theme, backref = db.backref('funruns'))
    # Fun Runs & Challenges are many to many
    funRun_challenge = db.relationship('Challenge', secondary = funRun_challenge, backref = db.backref('funruns'))

    # def __init__(self, id, name, address, date, distance, price, 
    #             hosts, sponsors, charities, website, description, 
    #             map_url, video_url, fb_url, short, quote_1, quote_2, 
    #             quote_3, landing_img, img_1, img_2, img_3, location_id, 
    #             funRuns_themes = [], funRuns_challenges = []):

    #     self.id = id
    #     self.name = name
    #     self.address = address
    #     self.date = date 
    #     self.distance = distance
    #     self.price = price 
    #     self.hosts = hosts
    #     self.sponsors = sponsors
    #     self.charities = charities
    #     self.website = website
    #     self.description = description 
    #     self.map_url = map_url
    #     self.video_url = video_url
    #     self.fb_url = fb_url
    #     self.short = short
    #     self.quote_1 = quote_1
    #     self.quote_2 = quote_2
    #     self.quote_3 = quote_3
    #     self.landing_img = landing_img
    #     self.img_1 = img_1
    #     self.img_2 = img_2
    #     self.img_3 = img_3
    #     self.location_id = location_id
    #     self.funRuns_themes = funRuns_themes
    #     self.funRuns_challenges = funRuns_challenges


    def __repr__(self):
        return '<Id %r>' % self.id


# ------------
# Themes table
# ------------ 
class Theme(db.Model):
    __tablename__ = 'theme'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    buzzwords= db.Column(db.String(300), unique=False)
    description = db.Column(db.String(600), unique=False)
    short = db.Column(db.String(250), unique=False)
    landing_img = db.Column(db.String(350), unique=False)
    img_1 = db.Column(db.String(350), unique=False)
    img_2 = db.Column(db.String(350), unique=False)
    img_3 = db.Column(db.String(350), unique=False)
    img_4 = db.Column(db.String(350), unique=False)
    img_5 = db.Column(db.String(350), unique=False)
    img_6 = db.Column(db.String(350), unique=False)
    img_7 = db.Column(db.String(350), unique=False)
    img_8 = db.Column(db.String(350), unique=False)


    # Themes & Challenges are many to many
    theme_challenge = db.relationship('Challenge', secondary = theme_challenge, backref = db.backref('theme'))
    # Fun Runs & Themes are many to many (see FunRun)

    # def __init__(self, id, name, buzzwords, description, 
    #             short, landing_img, img_1, img_2, img_3, 
    #             img_4, img_5, img_6, img_7, img_8, theme_challenge = []):
    #     self.id = id
    #     self.name = name
    #     self.buzzwords = buzzwords
    #     self.description = description
    #     self.short = short
    #     self.landing_img = landing_img
    #     self.img_1 = img_1
    #     self.img_2 = img_2
    #     self.img_3 = img_3
    #     self.img_4 = img_4
    #     self.img_5 = img_5
    #     self.img_6 = img_6
    #     self.img_7 = img_7
    #     self.img_8 = img_8
    #     self.theme_challenge = theme_challenge

    def __repr__(self):
        return '<Id %r>' % self.id

# ----------------
# Challenges table
# ----------------
class Challenge(db.Model):
    __tablename__ = 'challenge'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    difficulty = db.Column(db.Integer, unique=False)
    flavors= db.Column(db.String(300), unique=False)
    description = db.Column(db.String(600), unique=False)
    landing_img = db.Column(db.String(350), unique=False)
    img_1 = db.Column(db.String(350), unique=False)
    img_2 = db.Column(db.String(350), unique=False)
    img_3 = db.Column(db.String(350), unique=False)

    # Themes & Challenges are many to many (see Theme)
    # Fun Runs & Challenges are many to many (see FunRun)

    # def __init__(self, id, name, difficulty, flavors, description,
    #             landing_img, img_1, img_2, img_3):
    #     self.id = id
    #     self.name = name
    #     self.difficulty = difficulty
    #     self.flavors = flavors
    #     self.description = description 
    #     self.landing_img = landing_img
    #     self.img_1 = img_1
    #     self.img_2 = img_2
    #     self.img_3 = img_3

    def __repr__(self):
        return '<Id %r>' % self.id

# --------------
# Location table
# --------------
class Location(db.Model):
    #__tablename__ = 'locations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    nickname = db.Column(db.String(150), unique=False)
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
    website_url = db.Column(db.String(350), unique=False)
    description = db.Column(db.String(600), unique=False)
    landing_img = db.Column(db.String(350), unique=False)
    img = db.Column(db.String(350), unique=False)
    
    # Locations & Fun Runs are one to many
    #funruns = db.relationship('FunRun', backref=db.backref('locations'))
    
    # def __init__(self, id, name, nickname, winter_avgTemp, spring_avgTemp, summer_avgTemp, fall_avgTemp, winter_avgHumidity, spring_avgHumidity, summer_avgHumidity, 
    #             fall_avgHumidity, altitude, annual_rainfall, landmarks, 
    #             website_url, description, landing_img, img):
    #     self.id = id
    #     self.name = name
    #     self.nickname =  nickname
    #     self.winter_avgTemp = winter_avgTemp
    #     self.spring_avgTemp = spring_avgTemp
    #     self.summer_avgTemp = summer_avgTemp
    #     self.fall_avgTemp = fall_avgTemp
    #     self.winter_avgHumidity = winter_avgHumidity
    #     self.spring_avgHumidity = spring_avgHumidity
    #     self.summer_avgHumidity = summer_avgHumidity
    #     self.fall_avgHumidity = fall_avgHumidity
    #     self.altitude = altitude 
    #     self.annual_rainfall = annual_rainfall
    #     self.landmarks = landmarks
    #     self.website_url = website_url
    #     self.description = description
    #     self.landing_img = landing_img
    #     self.img = img

    def __repr__(self):
        return '<Id %r>' % self.id


db.reflect()
db.drop_all()
db.session.commit()

db.create_all()
db.session.commit()



chal1 = Challenge(0, '1', '2', '3')
theme1 = Theme(0, '1', '2', '3')
loc1 = Location(0, 'blah', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'LANDMARK')
frun1 = FunRun(0, 'name', 'addr', 'date', 'dist', 'price', 'hosts', 'spons', 'charit', 'web', 'desc', 'map', 0)

theme1.theme_challenge.append(chal1)
frun1.funRun_theme.append(theme1)
frun1.funRun_challenge.append(chal1)

db.session.add(chal1)
db.session.add(theme1)
db.session.add(loc1)
db.session.add(frun1)

db.session.commit()


