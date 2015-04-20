from flask import request, jsonify, Blueprint
from api_helpers import *
import re, operator
from types import *

# MOVE TO HELPERS
def isInt(inp):
	try:
		int(inp)
		return True
	except ValueError:
		return False

def isFloat(inp):
	try:
		float(inp)
		return True
	except ValueError:
		return False

def isNumber(inp):
	return isInt(inp) or isFloat(inp)

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

run_query_parameters = {'theme', 'challenge', 'location', 'min_price', 'max_price', 'min_length', 'max_length'}

@funruns_api.route('/funruns', methods = ['GET'])
def get_funruns():
	filtered_params = filter_query_parameters(run_query_parameters, request.args)
	
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	funruns = retrieve_funruns()

	filtered_funruns = funruns

	# THIS NEEDS TO BE CHANGED TO BE MORE GENERIC AND REUSABLE
	for k in filtered_params:
		if k == 'theme' or k == 'challenge':
			if isInt(filtered_params[k]):
				def fxn(e):
					for p in filtered_params[k]:
						return int(p) in e[k + str('s')]
				filtered_funruns = select(filtered_funruns, fxn)
		elif k == 'location':
			if isInt(filtered_params[k]):
				def fxn(e):
					for p in filtered_params[k]:
						return int(p) == e['loc']
				filtered_funruns = select(filtered_funruns, fxn)
		elif k == 'min_price' or k == 'max_price':
			if isNumber(filtered_params[k]):
				def get_prices(e):
					price_strings = re.split("\n", e['price'])
					prices = []
					for s in price_strings:
						match = re.search("[^\w$]*[$](\d*.\d*)", s)
						if match is not None:
							price = float(match.group(1))
							prices += [price]
					return prices

				def price_check(record, predicate):
					prices = get_prices(record)
					for price in prices:
						if predicate(int(filtered_params[k]), price):
							return True
					return False

				if k == 'min_price':
					def use_min(record):
						return price_check(record, operator.le)

					filtered_funruns = select(filtered_funruns, use_min)
				elif k == 'max_price':
					def use_max(record):
						return price_check(record, operator.ge)

					filtered_funruns = select(filtered_funruns, use_max)

		elif k == 'min_length' or k == 'max_length':
			if isNumber(filtered_params[k]):
				def get_lengths(e):
					length_strings = re.split(",\s", e["distance"])
					lengths = []
					for s in length_strings:
						match = re.search("(\d*)([a-zA-Z]*)", s)
						if match is not None:
							temp_len = match.group(1)
							units = match.group(2)
							if units.upper().startswith('Y'):
								length = float(temp_len) * 0.0009144
								lengths += [length]
							elif units.upper().startswith('MI'):
								length = float(temp_len) * 1.60934
								lengths += [length]
					return lengths

				def length_check(record, predicate):
					lengths = get_lengths(record)
					for length in lengths:
						if predicate(int(filtered_params[k]), length):
							return True
					return False

				if k == 'min_length':
					def use_min(record):
						return length_check(record, operator.le)

					filtered_funruns = select(filtered_funruns, use_min)
				elif k == 'max_length':
					def use_max(record):
						return length_check(record, operator.ge)

					filtered_funruns = select(filtered_funruns, use_max)

	return jsonify({'funruns': list(filtered_funruns)})

@funruns_api.route('/funruns/<int:id>', methods = ['GET'])
def get_funrun_by_id(id):
    funruns = retrieve_funruns()
    return jsonify({'funruns': funruns[id]})

@funruns_api.route('/funruns/<int:id>/themes', methods = ['GET'])
def get_funrun_themes(id):
	# ASSUMING THEMES IS THE LIST OF THEMES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	funruns = retrieve_funruns()
	themes = retrieve_themes()
	chosen_themes = []
	for i in funruns[id]['themes']:
		chosen_themes += [themes[i]]
	return jsonify({'themes': chosen_themes})

@funruns_api.route('/funruns/<int:id>/challenges', methods = ['GET'])
def get_funrun_challenges(id):
	# ASSUMING CHALLENGES IS THE ENTIRE LIST OF CHALLENGES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	funruns = retrieve_funruns()
	challenges = retrieve_challenges()
	chosen_challenges = []
	for i in funruns[id]['challenges']:
		chosen_challenges += [challenges[i]]
	return jsonify({'challenges': chosen_challenges})

# Theme Section of API

theme_query_parameters = {'funrun', 'challenge', 'buzzword'}

@funruns_api.route('/themes', methods = ['GET'])
def get_themes():
	filtered_params = filter_query_parameters(theme_query_parameters, request.args)
	
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	themes = retrieve_themes()

	filtered_themes = themes

	for k in filtered_params:
		if k == 'funrun' or k == 'challenge':
			if isInt(filtered_params[k]):
				def fxn(e):
					for p in filtered_params[k]:
						return int(p) in e[k + str('s')]
				filtered_themes = select(filtered_themes, fxn)
		elif k == 'buzzword':
			def check_buzzwords(e):
				buzzwords = re.split(",\s", e[k + str('s')])
				stored_buzzwords = set(buzzwords)
				return filtered_params[k] in stored_buzzwords
			filtered_themes = select(filtered_themes, check_buzzwords)

	return jsonify({'themes': filtered_themes})

