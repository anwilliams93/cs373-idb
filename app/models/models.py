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
    price = db.Column(db.String(650), unique=False)
    hosts = db.Column(db.String(80), unique=False)
    sponsors =db.Column(db.String(300), unique=False)
    charities = db.Column(db.String(300), unique=False)
    website = db.Column(db.String(300), unique=False)
    description =db.Column(db.String(600), unique=False)
    map_url = db.Column(db.String(350), unique=False)
    video_url = db.Column(db.String(350), unique=False)
    fb_url = db.Column(db.String(350), unique=False)
    short = db.Column(db.String(251), unique=False)
    quote_1 = db.Column(db.String(252), unique=False)
    quote_2 = db.Column(db.String(253), unique=False)
    quote_3 = db.Column(db.String(254), unique=False)
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

    def __repr__(self):
        return '<Id %r>' % self.id

# --------------
# Location table
# --------------
class Location(db.Model):
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
    altitude = db.Column(db.String(10), unique=False)
    annual_rainfall = db.Column(db.String(15), unique=False)
    landmarks = db.Column(db.String(350), unique=False)
    website_url = db.Column(db.String(350), unique=False)
    description = db.Column(db.String(600), unique=False)
    landing_img = db.Column(db.String(350), unique=False)
    img = db.Column(db.String(350), unique=False)
    
    # Locations & Fun Runs are one to many
    funruns = db.relationship('FunRun', backref=db.backref('location'))

    def __repr__(self):
        return '<Id %r>' % self.id
