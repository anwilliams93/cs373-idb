from flask import Flask, render_template, jsonify, url_for, redirect
app = Flask(__name__)

### PAGES ###

@app.route('/')
def landing():
    return render_template('index.html') 

@app.route('/funruns')
def funruns():
    return render_template('funruns.html') 

@app.route('/themes')
def themes():
    return render_template('themes.html') 

@app.route('/challenges')
def challenges():
    return render_template('challenges.html') 

@app.route('/locations')
def locations():
    return render_template('locations.html') 

@app.route('/about')
def about():
    return render_template('about.html') 

@app.route('/funruns/<runID>')
def funruntempl(runID):
    return render_template('funruntempl.html', runID = runID)


### REST API CALLS ###

@app.route('/api/funruns', methods=['GET'])
def get_funruns():

    return jsonify({'funruns': funruns})

@app.route('/api/funruns/<int:id>', methods=['GET'])
def get_funruns_id(id):
    return jsonify({'funruns': funruns[id]})

funruns = [
    {
        'id':           0,
        'name':         u'Wipeout Run',
        'city':         u'Baltimore, Maryland',
        'address':      u'Camden Yards\\n333 W Camden St.\\nBaltimore, MD 21201',
        'date':         u'June 6th, 2015',
        'distance':     u'5K',
        'price':        u'March 6th - April 9th: $56\\nApril 10th - May 7th: $61\\nMay 8th - May 21st: $66\\nMay 22nd - June 5th: $71\\nJune 6th: $81',
        'hosts':        u'Ridiculous Obstacle Challenge Race LLC, Endemol USA Inc.',
        'sponsors':     u'VaVi Sport & Social',
        'charities':    u'N/A',
        'website':      u'http://wipeoutrun.com/',
        'description':  u'Crash, smash, and splash your way through a 5k course with larger-than-life obstacles and elements inspired by the hit TV show Wipeout! Take on the infamous Big Balls, Sweeper, Wrecking Balls, and Happy Endings! Hilarious thrills and magnificent spills await!'
    },
    {
        'id':           1,
        'name':         u'A Christmas Story Run',
        'city':         u'Cleveland, Ohio',
        'address':      u'Cleveland Public Square\\nCleveland, OH 44113',
        'date':         u'December 5th, 2015',
        'distance':     u'5K, 10K',
        'price':        u'Before September 30th: $45\\nOctober 1st - December 5th: $55',
        'hosts':        u'A Christmas Story House & Museum',
        'sponsors':     u'Ovaltine, Renaissance HOtels, Dannon, Walmart, McDonalds, The Home Depot',
        'charities':    u'A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects',
        'website':      u'http://achristmasstoryrun.com/',
        'description':  u'The movie producers must have been runners, because the distance between the former Higbee’s Department Store and the A Christmas Story House & Museum is about 5K. Ralphie’s dad, The Old Man must have used the 1938 Oldsmobile to track the distance No GPS in the 1940′s. To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.'
    },
    {
        'id':           2,
        'name':         u'Dallas Turkey Trot',
        'city':         u'Dallas, Texas',
        'address':      u'City Hall Plaza\\n500 Marilla St.\\nDallas, TX 75201',
        'date':         u'November 26th, 2015',
        'distance':     u'5K, 8mi',
        'price':        u'Before September 30th: $30\\nSeptember 31st - November 25th: $35\\nNovember 26th: $45',
        'hosts':        u'YMCA, Capital One Bank',
        'sponsors':     u'The Dallas Morning News, Brand Keepers, City of Dallas, Kroger, Nike, The Dallas Cowboys',
        'charities':    u'The Y Community Programs',
        'website':      u'http://thetrot.org/',
        'description':  u'The Dallas Turkey Trot really proves that everything\'s bigger in Texas. One of the largest multi-event races in the country, this trot attracts elite runners and regular ol\' birds alike. In fact, in 2011, it set a world record for the largest gathering of people dressed as turkeys.'
    }
]



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
