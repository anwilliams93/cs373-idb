from flask import Flask, render_template, jsonify, url_for, redirect
from api import funruns_api
from test_functions import runTests

app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(funruns_api)


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

@app.route('/tech')
def tech():
    # output = runTests()
    # print(output)
    runTests()
    output = open('test_output.txt', 'r').read()
    return render_template('tech.html', output = output) 

@app.route('/funruns/<runID>')
def funruntempl(runID):
    return render_template('funruntempl.html', runID = runID)

@app.route('/themes/<themeID>') 
def themetempl(themeID):
    return render_template('themetempl.html', themeID = themeID)

@app.route('/challenges/<challengeID>')
def challengetempl(challengeID):
    return render_template('challengetempl.html', challengeID = challengeID)

@app.route('/locations/<locationID>')
def locationtempl(locationID):
    return render_template('locationtempl.html', locationID = locationID)

### REST API CALLS ###

# @app.route('/api/funruns', methods=['GET'])
# def get_funruns():
#     return jsonify({'funruns': funruns})

# @app.route('/api/funruns/<int:id>', methods=['GET'])
# def get_funrun_id(id):
#     return jsonify({'funruns': funruns[id]})

# @app.route('/api/themes', methods=['GET'])
# def get_themes():
#     return jsonify({'themes': themes})

# @app.route('/api/themes/<int:id>', methods=['GET'])
# def get_theme_id(id):
#     return jsonify({'themes': themes[id]})

# @app.route('/api/challenges', methods=['GET'])
# def get_challenges():
#     return jsonify({'challenges': challenges})

# @app.route('/api/challenges/<int:id>', methods=['GET'])
# def get_challenge_id(id):
#     return jsonify({'challenges': challenges[id]})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
