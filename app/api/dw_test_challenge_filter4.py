def test_challenge_filter_run4 (self) :
  url = server_address + '/api/challenges?funrun=1&theme=2'
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
    }
  ]
  }))
self.assertEqual(response_object, expected)