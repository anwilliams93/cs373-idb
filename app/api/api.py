from flask import request, jsonify, Blueprint
from api_helpers import *
import re, operator
from types import *
from models.models import db, Location, FunRun, Theme, Challenge

funruns_api = Blueprint('funruns_api', __name__, url_prefix='/api')


'''
ASSUME THAT ALL PARAMETERS EXCEPT MIN and MAX CAN BE USED ANY NUMBER OF TIMES
'''

# Root Section of API

@funruns_api.route('/', methods = ['GET'])
def get_entry_points():
	root_urls = retrieve_entry_points()
	return jsonify({'urls': root_urls})

# Run Section of API

run_query_parameters = {'theme', 'challenge', 'location', 'min_price', 'max_price', 'min_length', 'max_length', 'sort'}

@funruns_api.route('/funruns', methods = ['GET'])
def get_funruns():
	filtered_params = filter_query_parameters(run_query_parameters, request.args)
	
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUN OBJECTS
	filtered_funruns = retrieve_funruns()

	for k in filtered_params:
		if k == 'theme'	or k == 'challenge':
			if isInt(filtered_params[k]):
				def fxn(e):
					related_ids = []
					if k == 'theme':
						related_ids = e.get_related_theme_ids()
					elif k == 'challenge':
						related_ids = e.get_related_challenge_ids()
					for p in filtered_params[k]:
						return (int(p) + 1) in related_ids

				filtered_funruns = select(filtered_funruns, fxn)

		elif k == 'location':
			if isInt(filtered_params[k]):
				def fxn(e):
					for p in filtered_params[k]:
						return (int(p) + 1) == e.location_id
				filtered_funruns = select(filtered_funruns, fxn)

		elif k == 'min_price' or k == 'max_price':
			if isNumber(filtered_params[k]):
				if k == 'min_price':
					filtered_funruns = select(filtered_funruns, lambda element: max(record.get_prices()) >= filtered_params[k])

				elif k == 'max_price':
					filtered_funruns = select(filtered_funruns, lambda element: min(record.get_prices()) <= filtered_params[k])

		elif k == 'min_length' or k == 'max_length':
			if isNumber(filtered_params[k]):
				if k == 'min_length':
					filtered_funruns = select(filtered_funruns, lambda element: max(record.get_lengths()) >= filtered_params[k])

				elif k == 'max_length':
					filtered_funruns = select(filtered_funruns, lambda element: min(record.get_lengths()) <= filtered_params[k])

	if 'sort' in filtered_params:
		filtered_funruns = sort_funruns(filtered_funruns, filtered_params['sort'])

	converted_funruns = (funrun_object_to_dict(run) for run in filtered_funruns)
	return jsonify({'funruns': list(converted_funruns)})

@funruns_api.route('/funruns/<int:id>', methods = ['GET'])
def get_funrun_by_id(id):
    funrun_dict = funrun_object_to_dict(retrieve_funruns()[id])
    return jsonify({'funruns': funrun_dict})

@funruns_api.route('/funruns/<int:id>/themes', methods = ['GET'])
def get_funrun_themes(id):
	# ASSUMING THEMES IS THE LIST OF THEMES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	funruns = retrieve_funruns()
	themes = retrieve_themes()
	chosen_themes = []
	for theme in funruns[id].funRun_theme:
		chosen_themes += [theme_object_to_dict(theme)]
	return jsonify({'themes': chosen_themes})

@funruns_api.route('/funruns/<int:id>/challenges', methods = ['GET'])
def get_funrun_challenges(id):
	# ASSUMING CHALLENGES IS THE ENTIRE LIST OF CHALLENGES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	funruns = retrieve_funruns()
	challenges = retrieve_challenges()
	chosen_challenges = []
	for challenge in funruns[id].funRun_challenge:
		chosen_challenges += [challenge_object_to_dict(challenge)]
	return jsonify({'challenges': chosen_challenges})

# Theme Section of API

theme_query_parameters = {'funrun', 'challenge', 'buzzword', 'sort'}

@funruns_api.route('/themes', methods = ['GET'])
def get_themes():
	filtered_params = filter_query_parameters(theme_query_parameters, request.args)
	
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	filtered_themes = retrieve_themes()

	for k in filtered_params:
		if k == 'funrun' or k == 'challenge':
			if isInt(filtered_params[k]):
				def fxn(e):
					related_ids = []
					if k == 'funrun':
						related_ids = e.get_related_funrun_ids()
					elif k == 'challenge':
						related_ids = e.get_related_challenge_ids()
					for p in filtered_params[k]:
						return (int(p) + 1) in related_ids
					return False

				filtered_themes = select(filtered_themes, fxn)
		elif k == 'buzzword':
			def check_buzzwords(e):
				stored_buzzwords = set(e.get_buzzwords())
				return filtered_params[k] in stored_buzzwords
			filtered_themes = select(filtered_themes, check_buzzwords)

	if 'sort' in filtered_params:
		filtered_themes = sort_themes(filtered_themes, filtered_params['sort'])

	converted_themes = (theme_object_to_dict(theme) for theme in filtered_themes)
	return jsonify({'themes': list(converted_themes)})

@funruns_api.route('/themes/<int:id>', methods = ['GET'])
def get_theme_by_id(id):
    theme_dict = theme_object_to_dict(retrieve_themes()[id])
    return jsonify({'themes': theme_dict})

