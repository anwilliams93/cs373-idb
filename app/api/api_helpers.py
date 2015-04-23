# -*- coding: utf-8 -*-
from models.models import db, Location, FunRun, Theme, Challenge
import re

def filter_query_parameters(allowed_parameters, request_parameters):
	filtered_parameters = {}
	for k in allowed_parameters:
		if k in request_parameters:
			filtered_parameters[k] = request_parameters[k]
	return filtered_parameters

def select(table, predicate):
	return filter(predicate, table)

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

def retrieve_entry_points():
	root_urls = {
              		"funruns_url": "/funruns",
                	"themes_url": "/themes",
                	"challenges_url": "/challenges",
                	"locations_url": "/locations"
            	}
	return root_urls

def retrieve_funruns():
	return db.session.query(FunRun).order_by(FunRun.id)

def retrieve_themes():
	return db.session.query(Theme).order_by(Theme.id)

def retrieve_challenges():
	return db.session.query(Challenge).order_by(Challenge.id)

def retrieve_locations():
	return db.session.query(Location).order_by(Location.id)

def split_sort_string(sort_string):
	# Sort string is of format 'field:[asc or desc]'
	strings = re.split(':', sort_string)
	return (strings[0], strings[1])

def is_sort_descending(sort_order):
	return sort_order == 'desc'

