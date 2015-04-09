# -*- coding: utf-8 -*-
from models.models import db, Location, FunRun, Theme, Challenge

def filter_query_parameters(allowed_parameters, request_parameters):
	filtered_parameters = {}
	for k in allowed_parameters:
		if k in request_parameters:
			filtered_parameters[k] = request_parameters[k]
	return filtered_parameters

def select(table, predicate):
	return filter(predicate, table)

def retrieve_entry_points():
	root_urls = {
              		"funruns_url": "/funruns",
                	"themes_url": "/themes",
                	"challenges_url": "/challenges",
                	"locations_url": "/locations"
            	}
	return root_urls

def retrieve_funruns():
	funruns = []

	results = db.session.query(FunRun).order_by(FunRun.id)

	for run in results:
		object_dict = {}
		object_dict['id'] = run.id
		object_dict['name'] = run.name
		object_dict['address'] = run.address
		object_dict['distance'] = run.distance
		object_dict['price'] = run.price
		object_dict['sponsors'] = run.sponsors
		object_dict['charities'] = run.charities
		object_dict['website'] = run.website
		object_dict['description'] = run.description
		object_dict['map_url'] = run.map_url
		object_dict['video_url'] = run.video_url
		object_dict['fb_url'] = run.fb_url
		object_dict['short'] = run.short
		object_dict['landing_img'] = run.landing_img

		quotes = [run.quote_1, run.quote_2, run.quote_3]
		object_dict['quotes'] = quotes

		imgs = [run.img_1, run.img_2, run.img_3]
		object_dict['imgs'] = imgs

		object_dict['loc'] = run.location_id

		theme_ids = []
		for theme in run.funRun_theme:
			theme_ids += [theme.id]
		object_dict['themes'] = sorted(theme_ids)

		challenge_ids = []
		for challenge in run.funRun_challenge:
			challenge_ids += [challenge.id]
		object_dict['challenges'] = sorted(challenge_ids)

		funruns += [object_dict]

	return funruns

def retrieve_themes():
	themes = []

	results = db.session.query(Theme).order_by(Theme.id)

	for theme in results:
		object_dict = {}
		object_dict['id'] = theme.id
		object_dict['name'] = theme.name
		object_dict['buzzwords'] = theme.buzzwords
		object_dict['description'] = theme.description
		object_dict['short'] = theme.short
		object_dict['landing_img'] = theme.landing_img

		imgs = [theme.img_1, theme.img_2, theme.img_3, theme.img_4,
				theme.img_5, theme.img_6, theme.img_7, theme.img_8]
		object_dict['imgs'] = imgs

		run_ids = []
		for run in theme.funruns:
			run_ids += [run.id]
		object_dict['funruns'] = sorted(run_ids)

		challenge_ids = []
		for challenge in theme.theme_challenge:
			challenge_ids += [challenge.id]
		object_dict['challenges'] = sorted(challenge_ids)

		themes += [object_dict]

	return themes

def retrieve_challenges():
	challenges = []

	results = db.session.query(Challenge).order_by(Challenge.id)

	for challenge in results:
		object_dict = {}
		object_dict['id'] = challenge.id
		object_dict['name'] = challenge.name
		object_dict['difficulty'] = challenge.difficulty
		object_dict['flavors'] = challenge.flavors
		object_dict['description'] = challenge.description
		object_dict['landing_img'] = challenge.landing_img

		imgs = [challenge.img_1, challenge.img_2, challenge.img_3]
		object_dict['imgs'] = imgs

		run_ids = []
		for run in challenge.funruns:
			run_ids += [run.id]
		object_dict['funruns'] = sorted(run_ids)

		theme_ids = []
		for theme in challenge.theme:
			theme_ids += [theme.id]
		object_dict['themes'] = sorted(theme_ids)

		challenges += [object_dict]

	return challenges

def retrieve_locations():
	locations = []

	results = db.session.query(Location).order_by(Location.id)

	for location in results:
		object_dict = {}
		object_dict['id'] = location.id
		object_dict['name'] = location.name
		object_dict['nickname'] = location.nickname
		object_dict['winter_avgTemp'] = location.winter_avgTemp
		object_dict['spring_avgTemp'] = location.spring_avgTemp
		object_dict['summer_avgTemp'] = location.summer_avgTemp
		object_dict['fall_avgTemp'] = location.fall_avgTemp
		object_dict['winter_avgHumidity'] = location.winter_avgHumidity
		object_dict['spring_avgHumidity'] = location.spring_avgHumidity
		object_dict['summer_avgHumidity'] = location.summer_avgHumidity
		object_dict['fall_avgHumidity'] = location.fall_avgHumidity
		object_dict['altitude'] = location.altitude
		object_dict['annual_rainfall'] = location.annual_rainfall
		object_dict['landmarks'] = location.landmarks
		object_dict['website_url'] = location.website_url
		object_dict['description'] = location.description
		object_dict['landing_img'] = location.landing_img
		object_dict['img'] = location.img

		run_ids = []
		for run in location.funruns
			run_ids += [run.id]
		object_dict['funruns'] = sorted(run_ids)

		locations += [object_dict]

	return locations
