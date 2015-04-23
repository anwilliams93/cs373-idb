def test_challenge_filter_run3 (self) :
	url = server_address + '/api/challenges?funrun=3'
	response = urllib.request.urlopen(url)
	response_object = http_response_to_json_object(response)
	expected = json.loads(json.dumps( {
		"challenges": [
    {
      "description": "Ideally, running should be done in comfortable shorts and shirt. Instead, some dare to run in costumes - or a lack of costume - in self expression and, oftentimes, silliness.",
      "difficulty": 20,
      "flavors": "Mascots, Nude, Speedos, Costumes",
      "funruns": [
        1,
        2,
        3,
        4,
        10
      ],
      "id": 1,
      "imgs": [
        "/static/img/challengeTempl/costume1.jpg",
        "/static/img/challengeTempl/costume2.jpg",
        "/static/img/challengeTempl/costume3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/costume1.jpg",
      "name": "Moving In A Costume",
      "themes": [
        0,
        2,
        8,
        9
      ]
    },
    {
      "description": "Fight against gravity and prepare to go over steep hills in runs with hilly landscape. Feel those legs burn as you scale those inclines to the very end!",
      "difficulty": 30,
      "flavors": "High Elevation, Inclines, Steep Roads",
      "funruns": [
        0,
        3,
        8,
        11
      ],
      "id": 3,
      "imgs": [
        "/static/img/challengeTempl/hill1.jpg",
        "/static/img/challengeTempl/hill2.jpg",
        "/static/img/challengeTempl/hill3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/hill1.jpg",
      "name": "Going Over Hills",
      "themes": [
        1,
        3
      ]
    },
    {
      "description": "Take the food on the go and eat as fast as you can - it's part of the race! Some races will reward you with treats at the end or in the middle of the race, but not as a break - as a challenge!",
      "difficulty": 30,
      "flavors": "Food, Drink, Quick Consumption",
      "funruns": [
        3,
        7,
        9
      ],
      "id": 6,
      "imgs": [
        "/static/img/challengeTempl/consuming1.jpg",
        "/static/img/challengeTempl/consuming2.jpg",
        "/static/img/challengeTempl/consuming3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/consuming1.jpg",
      "name": "Consuming",
      "themes": [
        6,
        7
      ]
    }
  ]
  }))
self.assertEqual(response_object, expected)