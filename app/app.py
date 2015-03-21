from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('home.html') 

@app.route('/welcome')
def welcome():
	return render_template('welcome.html') 

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
	app.run(host='0.0.0.0', port=8000)
