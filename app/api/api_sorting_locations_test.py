from io       import StringIO
from unittest import main, TestCase
# import unittest
import urllib.request, codecs, json

server_address = 'http://104.239.139.43:8000'

def http_response_to_json_object (response) :
	reader = codecs.getreader("utf-8")
	return json.load(reader(response))

class TestLocationsSort (TestCase) :

	# Locations sort by name (ascending then descending)

	def test_sort_names_asc (self) :
		url = server_address + '/api/locations?sort=name:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps( {
	"locations": [
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		}
	]
}))
		self.assertEqual(response_object, expected)

	def test_sort_names_desc (self) :
		url = server_address + '/api/locations?sort=name:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		}
	]
}
))
		self.assertEqual(response_object, expected) 



	# Locations sorted by altitude (ascending then descending)

	def test_sort_altitude_asc (self) :
		url = server_address + '/api/locations?sort=altitude:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	def passtest_sort_date_desc (self) :
		url = server_address + '/api/locations?sort=altitude:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		}
	]
}
))
		self.assertEqual(response_object, expected)

	# Locations sorted by annual_rainfall (ascending then descending)

	def test_sort_altitude_desc (self) :
		url = server_address + '/api/locations?sort=annual_rainfall:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		}
	]
}
))
		self.assertEqual(response_object, expected) 



	def passpasstest_sort_date_desc (self) :
		url = server_address + '/api/locations?sort=annual_rainfall:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	# Locations sorted by winter_avgTemp (ascending then descending)


	def test_sort_winterAvgTemp_asc (self) :
		url = server_address + '/api/locations?sort=winter_avgTemp:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	def test_sort_winterAvgTemp_desc (self) :
		url = server_address + '/api/locations?sort=winter_avgTemp:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	# Locations sorted by spring_avgTemp (ascending then descending)

	def test_sort_springAvgTemp_asc (self) :
		url = server_address + '/api/locations?sort=spring_avgTemp:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	def test_sort_springAvgTemp_desc (self) :
		url = server_address + '/api/locations?sort=spring_avgTemp:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	# Locations sorted by summer_avgTemp (ascending then descending)

	def test_sort_summerAvgTemp_asc (self) :
		url = server_address + '/api/locations?sort=summer_avgTemp:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	def test_sort_summerAvgTemp_desc (self) :
		url = server_address + '/api/locations?sort=summer_avgTemp:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	# Locations sorted by fall_avgTemp (ascending then descending)

	def test_sort_fallAvgTemp_asc (self) :
		url = server_address + '/api/locations?sort=fall_avgTemp:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	def test_sort_fallAvgTemp_desc (self) :
		url = server_address + '/api/locations?sort=fall_avgTemp:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	# Locations sorted by winter_avgHumidity (ascending then descending)

	def test_sort_winterAvgHum_asc (self) :
		url = server_address + '/api/locations?sort=winter_avgHumidity:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	def test_sort_winterAvgHum_desc (self) :
		url = server_address + '/api/locations?sort=winter_avgHumidity:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	# Locations sorted by spring_avgHumidity (ascending then descending)

	def test_sort_springAvgHum_asc (self) :
		url = server_address + '/api/locations?sort=spring_avgHumidity:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	def test_sort_springAvgHum_desc (self) :
		url = server_address + '/api/locations?sort=spring_avgHumidity:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	# Locations sorted by summer_avgHumidity (ascending then descending)

	def test_sort_summerAvgHum_asc (self) :
		url = server_address + '/api/locations?sort=summer_avgHumidity:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	def test_sort_summerAvgHum_desc (self) :
		url = server_address + '/api/locations?sort=summer_avgHumidity:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	# Locations sorted by fall_avgHumidity (ascending then descending)

	def test_sort_fallAvgHum_asc (self) :
		url = server_address + '/api/locations?sort=fall_avgHumidity:asc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		}
	]
}
))
		self.assertEqual(response_object, expected) 


	def test_sort_fallAvgHum_desc (self) :
		url = server_address + '/api/locations?sort=fall_avgHumidity:desc'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
	"locations": [
		{
			"altitude": "13ft",
			"annual_rainfall": "47.8in",
			"description": "Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.",
			"fall_avgHumidity": 82,
			"fall_avgTemp": 64,
			"funruns": [
				4
			],
			"id": 7,
			"img": "/static/img/locationTempl/riverhead1.jpg",
			"landing_img": "/static/img/landing/locations/riverheadNYLanding.jpg",
			"landmarks": "Long Island Aquarium and Exhibition Center, Splish Splash",
			"name": "Riverhead, New York",
			"nickname": "Strong Island",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 59,
			"summer_avgHumidity": 90,
			"summer_avgTemp": 81,
			"website_url": "http://www.townofriverheadny.gov/",
			"winter_avgHumidity": 78,
			"winter_avgTemp": 41
		},
		{
			"altitude": "712ft",
			"annual_rainfall": "42.13in",
			"description": "Newry is a town in Oxfor County, Maine. It is the home of Sunday River Ski Resort and has a proportionately large population during winter.",
			"fall_avgHumidity": 80,
			"fall_avgTemp": 43,
			"funruns": [
				11
			],
			"id": 5,
			"img": "/static/img/locationTempl/newry1.jpg",
			"landing_img": "/static/img/landing/locations/newryMELanding.jpg",
			"landmarks": "Artists' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park",
			"name": "Newry, Maine",
			"nickname": "Sunday River Plantation",
			"spring_avgHumidity": 74,
			"spring_avgTemp": 38,
			"summer_avgHumidity": 82,
			"summer_avgTemp": 62,
			"website_url": "http://www.newrymaine.org/",
			"winter_avgHumidity": 84,
			"winter_avgTemp": 16
		},
		{
			"altitude": "1,027ft",
			"annual_rainfall": "52.06in",
			"description": "Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.",
			"fall_avgHumidity": 78,
			"fall_avgTemp": 63,
			"funruns": [
				8
			],
			"id": 3,
			"img": "/static/img/locationTempl/fairburn1.jpg",
			"landing_img": "/static/img/landing/locations/fairburnGALanding.jpg",
			"landmarks": "Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center",
			"name": "Fairburn, Georgia",
			"nickname": "A City Among the Hills",
			"spring_avgHumidity": 78,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 83,
			"summer_avgTemp": 77,
			"website_url": "http://www.fairburn.com/",
			"winter_avgHumidity": 65,
			"winter_avgTemp": 44
		},
		{
			"altitude": "52ft",
			"annual_rainfall": "23.64in",
			"description": "Perched atop hills and filled-in marshland at the entrance to one of the Pacific\u2019s largest natural harbors, San Francisco has had an outsized influence on the history of California and the United States. San Francisco is a center of wealth, military power, progressive culture and high technology.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 68,
			"funruns": [
				3
			],
			"id": 6,
			"img": "/static/img/locationTempl/sanfrancisco1.jpg",
			"landing_img": "/static/img/landing/locations/sanfranciscoCALanding.jpg",
			"landmarks": "Chinatown, Golden Gate Bridge, Golden Gate Park",
			"name": "San Francisco, California",
			"nickname": "The Golden Gate City",
			"spring_avgHumidity": 71,
			"spring_avgTemp": 63,
			"summer_avgHumidity": 79,
			"summer_avgTemp": 66,
			"website_url": "http://www.sanfrancisco.travel/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 58
		},
		{
			"altitude": "46ft",
			"annual_rainfall": "40.43in",
			"description": "Named after the Puyallup Tribe of Native Americans, Puyallup means 'the generous people'. Puyallup was first recognized as a Tree City USA in 2014.",
			"fall_avgHumidity": 73,
			"fall_avgTemp": 62,
			"funruns": [
				6
			],
			"id": 9,
			"img": "/static/img/locationTempl/puyallup1.jpg",
			"landing_img": "/static/img/landing/locations/puyallupWALanding.jpg",
			"landmarks": "U.S District Court, Historic Preservation, City of Tacoma",
			"name": "Puyallup, Washington",
			"nickname": "A Tree City USA",
			"spring_avgHumidity": 84,
			"spring_avgTemp": 61,
			"summer_avgHumidity": 75,
			"summer_avgTemp": 76,
			"website_url": "http://www.cityofpuyallup.org/",
			"winter_avgHumidity": 81,
			"winter_avgTemp": 48
		},
		{
			"altitude": "489ft",
			"annual_rainfall": "34.53in",
			"description": "Austin is the capital of Texas. It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.",
			"fall_avgHumidity": 70,
			"fall_avgTemp": 69,
			"funruns": [
				9,
				10
			],
			"id": 4,
			"img": "/static/img/locationTempl/austin1.jpg",
			"landing_img": "/static/img/landing/locations/austinTXLanding.jpg",
			"landmarks": "Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo",
			"name": "Austin, Texas",
			"nickname": "Live Music Capital of the World",
			"spring_avgHumidity": 86,
			"spring_avgTemp": 67,
			"summer_avgHumidity": 76,
			"summer_avgTemp": 83,
			"website_url": "http://www.austintexas.org/",
			"winter_avgHumidity": 77,
			"winter_avgTemp": 51
		},
		{
			"altitude": "33ft",
			"annual_rainfall": "40.72in",
			"description": "Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.",
			"fall_avgHumidity": 69,
			"fall_avgTemp": 69,
			"funruns": [
				0
			],
			"id": 0,
			"img": "/static/img/locationTempl/baltimore1.jpg",
			"landing_img": "/static/img/landing/locations/baltimoreMDLanding.jpg",
			"landmarks": "National Aquarium in Baltimore, Fort McHenry",
			"name": "Baltimore, Maryland",
			"nickname": "The Charm City",
			"spring_avgHumidity": 61,
			"spring_avgTemp": 65,
			"summer_avgHumidity": 69,
			"summer_avgTemp": 87,
			"website_url": "http://www.baltimorecity.gov/",
			"winter_avgHumidity": 63,
			"winter_avgTemp": 45
		},
		{
			"altitude": "337ft",
			"annual_rainfall": "53.68in",
			"description": "Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.",
			"fall_avgHumidity": 68,
			"fall_avgTemp": 74,
			"funruns": [
				5
			],
			"id": 8,
			"img": "/static/img/locationTempl/memphis1.jpg",
			"landing_img": "/static/img/landing/locations/memphisTNLanding.jpg",
			"landmarks": "Graceland, Memphis Zoo, Stax Museum of American Soul Music",
			"name": "Memphis, Tennessee",
			"nickname": "Home of the Blues",
			"spring_avgHumidity": 63,
			"spring_avgTemp": 73,
			"summer_avgHumidity": 68,
			"summer_avgTemp": 91,
			"website_url": "http://www.memphistn.gov/",
			"winter_avgHumidity": 67,
			"winter_avgTemp": 52
		},
		{
			"altitude": "653ft",
			"annual_rainfall": "39.12in",
			"description": "Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.",
			"fall_avgHumidity": 58,
			"fall_avgTemp": 72,
			"funruns": [
				1
			],
			"id": 2,
			"img": "/static/img/locationTempl/cleveland1.jpg",
			"landing_img": "/static/img/landing/locations/clevelandOHLanding.jpg",
			"landmarks": "Rock and Roll Hall of Fame, Cleveland Metroparks Zoo",
			"name": "Cleveland, Ohio",
			"nickname": "The Forest City",
			"spring_avgHumidity": 59,
			"spring_avgTemp": 58,
			"summer_avgHumidity": 55,
			"summer_avgTemp": 81,
			"website_url": "http://www.city.cleveland.oh.us/CityofCleveland/Home",
			"winter_avgHumidity": 71,
			"winter_avgTemp": 37
		},
		{
			"altitude": "430ft",
			"annual_rainfall": "40.55in",
			"description": "Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.",
			"fall_avgHumidity": 47,
			"fall_avgTemp": 78,
			"funruns": [
				2,
				7
			],
			"id": 1,
			"img": "/static/img/locationTempl/dallas1.jpg",
			"landing_img": "/static/img/landing/locations/dallasTXLanding.jpg",
			"landmarks": "Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium",
			"name": "Dallas, Texas",
			"nickname": "Home of the Cowboys",
			"spring_avgHumidity": 49,
			"spring_avgTemp": 77,
			"summer_avgHumidity": 44,
			"summer_avgTemp": 95,
			"website_url": "http://dallascityhall.com/Pages/default.aspx",
			"winter_avgHumidity": 52,
			"winter_avgTemp": 59
		}
	]
}
))
		self.assertEqual(response_object, expected) 


if __name__ == "__main__" :
		main()