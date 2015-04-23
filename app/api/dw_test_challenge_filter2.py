def test_challenge_filter_run2 (self) :
	url = server_address + '/api/challenges?funrun=6'
	response = urllib.request.urlopen(url)
	response_object = http_response_to_json_object(response)
	expected = json.loads(json.dumps( {
		"challenges": [
    {
      "description": "Want to run through a waterfall of bubbles and foam? Or would you rather stay away from the suds and go for the muds!? Either way, get dirty and have fun!",
      "difficulty": 10,
      "flavors": "Foam, Bubbles, Mud, Water, Powder",
      "funruns": [
        0,
        5,
        6,
        8,
        11
      ],
      "id": 5,
      "imgs": [
        "/static/img/challengeTempl/covered1.jpg",
        "/static/img/challengeTempl/covered2.jpg",
        "/static/img/challengeTempl/covered3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/covered1.jpg",
      "name": "Getting Covered in Stuff",
      "themes": [
        4,
        8
      ]
    },
    {
      "description": "Hope you have a 6th sense, because you'll need it where you'll be! Face the darkness and the unknown as you run to somewhere you can't even see!",
      "difficulty": 40,
      "flavors": "Darkness, Face Powder, Fog",
      "funruns": [
        5,
        6
      ],
      "id": 15,
      "imgs": [
        "/static/img/challengeTempl/visibility1.jpg",
        "/static/img/challengeTempl/visibility2.jpg",
        "/static/img/challengeTempl/visibility3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/visibility1.jpg",
      "name": "Running with Limited Visibility",
      "themes": [
        4,
        8
      ]
    }

  ]
  }))
self.assertEqual(response_object, expected)