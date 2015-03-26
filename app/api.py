from flask import request, jsonify, Blueprint
import api_helpers

funruns_api = Blueprint('funruns_api', __name__, url_prefix='/api')


'''
ASSUME THAT ALL PARAMETERS EXCEPT MIN and MAX CAN BE USED ANY NUMBER OF TIMES
'''

# Root Section of API

@funruns_api.route('/', methods = ['GET'])
def get_entry_points():
	root_urls = api_helpers.retrieve_entry_points()
	return jsonify({'urls': root_urls})

# Run Section of API

run_query_parameters = {'theme', 'challenge', 'location', 'min_price', 'max_price', 'min_length', 'max_length'}

@funruns_api.route('/funruns', methods = ['GET'])
def get_funruns():
	filtered_params = api_helpers.filter_query_parameters(run_query_parameters, request.args)
	
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	funruns = api_helpers.retrieve_funruns()

	filtered_funruns = funruns

	# THIS NEEDS TO BE CHANGED TO BE MORE GENERIC AND REUSABLE
	# for k in filtered_params:
	# 	if k == 'theme' or k == 'challenge' or k == 'location':
	# 		filtered_funruns = api_helpers.select(funruns, (lambda e : p in e[k + str('s')] for p in filtered_params[k]))
	# 	elif k == 'min_price' or k == 'min_length':
	# 		filtered_funruns = api_helpers.select(funruns, lambda e : filtered_params[k] <= e[k])
	# 	elif k == 'max_price' or k == 'max_length':
	# 		filtered_funruns = api_helpers.select(funruns, lambda e : e[k] <= filtered_params[k])

	return jsonify({'funruns': filtered_funruns})

@funruns_api.route('/funruns/<int:id>', methods = ['GET'])
def get_funrun_by_id(id):
    funruns = api_helpers.retrieve_funruns()
    return jsonify({'funruns': funruns[id]})

@funruns_api.route('/funruns/<int:id>/themes', methods = ['GET'])
def get_funrun_themes(id):
	# ASSUMING THEMES IS THE LIST OF THEMES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	funruns = api_helpers.retrieve_funruns()
	themes = api_helpers.retrieve_themes()
	chosen_themes = []
	for i in funruns[id]['themes']:
		chosen_themes += [themes[i]]
	return jsonify({'themes': chosen_themes})

@funruns_api.route('/funruns/<int:id>/challenges', methods = ['GET'])
def get_funrun_challenges(id):
	# ASSUMING CHALLENGES IS THE ENTIRE LIST OF CHALLENGES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	funruns = api_helpers.retrieve_funruns()
	challenges = api_helpers.retrieve_challenges()
	chosen_challenges = []
	for i in funruns[id]['challenges']:
		chosen_challenges += [challenges[i]]
	return jsonify({'challenges': chosen_challenges})

# Theme Section of API

theme_query_parameters = {'run', 'challenge', 'name', 'buzzword'}

@funruns_api.route('/themes', methods = ['GET'])
def get_themes():
	filtered_params = api_helpers.filter_query_parameters(theme_query_parameters, request.args)
	
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	themes = api_helpers.retrieve_themes()

	filtered_themes = themes

	# THIS NEEDS TO BE CHANGED TO BE MORE GENERIC AND REUSABLE
	# for k in filtered_params:
	# 	if k == 'theme' or k == 'challenge' or k == 'location':
	# 		filtered_themes = api_helpers.select(themes, (lambda e : p in e[k + str('s')] for p in filtered_params[k]))
	# 	elif k == 'min_price' or k == 'min_length':
	# 		filtered_themes = api_helpers.select(themes, lambda e : filtered_params[k] <= e[k])
	# 	elif k == 'max_price' or k == 'max_length':
	# 		filtered_themes = api_helpers.select(themes, lambda e : e[k] <= filtered_params[k])

	return jsonify({'themes': filtered_themes})

@funruns_api.route('/themes/<int:id>', methods = ['GET'])
def get_theme_by_id(id):
    themes = api_helpers.retrieve_themes()
    return jsonify({'themes': themes[id]})

@funruns_api.route('/themes/<int:id>/funruns', methods = ['GET'])
def get_theme_runs(id):
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	# ASSUMING THEMES IS THE LIST OF THEMES
	funruns = api_helpers.retrieve_funruns()
	themes = api_helpers.retrieve_themes()
	funruns = []
	for i in themes[id]['funruns']:
		funruns += [funruns[i]]
	return jsonify({'themes': funruns})

@funruns_api.route('/themes/<int:id>/challenges', methods = ['GET'])
def get_theme_challenges(id):
	# ASSUMING CHALLENGES IS THE ENTIRE LIST OF CHALLENGES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	themes = api_helpers.retrieve_themes()
	challenges = api_helpers.retrieve_challenges()
	chosen_challenges = []
	for i in themes[id]['challenges']:
		chosen_challenges += [challenges[i]]
	return jsonify({'challenges': chosen_challenges})

# Challenge Section of API

challenge_query_parameters = {'run', 'theme', 'name'}

@funruns_api.route('/challenges', methods = ['GET'])
def get_challenges():
	filtered_params = api_helpers.filter_query_parameters(challenge_query_parameters, request.args)
	
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	challenges = api_helpers.retrieve_challenges()

	filtered_challenges = challenges
	
	# THIS NEEDS TO BE CHANGED TO BE MORE GENERIC AND REUSABLE
	# for k in filtered_params:
	# 	if k == 'theme' or k == 'challenge' or k == 'location':
	# 		filtered_challenges = api_helpers.select(challenges, (lambda e : p in e[k + str('s')] for p in filtered_params[k]))
	# 	elif k == 'min_price' or k == 'min_length':
	# 		filtered_challenges = api_helpers.select(challenges, lambda e : filtered_params[k] <= e[k])
	# 	elif k == 'max_price' or k == 'max_length':
	# 		filtered_challenges = api_helpers.select(challenges, lambda e : e[k] <= filtered_params[k])
	return jsonify({'challenges': filtered_challenges})

@funruns.route('/challenges/<int:id>', methods = ['GET'])
def get_challenge_by_id(id):
	challenges = api_helpers.retrieve_challenges()
	return jsonify({'challenges': challenges[id]})

@funruns.route('/api/challenges/<int:id>/runs', methods = ['GET'])
def get_challenge_runs(id):
	# ASSUMING THEMES IS THE LIST OF THEMES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	challenges = api_helpers.retrieve_challenges()
	funruns = api_helpers.retrieve_funruns()
	chosen_funruns = []
	for i in challenges[id]['funruns']:
		chosen_funruns += [funruns[i]]
	return jsonify({'funruns': chosen_funruns})

@funruns.route('/api/challenges/<int:id>/themes', methods = ['GET'])
def get_challenge_themes(id):
	# ASSUMING CHALLENGES IS THE ENTIRE LIST OF CHALLENGES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	challenges = api_helpers.retrieve_challenges()
	themes = api_helpers.retrieve_themes()
	chosen_themes = []
	for i in challenges[id]['themes']:
		chosen_themes += [themes[i]]
	return jsonify({'themes': chosen_themes})
