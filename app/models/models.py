from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import re
from datetime import date
import calendar
from sqlalchemy.sql import func

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

    def get_prices(self):
        price_strings = re.split("\n", self.price)
        prices = []
        for s in price_strings:
            match = re.search("[^\w$]*[$](\d*.\d*)", s)
            if match is not None:
                price = float(match.group(1))
                prices += [price]
        return prices

    def get_lengths(self):
        length_strings = re.split(",\s", self.distance)
        lengths = []
        for s in length_strings:
            match = re.search("(\d*)([a-zA-Z]*)", s)
            if match is not None:
                print("FOUND MATCH")
                length = float(match.group(1))
                units = match.group(2)
                if units.upper().startswith('Y'):
                    length *= 0.0009144
                elif units.upper().startswith('MI'):
                    length *= 1.60934
                lengths += [length]
        return lengths

    def get_date_object(self):
        date_components = re.search("([a-zA-Z]+)\s(\d+)[a-zA-Z]+,\s(\d+)", self.date)
        if date_components is not None:
            month_string = date_components.group(1)
            day = int(date_components.group(2))
            year = int(date_components.group(3))
            months_dict = {v: k for k,v in enumerate(calendar.month_abbr)}
            month_int = months_dict[month_string[:3]]
            date_object = date(year, month_int, day)
            return date_object
        return None

    def get_related_theme_ids(self):
        return [theme.id for theme in self.funRun_theme]

    def get_related_challenge_ids(self):
        return [challenge.id for challenge in self.funRun_challenge]

    def get_body_text(self):
        return(self.name + "\n" + self.description + "\nAddress: " + self.address + "\nDate: " + self.date + "\nDistance: " + self.distance + "\nHosts: " + self.hosts + "\nSponsors: " + self.sponsors + "\nCharities: " + self.charities)

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

    def get_buzzwords(self):
        return re.split(",\s", self.buzzwords)

    def get_related_funrun_ids(self):
        return [funrun.id for funrun in self.funruns]

    def get_related_challenge_ids(self):
        return [challenge.id for challenge in self.theme_challenge]

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

    def get_related_funrun_ids(self):
        return [funrun.id for funrun in self.funruns]

    def get_related_theme_ids(self):
        return [theme.id for theme in self.theme]

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

    def get_related_funrun_ids(self):
        return [funrun.id for funrun in self.funruns]

    def get_altitude_as_integer(self):
        altitude_match = re.search('(\d+)[a-zA-Z]+', self.altitude)
        if altitude_match is not None:
            return int(altitude_match.group(1))

    def get_annual_rainfall_as_integer(self):
        rainfall_match = re.search('(\d+)[a-zA-Z]+', self.annual_rainfall)
        if rainfall_match is not None:
            return int(rainfall_match.group(1))


def funrun_object_to_dict(funrun):
    funrun_dict = {}
    funrun_dict['id'] = funrun.id - 1
    funrun_dict['name'] = funrun.name
    funrun_dict['date'] = funrun.date
    funrun_dict['city'] = funrun.location.name
    funrun_dict['address'] = funrun.address
    funrun_dict['distance'] = funrun.distance
    funrun_dict['price'] = funrun.price
    funrun_dict['hosts'] = funrun.hosts
    funrun_dict['sponsors'] = funrun.sponsors
    funrun_dict['charities'] = funrun.charities
    funrun_dict['website'] = funrun.website
    funrun_dict['description'] = funrun.description
    funrun_dict['map_url'] = funrun.map_url
    funrun_dict['video_url'] = funrun.video_url
    funrun_dict['fb_url'] = funrun.fb_url
    funrun_dict['short'] = funrun.short
    funrun_dict['landing_img'] = funrun.landing_img

    quotes = [funrun.quote_1, funrun.quote_2, funrun.quote_3]
    funrun_dict['quotes'] = quotes

    imgs = [funrun.img_1, funrun.img_2, funrun.img_3]
    funrun_dict['imgs'] = imgs

    funrun_dict['loc'] = funrun.location_id - 1

    theme_ids = []
    for theme in funrun.funRun_theme:
        theme_ids += [theme.id - 1]
    funrun_dict['themes'] = sorted(theme_ids)

    challenge_ids = []
    for challenge in funrun.funRun_challenge:
        challenge_ids += [challenge.id - 1]
    funrun_dict['challenges'] = sorted(challenge_ids)

    return funrun_dict

def theme_object_to_dict(theme):
    theme_dict = {}
    theme_dict['id'] = theme.id - 1
    theme_dict['name'] = theme.name
    theme_dict['buzzwords'] = theme.buzzwords
    theme_dict['description'] = theme.description
    theme_dict['short'] = theme.short
    theme_dict['landing_img'] = theme.landing_img

    imgs = [theme.img_1, theme.img_2, theme.img_3, theme.img_4,
            theme.img_5, theme.img_6, theme.img_7, theme.img_8]
    theme_dict['imgs'] = imgs

    run_ids = []
    for run in theme.funruns:
        run_ids += [run.id - 1]
    theme_dict['funruns'] = sorted(run_ids)

    challenge_ids = []
    for challenge in theme.theme_challenge:
        challenge_ids += [challenge.id - 1]
    theme_dict['challenges'] = sorted(challenge_ids)

    return theme_dict