# MOVE SORTING FUNCTIONS TO MDOELS.PY
def sort_funruns(funruns, sort_string):
	sort_field, sort_order = split_sort_string(sort_string)

	if sort_field == 'name':
		return sorted(funruns, key=lambda funrun:funrun.name, reverse=is_sort_descending(sort_order))
	elif sort_field == 'date':
		return sorted(funruns, key=lambda funrun:funrun.get_date_object(), reverse=is_sort_descending(sort_order))
	elif sort_field == 'distance':
		if is_sort_descending(sort_order):
			return sorted(funruns, key=lambda funrun:max(funrun.get_lengths()), reverse=is_sort_descending(sort_order))
		else:
			return sorted(funruns, key=lambda funrun:min(funrun.get_lengths()), reverse=is_sort_descending(sort_order))
	elif sort_field == 'price':
		if is_sort_descending(sort_order):
			return sorted(funruns, key=lambda funrun:max(funrun.get_prices()), reverse=is_sort_descending(sort_order))
		else:
			return sorted(funruns, key=lambda funrun:min(funrun.get_prices()), reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_themes':
		return sorted(funruns, key=lambda funrun:len(funrun.funRun_theme), reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_challenges':
		return sorted(funruns, key=lambda funrun:len(funrun.funRun_challenge), reverse=is_sort_descending(sort_order))

def sort_themes(themes, sort_string):
	sort_field, sort_order = split_sort_string(sort_string)

	if sort_field == 'name':
		return sorted(themes, key=lambda theme:theme.name, reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_runs':
		return sorted(themes, key=lambda theme:len(theme.funruns), reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_challenges':
		return sorted(themes, key=lambda theme:len(theme.theme_challenge), reverse=is_sort_descending(sort_order))

def sort_challenges(challenges, sort_string):
	sort_field, sort_order = split_sort_string(sort_string)

	if sort_field == 'name':
		return sorted(challenges, key=lambda challenge:challenge.name, reverse=is_sort_descending(sort_order))
	elif sort_field == 'difficulty':
		return sorted(challenges, key=lambda challenge:challenge.difficulty, reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_runs':
		return sorted(challenges, key=lambda challenge:len(challenge.funruns), reverse=is_sort_descending(sort_order))
	elif sort_field == 'number_of_themes':
		return sorted(challenges, key=lambda challenge:len(challenge.theme), reverse=is_sort_descending(sort_order))

def sort_locations(locations, sort_string):
	sort_field, sort_order = split_sort_string(sort_string)

	seasons = {'winter', 'spring', 'summer', 'fall'}

	if sort_field == 'name':
		return sorted(locations, key=lambda location:location.name, reverse=is_sort_descending(sort_order))
	elif sort_field.endswith('_avgTemp'):
		if sort_field[:-len('_avgTemp')] in seasons:
			return sorted(locations, key=lambda location:getattr(location, sort_field), reverse=is_sort_descending(sort_order))
	elif sort_field.endswith('_avgHumidity'):
		if sort_field[:-len('_avgHumidity')] in seasons:
			return sorted(locations, key=lambda location:getattr(location, sort_field), reverse=is_sort_descending(sort_order))
	elif sort_field == 'altitude':
		return sorted(locations, key=lambda location:location.get_altitude_as_integer(), reverse=is_sort_descending(sort_order))
	elif sort_field == 'annual_rainfall':
		return sorted(locations, key=lambda location:location.get_annual_rainfall_as_integer(), reverse=is_sort_descending(sort_order))

# MOVE OBJECT TO DICT FUNCTIONS TO MODELS
def funrun_object_to_dict(funrun):
	funrun_dict = {}
	funrun_dict['id'] = funrun.id - 1
	funrun_dict['name'] = funrun.name
	funrun_dict['city'] = funrun.location.name
	funrun_dict['address'] = funrun.address
	funrun_dict['distance'] = funrun.distance
	funrun_dict['price'] = funrun.price
	funrun_dict['hosts'] = funrun.hosts
	funrun_dict['sponsors'] = funrun.sponsors
	funrun_dict['charities'] = funrun.charities
	funrun_dict['website'] = funrun.website
	funrun_dict['description'] = funrun.description
	funrun_dict['map_url'] = funrun.map_url
	funrun_dict['video_url'] = funrun.video_url
	funrun_dict['fb_url'] = funrun.fb_url
	funrun_dict['short'] = funrun.short
	funrun_dict['landing_img'] = funrun.landing_img

	quotes = [funrun.quote_1, funrun.quote_2, funrun.quote_3]
	funrun_dict['quotes'] = quotes

	imgs = [funrun.img_1, funrun.img_2, funrun.img_3]
	funrun_dict['imgs'] = imgs

	funrun_dict['loc'] = funrun.location_id - 1

	theme_ids = []
	for theme in funrun.funRun_theme:
		theme_ids += [theme.id - 1]
	funrun_dict['themes'] = sorted(theme_ids)

	challenge_ids = []
	for challenge in funrun.funRun_challenge:
		challenge_ids += [challenge.id - 1]
	funrun_dict['challenges'] = sorted(challenge_ids)

	return funrun_dict

def theme_object_to_dict(theme):
	theme_dict = {}
	theme_dict['id'] = theme.id - 1
	theme_dict['name'] = theme.name
	theme_dict['buzzwords'] = theme.buzzwords
	theme_dict['description'] = theme.description
	theme_dict['short'] = theme.short
	theme_dict['landing_img'] = theme.landing_img

	imgs = [theme.img_1, theme.img_2, theme.img_3, theme.img_4,
			theme.img_5, theme.img_6, theme.img_7, theme.img_8]
	theme_dict['imgs'] = imgs

	run_ids = []
	for run in theme.funruns:
		run_ids += [run.id - 1]
	theme_dict['funruns'] = sorted(run_ids)

	challenge_ids = []
	for challenge in theme.theme_challenge:
		challenge_ids += [challenge.id - 1]
	theme_dict['challenges'] = sorted(challenge_ids)

	return theme_dict

def challenge_object_to_dict(challenge):
	challenge_dict = {}
	challenge_dict['id'] = challenge.id - 1
	challenge_dict['name'] = challenge.name
	challenge_dict['difficulty'] = challenge.difficulty
	challenge_dict['flavors'] = challenge.flavors
	challenge_dict['description'] = challenge.description
	challenge_dict['landing_img'] = challenge.landing_img

	imgs = [challenge.img_1, challenge.img_2, challenge.img_3]
	challenge_dict['imgs'] = imgs

	run_ids = []
	for run in challenge.funruns:
		run_ids += [run.id - 1]
	challenge_dict['funruns'] = sorted(run_ids)

	theme_ids = []
	for theme in challenge.theme:
		theme_ids += [theme.id - 1]
	challenge_dict['themes'] = sorted(theme_ids)

	return challenge_dict

def location_object_to_dict(location):
	location_dict = {}
	location_dict['id'] = location.id - 1
	location_dict['name'] = location.name
	location_dict['nickname'] = location.nickname
	location_dict['winter_avgTemp'] = location.winter_avgTemp
	location_dict['spring_avgTemp'] = location.spring_avgTemp
	location_dict['summer_avgTemp'] = location.summer_avgTemp
	location_dict['fall_avgTemp'] = location.fall_avgTemp
	location_dict['winter_avgHumidity'] = location.winter_avgHumidity
	location_dict['spring_avgHumidity'] = location.spring_avgHumidity
	location_dict['summer_avgHumidity'] = location.summer_avgHumidity
	location_dict['fall_avgHumidity'] = location.fall_avgHumidity
	location_dict['altitude'] = location.altitude
	location_dict['annual_rainfall'] = location.annual_rainfall
	location_dict['landmarks'] = location.landmarks
	location_dict['website_url'] = location.website_url
	location_dict['description'] = location.description
	location_dict['landing_img'] = location.landing_img
	location_dict['img'] = location.img

	run_ids = []
	for run in location.funruns:
		run_ids += [run.id - 1]
	location_dict['funruns'] = sorted(run_ids)

	return location_dict
