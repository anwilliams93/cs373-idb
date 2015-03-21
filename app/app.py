from flask import Flask, render_template, jsonify
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

### REST API CALLS ###

@app.route('/api/funruns', methods=['GET'])
def get_tasks():

    funruns = [
        {
            'id':           1,
            'name':         u'Wipeout Run',
            'city':         u'Baltimore, Maryland',
            'address':      u'Camden Yards\\n333 W Camden St.\\nBaltimore, MD 21201',
            'date':         u'June 6th, 2015',
            'distance':     u'5K',
            'price':        u'March 6th - April 9th: $56\\nApril 10th - May 7th: $61\\nMay 8th - May 21st: $66\\nMay 22nd - June 5th: $71\\nJune 6th: $81',
            'hosts':        u'Ridiculous Obstacle Challenge Race LLC\\nEndemol USA Inc.',
            'sponsors':     u'VaVi Sport & Social',
            'charities':    u'N/A',
            'website':      u'http://wipeoutrun.com/',
            'description':  u'Crash, smash, and splash your way through a 5k course with larger-than-life obstacles and elements inspired by the hit TV show Wipeout! Take on the infamous Big Balls, Sweeper, Wrecking Balls, and Happy Endings! Hilarious thrills and magnificent spills await!'
        }
    ]

    return jsonify({'funruns': funruns})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
