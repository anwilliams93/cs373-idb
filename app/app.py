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

@app.route('/themes/<themeID>')
def themetempl(themeID):
    return render_template('themetempl.html', themeID = themeID)

@app.route('/challenges/<challengeID>')
def challengetempl(challengeID):
    return render_template('challengetempl.html', challengeID = challengeID)


### REST API CALLS ###

@app.route('/api/funruns', methods=['GET'])
def get_funruns():
    return jsonify({'funruns': funruns})

@app.route('/api/funruns/<int:id>', methods=['GET'])
def get_funrun_id(id):
    return jsonify({'funruns': funruns[id]})

@app.route('/api/themes', methods=['GET'])
def get_themes():
    return jsonify({'themes': themes})

@app.route('/api/themes/<int:id>', methods=['GET'])
def get_theme_id(id):
    return jsonify({'themes': themes[id]})

@app.route('/api/challenges', methods=['GET'])
def get_challenges():
    return jsonify({'challenges': challenges})

@app.route('/api/challenges/<int:id>', methods=['GET'])
def get_challenge_id(id):
    return jsonify({'challenges': challenges[id]})

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

themes = [
    {
        'id':           1,
        'name':         u'Holiday',
        'buzzwords':    u'Christmas, Thanksgiving, Easter, Valentine\'s Day, St. Patrick\'s Day, New Year\'s, Halloween, 4th of July',
        'description':  u'Instead of sitting around the fire, talking of presents and Santa, why not go for a run with the family? Holiday runs are a great way to get out and celebrate during the festivities! Often featuring thematic competitions and costumes, they\re a sure way of making any holiday a memorable one.'
    },
    {
        'id':           2,
        'name':         u'Intense',
        'buzzwords':    u'Training, Diet, Hardcore, Recovery, Cutthroat',
        'description':  u'More interested in proving how much you can take than how much fun you\'ll actually have? Intense runs are exactly what you need - a good dose of body-numbing, soul-crushing exercise to show your stuff. See if you can survive the brutal difficulty of these events.'
    },
    {
        'id':           3,
        'name':         u'Costume',
        'buzzwords':    u'Silly, Uncomfortable, Dress-Up, Make-Believe',
        'description':  u'Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!'
    }
]

challenges = [
    {
        'id':           1,
        'name':         u'Running On Odd Ground',
        'flavors':      u'Ice, Inflatable Balls, Mud',
        'description':  u'Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.'
    },
    {
        'id':           2,
        'name':         u'Running In A Costume',
        'flavors':      u'Mascot Costumes, Halloween Outfits, Tutus, Nude, Banana Outfit',
        'description':  u'Ideally, running should be done in comfortable shorts and shirt. Instead, some dare to run in costumes - or a lack of costume - in self expression and, oftentimes, silliness.'
    },
    {
        'id':           3,
        'name':         u'Running In Cold Weather',
        'flavors':      u'Snow, Ice, Freezing Temperatures',
        'description':  u'Take on the cold fearlessly with fun runs in less than ideal temperatures. Will the icy winds get to you or will you make it to the finish line and prevail?'
    }
]


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