@funruns_api.route('/themes/<int:id>/funruns', methods = ['GET'])
def get_theme_runs(id):
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	# ASSUMING THEMES IS THE LIST OF THEMES
	funruns = retrieve_funruns()
	themes = retrieve_themes()
	chosen_funruns = []
	for funrun in themes[id].funruns:
		chosen_funruns += [funrun_object_to_dict(funrun)]
	return jsonify({'funruns': chosen_funruns})

@funruns_api.route('/themes/<int:id>/challenges', methods = ['GET'])
def get_theme_challenges(id):
	# ASSUMING CHALLENGES IS THE ENTIRE LIST OF CHALLENGES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	themes = retrieve_themes()
	challenges = retrieve_challenges()
	chosen_challenges = []
	for challenge in themes[id].theme_challenge:
		chosen_challenges += [challenge_object_to_dict(challenge)]
	return jsonify({'challenges': chosen_challenges})

# Challenge Section of API

challenge_query_parameters = {'funrun', 'theme', 'min_difficulty', 'max_difficulty', 'sort'}

@funruns_api.route('/challenges', methods = ['GET'])
def get_challenges():
	filtered_params = filter_query_parameters(challenge_query_parameters, request.args)

	filtered_challenges = retrieve_challenges()

	print(filtered_params)
	for k in filtered_params:
		if k == 'funrun' or k == 'theme':
			if isInt(filtered_params[k]):
				def fxn(e):
					related_ids = []
					if k == 'funrun':
						related_ids = e.get_related_funrun_ids()
					elif k == 'theme':
						related_ids = e.get_related_theme_ids()
					for p in filtered_params[k]:
						return (int(p) + 1) in related_ids

				filtered_challenges = select(filtered_challenges, fxn)
		elif k == 'min_difficulty' or k == 'max_difficulty':
			if isNumber(filtered_params[k]):
				if k == 'min_difficulty':
					filtered_challenges = select(filtered_challenges, lambda e : e.difficulty >= float(filtered_params[k]))
				else:
					filtered_challenges = select(filtered_challenges, lambda e : e.difficulty <= float(filtered_params[k]))
	
	if 'sort' in filtered_params:
		filtered_challenges = sort_challenges(filtered_challenges, filtered_params['sort'])

	converted_challenges = (challenge_object_to_dict(challenge) for challenge in filtered_challenges)
	return jsonify({'challenges': list(converted_challenges)})

@funruns_api.route('/challenges/<int:id>', methods = ['GET'])
def get_challenge_by_id(id):
	challenge_dict = challenge_object_to_dict(retrieve_challenges()[id])
	return jsonify({'challenges': challenge_dict})

@funruns_api.route('/challenges/<int:id>/funruns', methods = ['GET'])
def get_challenge_runs(id):
	# ASSUMING THEMES IS THE LIST OF THEMES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	challenges = retrieve_challenges()
	funruns = retrieve_funruns()
	chosen_funruns = []
	for funrun in challenges[id].funruns:
		chosen_funruns += [funrun_object_to_dict(funrun)]
	return jsonify({'funruns': chosen_funruns})

@funruns_api.route('/challenges/<int:id>/themes', methods = ['GET'])
def get_challenge_themes(id):
	# ASSUMING CHALLENGES IS THE ENTIRE LIST OF CHALLENGES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	challenges = retrieve_challenges()
	themes = retrieve_themes()
	chosen_themes = []
	for theme in challenges[id].theme:
		chosen_themes += [theme_object_to_dict(theme)]
	return jsonify({'themes': chosen_themes})


### ALYSSA ADDED THIS SHIZ ###
# Location Section of API

location_query_parameters = {'funrun', 'min_winter_temp', 'max_winter_temp', 'min_spring_temp', 'max_spring_temp', 'min_summer_temp', 'max_summer_temp', 'min_fall_temp', 'max_fall_temp',
										'min_winter_humid', 'max_winter_humid', 'min_spring_humid', 'max_spring_humid', 'min_summer_humid', 'max_summer_humid', 'min_fall_humid', 'max_fall_humid', 'sort'}

@funruns_api.route('/locations', methods = ['GET'])
def get_locations():
	filtered_params = filter_query_parameters(location_query_parameters, request.args)
	
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	filtered_locations = retrieve_locations()

	for k in filtered_params:
		if k == 'funrun':
			if isInt(filtered_params[k]):
				def fxn(e):
					for p in filtered_params[k]:
						return (int(p) + 1) in e.get_related_funrun_ids()
				filtered_locations = select(filtered_locations, fxn)
		elif k.startswith('min_') or k.startswith('max_'):
			if isNumber(filtered_params[k]):
				fxn = lambda: None
				if k.startswith('min_'):
					fxn = operator.le
				else:
					fxn = operator.ge
				object_key = ''
				if 'temp' in k:
					season = k[4:-5]
					object_key = season + '_avgTemp'
				elif 'humid' in k:	
					season = k[4:-6]
					object_key = season + '_avgHumidity'
				filtered_locations = select(filtered_locations, lambda e : fxn(float(filtered_params[k]), getattr(e, object_key)))
	
	if 'sort' in filtered_params:
		filtered_locations = sort_locations(filtered_locations, filtered_params['sort'])

	converted_locations = (location_object_to_dict(location) for location in filtered_locations)
	return jsonify({'locations': list(converted_locations)})

@funruns_api.route('/locations/<int:id>', methods = ['GET'])
def get_location_by_id(id):
	location_dict = location_object_to_dict(retrieve_locations()[id])
	return jsonify({'locations': location_dict})