def challenge_object_to_dict(challenge):
    challenge_dict = {}
    challenge_dict['id'] = challenge.id - 1
    challenge_dict['name'] = challenge.name
    challenge_dict['difficulty'] = challenge.difficulty
    challenge_dict['flavors'] = challenge.flavors
    challenge_dict['description'] = challenge.description
    challenge_dict['landing_img'] = challenge.landing_img

    imgs = [challenge.img_1, challenge.img_2, challenge.img_3]
    challenge_dict['imgs'] = imgs

    run_ids = []
    for run in challenge.funruns:
        run_ids += [run.id - 1]
    challenge_dict['funruns'] = sorted(run_ids)

    theme_ids = []
    for theme in challenge.theme:
        theme_ids += [theme.id - 1]
    challenge_dict['themes'] = sorted(theme_ids)

    return challenge_dict

def location_object_to_dict(location):
    location_dict = {}
    location_dict['id'] = location.id - 1
    location_dict['name'] = location.name
    location_dict['nickname'] = location.nickname
    location_dict['winter_avgTemp'] = location.winter_avgTemp
    location_dict['spring_avgTemp'] = location.spring_avgTemp
    location_dict['summer_avgTemp'] = location.summer_avgTemp
    location_dict['fall_avgTemp'] = location.fall_avgTemp
    location_dict['winter_avgHumidity'] = location.winter_avgHumidity
    location_dict['spring_avgHumidity'] = location.spring_avgHumidity
    location_dict['summer_avgHumidity'] = location.summer_avgHumidity
    location_dict['fall_avgHumidity'] = location.fall_avgHumidity
    location_dict['altitude'] = location.altitude
    location_dict['annual_rainfall'] = location.annual_rainfall
    location_dict['landmarks'] = location.landmarks
    location_dict['website_url'] = location.website_url
    location_dict['description'] = location.description
    location_dict['landing_img'] = location.landing_img
    location_dict['img'] = location.img

    run_ids = []
    for run in location.funruns:
        run_ids += [run.id - 1]
    location_dict['funruns'] = sorted(run_ids)

    return location_dict


# ------------
# Setup Search
# ------------

def setup_funruns_search(target, connection, **kw):
    # Add text search vector column
    connection.execute("""ALTER TABLE {0} ADD COLUMN search_column tsvector""".format(target.name))

    # Populate search column?
    connection.execute("""UPDATE {0} SET search_column = to_tsvector('english',
                        coalesce(name,'')           || ' ' || coalesce(address, '')     || ' ' ||
                        coalesce(distance, '')      || ' ' || coalesce(hosts, '')       || ' ' ||
                        coalesce(sponsors, '')      || ' ' || coalesce(charities, '')   || ' ' ||
                        coalesce(description, '')   || ' ' || coalesce(short, ''))""".format(target.name))

    # Index the search column
    connection.execute("""CREATE INDEX funrun_search_index ON {0} USING gen(search_column)""".format(target.name))

    connection.execute("""ALTER TABLE {0} ADD COLUMN body_text varchar""".format(target.name))

    connection.execute("""UPDATE {0} SET body_text = 
        coalesce(name, '') || '\n' || coalesce(description, '') ||
        '\nAddress: ' || coalesce(address, '') || '\nDate: ' || coalesce(date, '') ||
        '\nDistance: ' || coalesce(distance, '') || '\nHosts: ' || coalesce(hosts, '') ||
        '\nSponsors: ' || coalesce(sponsors, '') || '\nCharities: ' || coalesce(charities, ''))""")
    # # Create trigger to auto-update the search column
    # connection.execute("""CREATE TRIGGER funrun_search_update BEFORE INSERT OR UPDATE
    #                         ON {0} FOR EACH ROW EXECUTE PROCEDURE
    #                         tsvector_update_trigger('search_column', 'pg_catalog.english',
    #                         'name', 'address', 'distance', 'hosts', 'sponsors', 'charities', 'description', 'short')""".format(target.name))

def search_funruns(search_string):
    q = db.session.query(FunRun).filter(db.text('funrun.search_column @@ plainto_tsquery(:terms)'))
    q = q.params(terms=search_string)
    q = q.order_by(db.text('ts_rank_cd(funrun.search_column, plainto_tsquery(:terms)) DESC'))
    q = q.add_column(func.ts_headline('pg_catalog.english',db.text('funrun.body_text'),func.plainto_tsquery(search_string),'MaxFragments=1, StartSel = <strong>, StopSel = </strong>'))

    return [{'object':funrun_object_to_dict(funrun), 'fragment':fragment} for funrun, fragment in q]
    # return [(funrun, fragments.split()) for funrun, fragments in query]

def search_funruns_wrapper(search_string):
    and_list = search_funruns(search_string)
    or_list = search_funruns(re.sub(' ', ' | ', search_string))

@db.event.listens_for(FunRun, 'instrument_class')
def receive_instrument_class(mapper, class_):
    if mapper.local_table is not None:
        event.listen(mapper.local_table, 'after_create', setup_funruns_search)
        trigger_for_table(mapper.local_table)

def search_database(search_string):
    return search_funruns(search_string)

def search_database_wrapper(search_string):
    and_list = search_database(search_string)
    or_list = search_funruns(re.sub(' ', ' | ', search_string))

    return {'and_results':and_list, 'or_results':or_list}

