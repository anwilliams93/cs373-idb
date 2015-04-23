from io       import StringIO
from unittest import main, TestCase
# import unittest
import urllib.request, codecs, json

server_address = 'http://104.239.139.43:8000'

def http_response_to_json_object (response) :
	reader = codecs.getreader("utf-8")
	return json.load(reader(response))

class TestChallengesSort (TestCase) :

  # Challenges sorted by name (ascending then descending)

  def test_sort_name_asc (self) :
    url = server_address + '/api/challenges?sort=name:asc'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "challenges": [
    {
      "description": "Better have worked that upper body - you'll be needing it now! Whether it's monkey bars, a swing, or just a rope, you'll be flying high or failing.",
      "difficulty": 60,
      "flavors": "Monkey Bars, Rope Swings, Metal Swings",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 11,
      "imgs": [
        "/static/img/challengeTempl/suspended1.jpg",
        "/static/img/challengeTempl/suspended2.jpg",
        "/static/img/challengeTempl/suspended3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/suspended1.jpg",
      "name": "Being Suspended",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "As if carrying yourself to the finish was hard enough, try moving other objects from point A to point B as well! You better have worked those arms and not just your legs for these weight lifting obstacles.",
      "difficulty": 70,
      "flavors": "Sandbags, Other People, Logs",
      "funruns": [
        8,
        11
      ],
      "id": 7,
      "imgs": [
        "/static/img/challengeTempl/carry1.jpg",
        "/static/img/challengeTempl/carry2.jpg",
        "/static/img/challengeTempl/carry3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/carry1.jpg",
      "name": "Carrying an Object",
      "themes": [
        1,
        5,
        6,
        7
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
    },
    {
      "description": "Don't raise your head - you might just lose it! These challenges force you to get down and dirty, crawling beneath the danger and coming out unscathed.",
      "difficulty": 40,
      "flavors": "Barbed Wire, Tunnels, Electrical Wiring",
      "funruns": [
        4,
        8
      ],
      "id": 10,
      "imgs": [
        "/static/img/challengeTempl/crawling1.jpg",
        "/static/img/challengeTempl/crawling2.jpg",
        "/static/img/challengeTempl/crawling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/crawling1.jpg",
      "name": "Crawling Underneath Obstacles",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Take on extreme temps fearlessly with fun runs in less than ideal temperatures. Will the icy winds or intense heat get to you or will you make it to the finish line and prevail?",
      "difficulty": 80,
      "flavors": "Snow, Ice, Fire, Heat",
      "funruns": [
        1,
        2,
        8,
        10
      ],
      "id": 2,
      "imgs": [
        "/static/img/challengeTempl/extremetemp1.jpg",
        "/static/img/challengeTempl/extremetemp2.jpg",
        "/static/img/challengeTempl/extremetemp3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/extremetemp1.jpg",
      "name": "Enduring Extreme Temperatures",
      "themes": [
        0,
        1
      ]
    },
    {
      "description": "You don't have to outrun your pursuers, you just have to outrun the other people being chased! Don't let yourself get caught in hardcore survival runs where it's kill... or be killed.",
      "difficulty": 70,
      "flavors": "Pursued, Zombies, Capture The Flag",
      "funruns": [
        4
      ],
      "id": 4,
      "imgs": [
        "/static/img/challengeTempl/chased1.jpg",
        "/static/img/challengeTempl/chased2.jpg",
        "/static/img/challengeTempl/chased3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/chased1.jpg",
      "name": "Getting Chased",
      "themes": [
        1,
        9
      ]
    },
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
      "description": "Hope you're sturdy - because you're going to need to face all sorts of projectiles and bulldozing objects! Keep your feet on solid ground, or it might be your head instead!",
      "difficulty": 80,
      "flavors": "Inflated Bulldozer Balls, Thrown Items",
      "funruns": [
        0,
        8
      ],
      "id": 13,
      "imgs": [
        "/static/img/challengeTempl/gettinghit1.jpg",
        "/static/img/challengeTempl/gettinghit2.jpg",
        "/static/img/challengeTempl/gettinghit3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/gettinghit1.jpg",
      "name": "Getting Hit by Objects",
      "themes": [
        1,
        4
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
      "description": "This isn't your average trail - these are buildings, roads, and the urban environment for you to run and jump to your heart's content!",
      "difficulty": 60,
      "flavors": "Buildings, Construction Areas, Urban Areas",
      "funruns": [
        4
      ],
      "id": 14,
      "imgs": [
        "/static/img/challengeTempl/parkour1.jpg",
        "/static/img/challengeTempl/parkour2.jpg",
        "/static/img/challengeTempl/parkour3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/parkour1.jpg",
      "name": "Performing Urban Parkour",
      "themes": [
        1,
        9
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
    },
    {
      "description": "You thought you were almost there, but not you're blocked by an insurmountable wall! If you want to make it to the end, be ready to climb to the top of the wall or you better be ready to fall!",
      "difficulty": 70,
      "flavors": "Wooden Walls, Rope Walls, Chains, Rope Ladders",
      "funruns": [
        0,
        8
      ],
      "id": 8,
      "imgs": [
        "/static/img/challengeTempl/scaling1.jpg",
        "/static/img/challengeTempl/scaling2.jpg",
        "/static/img/challengeTempl/scaling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/scaling1.jpg",
      "name": "Scaling a Wall",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "These fun slides are a few moments of much-needed thrills. Give your legs a rest and get ready to go fast down these steep declines!",
      "difficulty": 10,
      "flavors": "Large Inflatable Slides, Mud Slides, Foam Slides",
      "funruns": [
        0,
        8
      ],
      "id": 9,
      "imgs": [
        "/static/img/challengeTempl/sliding1.jpg",
        "/static/img/challengeTempl/sliding2.jpg",
        "/static/img/challengeTempl/sliding3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/sliding1.jpg",
      "name": "Sliding Down Slopes",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Fall and face the consequences. These challenges keep you on your toes across planks, ropes, and anything you can shake a toe at!",
      "difficulty": 70,
      "flavors": "Balance beams, wooden beams, inflated walkways",
      "funruns": [
        0,
        4,
        8,
        11
      ],
      "id": 12,
      "imgs": [
        "/static/img/challengeTempl/balance1.jpg",
        "/static/img/challengeTempl/balance2.jpg",
        "/static/img/challengeTempl/balance3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/balance1.jpg",
      "name": "Staying Balanced",
      "themes": [
        1,
        4,
        5
      ]
    },
    {
      "description": "Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.",
      "difficulty": 60,
      "flavors": "Ice, Inflatable Balls, Mud",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 0,
      "imgs": [
        "/static/img/challengeTempl/oddGround1.jpg",
        "/static/img/challengeTempl/oddGround2.jpg",
        "/static/img/challengeTempl/oddGround3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/oddGround1.jpg",
      "name": "Stepping On Awkward Ground",
      "themes": [
        1,
        4
      ]
    }
  ]
}
))
    self.assertEqual(response_object, expected) 

  def test_sort_name_desc (self) :
    url = server_address + '/api/challenges?sort=name:desc'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "challenges": [
    {
      "description": "Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.",
      "difficulty": 60,
      "flavors": "Ice, Inflatable Balls, Mud",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 0,
      "imgs": [
        "/static/img/challengeTempl/oddGround1.jpg",
        "/static/img/challengeTempl/oddGround2.jpg",
        "/static/img/challengeTempl/oddGround3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/oddGround1.jpg",
      "name": "Stepping On Awkward Ground",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Fall and face the consequences. These challenges keep you on your toes across planks, ropes, and anything you can shake a toe at!",
      "difficulty": 70,
      "flavors": "Balance beams, wooden beams, inflated walkways",
      "funruns": [
        0,
        4,
        8,
        11
      ],
      "id": 12,
      "imgs": [
        "/static/img/challengeTempl/balance1.jpg",
        "/static/img/challengeTempl/balance2.jpg",
        "/static/img/challengeTempl/balance3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/balance1.jpg",
      "name": "Staying Balanced",
      "themes": [
        1,
        4,
        5
      ]
    },
    {
      "description": "These fun slides are a few moments of much-needed thrills. Give your legs a rest and get ready to go fast down these steep declines!",
      "difficulty": 10,
      "flavors": "Large Inflatable Slides, Mud Slides, Foam Slides",
      "funruns": [
        0,
        8
      ],
      "id": 9,
      "imgs": [
        "/static/img/challengeTempl/sliding1.jpg",
        "/static/img/challengeTempl/sliding2.jpg",
        "/static/img/challengeTempl/sliding3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/sliding1.jpg",
      "name": "Sliding Down Slopes",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "You thought you were almost there, but not you're blocked by an insurmountable wall! If you want to make it to the end, be ready to climb to the top of the wall or you better be ready to fall!",
      "difficulty": 70,
      "flavors": "Wooden Walls, Rope Walls, Chains, Rope Ladders",
      "funruns": [
        0,
        8
      ],
      "id": 8,
      "imgs": [
        "/static/img/challengeTempl/scaling1.jpg",
        "/static/img/challengeTempl/scaling2.jpg",
        "/static/img/challengeTempl/scaling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/scaling1.jpg",
      "name": "Scaling a Wall",
      "themes": [
        1,
        4
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
    },
    {
      "description": "This isn't your average trail - these are buildings, roads, and the urban environment for you to run and jump to your heart's content!",
      "difficulty": 60,
      "flavors": "Buildings, Construction Areas, Urban Areas",
      "funruns": [
        4
      ],
      "id": 14,
      "imgs": [
        "/static/img/challengeTempl/parkour1.jpg",
        "/static/img/challengeTempl/parkour2.jpg",
        "/static/img/challengeTempl/parkour3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/parkour1.jpg",
      "name": "Performing Urban Parkour",
      "themes": [
        1,
        9
      ]
    },
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
      "description": "Hope you're sturdy - because you're going to need to face all sorts of projectiles and bulldozing objects! Keep your feet on solid ground, or it might be your head instead!",
      "difficulty": 80,
      "flavors": "Inflated Bulldozer Balls, Thrown Items",
      "funruns": [
        0,
        8
      ],
      "id": 13,
      "imgs": [
        "/static/img/challengeTempl/gettinghit1.jpg",
        "/static/img/challengeTempl/gettinghit2.jpg",
        "/static/img/challengeTempl/gettinghit3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/gettinghit1.jpg",
      "name": "Getting Hit by Objects",
      "themes": [
        1,
        4
      ]
    },
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
      "description": "You don't have to outrun your pursuers, you just have to outrun the other people being chased! Don't let yourself get caught in hardcore survival runs where it's kill... or be killed.",
      "difficulty": 70,
      "flavors": "Pursued, Zombies, Capture The Flag",
      "funruns": [
        4
      ],
      "id": 4,
      "imgs": [
        "/static/img/challengeTempl/chased1.jpg",
        "/static/img/challengeTempl/chased2.jpg",
        "/static/img/challengeTempl/chased3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/chased1.jpg",
      "name": "Getting Chased",
      "themes": [
        1,
        9
      ]
    },
    {
      "description": "Take on extreme temps fearlessly with fun runs in less than ideal temperatures. Will the icy winds or intense heat get to you or will you make it to the finish line and prevail?",
      "difficulty": 80,
      "flavors": "Snow, Ice, Fire, Heat",
      "funruns": [
        1,
        2,
        8,
        10
      ],
      "id": 2,
      "imgs": [
        "/static/img/challengeTempl/extremetemp1.jpg",
        "/static/img/challengeTempl/extremetemp2.jpg",
        "/static/img/challengeTempl/extremetemp3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/extremetemp1.jpg",
      "name": "Enduring Extreme Temperatures",
      "themes": [
        0,
        1
      ]
    },
    {
      "description": "Don't raise your head - you might just lose it! These challenges force you to get down and dirty, crawling beneath the danger and coming out unscathed.",
      "difficulty": 40,
      "flavors": "Barbed Wire, Tunnels, Electrical Wiring",
      "funruns": [
        4,
        8
      ],
      "id": 10,
      "imgs": [
        "/static/img/challengeTempl/crawling1.jpg",
        "/static/img/challengeTempl/crawling2.jpg",
        "/static/img/challengeTempl/crawling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/crawling1.jpg",
      "name": "Crawling Underneath Obstacles",
      "themes": [
        1,
        4
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
    },
    {
      "description": "As if carrying yourself to the finish was hard enough, try moving other objects from point A to point B as well! You better have worked those arms and not just your legs for these weight lifting obstacles.",
      "difficulty": 70,
      "flavors": "Sandbags, Other People, Logs",
      "funruns": [
        8,
        11
      ],
      "id": 7,
      "imgs": [
        "/static/img/challengeTempl/carry1.jpg",
        "/static/img/challengeTempl/carry2.jpg",
        "/static/img/challengeTempl/carry3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/carry1.jpg",
      "name": "Carrying an Object",
      "themes": [
        1,
        5,
        6,
        7
      ]
    },
    {
      "description": "Better have worked that upper body - you'll be needing it now! Whether it's monkey bars, a swing, or just a rope, you'll be flying high or failing.",
      "difficulty": 60,
      "flavors": "Monkey Bars, Rope Swings, Metal Swings",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 11,
      "imgs": [
        "/static/img/challengeTempl/suspended1.jpg",
        "/static/img/challengeTempl/suspended2.jpg",
        "/static/img/challengeTempl/suspended3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/suspended1.jpg",
      "name": "Being Suspended",
      "themes": [
        1,
        4
      ]
    }
  ]
}
))
    self.assertEqual(response_object, expected) 

  # Challenges sorted by difficulty (ascending then descending)

  def test_sort_difficulty_asc (self) :
    url = server_address + '/api/challenges?sort=difficulty:asc'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
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
      "description": "These fun slides are a few moments of much-needed thrills. Give your legs a rest and get ready to go fast down these steep declines!",
      "difficulty": 10,
      "flavors": "Large Inflatable Slides, Mud Slides, Foam Slides",
      "funruns": [
        0,
        8
      ],
      "id": 9,
      "imgs": [
        "/static/img/challengeTempl/sliding1.jpg",
        "/static/img/challengeTempl/sliding2.jpg",
        "/static/img/challengeTempl/sliding3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/sliding1.jpg",
      "name": "Sliding Down Slopes",
      "themes": [
        1,
        4
      ]
    },
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
    },
    {
      "description": "Don't raise your head - you might just lose it! These challenges force you to get down and dirty, crawling beneath the danger and coming out unscathed.",
      "difficulty": 40,
      "flavors": "Barbed Wire, Tunnels, Electrical Wiring",
      "funruns": [
        4,
        8
      ],
      "id": 10,
      "imgs": [
        "/static/img/challengeTempl/crawling1.jpg",
        "/static/img/challengeTempl/crawling2.jpg",
        "/static/img/challengeTempl/crawling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/crawling1.jpg",
      "name": "Crawling Underneath Obstacles",
      "themes": [
        1,
        4
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
    },
    {
      "description": "Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.",
      "difficulty": 60,
      "flavors": "Ice, Inflatable Balls, Mud",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 0,
      "imgs": [
        "/static/img/challengeTempl/oddGround1.jpg",
        "/static/img/challengeTempl/oddGround2.jpg",
        "/static/img/challengeTempl/oddGround3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/oddGround1.jpg",
      "name": "Stepping On Awkward Ground",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Better have worked that upper body - you'll be needing it now! Whether it's monkey bars, a swing, or just a rope, you'll be flying high or failing.",
      "difficulty": 60,
      "flavors": "Monkey Bars, Rope Swings, Metal Swings",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 11,
      "imgs": [
        "/static/img/challengeTempl/suspended1.jpg",
        "/static/img/challengeTempl/suspended2.jpg",
        "/static/img/challengeTempl/suspended3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/suspended1.jpg",
      "name": "Being Suspended",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "This isn't your average trail - these are buildings, roads, and the urban environment for you to run and jump to your heart's content!",
      "difficulty": 60,
      "flavors": "Buildings, Construction Areas, Urban Areas",
      "funruns": [
        4
      ],
      "id": 14,
      "imgs": [
        "/static/img/challengeTempl/parkour1.jpg",
        "/static/img/challengeTempl/parkour2.jpg",
        "/static/img/challengeTempl/parkour3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/parkour1.jpg",
      "name": "Performing Urban Parkour",
      "themes": [
        1,
        9
      ]
    },
    {
      "description": "You don't have to outrun your pursuers, you just have to outrun the other people being chased! Don't let yourself get caught in hardcore survival runs where it's kill... or be killed.",
      "difficulty": 70,
      "flavors": "Pursued, Zombies, Capture The Flag",
      "funruns": [
        4
      ],
      "id": 4,
      "imgs": [
        "/static/img/challengeTempl/chased1.jpg",
        "/static/img/challengeTempl/chased2.jpg",
        "/static/img/challengeTempl/chased3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/chased1.jpg",
      "name": "Getting Chased",
      "themes": [
        1,
        9
      ]
    },
    {
      "description": "As if carrying yourself to the finish was hard enough, try moving other objects from point A to point B as well! You better have worked those arms and not just your legs for these weight lifting obstacles.",
      "difficulty": 70,
      "flavors": "Sandbags, Other People, Logs",
      "funruns": [
        8,
        11
      ],
      "id": 7,
      "imgs": [
        "/static/img/challengeTempl/carry1.jpg",
        "/static/img/challengeTempl/carry2.jpg",
        "/static/img/challengeTempl/carry3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/carry1.jpg",
      "name": "Carrying an Object",
      "themes": [
        1,
        5,
        6,
        7
      ]
    },
    {
      "description": "You thought you were almost there, but not you're blocked by an insurmountable wall! If you want to make it to the end, be ready to climb to the top of the wall or you better be ready to fall!",
      "difficulty": 70,
      "flavors": "Wooden Walls, Rope Walls, Chains, Rope Ladders",
      "funruns": [
        0,
        8
      ],
      "id": 8,
      "imgs": [
        "/static/img/challengeTempl/scaling1.jpg",
        "/static/img/challengeTempl/scaling2.jpg",
        "/static/img/challengeTempl/scaling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/scaling1.jpg",
      "name": "Scaling a Wall",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Fall and face the consequences. These challenges keep you on your toes across planks, ropes, and anything you can shake a toe at!",
      "difficulty": 70,
      "flavors": "Balance beams, wooden beams, inflated walkways",
      "funruns": [
        0,
        4,
        8,
        11
      ],
      "id": 12,
      "imgs": [
        "/static/img/challengeTempl/balance1.jpg",
        "/static/img/challengeTempl/balance2.jpg",
        "/static/img/challengeTempl/balance3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/balance1.jpg",
      "name": "Staying Balanced",
      "themes": [
        1,
        4,
        5
      ]
    },
    {
      "description": "Take on extreme temps fearlessly with fun runs in less than ideal temperatures. Will the icy winds or intense heat get to you or will you make it to the finish line and prevail?",
      "difficulty": 80,
      "flavors": "Snow, Ice, Fire, Heat",
      "funruns": [
        1,
        2,
        8,
        10
      ],
      "id": 2,
      "imgs": [
        "/static/img/challengeTempl/extremetemp1.jpg",
        "/static/img/challengeTempl/extremetemp2.jpg",
        "/static/img/challengeTempl/extremetemp3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/extremetemp1.jpg",
      "name": "Enduring Extreme Temperatures",
      "themes": [
        0,
        1
      ]
    },
    {
      "description": "Hope you're sturdy - because you're going to need to face all sorts of projectiles and bulldozing objects! Keep your feet on solid ground, or it might be your head instead!",
      "difficulty": 80,
      "flavors": "Inflated Bulldozer Balls, Thrown Items",
      "funruns": [
        0,
        8
      ],
      "id": 13,
      "imgs": [
        "/static/img/challengeTempl/gettinghit1.jpg",
        "/static/img/challengeTempl/gettinghit2.jpg",
        "/static/img/challengeTempl/gettinghit3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/gettinghit1.jpg",
      "name": "Getting Hit by Objects",
      "themes": [
        1,
        4
      ]
    }
  ]
}
))
    self.assertEqual(response_object, expected) 

  def test_sort_difficulty_desc (self) :
    url = server_address + '/api/challenges?sort=difficulty:desc'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "challenges": [
    {
      "description": "Take on extreme temps fearlessly with fun runs in less than ideal temperatures. Will the icy winds or intense heat get to you or will you make it to the finish line and prevail?",
      "difficulty": 80,
      "flavors": "Snow, Ice, Fire, Heat",
      "funruns": [
        1,
        2,
        8,
        10
      ],
      "id": 2,
      "imgs": [
        "/static/img/challengeTempl/extremetemp1.jpg",
        "/static/img/challengeTempl/extremetemp2.jpg",
        "/static/img/challengeTempl/extremetemp3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/extremetemp1.jpg",
      "name": "Enduring Extreme Temperatures",
      "themes": [
        0,
        1
      ]
    },
    {
      "description": "Hope you're sturdy - because you're going to need to face all sorts of projectiles and bulldozing objects! Keep your feet on solid ground, or it might be your head instead!",
      "difficulty": 80,
      "flavors": "Inflated Bulldozer Balls, Thrown Items",
      "funruns": [
        0,
        8
      ],
      "id": 13,
      "imgs": [
        "/static/img/challengeTempl/gettinghit1.jpg",
        "/static/img/challengeTempl/gettinghit2.jpg",
        "/static/img/challengeTempl/gettinghit3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/gettinghit1.jpg",
      "name": "Getting Hit by Objects",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "You don't have to outrun your pursuers, you just have to outrun the other people being chased! Don't let yourself get caught in hardcore survival runs where it's kill... or be killed.",
      "difficulty": 70,
      "flavors": "Pursued, Zombies, Capture The Flag",
      "funruns": [
        4
      ],
      "id": 4,
      "imgs": [
        "/static/img/challengeTempl/chased1.jpg",
        "/static/img/challengeTempl/chased2.jpg",
        "/static/img/challengeTempl/chased3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/chased1.jpg",
      "name": "Getting Chased",
      "themes": [
        1,
        9
      ]
    },
    {
      "description": "As if carrying yourself to the finish was hard enough, try moving other objects from point A to point B as well! You better have worked those arms and not just your legs for these weight lifting obstacles.",
      "difficulty": 70,
      "flavors": "Sandbags, Other People, Logs",
      "funruns": [
        8,
        11
      ],
      "id": 7,
      "imgs": [
        "/static/img/challengeTempl/carry1.jpg",
        "/static/img/challengeTempl/carry2.jpg",
        "/static/img/challengeTempl/carry3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/carry1.jpg",
      "name": "Carrying an Object",
      "themes": [
        1,
        5,
        6,
        7
      ]
    },
    {
      "description": "You thought you were almost there, but not you're blocked by an insurmountable wall! If you want to make it to the end, be ready to climb to the top of the wall or you better be ready to fall!",
      "difficulty": 70,
      "flavors": "Wooden Walls, Rope Walls, Chains, Rope Ladders",
      "funruns": [
        0,
        8
      ],
      "id": 8,
      "imgs": [
        "/static/img/challengeTempl/scaling1.jpg",
        "/static/img/challengeTempl/scaling2.jpg",
        "/static/img/challengeTempl/scaling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/scaling1.jpg",
      "name": "Scaling a Wall",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Fall and face the consequences. These challenges keep you on your toes across planks, ropes, and anything you can shake a toe at!",
      "difficulty": 70,
      "flavors": "Balance beams, wooden beams, inflated walkways",
      "funruns": [
        0,
        4,
        8,
        11
      ],
      "id": 12,
      "imgs": [
        "/static/img/challengeTempl/balance1.jpg",
        "/static/img/challengeTempl/balance2.jpg",
        "/static/img/challengeTempl/balance3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/balance1.jpg",
      "name": "Staying Balanced",
      "themes": [
        1,
        4,
        5
      ]
    },
    {
      "description": "Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.",
      "difficulty": 60,
      "flavors": "Ice, Inflatable Balls, Mud",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 0,
      "imgs": [
        "/static/img/challengeTempl/oddGround1.jpg",
        "/static/img/challengeTempl/oddGround2.jpg",
        "/static/img/challengeTempl/oddGround3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/oddGround1.jpg",
      "name": "Stepping On Awkward Ground",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Better have worked that upper body - you'll be needing it now! Whether it's monkey bars, a swing, or just a rope, you'll be flying high or failing.",
      "difficulty": 60,
      "flavors": "Monkey Bars, Rope Swings, Metal Swings",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 11,
      "imgs": [
        "/static/img/challengeTempl/suspended1.jpg",
        "/static/img/challengeTempl/suspended2.jpg",
        "/static/img/challengeTempl/suspended3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/suspended1.jpg",
      "name": "Being Suspended",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "This isn't your average trail - these are buildings, roads, and the urban environment for you to run and jump to your heart's content!",
      "difficulty": 60,
      "flavors": "Buildings, Construction Areas, Urban Areas",
      "funruns": [
        4
      ],
      "id": 14,
      "imgs": [
        "/static/img/challengeTempl/parkour1.jpg",
        "/static/img/challengeTempl/parkour2.jpg",
        "/static/img/challengeTempl/parkour3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/parkour1.jpg",
      "name": "Performing Urban Parkour",
      "themes": [
        1,
        9
      ]
    },
    {
      "description": "Don't raise your head - you might just lose it! These challenges force you to get down and dirty, crawling beneath the danger and coming out unscathed.",
      "difficulty": 40,
      "flavors": "Barbed Wire, Tunnels, Electrical Wiring",
      "funruns": [
        4,
        8
      ],
      "id": 10,
      "imgs": [
        "/static/img/challengeTempl/crawling1.jpg",
        "/static/img/challengeTempl/crawling2.jpg",
        "/static/img/challengeTempl/crawling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/crawling1.jpg",
      "name": "Crawling Underneath Obstacles",
      "themes": [
        1,
        4
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
    },
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
      "description": "These fun slides are a few moments of much-needed thrills. Give your legs a rest and get ready to go fast down these steep declines!",
      "difficulty": 10,
      "flavors": "Large Inflatable Slides, Mud Slides, Foam Slides",
      "funruns": [
        0,
        8
      ],
      "id": 9,
      "imgs": [
        "/static/img/challengeTempl/sliding1.jpg",
        "/static/img/challengeTempl/sliding2.jpg",
        "/static/img/challengeTempl/sliding3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/sliding1.jpg",
      "name": "Sliding Down Slopes",
      "themes": [
        1,
        4
      ]
    }
  ]
}
))
    self.assertEqual(response_object, expected) 

  # Challenges sorted by number_of_runs (ascending then descending)

  def test_sort_numberOfRuns_asc (self) :
    url = server_address + '/api/challenges?sort=number_of_runs:asc'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "challenges": [
    {
      "description": "You don't have to outrun your pursuers, you just have to outrun the other people being chased! Don't let yourself get caught in hardcore survival runs where it's kill... or be killed.",
      "difficulty": 70,
      "flavors": "Pursued, Zombies, Capture The Flag",
      "funruns": [
        4
      ],
      "id": 4,
      "imgs": [
        "/static/img/challengeTempl/chased1.jpg",
        "/static/img/challengeTempl/chased2.jpg",
        "/static/img/challengeTempl/chased3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/chased1.jpg",
      "name": "Getting Chased",
      "themes": [
        1,
        9
      ]
    },
    {
      "description": "This isn't your average trail - these are buildings, roads, and the urban environment for you to run and jump to your heart's content!",
      "difficulty": 60,
      "flavors": "Buildings, Construction Areas, Urban Areas",
      "funruns": [
        4
      ],
      "id": 14,
      "imgs": [
        "/static/img/challengeTempl/parkour1.jpg",
        "/static/img/challengeTempl/parkour2.jpg",
        "/static/img/challengeTempl/parkour3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/parkour1.jpg",
      "name": "Performing Urban Parkour",
      "themes": [
        1,
        9
      ]
    },
    {
      "description": "As if carrying yourself to the finish was hard enough, try moving other objects from point A to point B as well! You better have worked those arms and not just your legs for these weight lifting obstacles.",
      "difficulty": 70,
      "flavors": "Sandbags, Other People, Logs",
      "funruns": [
        8,
        11
      ],
      "id": 7,
      "imgs": [
        "/static/img/challengeTempl/carry1.jpg",
        "/static/img/challengeTempl/carry2.jpg",
        "/static/img/challengeTempl/carry3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/carry1.jpg",
      "name": "Carrying an Object",
      "themes": [
        1,
        5,
        6,
        7
      ]
    },
    {
      "description": "You thought you were almost there, but not you're blocked by an insurmountable wall! If you want to make it to the end, be ready to climb to the top of the wall or you better be ready to fall!",
      "difficulty": 70,
      "flavors": "Wooden Walls, Rope Walls, Chains, Rope Ladders",
      "funruns": [
        0,
        8
      ],
      "id": 8,
      "imgs": [
        "/static/img/challengeTempl/scaling1.jpg",
        "/static/img/challengeTempl/scaling2.jpg",
        "/static/img/challengeTempl/scaling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/scaling1.jpg",
      "name": "Scaling a Wall",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "These fun slides are a few moments of much-needed thrills. Give your legs a rest and get ready to go fast down these steep declines!",
      "difficulty": 10,
      "flavors": "Large Inflatable Slides, Mud Slides, Foam Slides",
      "funruns": [
        0,
        8
      ],
      "id": 9,
      "imgs": [
        "/static/img/challengeTempl/sliding1.jpg",
        "/static/img/challengeTempl/sliding2.jpg",
        "/static/img/challengeTempl/sliding3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/sliding1.jpg",
      "name": "Sliding Down Slopes",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Don't raise your head - you might just lose it! These challenges force you to get down and dirty, crawling beneath the danger and coming out unscathed.",
      "difficulty": 40,
      "flavors": "Barbed Wire, Tunnels, Electrical Wiring",
      "funruns": [
        4,
        8
      ],
      "id": 10,
      "imgs": [
        "/static/img/challengeTempl/crawling1.jpg",
        "/static/img/challengeTempl/crawling2.jpg",
        "/static/img/challengeTempl/crawling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/crawling1.jpg",
      "name": "Crawling Underneath Obstacles",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Hope you're sturdy - because you're going to need to face all sorts of projectiles and bulldozing objects! Keep your feet on solid ground, or it might be your head instead!",
      "difficulty": 80,
      "flavors": "Inflated Bulldozer Balls, Thrown Items",
      "funruns": [
        0,
        8
      ],
      "id": 13,
      "imgs": [
        "/static/img/challengeTempl/gettinghit1.jpg",
        "/static/img/challengeTempl/gettinghit2.jpg",
        "/static/img/challengeTempl/gettinghit3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/gettinghit1.jpg",
      "name": "Getting Hit by Objects",
      "themes": [
        1,
        4
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
    },
    {
      "description": "Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.",
      "difficulty": 60,
      "flavors": "Ice, Inflatable Balls, Mud",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 0,
      "imgs": [
        "/static/img/challengeTempl/oddGround1.jpg",
        "/static/img/challengeTempl/oddGround2.jpg",
        "/static/img/challengeTempl/oddGround3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/oddGround1.jpg",
      "name": "Stepping On Awkward Ground",
      "themes": [
        1,
        4
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
    },
    {
      "description": "Better have worked that upper body - you'll be needing it now! Whether it's monkey bars, a swing, or just a rope, you'll be flying high or failing.",
      "difficulty": 60,
      "flavors": "Monkey Bars, Rope Swings, Metal Swings",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 11,
      "imgs": [
        "/static/img/challengeTempl/suspended1.jpg",
        "/static/img/challengeTempl/suspended2.jpg",
        "/static/img/challengeTempl/suspended3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/suspended1.jpg",
      "name": "Being Suspended",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Take on extreme temps fearlessly with fun runs in less than ideal temperatures. Will the icy winds or intense heat get to you or will you make it to the finish line and prevail?",
      "difficulty": 80,
      "flavors": "Snow, Ice, Fire, Heat",
      "funruns": [
        1,
        2,
        8,
        10
      ],
      "id": 2,
      "imgs": [
        "/static/img/challengeTempl/extremetemp1.jpg",
        "/static/img/challengeTempl/extremetemp2.jpg",
        "/static/img/challengeTempl/extremetemp3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/extremetemp1.jpg",
      "name": "Enduring Extreme Temperatures",
      "themes": [
        0,
        1
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
      "description": "Fall and face the consequences. These challenges keep you on your toes across planks, ropes, and anything you can shake a toe at!",
      "difficulty": 70,
      "flavors": "Balance beams, wooden beams, inflated walkways",
      "funruns": [
        0,
        4,
        8,
        11
      ],
      "id": 12,
      "imgs": [
        "/static/img/challengeTempl/balance1.jpg",
        "/static/img/challengeTempl/balance2.jpg",
        "/static/img/challengeTempl/balance3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/balance1.jpg",
      "name": "Staying Balanced",
      "themes": [
        1,
        4,
        5
      ]
    },
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
    }
  ]
}
))
    self.assertEqual(response_object, expected) 

  def test_sort_numberOfRuns_desc (self) :
    url = server_address + '/api/challenges?sort=number_of_runs:desc'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
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
      "description": "Take on extreme temps fearlessly with fun runs in less than ideal temperatures. Will the icy winds or intense heat get to you or will you make it to the finish line and prevail?",
      "difficulty": 80,
      "flavors": "Snow, Ice, Fire, Heat",
      "funruns": [
        1,
        2,
        8,
        10
      ],
      "id": 2,
      "imgs": [
        "/static/img/challengeTempl/extremetemp1.jpg",
        "/static/img/challengeTempl/extremetemp2.jpg",
        "/static/img/challengeTempl/extremetemp3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/extremetemp1.jpg",
      "name": "Enduring Extreme Temperatures",
      "themes": [
        0,
        1
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
      "description": "Fall and face the consequences. These challenges keep you on your toes across planks, ropes, and anything you can shake a toe at!",
      "difficulty": 70,
      "flavors": "Balance beams, wooden beams, inflated walkways",
      "funruns": [
        0,
        4,
        8,
        11
      ],
      "id": 12,
      "imgs": [
        "/static/img/challengeTempl/balance1.jpg",
        "/static/img/challengeTempl/balance2.jpg",
        "/static/img/challengeTempl/balance3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/balance1.jpg",
      "name": "Staying Balanced",
      "themes": [
        1,
        4,
        5
      ]
    },
    {
      "description": "Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.",
      "difficulty": 60,
      "flavors": "Ice, Inflatable Balls, Mud",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 0,
      "imgs": [
        "/static/img/challengeTempl/oddGround1.jpg",
        "/static/img/challengeTempl/oddGround2.jpg",
        "/static/img/challengeTempl/oddGround3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/oddGround1.jpg",
      "name": "Stepping On Awkward Ground",
      "themes": [
        1,
        4
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
    },
    {
      "description": "Better have worked that upper body - you'll be needing it now! Whether it's monkey bars, a swing, or just a rope, you'll be flying high or failing.",
      "difficulty": 60,
      "flavors": "Monkey Bars, Rope Swings, Metal Swings",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 11,
      "imgs": [
        "/static/img/challengeTempl/suspended1.jpg",
        "/static/img/challengeTempl/suspended2.jpg",
        "/static/img/challengeTempl/suspended3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/suspended1.jpg",
      "name": "Being Suspended",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "As if carrying yourself to the finish was hard enough, try moving other objects from point A to point B as well! You better have worked those arms and not just your legs for these weight lifting obstacles.",
      "difficulty": 70,
      "flavors": "Sandbags, Other People, Logs",
      "funruns": [
        8,
        11
      ],
      "id": 7,
      "imgs": [
        "/static/img/challengeTempl/carry1.jpg",
        "/static/img/challengeTempl/carry2.jpg",
        "/static/img/challengeTempl/carry3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/carry1.jpg",
      "name": "Carrying an Object",
      "themes": [
        1,
        5,
        6,
        7
      ]
    },
    {
      "description": "You thought you were almost there, but not you're blocked by an insurmountable wall! If you want to make it to the end, be ready to climb to the top of the wall or you better be ready to fall!",
      "difficulty": 70,
      "flavors": "Wooden Walls, Rope Walls, Chains, Rope Ladders",
      "funruns": [
        0,
        8
      ],
      "id": 8,
      "imgs": [
        "/static/img/challengeTempl/scaling1.jpg",
        "/static/img/challengeTempl/scaling2.jpg",
        "/static/img/challengeTempl/scaling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/scaling1.jpg",
      "name": "Scaling a Wall",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "These fun slides are a few moments of much-needed thrills. Give your legs a rest and get ready to go fast down these steep declines!",
      "difficulty": 10,
      "flavors": "Large Inflatable Slides, Mud Slides, Foam Slides",
      "funruns": [
        0,
        8
      ],
      "id": 9,
      "imgs": [
        "/static/img/challengeTempl/sliding1.jpg",
        "/static/img/challengeTempl/sliding2.jpg",
        "/static/img/challengeTempl/sliding3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/sliding1.jpg",
      "name": "Sliding Down Slopes",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Don't raise your head - you might just lose it! These challenges force you to get down and dirty, crawling beneath the danger and coming out unscathed.",
      "difficulty": 40,
      "flavors": "Barbed Wire, Tunnels, Electrical Wiring",
      "funruns": [
        4,
        8
      ],
      "id": 10,
      "imgs": [
        "/static/img/challengeTempl/crawling1.jpg",
        "/static/img/challengeTempl/crawling2.jpg",
        "/static/img/challengeTempl/crawling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/crawling1.jpg",
      "name": "Crawling Underneath Obstacles",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Hope you're sturdy - because you're going to need to face all sorts of projectiles and bulldozing objects! Keep your feet on solid ground, or it might be your head instead!",
      "difficulty": 80,
      "flavors": "Inflated Bulldozer Balls, Thrown Items",
      "funruns": [
        0,
        8
      ],
      "id": 13,
      "imgs": [
        "/static/img/challengeTempl/gettinghit1.jpg",
        "/static/img/challengeTempl/gettinghit2.jpg",
        "/static/img/challengeTempl/gettinghit3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/gettinghit1.jpg",
      "name": "Getting Hit by Objects",
      "themes": [
        1,
        4
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
    },
    {
      "description": "You don't have to outrun your pursuers, you just have to outrun the other people being chased! Don't let yourself get caught in hardcore survival runs where it's kill... or be killed.",
      "difficulty": 70,
      "flavors": "Pursued, Zombies, Capture The Flag",
      "funruns": [
        4
      ],
      "id": 4,
      "imgs": [
        "/static/img/challengeTempl/chased1.jpg",
        "/static/img/challengeTempl/chased2.jpg",
        "/static/img/challengeTempl/chased3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/chased1.jpg",
      "name": "Getting Chased",
      "themes": [
        1,
        9
      ]
    },
    {
      "description": "This isn't your average trail - these are buildings, roads, and the urban environment for you to run and jump to your heart's content!",
      "difficulty": 60,
      "flavors": "Buildings, Construction Areas, Urban Areas",
      "funruns": [
        4
      ],
      "id": 14,
      "imgs": [
        "/static/img/challengeTempl/parkour1.jpg",
        "/static/img/challengeTempl/parkour2.jpg",
        "/static/img/challengeTempl/parkour3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/parkour1.jpg",
      "name": "Performing Urban Parkour",
      "themes": [
        1,
        9
      ]
    }
  ]
}
))
    self.assertEqual(response_object, expected) 

  # Challenges sorted by number_of_themes (ascending then descending)

  def test_sort_numberOfThemes_asc (self) :
    url = server_address + '/api/challenges?sort=number_of_themes:asc'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "challenges": [
    {
      "description": "Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.",
      "difficulty": 60,
      "flavors": "Ice, Inflatable Balls, Mud",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 0,
      "imgs": [
        "/static/img/challengeTempl/oddGround1.jpg",
        "/static/img/challengeTempl/oddGround2.jpg",
        "/static/img/challengeTempl/oddGround3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/oddGround1.jpg",
      "name": "Stepping On Awkward Ground",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Take on extreme temps fearlessly with fun runs in less than ideal temperatures. Will the icy winds or intense heat get to you or will you make it to the finish line and prevail?",
      "difficulty": 80,
      "flavors": "Snow, Ice, Fire, Heat",
      "funruns": [
        1,
        2,
        8,
        10
      ],
      "id": 2,
      "imgs": [
        "/static/img/challengeTempl/extremetemp1.jpg",
        "/static/img/challengeTempl/extremetemp2.jpg",
        "/static/img/challengeTempl/extremetemp3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/extremetemp1.jpg",
      "name": "Enduring Extreme Temperatures",
      "themes": [
        0,
        1
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
      "description": "You don't have to outrun your pursuers, you just have to outrun the other people being chased! Don't let yourself get caught in hardcore survival runs where it's kill... or be killed.",
      "difficulty": 70,
      "flavors": "Pursued, Zombies, Capture The Flag",
      "funruns": [
        4
      ],
      "id": 4,
      "imgs": [
        "/static/img/challengeTempl/chased1.jpg",
        "/static/img/challengeTempl/chased2.jpg",
        "/static/img/challengeTempl/chased3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/chased1.jpg",
      "name": "Getting Chased",
      "themes": [
        1,
        9
      ]
    },
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
    },
    {
      "description": "You thought you were almost there, but not you're blocked by an insurmountable wall! If you want to make it to the end, be ready to climb to the top of the wall or you better be ready to fall!",
      "difficulty": 70,
      "flavors": "Wooden Walls, Rope Walls, Chains, Rope Ladders",
      "funruns": [
        0,
        8
      ],
      "id": 8,
      "imgs": [
        "/static/img/challengeTempl/scaling1.jpg",
        "/static/img/challengeTempl/scaling2.jpg",
        "/static/img/challengeTempl/scaling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/scaling1.jpg",
      "name": "Scaling a Wall",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "These fun slides are a few moments of much-needed thrills. Give your legs a rest and get ready to go fast down these steep declines!",
      "difficulty": 10,
      "flavors": "Large Inflatable Slides, Mud Slides, Foam Slides",
      "funruns": [
        0,
        8
      ],
      "id": 9,
      "imgs": [
        "/static/img/challengeTempl/sliding1.jpg",
        "/static/img/challengeTempl/sliding2.jpg",
        "/static/img/challengeTempl/sliding3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/sliding1.jpg",
      "name": "Sliding Down Slopes",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Don't raise your head - you might just lose it! These challenges force you to get down and dirty, crawling beneath the danger and coming out unscathed.",
      "difficulty": 40,
      "flavors": "Barbed Wire, Tunnels, Electrical Wiring",
      "funruns": [
        4,
        8
      ],
      "id": 10,
      "imgs": [
        "/static/img/challengeTempl/crawling1.jpg",
        "/static/img/challengeTempl/crawling2.jpg",
        "/static/img/challengeTempl/crawling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/crawling1.jpg",
      "name": "Crawling Underneath Obstacles",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Better have worked that upper body - you'll be needing it now! Whether it's monkey bars, a swing, or just a rope, you'll be flying high or failing.",
      "difficulty": 60,
      "flavors": "Monkey Bars, Rope Swings, Metal Swings",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 11,
      "imgs": [
        "/static/img/challengeTempl/suspended1.jpg",
        "/static/img/challengeTempl/suspended2.jpg",
        "/static/img/challengeTempl/suspended3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/suspended1.jpg",
      "name": "Being Suspended",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Hope you're sturdy - because you're going to need to face all sorts of projectiles and bulldozing objects! Keep your feet on solid ground, or it might be your head instead!",
      "difficulty": 80,
      "flavors": "Inflated Bulldozer Balls, Thrown Items",
      "funruns": [
        0,
        8
      ],
      "id": 13,
      "imgs": [
        "/static/img/challengeTempl/gettinghit1.jpg",
        "/static/img/challengeTempl/gettinghit2.jpg",
        "/static/img/challengeTempl/gettinghit3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/gettinghit1.jpg",
      "name": "Getting Hit by Objects",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "This isn't your average trail - these are buildings, roads, and the urban environment for you to run and jump to your heart's content!",
      "difficulty": 60,
      "flavors": "Buildings, Construction Areas, Urban Areas",
      "funruns": [
        4
      ],
      "id": 14,
      "imgs": [
        "/static/img/challengeTempl/parkour1.jpg",
        "/static/img/challengeTempl/parkour2.jpg",
        "/static/img/challengeTempl/parkour3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/parkour1.jpg",
      "name": "Performing Urban Parkour",
      "themes": [
        1,
        9
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
    },
    {
      "description": "Fall and face the consequences. These challenges keep you on your toes across planks, ropes, and anything you can shake a toe at!",
      "difficulty": 70,
      "flavors": "Balance beams, wooden beams, inflated walkways",
      "funruns": [
        0,
        4,
        8,
        11
      ],
      "id": 12,
      "imgs": [
        "/static/img/challengeTempl/balance1.jpg",
        "/static/img/challengeTempl/balance2.jpg",
        "/static/img/challengeTempl/balance3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/balance1.jpg",
      "name": "Staying Balanced",
      "themes": [
        1,
        4,
        5
      ]
    },
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
      "description": "As if carrying yourself to the finish was hard enough, try moving other objects from point A to point B as well! You better have worked those arms and not just your legs for these weight lifting obstacles.",
      "difficulty": 70,
      "flavors": "Sandbags, Other People, Logs",
      "funruns": [
        8,
        11
      ],
      "id": 7,
      "imgs": [
        "/static/img/challengeTempl/carry1.jpg",
        "/static/img/challengeTempl/carry2.jpg",
        "/static/img/challengeTempl/carry3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/carry1.jpg",
      "name": "Carrying an Object",
      "themes": [
        1,
        5,
        6,
        7
      ]
    }
  ]
}
))
    self.assertEqual(response_object, expected) 

  def test_sort_numberOfThemes_desc (self) :
    url = server_address + '/api/challenges?sort=number_of_themes:desc'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
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
      "description": "As if carrying yourself to the finish was hard enough, try moving other objects from point A to point B as well! You better have worked those arms and not just your legs for these weight lifting obstacles.",
      "difficulty": 70,
      "flavors": "Sandbags, Other People, Logs",
      "funruns": [
        8,
        11
      ],
      "id": 7,
      "imgs": [
        "/static/img/challengeTempl/carry1.jpg",
        "/static/img/challengeTempl/carry2.jpg",
        "/static/img/challengeTempl/carry3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/carry1.jpg",
      "name": "Carrying an Object",
      "themes": [
        1,
        5,
        6,
        7
      ]
    },
    {
      "description": "Fall and face the consequences. These challenges keep you on your toes across planks, ropes, and anything you can shake a toe at!",
      "difficulty": 70,
      "flavors": "Balance beams, wooden beams, inflated walkways",
      "funruns": [
        0,
        4,
        8,
        11
      ],
      "id": 12,
      "imgs": [
        "/static/img/challengeTempl/balance1.jpg",
        "/static/img/challengeTempl/balance2.jpg",
        "/static/img/challengeTempl/balance3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/balance1.jpg",
      "name": "Staying Balanced",
      "themes": [
        1,
        4,
        5
      ]
    },
    {
      "description": "Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.",
      "difficulty": 60,
      "flavors": "Ice, Inflatable Balls, Mud",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 0,
      "imgs": [
        "/static/img/challengeTempl/oddGround1.jpg",
        "/static/img/challengeTempl/oddGround2.jpg",
        "/static/img/challengeTempl/oddGround3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/oddGround1.jpg",
      "name": "Stepping On Awkward Ground",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Take on extreme temps fearlessly with fun runs in less than ideal temperatures. Will the icy winds or intense heat get to you or will you make it to the finish line and prevail?",
      "difficulty": 80,
      "flavors": "Snow, Ice, Fire, Heat",
      "funruns": [
        1,
        2,
        8,
        10
      ],
      "id": 2,
      "imgs": [
        "/static/img/challengeTempl/extremetemp1.jpg",
        "/static/img/challengeTempl/extremetemp2.jpg",
        "/static/img/challengeTempl/extremetemp3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/extremetemp1.jpg",
      "name": "Enduring Extreme Temperatures",
      "themes": [
        0,
        1
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
      "description": "You don't have to outrun your pursuers, you just have to outrun the other people being chased! Don't let yourself get caught in hardcore survival runs where it's kill... or be killed.",
      "difficulty": 70,
      "flavors": "Pursued, Zombies, Capture The Flag",
      "funruns": [
        4
      ],
      "id": 4,
      "imgs": [
        "/static/img/challengeTempl/chased1.jpg",
        "/static/img/challengeTempl/chased2.jpg",
        "/static/img/challengeTempl/chased3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/chased1.jpg",
      "name": "Getting Chased",
      "themes": [
        1,
        9
      ]
    },
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
    },
    {
      "description": "You thought you were almost there, but not you're blocked by an insurmountable wall! If you want to make it to the end, be ready to climb to the top of the wall or you better be ready to fall!",
      "difficulty": 70,
      "flavors": "Wooden Walls, Rope Walls, Chains, Rope Ladders",
      "funruns": [
        0,
        8
      ],
      "id": 8,
      "imgs": [
        "/static/img/challengeTempl/scaling1.jpg",
        "/static/img/challengeTempl/scaling2.jpg",
        "/static/img/challengeTempl/scaling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/scaling1.jpg",
      "name": "Scaling a Wall",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "These fun slides are a few moments of much-needed thrills. Give your legs a rest and get ready to go fast down these steep declines!",
      "difficulty": 10,
      "flavors": "Large Inflatable Slides, Mud Slides, Foam Slides",
      "funruns": [
        0,
        8
      ],
      "id": 9,
      "imgs": [
        "/static/img/challengeTempl/sliding1.jpg",
        "/static/img/challengeTempl/sliding2.jpg",
        "/static/img/challengeTempl/sliding3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/sliding1.jpg",
      "name": "Sliding Down Slopes",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Don't raise your head - you might just lose it! These challenges force you to get down and dirty, crawling beneath the danger and coming out unscathed.",
      "difficulty": 40,
      "flavors": "Barbed Wire, Tunnels, Electrical Wiring",
      "funruns": [
        4,
        8
      ],
      "id": 10,
      "imgs": [
        "/static/img/challengeTempl/crawling1.jpg",
        "/static/img/challengeTempl/crawling2.jpg",
        "/static/img/challengeTempl/crawling3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/crawling1.jpg",
      "name": "Crawling Underneath Obstacles",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Better have worked that upper body - you'll be needing it now! Whether it's monkey bars, a swing, or just a rope, you'll be flying high or failing.",
      "difficulty": 60,
      "flavors": "Monkey Bars, Rope Swings, Metal Swings",
      "funruns": [
        0,
        8,
        11
      ],
      "id": 11,
      "imgs": [
        "/static/img/challengeTempl/suspended1.jpg",
        "/static/img/challengeTempl/suspended2.jpg",
        "/static/img/challengeTempl/suspended3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/suspended1.jpg",
      "name": "Being Suspended",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "Hope you're sturdy - because you're going to need to face all sorts of projectiles and bulldozing objects! Keep your feet on solid ground, or it might be your head instead!",
      "difficulty": 80,
      "flavors": "Inflated Bulldozer Balls, Thrown Items",
      "funruns": [
        0,
        8
      ],
      "id": 13,
      "imgs": [
        "/static/img/challengeTempl/gettinghit1.jpg",
        "/static/img/challengeTempl/gettinghit2.jpg",
        "/static/img/challengeTempl/gettinghit3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/gettinghit1.jpg",
      "name": "Getting Hit by Objects",
      "themes": [
        1,
        4
      ]
    },
    {
      "description": "This isn't your average trail - these are buildings, roads, and the urban environment for you to run and jump to your heart's content!",
      "difficulty": 60,
      "flavors": "Buildings, Construction Areas, Urban Areas",
      "funruns": [
        4
      ],
      "id": 14,
      "imgs": [
        "/static/img/challengeTempl/parkour1.jpg",
        "/static/img/challengeTempl/parkour2.jpg",
        "/static/img/challengeTempl/parkour3.jpg"
      ],
      "landing_img": "/static/img/landing/challenges/parkour1.jpg",
      "name": "Performing Urban Parkour",
      "themes": [
        1,
        9
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
}
))
    self.assertEqual(response_object, expected) 

	

if __name__ == "__main__" :
    main()