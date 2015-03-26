from flask import Request
import api_helpers.py


'''
ASSUME THAT ALL PARAMETERS EXCEPT MIN and MAX CAN BE USED ANY NUMBER OF TIMES
'''

# Root Section of API

@app.route('/api', methods = ['GET'])
def get_entry_points():

# Run Section of API

	run_query_parameters = {'theme', 'challenge', 'location', 'min_price', 'max_price', 'min_length', 'max_length'}

@app.route('/api/runs', methods = ['GET'])
def get_runs():
	filtered_params = filter_query_parameters(run_query_parameters, request.args)
	
	# ASSUMING RUNS IS THE ENTIRE LIST OF RUNS
	filtered_runs = runs

	# THIS NEEDS TO BE CHANGED TO BE MORE GENERIC AND REUSABLE
	for k in filtered_params:
		if k == 'theme' or k == 'challenge' or k == 'location':
			filtered_runs = select(runs, lambda e : p in e[k] for p in filtered_params[k])
		elif k == 'min_price' or k == 'min_length':
			filtered_runs = select(runs, lambda e : filtered_params[k] <= e[k])
		elif k == 'max_price' or k == 'max_length':
			filtered_runs = select(runs, lambda e : e[k] <= filtered_params[k])

	return jsonify({'runs': filtered_runs})

@app.route('/api/runs/<int:id>', methods = ['GET'])
def get_run_by_id(id):
    return jsonify({'run': runs[id]})

@app.route('/api/runs/<int:id>/themes', methods = ['GET'])
def get_run_themes(id):
	# Assuming themes is the list of themes
	chosen_themes = []
	for r in runs:
		for i in r[theme]:
			chosen_themes += [themes[i]]
	return jsonify({'themes': chosen_themes})

@app.route('/api/runs/<int:id>/challenges', methods = ['GET'])
def get_run_challenges(id):
	# Assuming challenges is the entire list of challenges
	chosen_challenges = []
	for r in runs:
		for i in r[challenge]:
			chosen_challenges += [challenges[i]]
	return jsonify({'challenges': chosen_challenges})

# Theme Section of API

theme_query_parameters = {'run', 'challenge', 'name', 'buzzword'}

@app.route('/api/themes', methods = ['GET'])
def get_themes():
	request.args
	return jsonify({'runs': runs})

@app.route('/api/themes/<int:id>', methods = ['GET'])
def get_theme_by_id(id):
    return jsonify({'theme': themes[id]})

@app.route('/api/themes/<int:id>/runs', methods = ['GET'])
def get_theme_runs(id):

@app.route('/api/themes/<int:id>/challenges', methods = ['GET'])
def get_theme_challenges(id):

# Challenge Section of API
	challenge_query_parameters = {'run', 'theme', 'name'}

@app.route('/api/challenges', methods = ['GET'])
def get_runs():
	request.args
    return jsonify({'runs': runs})

@app.route('/api/challenges/<int:id>', methods = ['GET'])
def get_challenge_by_id(id):
    return jsonify({'challenge': challenges[id]})

@app.route('/api/challenges/<int:id>/runs', methods = ['GET'])
def get_challenge_runs(id):

@app.route('/api/challenges/<int:id>/themes', methods = ['GET'])
def get_challenge_themes(id):