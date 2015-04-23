from io       import StringIO
from unittest import main, TestCase
# import unittest
import urllib.request, codecs, json

server_address = 'http://104.239.139.43:8000'

def http_response_to_json_object (response) :
  reader = codecs.getreader("utf-8")
  return json.load(reader(response))

class TestChallengesSort (TestCase) :

  # Themes filtered by containing funruns with id 0

  def test_filter_funrun (self) :
    url = server_address + '/api/themes?funrun=0'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "themes": [
    {
      "buzzwords": "Training, Hardcore, Cutthroat, Military-Style",
      "challenges": [
        0,
        2,
        3,
        4,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14
      ],
      "description": "More interested in proving how much you can take than how much fun you'll actually have? Intense runs are exactly what you need - a good dose of body-numbing, soul-crushing exercise to show your stuff. See if you can survive the brutal difficulty of these events.",
      "funruns": [
        0,
        4,
        8
      ],
      "id": 1,
      "imgs": [
        "/static/img/themeTempl/intense1.jpg",
        "/static/img/themeTempl/intense2.jpg",
        "/static/img/themeTempl/intense3.jpg",
        "/static/img/themeTempl/intense4.jpg",
        "/static/img/themeTempl/intense5.jpg",
        "/static/img/themeTempl/intense6.jpg",
        "/static/img/themeTempl/intense7.jpg",
        "/static/img/themeTempl/intense8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/intense1.jpg",
      "name": "Intense",
      "short": "Test your endurance in these hardcore races."
    }
  ]
}
))
    self.assertEqual(response_object, expected) 

  # Themes filtered by containing challenges with id 0

  def test_filter_challenge (self) :
    url = server_address + '/api/themes?challenge=0'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "themes": [
    {
      "buzzwords": "Training, Hardcore, Cutthroat, Military-Style",
      "challenges": [
        0,
        2,
        3,
        4,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14
      ],
      "description": "More interested in proving how much you can take than how much fun you'll actually have? Intense runs are exactly what you need - a good dose of body-numbing, soul-crushing exercise to show your stuff. See if you can survive the brutal difficulty of these events.",
      "funruns": [
        0,
        4,
        8
      ],
      "id": 1,
      "imgs": [
        "/static/img/themeTempl/intense1.jpg",
        "/static/img/themeTempl/intense2.jpg",
        "/static/img/themeTempl/intense3.jpg",
        "/static/img/themeTempl/intense4.jpg",
        "/static/img/themeTempl/intense5.jpg",
        "/static/img/themeTempl/intense6.jpg",
        "/static/img/themeTempl/intense7.jpg",
        "/static/img/themeTempl/intense8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/intense1.jpg",
      "name": "Intense",
      "short": "Test your endurance in these hardcore races."
    },
    {
      "buzzwords": "Mud, Color Paint, Wet, Powder, Foam",
      "challenges": [
        0,
        5,
        8,
        9,
        10,
        11,
        12,
        13,
        15
      ],
      "description": "Want to run through mud pits, climb walls, and get blasted with paint? Challenge yourself with get-down-and-dirty runs. You'll be covered with all sorts of stuff all the way to the finish line!",
      "funruns": [
        5,
        6,
        8,
        11
      ],
      "id": 4,
      "imgs": [
        "/static/img/themeTempl/dirty1.jpg",
        "/static/img/themeTempl/dirty2.jpg",
        "/static/img/themeTempl/dirty3.jpg",
        "/static/img/themeTempl/dirty4.jpg",
        "/static/img/themeTempl/dirty5.jpg",
        "/static/img/themeTempl/dirty6.jpg",
        "/static/img/themeTempl/dirty7.jpg",
        "/static/img/themeTempl/dirty8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/dirty1.jpg",
      "name": "Dirty",
      "short": "Get ready to take a long shower after these runs!"
    }
  ]
}
))
    self.assertEqual(response_object, expected) 

  # Themes filtered by containing the buzzword Hardcore

  def test_filter_buzzword (self) :
    url = server_address + '/api/themes?buzzword=Hardcore'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "themes": [
    {
      "buzzwords": "Training, Hardcore, Cutthroat, Military-Style",
      "challenges": [
        0,
        2,
        3,
        4,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14
      ],
      "description": "More interested in proving how much you can take than how much fun you'll actually have? Intense runs are exactly what you need - a good dose of body-numbing, soul-crushing exercise to show your stuff. See if you can survive the brutal difficulty of these events.",
      "funruns": [
        0,
        4,
        8
      ],
      "id": 1,
      "imgs": [
        "/static/img/themeTempl/intense1.jpg",
        "/static/img/themeTempl/intense2.jpg",
        "/static/img/themeTempl/intense3.jpg",
        "/static/img/themeTempl/intense4.jpg",
        "/static/img/themeTempl/intense5.jpg",
        "/static/img/themeTempl/intense6.jpg",
        "/static/img/themeTempl/intense7.jpg",
        "/static/img/themeTempl/intense8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/intense1.jpg",
      "name": "Intense",
      "short": "Test your endurance in these hardcore races."
    }
  ]
}
))
    self.assertEqual(response_object, expected)  

  # Themes filtered by containing funrun with id 1 and funrun with id 10

  def test_filter_two_funruns (self) :
    url = server_address + '/api/themes?funrun=1&funrun=10'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "themes": [
    {
      "buzzwords": "Christmas, Thanksgiving, Easter, Valentine's Day, St. Patrick's Day, New Year's, Halloween, 4th of July",
      "challenges": [
        1,
        2
      ],
      "description": "Instead of sitting around the fire, talking of presents and Santa, why not go for a run with the family? Holiday runs are a great way to get out and celebrate during the festivities! Often featuring thematic competitions and costumes, they're a sure way of making any holiday a memorable one.",
      "funruns": [
        1,
        2
      ],
      "id": 0,
      "imgs": [
        "/static/img/themeTempl/holiday1.jpg",
        "/static/img/themeTempl/holiday2.jpg",
        "/static/img/themeTempl/holiday3.jpg",
        "/static/img/themeTempl/holiday4.jpg",
        "/static/img/themeTempl/holiday5.jpg",
        "/static/img/themeTempl/holiday6.jpg",
        "/static/img/themeTempl/holiday7.jpg",
        "/static/img/themeTempl/holiday8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/holiday1.jpg",
      "name": "Holiday",
      "short": "Celebrate the holidays with a festive run."
    },
    {
      "buzzwords": "Silly, Uncomfortable, Dress-Up, Make-Believe",
      "challenges": [
        1
      ],
      "description": "Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!",
      "funruns": [
        1,
        2,
        3,
        4,
        10
      ],
      "id": 2,
      "imgs": [
        "/static/img/themeTempl/costume1.jpg",
        "/static/img/themeTempl/costume2.jpg",
        "/static/img/themeTempl/costume3.jpg",
        "/static/img/themeTempl/costume4.jpg",
        "/static/img/themeTempl/costume5.jpg",
        "/static/img/themeTempl/costume6.jpg",
        "/static/img/themeTempl/costume7.jpg",
        "/static/img/themeTempl/costume8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/costume1.jpg",
      "name": "Costume",
      "short": "Put on your silliest outfit and get running."
    },
    {
      "buzzwords": "Landmarks, Rivers, Downtown, Parks, Lakes, Views, Monuments",
      "challenges": [
        3
      ],
      "description": "Whether it is an excuse to travel and exercise or just a good distraction from the aches and pains of running, the location of a race is a great factor in deciding which run works for you! Explore famous landmarks as you race to glory!",
      "funruns": [
        1,
        10
      ],
      "id": 3,
      "imgs": [
        "/static/img/themeTempl/location1.jpg",
        "/static/img/themeTempl/location2.jpg",
        "/static/img/themeTempl/location3.jpg",
        "/static/img/themeTempl/location4.jpg",
        "/static/img/themeTempl/location5.jpg",
        "/static/img/themeTempl/location6.jpg",
        "/static/img/themeTempl/location7.jpg",
        "/static/img/themeTempl/location8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/location1.jpg",
      "name": "Location",
      "short": "Enjoy scenic views while getting your exercise on."
    }
  ]
}
))
    self.assertEqual(response_object, expected)  

  # Themes filtered by containing challenge with id 1 and challenge with id 4

  def test_filter_two_challenges (self) :
    url = server_address + '/api/themes?challenge=1&challenge=4'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "themes": [
    {
      "buzzwords": "Christmas, Thanksgiving, Easter, Valentine's Day, St. Patrick's Day, New Year's, Halloween, 4th of July",
      "challenges": [
        1,
        2
      ],
      "description": "Instead of sitting around the fire, talking of presents and Santa, why not go for a run with the family? Holiday runs are a great way to get out and celebrate during the festivities! Often featuring thematic competitions and costumes, they're a sure way of making any holiday a memorable one.",
      "funruns": [
        1,
        2
      ],
      "id": 0,
      "imgs": [
        "/static/img/themeTempl/holiday1.jpg",
        "/static/img/themeTempl/holiday2.jpg",
        "/static/img/themeTempl/holiday3.jpg",
        "/static/img/themeTempl/holiday4.jpg",
        "/static/img/themeTempl/holiday5.jpg",
        "/static/img/themeTempl/holiday6.jpg",
        "/static/img/themeTempl/holiday7.jpg",
        "/static/img/themeTempl/holiday8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/holiday1.jpg",
      "name": "Holiday",
      "short": "Celebrate the holidays with a festive run."
    },
    {
      "buzzwords": "Silly, Uncomfortable, Dress-Up, Make-Believe",
      "challenges": [
        1
      ],
      "description": "Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!",
      "funruns": [
        1,
        2,
        3,
        4,
        10
      ],
      "id": 2,
      "imgs": [
        "/static/img/themeTempl/costume1.jpg",
        "/static/img/themeTempl/costume2.jpg",
        "/static/img/themeTempl/costume3.jpg",
        "/static/img/themeTempl/costume4.jpg",
        "/static/img/themeTempl/costume5.jpg",
        "/static/img/themeTempl/costume6.jpg",
        "/static/img/themeTempl/costume7.jpg",
        "/static/img/themeTempl/costume8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/costume1.jpg",
      "name": "Costume",
      "short": "Put on your silliest outfit and get running."
    },
    {
      "buzzwords": "Rhythm, Dance, Banger",
      "challenges": [
        1,
        5,
        15
      ],
      "description": "No need for a pre-workout for these runs. Let the bass warm you and the melodies move you! You'll be moved by the rhythms and busting to the beats. The music will get you pumped and ready to hit the ground running!",
      "funruns": [
        5,
        6,
        10
      ],
      "id": 8,
      "imgs": [
        "/static/img/themeTempl/music1.jpg",
        "/static/img/themeTempl/music2.jpg",
        "/static/img/themeTempl/music3.jpg",
        "/static/img/themeTempl/music4.jpg",
        "/static/img/themeTempl/music5.jpg",
        "/static/img/themeTempl/music6.jpg",
        "/static/img/themeTempl/music7.jpg",
        "/static/img/themeTempl/music8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/music1.jpg",
      "name": "Music",
      "short": "Let the music move you until the very end."
    },
    {
      "buzzwords": "Dreams, Monsters, Supernatural, Disney",
      "challenges": [
        1,
        4,
        14
      ],
      "description": "Fantasy runs will make your imagination fly wild with their supernatural sights and experiences. See for yourself and get immersed into a run that is out of this world! Live out apocalyptic scenarios, Disney magic, or anything your heart desires!",
      "funruns": [
        4
      ],
      "id": 9,
      "imgs": [
        "/static/img/themeTempl/fantasy1.jpg",
        "/static/img/themeTempl/fantasy2.jpg",
        "/static/img/themeTempl/fantasy3.jpg",
        "/static/img/themeTempl/fantasy4.jpg",
        "/static/img/themeTempl/fantasy5.jpg",
        "/static/img/themeTempl/fantasy6.jpg",
        "/static/img/themeTempl/fantasy7.jpg",
        "/static/img/themeTempl/fantasy8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/fantasy1.jpg",
      "name": "Fantasy",
      "short": "Race through your wildest fantasies - come true."
    }
  ]
}
))
    self.assertEqual(response_object, expected) 

  # Themes filtered by containing buzzword Harcore and buzzword Training

  def test_filter_two_buzzwords (self) :
    url = server_address + '/api/themes?buzzword=Hardcore&buzzword=Training'
    response = urllib.request.urlopen(url)
    response_object = http_response_to_json_object(response)
    expected = json.loads(json.dumps({
  "themes": [
    {
      "buzzwords": "Training, Hardcore, Cutthroat, Military-Style",
      "challenges": [
        0,
        2,
        3,
        4,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14
      ],
      "description": "More interested in proving how much you can take than how much fun you'll actually have? Intense runs are exactly what you need - a good dose of body-numbing, soul-crushing exercise to show your stuff. See if you can survive the brutal difficulty of these events.",
      "funruns": [
        0,
        4,
        8
      ],
      "id": 1,
      "imgs": [
        "/static/img/themeTempl/intense1.jpg",
        "/static/img/themeTempl/intense2.jpg",
        "/static/img/themeTempl/intense3.jpg",
        "/static/img/themeTempl/intense4.jpg",
        "/static/img/themeTempl/intense5.jpg",
        "/static/img/themeTempl/intense6.jpg",
        "/static/img/themeTempl/intense7.jpg",
        "/static/img/themeTempl/intense8.jpg"
      ],
      "landing_img": "/static/img/landing/themes/intense1.jpg",
      "name": "Intense",
      "short": "Test your endurance in these hardcore races."
    }
  ]
}
))
    self.assertEqual(response_object, expected)

  

if __name__ == "__main__" :
    main()