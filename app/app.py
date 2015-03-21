from flask import Flask, render_template, jsonify
app = Flask(__name__)

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

funruns = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/funruns', methods=['GET'])
def get_tasks():
    return jsonify({'funruns': funruns})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000, debug=True)