@funruns_api.route('/themes/<int:id>', methods = ['GET'])
def get_theme_by_id(id):
    themes = retrieve_themes()
    return jsonify({'themes': themes[id]})

@funruns_api.route('/themes/<int:id>/funruns', methods = ['GET'])
def get_theme_runs(id):
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	# ASSUMING THEMES IS THE LIST OF THEMES
	funruns = retrieve_funruns()
	themes = retrieve_themes()
	chosen_funruns = []
	for i in themes[id]['funruns']:
		chosen_funruns += [funruns[i]]
	return jsonify({'themes': chosen_funruns})

@funruns_api.route('/themes/<int:id>/challenges', methods = ['GET'])
def get_theme_challenges(id):
	# ASSUMING CHALLENGES IS THE ENTIRE LIST OF CHALLENGES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	themes = retrieve_themes()
	challenges = retrieve_challenges()
	chosen_challenges = []
	for i in themes[id]['challenges']:
		chosen_challenges += [challenges[i]]
	return jsonify({'challenges': chosen_challenges})

# Challenge Section of API

challenge_query_parameters = {'funrun', 'theme', 'min_difficulty', 'max_difficulty'}

@funruns_api.route('/challenges', methods = ['GET'])
def get_challenges():
	filtered_params = filter_query_parameters(challenge_query_parameters, request.args)
	
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	challenges = retrieve_challenges()

	filtered_challenges = challenges

	for k in filtered_params:
		if k == 'funrun' or k == 'theme':
			if isInt(filtered_params[k]):
				def fxn(e):
					for p in filtered_params[k]:
						return int(p) in e[k + str('s')]
				filtered_challenges = select(filtered_challenges, fxn)
		elif k == 'min_difficulty' or k == 'max_difficulty':
			if isNumber(filtered_params[k]):
				fxn = lambda: None
				if k == 'min_difficulty':
					fxn = operator.le
				else:
					fxn = operator.ge
				filtered_challenges = select(filtered_challenges, lambda e : fxn(float(filtered_params[k]), e['difficulty']))
	return jsonify({'challenges': filtered_challenges})

@funruns_api.route('/challenges/<int:id>', methods = ['GET'])
def get_challenge_by_id(id):
	challenges = retrieve_challenges()
	return jsonify({'challenges': challenges[id]})

@funruns_api.route('/challenges/<int:id>/funruns', methods = ['GET'])
def get_challenge_runs(id):
	# ASSUMING THEMES IS THE LIST OF THEMES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	challenges = retrieve_challenges()
	funruns = retrieve_funruns()
	chosen_funruns = []
	for i in challenges[id]['funruns']:
		chosen_funruns += [funruns[i]]
	return jsonify({'funruns': chosen_funruns})

@funruns_api.route('/challenges/<int:id>/themes', methods = ['GET'])
def get_challenge_themes(id):
	# ASSUMING CHALLENGES IS THE ENTIRE LIST OF CHALLENGES
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	challenges = retrieve_challenges()
	themes = retrieve_themes()
	chosen_themes = []
	for i in challenges[id]['themes']:
		chosen_themes += [themes[i]]
	return jsonify({'themes': chosen_themes})


### ALYSSA ADDED THIS SHIZ ###
# Location Section of API

location_query_parameters = {'funrun', 'min_winter_temp', 'max_winter_temp', 'min_spring_temp', 'max_spring_temp', 'min_summer_temp', 'max_summer_temp', 'min_fall_temp', 'max_fall_temp',
										'min_winter_humid', 'max_winter_humid', 'min_spring_humid', 'max_spring_humid', 'min_summer_humid', 'max_summer_humid', 'min_fall_humid', 'max_fall_humid'}

@funruns_api.route('/locations', methods = ['GET'])
def get_locations():
	filtered_params = filter_query_parameters(location_query_parameters, request.args)
	
	# ASSUMING FUNRUNS IS THE ENTIRE LIST OF FUNRUNS
	locations = retrieve_locations()

	filtered_locations = locations

	for k in filtered_params:
		if k == 'funrun':
			if isInt(filtered_params[k]):
				def fxn(e):
					for p in filtered_params[k]:
						return int(p) in e[k + str('s')]
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
				filtered_locations = select(filtered_locations, lambda e : fxn(float(filtered_params[k]), e[object_key]))
	return jsonify({'locations': list(filtered_locations)})

@funruns_api.route('/locations/<int:id>', methods = ['GET'])
def get_location_by_id(id):
	locations = retrieve_locations()
	return jsonify({'locations': locations[id]})




