from io       import StringIO
from unittest import main, TestCase
# import unittest
import urllib.request, codecs, json

server_address = 'http://104.239.139.43:8000'

def http_response_to_json_object (response) :
	reader = codecs.getreader("utf-8")
	return json.load(reader(response))

class TestAPI (TestCase) :

	def test_root (self) :
		url = server_address + '/api'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads('{"urls":	{\
									              		"funruns_url": "/funruns",\
									                	"themes_url": "/themes",\
									                	"challenges_url": "/challenges",\
									                	"locations_url": "/locations"\
									            		}\
											}')
		self.assertEqual(response_object, expected)

	def test_root_slash (self) :
		url = server_address + '/api/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads('{"urls":	{\
									              		"funruns_url": "/funruns",\
									                	"themes_url": "/themes",\
									                	"challenges_url": "/challenges",\
									                	"locations_url": "/locations"\
									            		}\
											}')
		self.assertEqual(response_object, expected)

	# Fun Runs Pillar Tests

	def test_get_runs (self) :
		url = server_address + '/api/funruns'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
  "funruns": [
    {
      "address": "Camden Yards\n333 W Camden St.\nBaltimore, MD 21201",
      "challenges": [
        0,
        3,
        5,
        8,
        9,
        11,
        12,
        13
      ],
      "charities": "N/A",
      "city": "Baltimore, Maryland",
      "description": "Crash, smash, and splash your way through a 5k course with larger-than-life obstacles and elements inspired by the hit TV show Wipeout! Take on the infamous Big Balls, Sweeper, Wrecking Balls, and Happy Endings! Hilarious thrills and magnificent spills await!",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/WIPEOUTRUN",
      "hosts": "Ridiculous Obstacle Challenge Race LLC, Endemol USA Inc.",
      "id": 0,
      "imgs": [
        "/static/img/runTempl/wipeout1.jpg",
        "/static/img/runTempl/wipeout2.jpg",
        "/static/img/runTempl/wipeout3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/wipeoutLanding.jpg",
      "loc": 0,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12352.756020060675!2d-76.621608!3d39.283964!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x2428d93f0397c539!2sOriole+Park+at+Camden+Yards!5e0!3m2!1sen!2sus!4v1427230426235",
      "name": "Wipeout Run",
      "price": "March 6th - April 9th: $56\nApril 10th - May 7th: $61\nMay 8th - May 21st: $66\nMay 22nd - June 5th: $71\nJune 6th: $81",
      "quotes": [
        "Seriously, best race I've done. So much fun. Thanks for coming to Dallas! Hope to see you here in the future!",
        "Had a great time participating in the WIPEOUTRUN!",
        "Such a blast! Let's do it again next year!"
      ],
      "short": "Try out the obstacles from the hit TV show \"Wipeout\"!",
      "sponsors": "VaVi Sport & Social",
      "themes": [
        1
      ],
      "video_url": "https://www.youtube.com/embed/1uOII9K5c0c",
      "website": "http://wipeoutrun.com/"
    },
    {
      "address": "Cleveland Public Square\nCleveland, OH 44113",
      "challenges": [
        1,
        2
      ],
      "charities": "A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects",
      "city": "Cleveland, Ohio",
      "description": "The movie producers must have been runners, because the distance between the former Higbee's Department Store and the A Christmas Story House and Museum is about 5K.  Ralphie's dad, The Old Man must have used the 1938 Oldsmobile to track the distance, since there was no GPS in the 1940's.  To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.",
      "distance": "5K, 10K",
      "fb_url": "https://www.facebook.com/AChristmasStoryRun",
      "hosts": "A Christmas Story House & Museum",
      "id": 1,
      "imgs": [
        "/static/img/runTempl/christmasstory1.jpg",
        "/static/img/runTempl/christmasstory2.jpg",
        "/static/img/runTempl/christmasstory3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/christmasStoryRunLanding.jpg",
      "loc": 2,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2988.260792402495!2d-81.694473!3d41.498622999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830f07e4562d241%3A0x94e8396bc5227630!2sRenaissance+Cleveland+Hotel!5e0!3m2!1sen!2sus!4v1427230544965",
      "name": "A Christmas Story Run",
      "price": "Before September 30th: $45\nOctober 1st - December 5th: $55",
      "quotes": [
        "I was so excited to get my finisher medal and enjoy a well deserved Christmas Ale.",
        "Despite the crowds, it was so much fun seeing everyone in costume celebrating the movie and our city.",
        "All in all Pepper gives this fun run an A+!"
      ],
      "short": "Experience the classic movie \"A Christmas Story\" in person.",
      "sponsors": "Ovaltine, Renaissance Hotels, Dannon, Walmart, McDonalds, The Home Depot",
      "themes": [
        0,
        2,
        3
      ],
      "video_url": "https://www.youtube.com/embed/uPiN-_p7q2k",
      "website": "http://achristmasstoryrun.com/"
    },
    {
      "address": "City Hall Plaza\n500 Marilla St.\nDallas, TX 75201",
      "challenges": [
        1,
        2
      ],
      "charities": "The Y Community Programs",
      "city": "Dallas, Texas",
      "description": "The Dallas Turkey Trot really proves that everything's bigger in Texas. One of the largest multi-event races in the country, this trot attracts elite runners and regular ol' birds alike. In fact, in 2011, it set a world record for the largest gathering of people dressed as turkeys.",
      "distance": "5K, 8mi",
      "fb_url": "https://www.facebook.com/DallasYMCATrot",
      "hosts": "YMCA, Capital One Bank",
      "id": 2,
      "imgs": [
        "/static/img/runTempl/dallasturkey1.jpg",
        "/static/img/runTempl/dallasturkey2.jpg",
        "/static/img/runTempl/dallasturkey3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/dallasTurkeyTrotLanding.jpg",
      "loc": 1,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13418.251274220785!2d-96.79709!3d32.777333!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc83854fdfdad6162!2sDallas+City+Hall!5e0!3m2!1sen!2sus!4v1427228610474",
      "name": "Dallas Turkey Trot",
      "price": "Before September 30th: $30\nSeptember 31st - November 25th: $35\nNovember 26th: $45",
      "quotes": [
        "This will be the sixth year my wife and I have run the Dallas Turkey Trot. We began running this race the first year we got married and have kept it a tradition every year. Love this race!",
        "This event is by far the best family friendly event that takes place in Dallas each year!",
        "I had a blast running the Turkey Trot this year. Even though it's my first time doing it, I will definitely make it a tradition every year"
      ],
      "short": "Run in the largest Thanksgiving Day event of its kind.",
      "sponsors": "The Dallas Morning News, Brand Keepers, City of Dallas, Kroger, Nike, The Dallas Cowboys",
      "themes": [
        0,
        2
      ],
      "video_url": "https://www.youtube.com/embed/qdnzjhWgCOg",
      "website": "http://thetrot.org/"
    },
    {
      "address": "Main St & Howard St\nSan Francisco, CA 94105",
      "challenges": [
        1,
        3,
        6
      ],
      "charities": "Mo'MAGIC, United Way of the Bay Area, National Kidney Foundation",
      "city": "San Francisco, California",
      "description": "The Zappos.com Bay to Breakers 12K race runs west through the city and finishes at the Great Highway along the Pacific Coasts Ocean Beach. Participants run up the iconic Hayes Street Hill, along the Panhandle and through Golden Gate Park, while the city of San Francisco cheers them on.",
      "distance": "12K",
      "fb_url": "https://www.facebook.com/zapposbaytobreakers",
      "hosts": "Zappos.com",
      "id": 3,
      "imgs": [
        "/static/img/runTempl/baytobreakers1.jpg",
        "/static/img/runTempl/baytobreakers2.jpg",
        "/static/img/runTempl/baytobreakers3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/baytobreakersLanding.jpg",
      "loc": 6,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3152.984846292559!2d-122.39335585211597!3d37.79039490045594!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064dca37cb7%3A0x3509f87b15b8eae5!2s219+Howard+St%2C+San+Francisco%2C+CA+94105!5e0!3m2!1sen!2sus!4v1428532134914",
      "name": "Bay To Breakers",
      "price": "Adult: $59\nChild: $29.50\nVIP: $139\nGroup/Centipede: $54",
      "quotes": [
        "Bay to Breakers is a direct route to the city's heart and soul.",
        "This 12k seriously looks like a party!",
        "This is an amazing experience that will last forever. It is not only a race, but an incredible party throughout the streets of San Francisco."
      ],
      "short": "Explore SF from the bay to the Ocean Beach breakers.",
      "sponsors": "Under Armour, MapMyRun, Geico, Hyatt Regency, TomTom, Kron4, Kettle Brand, Big 5 Sporting Goods, Hangzhou, Mio",
      "themes": [
        2,
        5
      ],
      "video_url": "https://www.youtube.com/embed/NVEVGSEJmOc",
      "website": "http://zapposbaytobreakers.com/"
    },
    {
      "address": "3186 DPH 4-H Camp\nSound Avenue\nRiverhead, NY 11901",
      "challenges": [
        1,
        4,
        10,
        12,
        14
      ],
      "charities": "Local Charities",
      "city": "Riverhead, New York",
      "description": "Join us at ZOMBIE RACE! A 5k & 15k run infested with zombies. From the moment the humans leave the start line, theyll be running, crawling, and fleeing in horror from the hordes of undead whose only mission is to devour them alive! Don't let the zombies pull your flags!",
      "distance": "5K, 15K",
      "fb_url": "https://www.facebook.com/zombieracellc",
      "hosts": "Great Vision Productions LLC",
      "id": 4,
      "imgs": [
        "/static/img/runTempl/zombierun1.jpg",
        "/static/img/runTempl/zombierun2.jpg",
        "/static/img/runTempl/zombierun3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/zombierunLanding.jpg",
      "loc": 7,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d48208.84256933457!2d-72.7160401!3d40.9584252!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e861d37b7288b9%3A0x67dff709a1d00494!2sNassau+County+4H+Camp!5e0!3m2!1sen!2sus!4v1428532216187",
      "name": "Zombie Run",
      "price": "5K Prices\nBefore February 6th: $55\nFebruary 7th - February 27th: $65\nFebruary 28th - March 27th: $75\nMarch 28th - April 17th: $85\nApril 18th - May 1st: $95\n15K Prices\nBefore February 6th: $75\nFebruary 7th - February 27th: $85\nFebruary 28th - March 27th: $95\nMarch 28th - April 17th: $105\nApril 18th - May 1st: $155\nZombie Price\nBefore February 6th: $20\nFebruary 7th - February 27th: $25\nFebruary 28th - March 27th: $30\nMarch 28th - April 17th: $35\nApril 18th - May 1st: $40",
      "quotes": [
        "They don't like fast food",
        "Run like zombies are chasing you!",
        "This is one of the funnest events I've ever attended!"
      ],
      "short": "Escape the zombies and get to the finish line!",
      "sponsors": "WholeSale Halloween Costumes",
      "themes": [
        1,
        2,
        9
      ],
      "video_url": "https://www.youtube.com/embed/yhrC2CO9gKM",
      "website": "http://www.zombierace.co/index.php"
    },
    {
      "address": "Memphis International Raceway\n5500 Victory Ln\nMillington, TN 38053",
      "challenges": [
        5,
        15
      ],
      "charities": "Children's Hospital",
      "city": "Memphis, Tennessee",
      "description": "Blacklight Run is a unique night 5K fun run focused less on speed and more on UV Neon Glowing fun with friends and family. Glowing participants come from all different ages, shapes, sizes, and speeds; every participant will get Glowed and will have the time of their life!",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/BlacklightRun",
      "hosts": "Blacklight Run Corporate",
      "id": 5,
      "imgs": [
        "/static/img/runTempl/blacklight1.jpg",
        "/static/img/runTempl/blacklight2.jpg",
        "/static/img/runTempl/blacklight3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/blacklightrunLanding.jpg",
      "loc": 8,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3256.9248763636133!2d-89.9476!3d35.282993999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x887f7ec1c0a48aa5%3A0x7ef6ea23d0ad044a!2sMemphis+International+Raceway!5e0!3m2!1sen!2sus!4v1428532262614",
      "name": "Blacklight Run",
      "price": "Standard Registration\nBefore April 8th: $20\nApril 8th - May 9th: $40\nVIP Registration\nBefore April 8th: $45\nApril 8th - May 9th: $75",
      "quotes": [
        "Survived another 5k! Finished the Blacklight Run - I love fun runs because there's less pressure and the obstacles make the race that much more challenging!",
        "I loved tonight's run at Qualcomm stadium in San Diego! California knows how to party! Can't wait to have you guys here again and do it again!",
        "This run leaves runners looking like they fell into a Ghost Buster's movie (minus the slime)."
      ],
      "short": "Get going and get glowing with this neon powder run!",
      "sponsors": "Local Sponsors",
      "themes": [
        4,
        8
      ],
      "video_url": "https://www.youtube.com/embed/TgMgEtXjSUk",
      "website": "http://www.blacklightrun.com/"
    },
    {
      "address": "Washington State Fair Events Center\n110 9th Avenue\nPuyallup, WA 98371",
      "challenges": [
        5,
        15
      ],
      "charities": "Mary Bridge Children's Foundation",
      "city": "Puyallup, Washington",
      "description": "Electric Run is the ultimate nighttime 5k run/walk adventure, where the participants are an integrated part of the show. Featuring immersive \"Lands\" of light and sound that transport the participant into an electric wonderland.",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/electricrun",
      "hosts": "Washington State Fair Events Center",
      "id": 6,
      "imgs": [
        "/static/img/runTempl/electricrun1.jpg",
        "/static/img/runTempl/electricrun2.jpg",
        "/static/img/runTempl/electricrun3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/electricrunLanding.jpg",
      "loc": 9,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d21692.65452180003!2d-122.3073378!3d47.1856237!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5490fc035e7af37d%3A0x5fb822881e1b0c46!2sWashington+State+Fair!5e0!3m2!1sen!2sus!4v1428532299643",
      "name": "Electric Run",
      "price": "Before April 15th: $45\nApril 16th - May 1st: $50",
      "quotes": [
        "You've GOT to bring The Electric Run back to ATLANTA!",
        "I loved the event last year!",
        "It was a blast! Can't wait for this year!"
      ],
      "short": "Become part of the electric run in this nighttime adventure.",
      "sponsors": "WholeSale Halloween Costumes",
      "themes": [
        4,
        8
      ],
      "video_url": "https://www.youtube.com/embed/R0uhmZI1yy4",
      "website": "http://electricrun.com/seatac"
    },
    {
      "address": "Fair Park Dallas\n1300 Robert B Cullum Boulevard\nDallas, TX 78210",
      "challenges": [
        6
      ],
      "charities": "Local Breweries, Local Food, Local Music",
      "city": "Dallas, Texas",
      "description": "The Brew Mile is your chance to combine your love of running with the finest beverage on the face of this good green earth  BEER. Finally an event that tests your liver as much as it tests your lungs, and is followed by one of the best parties of the year!",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/brewmileseries",
      "hosts": "Blacklight Run Corporate",
      "id": 7,
      "imgs": [
        "/static/img/runTempl/brewmile1.jpg",
        "/static/img/runTempl/brewmile2.jpg",
        "/static/img/runTempl/brewmile3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/brewrunLanding.jpg",
      "loc": 1,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3354.4074902321736!2d-96.76173600000001!3d32.781453!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x864e9897a14862d7%3A0x64277dc82ee9144!2sFair+Park!5e0!3m2!1sen!2sus!4v1428532340130",
      "name": "Brew Mile",
      "price": "February 1st - March 12th: $55\nMarch 13th - April 9th: $65\nApril 10th - April 30th: $75\nMay 1st: $80",
      "quotes": [
        "Super excited for us to do this run.",
        "Drinking a beer after a run is freaking awesome.",
        "I HAVE NEVER BEEN SO EXCITED TO RUN A MILE."
      ],
      "short": "Take on a mile while chugging beer!",
      "sponsors": "Upslope Brewing Co, TwinPeaks Brewing Co, Nine Band Brewing Co, Pedernales Brewing Co, Saint Arnold Brewing Co",
      "themes": [
        6
      ],
      "video_url": "https://www.youtube.com/embed/cXrafhIBdlI",
      "website": "http://brewmile.com/"
    },
    {
      "address": "Bouckaert Farm\n10045 Cedar Grove\nFairburn, GA 30213",
      "challenges": [
        0,
        2,
        3,
        5,
        7,
        8,
        9,
        10,
        11,
        12,
        13
      ],
      "charities": "Wounded Warrior Project, U.S. Army",
      "city": "Fairburn, Georgia",
      "description": "Tough Mudder is a team-oriented obstacle course designed to test physical strength and mental grit. It puts camaraderie over finisher rankings and is not a timed race but a team challenge that allows participants to experience exhilarating, yet safe, world-class obstacles they won't find anywhere else",
      "distance": "19K",
      "fb_url": "https://www.facebook.com/toughmudder",
      "hosts": "Tough Mudder",
      "id": 8,
      "imgs": [
        "/static/img/runTempl/toughmudder1.jpg",
        "/static/img/runTempl/toughmudder2.jpg",
        "/static/img/runTempl/toughmudder3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/toughmudderLanding.jpg",
      "loc": 3,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3322.038929257956!2d-84.7159338!3d33.6302326!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f4d91a281b01bf%3A0x5e4b7c6398a7c91e!2s10045+Cedar+Grove+Rd%2C+Fairburn%2C+GA+30213!5e0!3m2!1sen!2sus!4v1428532369676",
      "name": "Tough Mudder",
      "price": "Before May 2nd: $185\nMay 2nd: $185",
      "quotes": [
        "The teamwork and camaraderie out there was amazing.",
        "The idea of Tough Mudder is not to win... but to have a story to tell.",
        "Tough Mudder is a culture and community of taking on challenges and supporting each other."
      ],
      "short": "Get through 12 miles of military-style obstacles!",
      "sponsors": "Toyo Tires, Cellucor, Shock-Top, MET-Rx, Oberto, Radisson, Wheaties, Under Armour",
      "themes": [
        1,
        4,
        5
      ],
      "video_url": "https://www.youtube.com/embed/Jim-ksScOoc",
      "website": "https://toughmudder.com/"
    },
    {
      "address": "Browning Hangar\n4550 Mueller Blvd.\nAustin, TX 78723",
      "challenges": [
        6
      ],
      "charities": "Make A Film Foundation, American Diabetes Association",
      "city": "Austin, Texas",
      "description": "Cooking Light & Health's The Fit Foodie 5K Race is the ultimate celebration of food, fitness, and fun. Put those running shoes to work as you navigate your way around a beautiful 5K course.",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/pages/The-Fit-Foodie-Race-Series/177814812394419",
      "hosts": "Cooking Light & Health",
      "id": 9,
      "imgs": [
        "/static/img/runTempl/fitfoodie1.jpg",
        "/static/img/runTempl/fitfoodie2.jpg",
        "/static/img/runTempl/fitfoodie3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/fitfoodieLanding.jpg",
      "loc": 4,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3444.8924904757855!2d-97.7073052!3d30.297122100000003!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b5f84578082f%3A0x42afd5562f2f2df1!2s4550+Mueller+Blvd%2C+Austin%2C+TX+78723!5e0!3m2!1sen!2sus!4v1428532415527",
      "name": "Fit Foodie 5K",
      "price": "Before June 13th: $55\nJune 13th: $60",
      "quotes": [
        "The race was great, but the festivities after were even greater!",
        "It's more than a race, it is a fitness and culinary experience.",
        "Where delicious meets fitness."
      ],
      "short": "Cruise to the finish and food away!",
      "sponsors": "Cooking Light, Health, Aveeno, Hawaiian Host, Fabletics, Rove, Sartori, Tom's, Mueller, Fast Forward Ventures",
      "themes": [
        7
      ],
      "video_url": "https://www.youtube.com/embed/cVG9FATjIyk",
      "website": "http://fitfoodierun.com/"
    },
    {
      "address": "The Long Center Grounds\n701 W Riverside Dr.\nAustin, TX 78704",
      "challenges": [
        1,
        2
      ],
      "charities": "Capital Area Food Bank of Texas",
      "city": "Austin, Texas",
      "description": "Slip into your weirdest costume, slap on your favorite light up running shoes and throw your timer into Lady Bird Lake! This is the slowest 5K on the planet - the wildest, weirdest and most memorable!",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/pages/Keep-Austin-Weird-Festival-5K/121126484577639",
      "hosts": "The Long Center",
      "id": 10,
      "imgs": [
        "/static/img/runTempl/keepAustinWeird1.jpg",
        "/static/img/runTempl/keepAustinWeird2.jpg",
        "/static/img/runTempl/keepAustinWeird3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/keepAustinWeirdLanding.jpg",
      "loc": 4,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3446.1964982159493!2d-97.751079!3d30.259982!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b504ea2084d7%3A0xa8a514235a56453e!2s701+W+Riverside+Dr%2C+Austin%2C+TX+78704!5e0!3m2!1sen!2sus!4v1428532467708",
      "name": "Keep Austin Weird 5K",
      "price": "VIP: $75\nAdults: $22.50\nKids: $12",
      "quotes": [
        "So much fun! Drove down from Oklahoma City to attend!",
        "So well done! Loads of fun!",
        "It was our first time attending the fest and we had a blast! I will be back next year for sure!"
      ],
      "short": "Make Austin weird in the slowest race ever!",
      "sponsors": "HotSchedules, AT&T U-verse, Amy's Ice Cream, Babyearth, Beatbox Beverages",
      "themes": [
        2,
        3,
        8
      ],
      "video_url": "https://www.youtube.com/embed/9sL-B1D7v34",
      "website": "http://keepaustinweirdfest.com/festival/"
    },
    {
      "address": "Sunday River Ski Resort\n15 S Ridge Rd.\nNewry, ME 04261",
      "challenges": [
        0,
        3,
        5,
        7,
        11,
        12
      ],
      "charities": "N/A",
      "city": "Newry, Maine",
      "description": "Carry your wife to the finish and win her weight in beer! The course at Sunday River is built to international specifications at 278 yards in length, with two dry obstacles and one water obstacle.",
      "distance": "278yd",
      "fb_url": "https://www.facebook.com/sundayriver",
      "hosts": "Sunday River",
      "id": 11,
      "imgs": [
        "/static/img/runTempl/wifecarry1.jpg",
        "/static/img/runTempl/wifecarry2.jpg",
        "/static/img/runTempl/wifecarry3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/wifecarryLanding.jpg",
      "loc": 5,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2847.0332106871697!2d-70.856894!3d44.473492!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cb3dd81009e321b%3A0xd2eb7c1aecb4af6e!2sSunday+River+Ski+Resort!5e0!3m2!1sen!2sus!4v1428532505050",
      "name": "North American Wife Carrying Championship",
      "price": "N/A",
      "quotes": [
        "It was a very cool event! Sunday River does a good job with it!",
        "I'm wicked strong and she's wicked small!",
        "Hardly fair playing field but fun to watch none the less."
      ],
      "short": "Carry your wife and win her weight in beer!",
      "sponsors": "BudLight, Bethel Inn Resort",
      "themes": [
        4,
        5
      ],
      "video_url": "https://player.vimeo.com/video/112507533",
      "website": "http://www.sundayriver.com/events-and-activities/events-calendar/north-american-wife-carrying-championship"
    }
  ]
}
									))
		self.assertEqual(response_object, expected)

	def test_get_runs_slash (self) :
		url = server_address + '/api/funruns/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
  "funruns": [
    {
      "address": "Camden Yards\n333 W Camden St.\nBaltimore, MD 21201",
      "challenges": [
        0,
        3,
        5,
        8,
        9,
        11,
        12,
        13
      ],
      "charities": "N/A",
      "city": "Baltimore, Maryland",
      "description": "Crash, smash, and splash your way through a 5k course with larger-than-life obstacles and elements inspired by the hit TV show Wipeout! Take on the infamous Big Balls, Sweeper, Wrecking Balls, and Happy Endings! Hilarious thrills and magnificent spills await!",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/WIPEOUTRUN",
      "hosts": "Ridiculous Obstacle Challenge Race LLC, Endemol USA Inc.",
      "id": 0,
      "imgs": [
        "/static/img/runTempl/wipeout1.jpg",
        "/static/img/runTempl/wipeout2.jpg",
        "/static/img/runTempl/wipeout3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/wipeoutLanding.jpg",
      "loc": 0,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12352.756020060675!2d-76.621608!3d39.283964!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x2428d93f0397c539!2sOriole+Park+at+Camden+Yards!5e0!3m2!1sen!2sus!4v1427230426235",
      "name": "Wipeout Run",
      "price": "March 6th - April 9th: $56\nApril 10th - May 7th: $61\nMay 8th - May 21st: $66\nMay 22nd - June 5th: $71\nJune 6th: $81",
      "quotes": [
        "Seriously, best race I've done. So much fun. Thanks for coming to Dallas! Hope to see you here in the future!",
        "Had a great time participating in the WIPEOUTRUN!",
        "Such a blast! Let's do it again next year!"
      ],
      "short": "Try out the obstacles from the hit TV show \"Wipeout\"!",
      "sponsors": "VaVi Sport & Social",
      "themes": [
        1
      ],
      "video_url": "https://www.youtube.com/embed/1uOII9K5c0c",
      "website": "http://wipeoutrun.com/"
    },
    {
      "address": "Cleveland Public Square\nCleveland, OH 44113",
      "challenges": [
        1,
        2
      ],
      "charities": "A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects",
      "city": "Cleveland, Ohio",
      "description": "The movie producers must have been runners, because the distance between the former Higbee's Department Store and the A Christmas Story House and Museum is about 5K.  Ralphie's dad, The Old Man must have used the 1938 Oldsmobile to track the distance, since there was no GPS in the 1940's.  To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.",
      "distance": "5K, 10K",
      "fb_url": "https://www.facebook.com/AChristmasStoryRun",
      "hosts": "A Christmas Story House & Museum",
      "id": 1,
      "imgs": [
        "/static/img/runTempl/christmasstory1.jpg",
        "/static/img/runTempl/christmasstory2.jpg",
        "/static/img/runTempl/christmasstory3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/christmasStoryRunLanding.jpg",
      "loc": 2,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2988.260792402495!2d-81.694473!3d41.498622999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830f07e4562d241%3A0x94e8396bc5227630!2sRenaissance+Cleveland+Hotel!5e0!3m2!1sen!2sus!4v1427230544965",
      "name": "A Christmas Story Run",
      "price": "Before September 30th: $45\nOctober 1st - December 5th: $55",
      "quotes": [
        "I was so excited to get my finisher medal and enjoy a well deserved Christmas Ale.",
        "Despite the crowds, it was so much fun seeing everyone in costume celebrating the movie and our city.",
        "All in all Pepper gives this fun run an A+!"
      ],
      "short": "Experience the classic movie \"A Christmas Story\" in person.",
      "sponsors": "Ovaltine, Renaissance Hotels, Dannon, Walmart, McDonalds, The Home Depot",
      "themes": [
        0,
        2,
        3
      ],
      "video_url": "https://www.youtube.com/embed/uPiN-_p7q2k",
      "website": "http://achristmasstoryrun.com/"
    },
    {
      "address": "City Hall Plaza\n500 Marilla St.\nDallas, TX 75201",
      "challenges": [
        1,
        2
      ],
      "charities": "The Y Community Programs",
      "city": "Dallas, Texas",
      "description": "The Dallas Turkey Trot really proves that everything's bigger in Texas. One of the largest multi-event races in the country, this trot attracts elite runners and regular ol' birds alike. In fact, in 2011, it set a world record for the largest gathering of people dressed as turkeys.",
      "distance": "5K, 8mi",
      "fb_url": "https://www.facebook.com/DallasYMCATrot",
      "hosts": "YMCA, Capital One Bank",
      "id": 2,
      "imgs": [
        "/static/img/runTempl/dallasturkey1.jpg",
        "/static/img/runTempl/dallasturkey2.jpg",
        "/static/img/runTempl/dallasturkey3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/dallasTurkeyTrotLanding.jpg",
      "loc": 1,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13418.251274220785!2d-96.79709!3d32.777333!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc83854fdfdad6162!2sDallas+City+Hall!5e0!3m2!1sen!2sus!4v1427228610474",
      "name": "Dallas Turkey Trot",
      "price": "Before September 30th: $30\nSeptember 31st - November 25th: $35\nNovember 26th: $45",
      "quotes": [
        "This will be the sixth year my wife and I have run the Dallas Turkey Trot. We began running this race the first year we got married and have kept it a tradition every year. Love this race!",
        "This event is by far the best family friendly event that takes place in Dallas each year!",
        "I had a blast running the Turkey Trot this year. Even though it's my first time doing it, I will definitely make it a tradition every year"
      ],
      "short": "Run in the largest Thanksgiving Day event of its kind.",
      "sponsors": "The Dallas Morning News, Brand Keepers, City of Dallas, Kroger, Nike, The Dallas Cowboys",
      "themes": [
        0,
        2
      ],
      "video_url": "https://www.youtube.com/embed/qdnzjhWgCOg",
      "website": "http://thetrot.org/"
    },
    {
      "address": "Main St & Howard St\nSan Francisco, CA 94105",
      "challenges": [
        1,
        3,
        6
      ],
      "charities": "Mo'MAGIC, United Way of the Bay Area, National Kidney Foundation",
      "city": "San Francisco, California",
      "description": "The Zappos.com Bay to Breakers 12K race runs west through the city and finishes at the Great Highway along the Pacific Coasts Ocean Beach. Participants run up the iconic Hayes Street Hill, along the Panhandle and through Golden Gate Park, while the city of San Francisco cheers them on.",
      "distance": "12K",
      "fb_url": "https://www.facebook.com/zapposbaytobreakers",
      "hosts": "Zappos.com",
      "id": 3,
      "imgs": [
        "/static/img/runTempl/baytobreakers1.jpg",
        "/static/img/runTempl/baytobreakers2.jpg",
        "/static/img/runTempl/baytobreakers3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/baytobreakersLanding.jpg",
      "loc": 6,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3152.984846292559!2d-122.39335585211597!3d37.79039490045594!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064dca37cb7%3A0x3509f87b15b8eae5!2s219+Howard+St%2C+San+Francisco%2C+CA+94105!5e0!3m2!1sen!2sus!4v1428532134914",
      "name": "Bay To Breakers",
      "price": "Adult: $59\nChild: $29.50\nVIP: $139\nGroup/Centipede: $54",
      "quotes": [
        "Bay to Breakers is a direct route to the city's heart and soul.",
        "This 12k seriously looks like a party!",
        "This is an amazing experience that will last forever. It is not only a race, but an incredible party throughout the streets of San Francisco."
      ],
      "short": "Explore SF from the bay to the Ocean Beach breakers.",
      "sponsors": "Under Armour, MapMyRun, Geico, Hyatt Regency, TomTom, Kron4, Kettle Brand, Big 5 Sporting Goods, Hangzhou, Mio",
      "themes": [
        2,
        5
      ],
      "video_url": "https://www.youtube.com/embed/NVEVGSEJmOc",
      "website": "http://zapposbaytobreakers.com/"
    },
    {
      "address": "3186 DPH 4-H Camp\nSound Avenue\nRiverhead, NY 11901",
      "challenges": [
        1,
        4,
        10,
        12,
        14
      ],
      "charities": "Local Charities",
      "city": "Riverhead, New York",
      "description": "Join us at ZOMBIE RACE! A 5k & 15k run infested with zombies. From the moment the humans leave the start line, theyll be running, crawling, and fleeing in horror from the hordes of undead whose only mission is to devour them alive! Don't let the zombies pull your flags!",
      "distance": "5K, 15K",
      "fb_url": "https://www.facebook.com/zombieracellc",
      "hosts": "Great Vision Productions LLC",
      "id": 4,
      "imgs": [
        "/static/img/runTempl/zombierun1.jpg",
        "/static/img/runTempl/zombierun2.jpg",
        "/static/img/runTempl/zombierun3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/zombierunLanding.jpg",
      "loc": 7,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d48208.84256933457!2d-72.7160401!3d40.9584252!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e861d37b7288b9%3A0x67dff709a1d00494!2sNassau+County+4H+Camp!5e0!3m2!1sen!2sus!4v1428532216187",
      "name": "Zombie Run",
      "price": "5K Prices\nBefore February 6th: $55\nFebruary 7th - February 27th: $65\nFebruary 28th - March 27th: $75\nMarch 28th - April 17th: $85\nApril 18th - May 1st: $95\n15K Prices\nBefore February 6th: $75\nFebruary 7th - February 27th: $85\nFebruary 28th - March 27th: $95\nMarch 28th - April 17th: $105\nApril 18th - May 1st: $155\nZombie Price\nBefore February 6th: $20\nFebruary 7th - February 27th: $25\nFebruary 28th - March 27th: $30\nMarch 28th - April 17th: $35\nApril 18th - May 1st: $40",
      "quotes": [
        "They don't like fast food",
        "Run like zombies are chasing you!",
        "This is one of the funnest events I've ever attended!"
      ],
      "short": "Escape the zombies and get to the finish line!",
      "sponsors": "WholeSale Halloween Costumes",
      "themes": [
        1,
        2,
        9
      ],
      "video_url": "https://www.youtube.com/embed/yhrC2CO9gKM",
      "website": "http://www.zombierace.co/index.php"
    },
    {
      "address": "Memphis International Raceway\n5500 Victory Ln\nMillington, TN 38053",
      "challenges": [
        5,
        15
      ],
      "charities": "Children's Hospital",
      "city": "Memphis, Tennessee",
      "description": "Blacklight Run is a unique night 5K fun run focused less on speed and more on UV Neon Glowing fun with friends and family. Glowing participants come from all different ages, shapes, sizes, and speeds; every participant will get Glowed and will have the time of their life!",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/BlacklightRun",
      "hosts": "Blacklight Run Corporate",
      "id": 5,
      "imgs": [
        "/static/img/runTempl/blacklight1.jpg",
        "/static/img/runTempl/blacklight2.jpg",
        "/static/img/runTempl/blacklight3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/blacklightrunLanding.jpg",
      "loc": 8,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3256.9248763636133!2d-89.9476!3d35.282993999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x887f7ec1c0a48aa5%3A0x7ef6ea23d0ad044a!2sMemphis+International+Raceway!5e0!3m2!1sen!2sus!4v1428532262614",
      "name": "Blacklight Run",
      "price": "Standard Registration\nBefore April 8th: $20\nApril 8th - May 9th: $40\nVIP Registration\nBefore April 8th: $45\nApril 8th - May 9th: $75",
      "quotes": [
        "Survived another 5k! Finished the Blacklight Run - I love fun runs because there's less pressure and the obstacles make the race that much more challenging!",
        "I loved tonight's run at Qualcomm stadium in San Diego! California knows how to party! Can't wait to have you guys here again and do it again!",
        "This run leaves runners looking like they fell into a Ghost Buster's movie (minus the slime)."
      ],
      "short": "Get going and get glowing with this neon powder run!",
      "sponsors": "Local Sponsors",
      "themes": [
        4,
        8
      ],
      "video_url": "https://www.youtube.com/embed/TgMgEtXjSUk",
      "website": "http://www.blacklightrun.com/"
    },
    {
      "address": "Washington State Fair Events Center\n110 9th Avenue\nPuyallup, WA 98371",
      "challenges": [
        5,
        15
      ],
      "charities": "Mary Bridge Children's Foundation",
      "city": "Puyallup, Washington",
      "description": "Electric Run is the ultimate nighttime 5k run/walk adventure, where the participants are an integrated part of the show. Featuring immersive \"Lands\" of light and sound that transport the participant into an electric wonderland.",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/electricrun",
      "hosts": "Washington State Fair Events Center",
      "id": 6,
      "imgs": [
        "/static/img/runTempl/electricrun1.jpg",
        "/static/img/runTempl/electricrun2.jpg",
        "/static/img/runTempl/electricrun3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/electricrunLanding.jpg",
      "loc": 9,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d21692.65452180003!2d-122.3073378!3d47.1856237!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5490fc035e7af37d%3A0x5fb822881e1b0c46!2sWashington+State+Fair!5e0!3m2!1sen!2sus!4v1428532299643",
      "name": "Electric Run",
      "price": "Before April 15th: $45\nApril 16th - May 1st: $50",
      "quotes": [
        "You've GOT to bring The Electric Run back to ATLANTA!",
        "I loved the event last year!",
        "It was a blast! Can't wait for this year!"
      ],
      "short": "Become part of the electric run in this nighttime adventure.",
      "sponsors": "WholeSale Halloween Costumes",
      "themes": [
        4,
        8
      ],
      "video_url": "https://www.youtube.com/embed/R0uhmZI1yy4",
      "website": "http://electricrun.com/seatac"
    },
    {
      "address": "Fair Park Dallas\n1300 Robert B Cullum Boulevard\nDallas, TX 78210",
      "challenges": [
        6
      ],
      "charities": "Local Breweries, Local Food, Local Music",
      "city": "Dallas, Texas",
      "description": "The Brew Mile is your chance to combine your love of running with the finest beverage on the face of this good green earth  BEER. Finally an event that tests your liver as much as it tests your lungs, and is followed by one of the best parties of the year!",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/brewmileseries",
      "hosts": "Blacklight Run Corporate",
      "id": 7,
      "imgs": [
        "/static/img/runTempl/brewmile1.jpg",
        "/static/img/runTempl/brewmile2.jpg",
        "/static/img/runTempl/brewmile3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/brewrunLanding.jpg",
      "loc": 1,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3354.4074902321736!2d-96.76173600000001!3d32.781453!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x864e9897a14862d7%3A0x64277dc82ee9144!2sFair+Park!5e0!3m2!1sen!2sus!4v1428532340130",
      "name": "Brew Mile",
      "price": "February 1st - March 12th: $55\nMarch 13th - April 9th: $65\nApril 10th - April 30th: $75\nMay 1st: $80",
      "quotes": [
        "Super excited for us to do this run.",
        "Drinking a beer after a run is freaking awesome.",
        "I HAVE NEVER BEEN SO EXCITED TO RUN A MILE."
      ],
      "short": "Take on a mile while chugging beer!",
      "sponsors": "Upslope Brewing Co, TwinPeaks Brewing Co, Nine Band Brewing Co, Pedernales Brewing Co, Saint Arnold Brewing Co",
      "themes": [
        6
      ],
      "video_url": "https://www.youtube.com/embed/cXrafhIBdlI",
      "website": "http://brewmile.com/"
    },
    {
      "address": "Bouckaert Farm\n10045 Cedar Grove\nFairburn, GA 30213",
      "challenges": [
        0,
        2,
        3,
        5,
        7,
        8,
        9,
        10,
        11,
        12,
        13
      ],
      "charities": "Wounded Warrior Project, U.S. Army",
      "city": "Fairburn, Georgia",
      "description": "Tough Mudder is a team-oriented obstacle course designed to test physical strength and mental grit. It puts camaraderie over finisher rankings and is not a timed race but a team challenge that allows participants to experience exhilarating, yet safe, world-class obstacles they won't find anywhere else",
      "distance": "19K",
      "fb_url": "https://www.facebook.com/toughmudder",
      "hosts": "Tough Mudder",
      "id": 8,
      "imgs": [
        "/static/img/runTempl/toughmudder1.jpg",
        "/static/img/runTempl/toughmudder2.jpg",
        "/static/img/runTempl/toughmudder3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/toughmudderLanding.jpg",
      "loc": 3,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3322.038929257956!2d-84.7159338!3d33.6302326!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f4d91a281b01bf%3A0x5e4b7c6398a7c91e!2s10045+Cedar+Grove+Rd%2C+Fairburn%2C+GA+30213!5e0!3m2!1sen!2sus!4v1428532369676",
      "name": "Tough Mudder",
      "price": "Before May 2nd: $185\nMay 2nd: $185",
      "quotes": [
        "The teamwork and camaraderie out there was amazing.",
        "The idea of Tough Mudder is not to win... but to have a story to tell.",
        "Tough Mudder is a culture and community of taking on challenges and supporting each other."
      ],
      "short": "Get through 12 miles of military-style obstacles!",
      "sponsors": "Toyo Tires, Cellucor, Shock-Top, MET-Rx, Oberto, Radisson, Wheaties, Under Armour",
      "themes": [
        1,
        4,
        5
      ],
      "video_url": "https://www.youtube.com/embed/Jim-ksScOoc",
      "website": "https://toughmudder.com/"
    },
    {
      "address": "Browning Hangar\n4550 Mueller Blvd.\nAustin, TX 78723",
      "challenges": [
        6
      ],
      "charities": "Make A Film Foundation, American Diabetes Association",
      "city": "Austin, Texas",
      "description": "Cooking Light & Health's The Fit Foodie 5K Race is the ultimate celebration of food, fitness, and fun. Put those running shoes to work as you navigate your way around a beautiful 5K course.",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/pages/The-Fit-Foodie-Race-Series/177814812394419",
      "hosts": "Cooking Light & Health",
      "id": 9,
      "imgs": [
        "/static/img/runTempl/fitfoodie1.jpg",
        "/static/img/runTempl/fitfoodie2.jpg",
        "/static/img/runTempl/fitfoodie3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/fitfoodieLanding.jpg",
      "loc": 4,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3444.8924904757855!2d-97.7073052!3d30.297122100000003!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b5f84578082f%3A0x42afd5562f2f2df1!2s4550+Mueller+Blvd%2C+Austin%2C+TX+78723!5e0!3m2!1sen!2sus!4v1428532415527",
      "name": "Fit Foodie 5K",
      "price": "Before June 13th: $55\nJune 13th: $60",
      "quotes": [
        "The race was great, but the festivities after were even greater!",
        "It's more than a race, it is a fitness and culinary experience.",
        "Where delicious meets fitness."
      ],
      "short": "Cruise to the finish and food away!",
      "sponsors": "Cooking Light, Health, Aveeno, Hawaiian Host, Fabletics, Rove, Sartori, Tom's, Mueller, Fast Forward Ventures",
      "themes": [
        7
      ],
      "video_url": "https://www.youtube.com/embed/cVG9FATjIyk",
      "website": "http://fitfoodierun.com/"
    },
    {
      "address": "The Long Center Grounds\n701 W Riverside Dr.\nAustin, TX 78704",
      "challenges": [
        1,
        2
      ],
      "charities": "Capital Area Food Bank of Texas",
      "city": "Austin, Texas",
      "description": "Slip into your weirdest costume, slap on your favorite light up running shoes and throw your timer into Lady Bird Lake! This is the slowest 5K on the planet - the wildest, weirdest and most memorable!",
      "distance": "5K",
      "fb_url": "https://www.facebook.com/pages/Keep-Austin-Weird-Festival-5K/121126484577639",
      "hosts": "The Long Center",
      "id": 10,
      "imgs": [
        "/static/img/runTempl/keepAustinWeird1.jpg",
        "/static/img/runTempl/keepAustinWeird2.jpg",
        "/static/img/runTempl/keepAustinWeird3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/keepAustinWeirdLanding.jpg",
      "loc": 4,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3446.1964982159493!2d-97.751079!3d30.259982!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b504ea2084d7%3A0xa8a514235a56453e!2s701+W+Riverside+Dr%2C+Austin%2C+TX+78704!5e0!3m2!1sen!2sus!4v1428532467708",
      "name": "Keep Austin Weird 5K",
      "price": "VIP: $75\nAdults: $22.50\nKids: $12",
      "quotes": [
        "So much fun! Drove down from Oklahoma City to attend!",
        "So well done! Loads of fun!",
        "It was our first time attending the fest and we had a blast! I will be back next year for sure!"
      ],
      "short": "Make Austin weird in the slowest race ever!",
      "sponsors": "HotSchedules, AT&T U-verse, Amy's Ice Cream, Babyearth, Beatbox Beverages",
      "themes": [
        2,
        3,
        8
      ],
      "video_url": "https://www.youtube.com/embed/9sL-B1D7v34",
      "website": "http://keepaustinweirdfest.com/festival/"
    },
    {
      "address": "Sunday River Ski Resort\n15 S Ridge Rd.\nNewry, ME 04261",
      "challenges": [
        0,
        3,
        5,
        7,
        11,
        12
      ],
      "charities": "N/A",
      "city": "Newry, Maine",
      "description": "Carry your wife to the finish and win her weight in beer! The course at Sunday River is built to international specifications at 278 yards in length, with two dry obstacles and one water obstacle.",
      "distance": "278yd",
      "fb_url": "https://www.facebook.com/sundayriver",
      "hosts": "Sunday River",
      "id": 11,
      "imgs": [
        "/static/img/runTempl/wifecarry1.jpg",
        "/static/img/runTempl/wifecarry2.jpg",
        "/static/img/runTempl/wifecarry3.jpg"
      ],
      "landing_img": "/static/img/landing/funruns/wifecarryLanding.jpg",
      "loc": 5,
      "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2847.0332106871697!2d-70.856894!3d44.473492!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cb3dd81009e321b%3A0xd2eb7c1aecb4af6e!2sSunday+River+Ski+Resort!5e0!3m2!1sen!2sus!4v1428532505050",
      "name": "North American Wife Carrying Championship",
      "price": "N/A",
      "quotes": [
        "It was a very cool event! Sunday River does a good job with it!",
        "I'm wicked strong and she's wicked small!",
        "Hardly fair playing field but fun to watch none the less."
      ],
      "short": "Carry your wife and win her weight in beer!",
      "sponsors": "BudLight, Bethel Inn Resort",
      "themes": [
        4,
        5
      ],
      "video_url": "https://player.vimeo.com/video/112507533",
      "website": "http://www.sundayriver.com/events-and-activities/events-calendar/north-american-wife-carrying-championship"
    }
  ]
}
									))
		self.assertEqual(response_object, expected)


	def test_get_run_by_id_0 (self) :
		url = server_address + '/api/funruns/0'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
  "funruns": {
    "address": "Camden Yards\n333 W Camden St.\nBaltimore, MD 21201",
    "challenges": [
      0,
      3,
      5,
      8,
      9,
      11,
      12,
      13
    ],
    "charities": "N/A",
    "city": "Baltimore, Maryland",
    "description": "Crash, smash, and splash your way through a 5k course with larger-than-life obstacles and elements inspired by the hit TV show Wipeout! Take on the infamous Big Balls, Sweeper, Wrecking Balls, and Happy Endings! Hilarious thrills and magnificent spills await!",
    "distance": "5K",
    "fb_url": "https://www.facebook.com/WIPEOUTRUN",
    "hosts": "Ridiculous Obstacle Challenge Race LLC, Endemol USA Inc.",
    "id": 0,
    "imgs": [
      "/static/img/runTempl/wipeout1.jpg",
      "/static/img/runTempl/wipeout2.jpg",
      "/static/img/runTempl/wipeout3.jpg"
    ],
    "landing_img": "/static/img/landing/funruns/wipeoutLanding.jpg",
    "loc": 0,
    "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12352.756020060675!2d-76.621608!3d39.283964!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x2428d93f0397c539!2sOriole+Park+at+Camden+Yards!5e0!3m2!1sen!2sus!4v1427230426235",
    "name": "Wipeout Run",
    "price": "March 6th - April 9th: $56\nApril 10th - May 7th: $61\nMay 8th - May 21st: $66\nMay 22nd - June 5th: $71\nJune 6th: $81",
    "quotes": [
      "Seriously, best race I've done. So much fun. Thanks for coming to Dallas! Hope to see you here in the future!",
      "Had a great time participating in the WIPEOUTRUN!",
      "Such a blast! Let's do it again next year!"
    ],
    "short": "Try out the obstacles from the hit TV show \"Wipeout\"!",
    "sponsors": "VaVi Sport & Social",
    "themes": [
      1
    ],
    "video_url": "https://www.youtube.com/embed/1uOII9K5c0c",
    "website": "http://wipeoutrun.com/"
  }
}))
		self.assertEqual(response_object, expected)

	def test_get_run_by_id_0_slash (self) :
		url = server_address + '/api/funruns/0/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
  "funruns": {
    "address": "Camden Yards\n333 W Camden St.\nBaltimore, MD 21201",
    "challenges": [
      0,
      3,
      5,
      8,
      9,
      11,
      12,
      13
    ],
    "charities": "N/A",
    "city": "Baltimore, Maryland",
    "description": "Crash, smash, and splash your way through a 5k course with larger-than-life obstacles and elements inspired by the hit TV show Wipeout! Take on the infamous Big Balls, Sweeper, Wrecking Balls, and Happy Endings! Hilarious thrills and magnificent spills await!",
    "distance": "5K",
    "fb_url": "https://www.facebook.com/WIPEOUTRUN",
    "hosts": "Ridiculous Obstacle Challenge Race LLC, Endemol USA Inc.",
    "id": 0,
    "imgs": [
      "/static/img/runTempl/wipeout1.jpg",
      "/static/img/runTempl/wipeout2.jpg",
      "/static/img/runTempl/wipeout3.jpg"
    ],
    "landing_img": "/static/img/landing/funruns/wipeoutLanding.jpg",
    "loc": 0,
    "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12352.756020060675!2d-76.621608!3d39.283964!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x2428d93f0397c539!2sOriole+Park+at+Camden+Yards!5e0!3m2!1sen!2sus!4v1427230426235",
    "name": "Wipeout Run",
    "price": "March 6th - April 9th: $56\nApril 10th - May 7th: $61\nMay 8th - May 21st: $66\nMay 22nd - June 5th: $71\nJune 6th: $81",
    "quotes": [
      "Seriously, best race I've done. So much fun. Thanks for coming to Dallas! Hope to see you here in the future!",
      "Had a great time participating in the WIPEOUTRUN!",
      "Such a blast! Let's do it again next year!"
    ],
    "short": "Try out the obstacles from the hit TV show \"Wipeout\"!",
    "sponsors": "VaVi Sport & Social",
    "themes": [
      1
    ],
    "video_url": "https://www.youtube.com/embed/1uOII9K5c0c",
    "website": "http://wipeoutrun.com/"
  }
}))
		self.assertEqual(response_object, expected)

	def test_get_run_by_id_1 (self) :
		url = server_address + '/api/funruns/1/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
  "funruns": {
    "address": "Cleveland Public Square\nCleveland, OH 44113",
    "challenges": [
      1,
      2
    ],
    "charities": "A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects",
    "city": "Cleveland, Ohio",
    "description": "The movie producers must have been runners, because the distance between the former Higbee's Department Store and the A Christmas Story House and Museum is about 5K.  Ralphie's dad, The Old Man must have used the 1938 Oldsmobile to track the distance, since there was no GPS in the 1940's.  To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.",
    "distance": "5K, 10K",
    "fb_url": "https://www.facebook.com/AChristmasStoryRun",
    "hosts": "A Christmas Story House & Museum",
    "id": 1,
    "imgs": [
      "/static/img/runTempl/christmasstory1.jpg",
      "/static/img/runTempl/christmasstory2.jpg",
      "/static/img/runTempl/christmasstory3.jpg"
    ],
    "landing_img": "/static/img/landing/funruns/christmasStoryRunLanding.jpg",
    "loc": 2,
    "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2988.260792402495!2d-81.694473!3d41.498622999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830f07e4562d241%3A0x94e8396bc5227630!2sRenaissance+Cleveland+Hotel!5e0!3m2!1sen!2sus!4v1427230544965",
    "name": "A Christmas Story Run",
    "price": "Before September 30th: $45\nOctober 1st - December 5th: $55",
    "quotes": [
      "I was so excited to get my finisher medal and enjoy a well deserved Christmas Ale.",
      "Despite the crowds, it was so much fun seeing everyone in costume celebrating the movie and our city.",
      "All in all Pepper gives this fun run an A+!"
    ],
    "short": "Experience the classic movie \"A Christmas Story\" in person.",
    "sponsors": "Ovaltine, Renaissance Hotels, Dannon, Walmart, McDonalds, The Home Depot",
    "themes": [
      0,
      2,
      3
    ],
    "video_url": "https://www.youtube.com/embed/uPiN-_p7q2k",
    "website": "http://achristmasstoryrun.com/"
  }
}))
		self.assertEqual(response_object, expected)


	def test_get_run_by_id_2 (self) :
		url = server_address + '/api/funruns/2/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
  "funruns": {
    "address": "City Hall Plaza\n500 Marilla St.\nDallas, TX 75201",
    "challenges": [
      1,
      2
    ],
    "charities": "The Y Community Programs",
    "city": "Dallas, Texas",
    "description": "The Dallas Turkey Trot really proves that everything's bigger in Texas. One of the largest multi-event races in the country, this trot attracts elite runners and regular ol' birds alike. In fact, in 2011, it set a world record for the largest gathering of people dressed as turkeys.",
    "distance": "5K, 8mi",
    "fb_url": "https://www.facebook.com/DallasYMCATrot",
    "hosts": "YMCA, Capital One Bank",
    "id": 2,
    "imgs": [
      "/static/img/runTempl/dallasturkey1.jpg",
      "/static/img/runTempl/dallasturkey2.jpg",
      "/static/img/runTempl/dallasturkey3.jpg"
    ],
    "landing_img": "/static/img/landing/funruns/dallasTurkeyTrotLanding.jpg",
    "loc": 1,
    "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13418.251274220785!2d-96.79709!3d32.777333!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc83854fdfdad6162!2sDallas+City+Hall!5e0!3m2!1sen!2sus!4v1427228610474",
    "name": "Dallas Turkey Trot",
    "price": "Before September 30th: $30\nSeptember 31st - November 25th: $35\nNovember 26th: $45",
    "quotes": [
      "This will be the sixth year my wife and I have run the Dallas Turkey Trot. We began running this race the first year we got married and have kept it a tradition every year. Love this race!",
      "This event is by far the best family friendly event that takes place in Dallas each year!",
      "I had a blast running the Turkey Trot this year. Even though it's my first time doing it, I will definitely make it a tradition every year"
    ],
    "short": "Run in the largest Thanksgiving Day event of its kind.",
    "sponsors": "The Dallas Morning News, Brand Keepers, City of Dallas, Kroger, Nike, The Dallas Cowboys",
    "themes": [
      0,
      2
    ],
    "video_url": "https://www.youtube.com/embed/qdnzjhWgCOg",
    "website": "http://thetrot.org/"
  }
}))
		self.assertEqual(response_object, expected)

	def test_get_run_themes_0 (self) :
		url = server_address + '/api/funruns/0/themes/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
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
										}))
		self.assertEqual(response_object, expected)

	def test_get_run_themes_1 (self) :
		self.maxDiff = None
		url = server_address + '/api/funruns/1/themes/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
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
										}))
		self.assertEqual(response_object, expected)


	def test_get_run_themes_2 (self) :
		url = server_address + '/api/funruns/2/themes/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
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
										    }
										  ]
										}))
		self.assertEqual(response_object, expected)

	def test_get_run_challenges_0 (self) :
		url = server_address + '/api/funruns/0/challenges/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
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
										}))
		self.assertEqual(response_object, expected)

	def test_get_run_challenges_1 (self) :
		url = server_address + '/api/funruns/1/challenges/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
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
										    }
										  ]
										}))
		self.assertEqual(response_object, expected)


	def test_get_run_challenges_2 (self) :
		url = server_address + '/api/funruns/2/challenges/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
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
										    }
										  ]
										}))
		self.assertEqual(response_object, expected)

	# Themes Pillar Tests

	def test_get_themes (self) :
		url = server_address + '/api/themes'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
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
										    },
										    {
										      "buzzwords": "Group, Partner(s), Family, Friends",
										      "challenges": [
										        7,
										        12
										      ],
										      "description": "Everything is more enjoyable with friends! Get crazy in crazy runs with a posse! Register for races in a team - whether you're sporting a theme or just running together for support - you'll be glad you did!",
										      "funruns": [
										        3,
										        8,
										        11
										      ],
										      "id": 5,
										      "imgs": [
										        "/static/img/themeTempl/team1.jpg",
										        "/static/img/themeTempl/team2.jpg",
										        "/static/img/themeTempl/team3.jpg",
										        "/static/img/themeTempl/team4.jpg",
										        "/static/img/themeTempl/team5.jpg",
										        "/static/img/themeTempl/team6.jpg",
										        "/static/img/themeTempl/team7.jpg",
										        "/static/img/themeTempl/team8.jpg"
										      ],
										      "landing_img": "/static/img/landing/themes/team1.jpg",
										      "name": "Team",
										      "short": "Share the fun and join a team to run!"
										    },
										    {
										      "buzzwords": "Beer, Hot Chocolate, Water",
										      "challenges": [
										        6,
										        7
										      ],
										      "description": "Ever try keeping down a couple of drinks while running long distances? Or maybe you want to enjoy the post-race with a nice swig? There are runs out there just for enjoying the liquid-y things in life! Drink runs test your endurance... and your bladder.",
										      "funruns": [
										        7
										      ],
										      "id": 6,
										      "imgs": [
										        "/static/img/themeTempl/drink1.jpg",
										        "/static/img/themeTempl/drink2.jpg",
										        "/static/img/themeTempl/drink3.jpg",
										        "/static/img/themeTempl/drink4.jpg",
										        "/static/img/themeTempl/drink5.jpg",
										        "/static/img/themeTempl/drink6.jpg",
										        "/static/img/themeTempl/drink7.jpg",
										        "/static/img/themeTempl/drink8.jpg"
										      ],
										      "landing_img": "/static/img/landing/themes/drink1.jpg",
										      "name": "Drink",
										      "short": "Run, drink liquids, and drown in utter victory."
										    },
										    {
										      "buzzwords": "Hot Dogs, Pizza, Twinkies, Candy",
										      "challenges": [
										        6,
										        7
										      ],
										      "description": "Forget pre-race bananas and post-race barbecues. How about food as part of the race itself? Start on an empty stomach, because in food races, chowing down is part of the competition - so eat, swallow, rinse, repeat!",
										      "funruns": [
										        9
										      ],
										      "id": 7,
										      "imgs": [
										        "/static/img/themeTempl/food1.jpg",
										        "/static/img/themeTempl/food2.jpg",
										        "/static/img/themeTempl/food3.jpg",
										        "/static/img/themeTempl/food4.jpg",
										        "/static/img/themeTempl/food5.jpg",
										        "/static/img/themeTempl/food6.jpg",
										        "/static/img/themeTempl/food7.jpg",
										        "/static/img/themeTempl/food8.jpg"
										      ],
										      "landing_img": "/static/img/landing/themes/food1.jpg",
										      "name": "Food",
										      "short": "Start on an empty stomach: to beat, you must eat."
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
										}))
		self.assertEqual(response_object, expected)

	def test_get_themes_slash (self) :
		url = server_address + '/api/themes/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
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
										    },
										    {
										      "buzzwords": "Group, Partner(s), Family, Friends",
										      "challenges": [
										        7,
										        12
										      ],
										      "description": "Everything is more enjoyable with friends! Get crazy in crazy runs with a posse! Register for races in a team - whether you're sporting a theme or just running together for support - you'll be glad you did!",
										      "funruns": [
										        3,
										        8,
										        11
										      ],
										      "id": 5,
										      "imgs": [
										        "/static/img/themeTempl/team1.jpg",
										        "/static/img/themeTempl/team2.jpg",
										        "/static/img/themeTempl/team3.jpg",
										        "/static/img/themeTempl/team4.jpg",
										        "/static/img/themeTempl/team5.jpg",
										        "/static/img/themeTempl/team6.jpg",
										        "/static/img/themeTempl/team7.jpg",
										        "/static/img/themeTempl/team8.jpg"
										      ],
										      "landing_img": "/static/img/landing/themes/team1.jpg",
										      "name": "Team",
										      "short": "Share the fun and join a team to run!"
										    },
										    {
										      "buzzwords": "Beer, Hot Chocolate, Water",
										      "challenges": [
										        6,
										        7
										      ],
										      "description": "Ever try keeping down a couple of drinks while running long distances? Or maybe you want to enjoy the post-race with a nice swig? There are runs out there just for enjoying the liquid-y things in life! Drink runs test your endurance... and your bladder.",
										      "funruns": [
										        7
										      ],
										      "id": 6,
										      "imgs": [
										        "/static/img/themeTempl/drink1.jpg",
										        "/static/img/themeTempl/drink2.jpg",
										        "/static/img/themeTempl/drink3.jpg",
										        "/static/img/themeTempl/drink4.jpg",
										        "/static/img/themeTempl/drink5.jpg",
										        "/static/img/themeTempl/drink6.jpg",
										        "/static/img/themeTempl/drink7.jpg",
										        "/static/img/themeTempl/drink8.jpg"
										      ],
										      "landing_img": "/static/img/landing/themes/drink1.jpg",
										      "name": "Drink",
										      "short": "Run, drink liquids, and drown in utter victory."
										    },
										    {
										      "buzzwords": "Hot Dogs, Pizza, Twinkies, Candy",
										      "challenges": [
										        6,
										        7
										      ],
										      "description": "Forget pre-race bananas and post-race barbecues. How about food as part of the race itself? Start on an empty stomach, because in food races, chowing down is part of the competition - so eat, swallow, rinse, repeat!",
										      "funruns": [
										        9
										      ],
										      "id": 7,
										      "imgs": [
										        "/static/img/themeTempl/food1.jpg",
										        "/static/img/themeTempl/food2.jpg",
										        "/static/img/themeTempl/food3.jpg",
										        "/static/img/themeTempl/food4.jpg",
										        "/static/img/themeTempl/food5.jpg",
										        "/static/img/themeTempl/food6.jpg",
										        "/static/img/themeTempl/food7.jpg",
										        "/static/img/themeTempl/food8.jpg"
										      ],
										      "landing_img": "/static/img/landing/themes/food1.jpg",
										      "name": "Food",
										      "short": "Start on an empty stomach: to beat, you must eat."
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
										}))
		self.assertEqual(response_object, expected)

	def test_themes_by_id_0 (self) :
		url = server_address + '/api/themes/0'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "themes": {
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
      }
    }))
		self.assertEqual(response_object, expected)

	def test_themes_by_id_0_slash (self) :
		url = server_address + '/api/themes/0'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "themes": {
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
      }
    }))
		self.assertEqual(response_object, expected)

	def test_themes_by_id_1 (self) :
		url = server_address + '/api/themes/1'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "themes": {
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
    }))
		self.assertEqual(response_object, expected)

	def test_themes_by_id_1_slash (self) :
		url = server_address + '/api/themes/1/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "themes": {
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
    }))
		self.assertEqual(response_object, expected)

	def test_themes_by_id_2 (self) :
		url = server_address + '/api/themes/2'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "themes": {
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
      }
    }))
		self.assertEqual(response_object, expected)


	def test_theme_run_0 (self) :
		url = server_address + '/api/themes/0/funruns'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "themes": [
        {
          "address": "Cleveland Public Square\nCleveland, OH 44113",
          "challenges": [
            1,
            2
          ],
          "charities": "A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects",
          "city": "Cleveland, Ohio",
          "description": "The movie producers must have been runners, because the distance between the former Higbee's Department Store and the A Christmas Story House and Museum is about 5K.  Ralphie's dad, The Old Man must have used the 1938 Oldsmobile to track the distance, since there was no GPS in the 1940's.  To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.",
          "distance": "5K, 10K",
          "fb_url": "https://www.facebook.com/AChristmasStoryRun",
          "hosts": "A Christmas Story House & Museum",
          "id": 1,
          "imgs": [
            "/static/img/runTempl/christmasstory1.jpg",
            "/static/img/runTempl/christmasstory2.jpg",
            "/static/img/runTempl/christmasstory3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/christmasStoryRunLanding.jpg",
          "loc": 2,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2988.260792402495!2d-81.694473!3d41.498622999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830f07e4562d241%3A0x94e8396bc5227630!2sRenaissance+Cleveland+Hotel!5e0!3m2!1sen!2sus!4v1427230544965",
          "name": "A Christmas Story Run",
          "price": "Before September 30th: $45\nOctober 1st - December 5th: $55",
          "quotes": [
            "I was so excited to get my finisher medal and enjoy a well deserved Christmas Ale.",
            "Despite the crowds, it was so much fun seeing everyone in costume celebrating the movie and our city.",
            "All in all Pepper gives this fun run an A+!"
          ],
          "short": "Experience the classic movie \"A Christmas Story\" in person.",
          "sponsors": "Ovaltine, Renaissance Hotels, Dannon, Walmart, McDonalds, The Home Depot",
          "themes": [
            0,
            2,
            3
          ],
          "video_url": "https://www.youtube.com/embed/uPiN-_p7q2k",
          "website": "http://achristmasstoryrun.com/"
        },
        {
          "address": "City Hall Plaza\n500 Marilla St.\nDallas, TX 75201",
          "challenges": [
            1,
            2
          ],
          "charities": "The Y Community Programs",
          "city": "Dallas, Texas",
          "description": "The Dallas Turkey Trot really proves that everything's bigger in Texas. One of the largest multi-event races in the country, this trot attracts elite runners and regular ol' birds alike. In fact, in 2011, it set a world record for the largest gathering of people dressed as turkeys.",
          "distance": "5K, 8mi",
          "fb_url": "https://www.facebook.com/DallasYMCATrot",
          "hosts": "YMCA, Capital One Bank",
          "id": 2,
          "imgs": [
            "/static/img/runTempl/dallasturkey1.jpg",
            "/static/img/runTempl/dallasturkey2.jpg",
            "/static/img/runTempl/dallasturkey3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/dallasTurkeyTrotLanding.jpg",
          "loc": 1,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13418.251274220785!2d-96.79709!3d32.777333!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc83854fdfdad6162!2sDallas+City+Hall!5e0!3m2!1sen!2sus!4v1427228610474",
          "name": "Dallas Turkey Trot",
          "price": "Before September 30th: $30\nSeptember 31st - November 25th: $35\nNovember 26th: $45",
          "quotes": [
            "This will be the sixth year my wife and I have run the Dallas Turkey Trot. We began running this race the first year we got married and have kept it a tradition every year. Love this race!",
            "This event is by far the best family friendly event that takes place in Dallas each year!",
            "I had a blast running the Turkey Trot this year. Even though it's my first time doing it, I will definitely make it a tradition every year"
          ],
          "short": "Run in the largest Thanksgiving Day event of its kind.",
          "sponsors": "The Dallas Morning News, Brand Keepers, City of Dallas, Kroger, Nike, The Dallas Cowboys",
          "themes": [
            0,
            2
          ],
          "video_url": "https://www.youtube.com/embed/qdnzjhWgCOg",
          "website": "http://thetrot.org/"
        }
      ]
    }))
		self.assertEqual(response_object, expected)

	def test_theme_run_1 (self) :
		url = server_address + '/api/themes/1/funruns'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "themes": [
        {
          "address": "Camden Yards\n333 W Camden St.\nBaltimore, MD 21201",
          "challenges": [
            0,
            3,
            5,
            8,
            9,
            11,
            12,
            13
          ],
          "charities": "N/A",
          "city": "Baltimore, Maryland",
          "description": "Crash, smash, and splash your way through a 5k course with larger-than-life obstacles and elements inspired by the hit TV show Wipeout! Take on the infamous Big Balls, Sweeper, Wrecking Balls, and Happy Endings! Hilarious thrills and magnificent spills await!",
          "distance": "5K",
          "fb_url": "https://www.facebook.com/WIPEOUTRUN",
          "hosts": "Ridiculous Obstacle Challenge Race LLC, Endemol USA Inc.",
          "id": 0,
          "imgs": [
            "/static/img/runTempl/wipeout1.jpg",
            "/static/img/runTempl/wipeout2.jpg",
            "/static/img/runTempl/wipeout3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/wipeoutLanding.jpg",
          "loc": 0,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12352.756020060675!2d-76.621608!3d39.283964!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x2428d93f0397c539!2sOriole+Park+at+Camden+Yards!5e0!3m2!1sen!2sus!4v1427230426235",
          "name": "Wipeout Run",
          "price": "March 6th - April 9th: $56\nApril 10th - May 7th: $61\nMay 8th - May 21st: $66\nMay 22nd - June 5th: $71\nJune 6th: $81",
          "quotes": [
            "Seriously, best race I've done. So much fun. Thanks for coming to Dallas! Hope to see you here in the future!",
            "Had a great time participating in the WIPEOUTRUN!",
            "Such a blast! Let's do it again next year!"
          ],
          "short": "Try out the obstacles from the hit TV show \"Wipeout\"!",
          "sponsors": "VaVi Sport & Social",
          "themes": [
            1
          ],
          "video_url": "https://www.youtube.com/embed/1uOII9K5c0c",
          "website": "http://wipeoutrun.com/"
        },
        {
          "address": "3186 DPH 4-H Camp\nSound Avenue\nRiverhead, NY 11901",
          "challenges": [
            1,
            4,
            10,
            12,
            14
          ],
          "charities": "Local Charities",
          "city": "Riverhead, New York",
          "description": "Join us at ZOMBIE RACE! A 5k & 15k run infested with zombies. From the moment the humans leave the start line, theyll be running, crawling, and fleeing in horror from the hordes of undead whose only mission is to devour them alive! Don't let the zombies pull your flags!",
          "distance": "5K, 15K",
          "fb_url": "https://www.facebook.com/zombieracellc",
          "hosts": "Great Vision Productions LLC",
          "id": 4,
          "imgs": [
            "/static/img/runTempl/zombierun1.jpg",
            "/static/img/runTempl/zombierun2.jpg",
            "/static/img/runTempl/zombierun3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/zombierunLanding.jpg",
          "loc": 7,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d48208.84256933457!2d-72.7160401!3d40.9584252!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e861d37b7288b9%3A0x67dff709a1d00494!2sNassau+County+4H+Camp!5e0!3m2!1sen!2sus!4v1428532216187",
          "name": "Zombie Run",
          "price": "5K Prices\nBefore February 6th: $55\nFebruary 7th - February 27th: $65\nFebruary 28th - March 27th: $75\nMarch 28th - April 17th: $85\nApril 18th - May 1st: $95\n15K Prices\nBefore February 6th: $75\nFebruary 7th - February 27th: $85\nFebruary 28th - March 27th: $95\nMarch 28th - April 17th: $105\nApril 18th - May 1st: $155\nZombie Price\nBefore February 6th: $20\nFebruary 7th - February 27th: $25\nFebruary 28th - March 27th: $30\nMarch 28th - April 17th: $35\nApril 18th - May 1st: $40",
          "quotes": [
            "They don't like fast food",
            "Run like zombies are chasing you!",
            "This is one of the funnest events I've ever attended!"
          ],
          "short": "Escape the zombies and get to the finish line!",
          "sponsors": "WholeSale Halloween Costumes",
          "themes": [
            1,
            2,
            9
          ],
          "video_url": "https://www.youtube.com/embed/yhrC2CO9gKM",
          "website": "http://www.zombierace.co/index.php"
        },
        {
          "address": "Bouckaert Farm\n10045 Cedar Grove\nFairburn, GA 30213",
          "challenges": [
            0,
            2,
            3,
            5,
            7,
            8,
            9,
            10,
            11,
            12,
            13
          ],
          "charities": "Wounded Warrior Project, U.S. Army",
          "city": "Fairburn, Georgia",
          "description": "Tough Mudder is a team-oriented obstacle course designed to test physical strength and mental grit. It puts camaraderie over finisher rankings and is not a timed race but a team challenge that allows participants to experience exhilarating, yet safe, world-class obstacles they won't find anywhere else",
          "distance": "19K",
          "fb_url": "https://www.facebook.com/toughmudder",
          "hosts": "Tough Mudder",
          "id": 8,
          "imgs": [
            "/static/img/runTempl/toughmudder1.jpg",
            "/static/img/runTempl/toughmudder2.jpg",
            "/static/img/runTempl/toughmudder3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/toughmudderLanding.jpg",
          "loc": 3,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3322.038929257956!2d-84.7159338!3d33.6302326!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f4d91a281b01bf%3A0x5e4b7c6398a7c91e!2s10045+Cedar+Grove+Rd%2C+Fairburn%2C+GA+30213!5e0!3m2!1sen!2sus!4v1428532369676",
          "name": "Tough Mudder",
          "price": "Before May 2nd: $185\nMay 2nd: $185",
          "quotes": [
            "The teamwork and camaraderie out there was amazing.",
            "The idea of Tough Mudder is not to win... but to have a story to tell.",
            "Tough Mudder is a culture and community of taking on challenges and supporting each other."
          ],
          "short": "Get through 12 miles of military-style obstacles!",
          "sponsors": "Toyo Tires, Cellucor, Shock-Top, MET-Rx, Oberto, Radisson, Wheaties, Under Armour",
          "themes": [
            1,
            4,
            5
          ],
          "video_url": "https://www.youtube.com/embed/Jim-ksScOoc",
          "website": "https://toughmudder.com/"
        }
      ]
    }))
		self.assertEqual(response_object, expected)

	def test_theme_run_2 (self) :
		url = server_address + '/api/themes/2/funruns'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "themes": [
        {
          "address": "Cleveland Public Square\nCleveland, OH 44113",
          "challenges": [
            1,
            2
          ],
          "charities": "A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects",
          "city": "Cleveland, Ohio",
          "description": "The movie producers must have been runners, because the distance between the former Higbee's Department Store and the A Christmas Story House and Museum is about 5K.  Ralphie's dad, The Old Man must have used the 1938 Oldsmobile to track the distance, since there was no GPS in the 1940's.  To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.",
          "distance": "5K, 10K",
          "fb_url": "https://www.facebook.com/AChristmasStoryRun",
          "hosts": "A Christmas Story House & Museum",
          "id": 1,
          "imgs": [
            "/static/img/runTempl/christmasstory1.jpg",
            "/static/img/runTempl/christmasstory2.jpg",
            "/static/img/runTempl/christmasstory3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/christmasStoryRunLanding.jpg",
          "loc": 2,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2988.260792402495!2d-81.694473!3d41.498622999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830f07e4562d241%3A0x94e8396bc5227630!2sRenaissance+Cleveland+Hotel!5e0!3m2!1sen!2sus!4v1427230544965",
          "name": "A Christmas Story Run",
          "price": "Before September 30th: $45\nOctober 1st - December 5th: $55",
          "quotes": [
            "I was so excited to get my finisher medal and enjoy a well deserved Christmas Ale.",
            "Despite the crowds, it was so much fun seeing everyone in costume celebrating the movie and our city.",
            "All in all Pepper gives this fun run an A+!"
          ],
          "short": "Experience the classic movie \"A Christmas Story\" in person.",
          "sponsors": "Ovaltine, Renaissance Hotels, Dannon, Walmart, McDonalds, The Home Depot",
          "themes": [
            0,
            2,
            3
          ],
          "video_url": "https://www.youtube.com/embed/uPiN-_p7q2k",
          "website": "http://achristmasstoryrun.com/"
        },
        {
          "address": "City Hall Plaza\n500 Marilla St.\nDallas, TX 75201",
          "challenges": [
            1,
            2
          ],
          "charities": "The Y Community Programs",
          "city": "Dallas, Texas",
          "description": "The Dallas Turkey Trot really proves that everything's bigger in Texas. One of the largest multi-event races in the country, this trot attracts elite runners and regular ol' birds alike. In fact, in 2011, it set a world record for the largest gathering of people dressed as turkeys.",
          "distance": "5K, 8mi",
          "fb_url": "https://www.facebook.com/DallasYMCATrot",
          "hosts": "YMCA, Capital One Bank",
          "id": 2,
          "imgs": [
            "/static/img/runTempl/dallasturkey1.jpg",
            "/static/img/runTempl/dallasturkey2.jpg",
            "/static/img/runTempl/dallasturkey3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/dallasTurkeyTrotLanding.jpg",
          "loc": 1,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13418.251274220785!2d-96.79709!3d32.777333!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc83854fdfdad6162!2sDallas+City+Hall!5e0!3m2!1sen!2sus!4v1427228610474",
          "name": "Dallas Turkey Trot",
          "price": "Before September 30th: $30\nSeptember 31st - November 25th: $35\nNovember 26th: $45",
          "quotes": [
            "This will be the sixth year my wife and I have run the Dallas Turkey Trot. We began running this race the first year we got married and have kept it a tradition every year. Love this race!",
            "This event is by far the best family friendly event that takes place in Dallas each year!",
            "I had a blast running the Turkey Trot this year. Even though it's my first time doing it, I will definitely make it a tradition every year"
          ],
          "short": "Run in the largest Thanksgiving Day event of its kind.",
          "sponsors": "The Dallas Morning News, Brand Keepers, City of Dallas, Kroger, Nike, The Dallas Cowboys",
          "themes": [
            0,
            2
          ],
          "video_url": "https://www.youtube.com/embed/qdnzjhWgCOg",
          "website": "http://thetrot.org/"
        },
        {
          "address": "Main St & Howard St\nSan Francisco, CA 94105",
          "challenges": [
            1,
            3,
            6
          ],
          "charities": "Mo'MAGIC, United Way of the Bay Area, National Kidney Foundation",
          "city": "San Francisco, California",
          "description": "The Zappos.com Bay to Breakers 12K race runs west through the city and finishes at the Great Highway along the Pacific Coasts Ocean Beach. Participants run up the iconic Hayes Street Hill, along the Panhandle and through Golden Gate Park, while the city of San Francisco cheers them on.",
          "distance": "12K",
          "fb_url": "https://www.facebook.com/zapposbaytobreakers",
          "hosts": "Zappos.com",
          "id": 3,
          "imgs": [
            "/static/img/runTempl/baytobreakers1.jpg",
            "/static/img/runTempl/baytobreakers2.jpg",
            "/static/img/runTempl/baytobreakers3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/baytobreakersLanding.jpg",
          "loc": 6,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3152.984846292559!2d-122.39335585211597!3d37.79039490045594!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064dca37cb7%3A0x3509f87b15b8eae5!2s219+Howard+St%2C+San+Francisco%2C+CA+94105!5e0!3m2!1sen!2sus!4v1428532134914",
          "name": "Bay To Breakers",
          "price": "Adult: $59\nChild: $29.50\nVIP: $139\nGroup/Centipede: $54",
          "quotes": [
            "Bay to Breakers is a direct route to the city's heart and soul.",
            "This 12k seriously looks like a party!",
            "This is an amazing experience that will last forever. It is not only a race, but an incredible party throughout the streets of San Francisco."
          ],
          "short": "Explore SF from the bay to the Ocean Beach breakers.",
          "sponsors": "Under Armour, MapMyRun, Geico, Hyatt Regency, TomTom, Kron4, Kettle Brand, Big 5 Sporting Goods, Hangzhou, Mio",
          "themes": [
            2,
            5
          ],
          "video_url": "https://www.youtube.com/embed/NVEVGSEJmOc",
          "website": "http://zapposbaytobreakers.com/"
        },
        {
          "address": "3186 DPH 4-H Camp\nSound Avenue\nRiverhead, NY 11901",
          "challenges": [
            1,
            4,
            10,
            12,
            14
          ],
          "charities": "Local Charities",
          "city": "Riverhead, New York",
          "description": "Join us at ZOMBIE RACE! A 5k & 15k run infested with zombies. From the moment the humans leave the start line, theyll be running, crawling, and fleeing in horror from the hordes of undead whose only mission is to devour them alive! Don't let the zombies pull your flags!",
          "distance": "5K, 15K",
          "fb_url": "https://www.facebook.com/zombieracellc",
          "hosts": "Great Vision Productions LLC",
          "id": 4,
          "imgs": [
            "/static/img/runTempl/zombierun1.jpg",
            "/static/img/runTempl/zombierun2.jpg",
            "/static/img/runTempl/zombierun3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/zombierunLanding.jpg",
          "loc": 7,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d48208.84256933457!2d-72.7160401!3d40.9584252!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e861d37b7288b9%3A0x67dff709a1d00494!2sNassau+County+4H+Camp!5e0!3m2!1sen!2sus!4v1428532216187",
          "name": "Zombie Run",
          "price": "5K Prices\nBefore February 6th: $55\nFebruary 7th - February 27th: $65\nFebruary 28th - March 27th: $75\nMarch 28th - April 17th: $85\nApril 18th - May 1st: $95\n15K Prices\nBefore February 6th: $75\nFebruary 7th - February 27th: $85\nFebruary 28th - March 27th: $95\nMarch 28th - April 17th: $105\nApril 18th - May 1st: $155\nZombie Price\nBefore February 6th: $20\nFebruary 7th - February 27th: $25\nFebruary 28th - March 27th: $30\nMarch 28th - April 17th: $35\nApril 18th - May 1st: $40",
          "quotes": [
            "They don't like fast food",
            "Run like zombies are chasing you!",
            "This is one of the funnest events I've ever attended!"
          ],
          "short": "Escape the zombies and get to the finish line!",
          "sponsors": "WholeSale Halloween Costumes",
          "themes": [
            1,
            2,
            9
          ],
          "video_url": "https://www.youtube.com/embed/yhrC2CO9gKM",
          "website": "http://www.zombierace.co/index.php"
        },
        {
          "address": "The Long Center Grounds\n701 W Riverside Dr.\nAustin, TX 78704",
          "challenges": [
            1,
            2
          ],
          "charities": "Capital Area Food Bank of Texas",
          "city": "Austin, Texas",
          "description": "Slip into your weirdest costume, slap on your favorite light up running shoes and throw your timer into Lady Bird Lake! This is the slowest 5K on the planet - the wildest, weirdest and most memorable!",
          "distance": "5K",
          "fb_url": "https://www.facebook.com/pages/Keep-Austin-Weird-Festival-5K/121126484577639",
          "hosts": "The Long Center",
          "id": 10,
          "imgs": [
            "/static/img/runTempl/keepAustinWeird1.jpg",
            "/static/img/runTempl/keepAustinWeird2.jpg",
            "/static/img/runTempl/keepAustinWeird3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/keepAustinWeirdLanding.jpg",
          "loc": 4,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3446.1964982159493!2d-97.751079!3d30.259982!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b504ea2084d7%3A0xa8a514235a56453e!2s701+W+Riverside+Dr%2C+Austin%2C+TX+78704!5e0!3m2!1sen!2sus!4v1428532467708",
          "name": "Keep Austin Weird 5K",
          "price": "VIP: $75\nAdults: $22.50\nKids: $12",
          "quotes": [
            "So much fun! Drove down from Oklahoma City to attend!",
            "So well done! Loads of fun!",
            "It was our first time attending the fest and we had a blast! I will be back next year for sure!"
          ],
          "short": "Make Austin weird in the slowest race ever!",
          "sponsors": "HotSchedules, AT&T U-verse, Amy's Ice Cream, Babyearth, Beatbox Beverages",
          "themes": [
            2,
            3,
            8
          ],
          "video_url": "https://www.youtube.com/embed/9sL-B1D7v34",
          "website": "http://keepaustinweirdfest.com/festival/"
        }
      ]
    }))
		self.assertEqual(response_object, expected)

	def test_theme_challenges_0 (self) :
		url = server_address + '/api/themes/0/challenges'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps(	{
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
        }
      ]
    }))
		self.assertEqual(response_object, expected)

	def test_theme_challenges_0_slash (self) :
		url = server_address + '/api/themes/0/challenges/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps(	{
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
        }
      ]
    }))
		self.assertEqual(response_object, expected)

	def test_theme_challenges_1 (self) :
		url = server_address + '/api/themes/1/challenges'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps(	{
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
        }
      ]
    }))
		self.assertEqual(response_object, expected)

	def test_theme_challenges_2 (self) :
		url = server_address + '/api/themes/2/challenges'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps(	{
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

	# Challenges Pillar Tests

	def test_get_challenges (self) :
		url = server_address + '/api/challenges'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
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
    }))
		self.assertEqual(response_object, expected)

	def test_get_challenges_slash (self) :
		url = server_address + '/api/challenges/'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
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
    }))
		self.assertEqual(response_object, expected)

	def test_challenges_by_id_0 (self) :
		url = server_address + '/api/challenges/0'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "challenges": {
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
    }))
		self.assertEqual(response_object, expected)

	def test_challenges_by_id_1 (self) :
		url = server_address + '/api/challenges/1'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "challenges": {
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
    }))
		self.assertEqual(response_object, expected)


	def test_challenges_by_id_2 (self) :
		url = server_address + '/api/challenges/2'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "challenges": {
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
      }
    }))
		self.assertEqual(response_object, expected)


	def test_challenge_run_0 (self) :
		url = server_address + '/api/challenges/0/funruns'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "funruns": [
        {
          "address": "Camden Yards\n333 W Camden St.\nBaltimore, MD 21201",
          "challenges": [
            0,
            3,
            5,
            8,
            9,
            11,
            12,
            13
          ],
          "charities": "N/A",
          "city": "Baltimore, Maryland",
          "description": "Crash, smash, and splash your way through a 5k course with larger-than-life obstacles and elements inspired by the hit TV show Wipeout! Take on the infamous Big Balls, Sweeper, Wrecking Balls, and Happy Endings! Hilarious thrills and magnificent spills await!",
          "distance": "5K",
          "fb_url": "https://www.facebook.com/WIPEOUTRUN",
          "hosts": "Ridiculous Obstacle Challenge Race LLC, Endemol USA Inc.",
          "id": 0,
          "imgs": [
            "/static/img/runTempl/wipeout1.jpg",
            "/static/img/runTempl/wipeout2.jpg",
            "/static/img/runTempl/wipeout3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/wipeoutLanding.jpg",
          "loc": 0,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12352.756020060675!2d-76.621608!3d39.283964!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x2428d93f0397c539!2sOriole+Park+at+Camden+Yards!5e0!3m2!1sen!2sus!4v1427230426235",
          "name": "Wipeout Run",
          "price": "March 6th - April 9th: $56\nApril 10th - May 7th: $61\nMay 8th - May 21st: $66\nMay 22nd - June 5th: $71\nJune 6th: $81",
          "quotes": [
            "Seriously, best race I've done. So much fun. Thanks for coming to Dallas! Hope to see you here in the future!",
            "Had a great time participating in the WIPEOUTRUN!",
            "Such a blast! Let's do it again next year!"
          ],
          "short": "Try out the obstacles from the hit TV show \"Wipeout\"!",
          "sponsors": "VaVi Sport & Social",
          "themes": [
            1
          ],
          "video_url": "https://www.youtube.com/embed/1uOII9K5c0c",
          "website": "http://wipeoutrun.com/"
        },
        {
          "address": "Bouckaert Farm\n10045 Cedar Grove\nFairburn, GA 30213",
          "challenges": [
            0,
            2,
            3,
            5,
            7,
            8,
            9,
            10,
            11,
            12,
            13
          ],
          "charities": "Wounded Warrior Project, U.S. Army",
          "city": "Fairburn, Georgia",
          "description": "Tough Mudder is a team-oriented obstacle course designed to test physical strength and mental grit. It puts camaraderie over finisher rankings and is not a timed race but a team challenge that allows participants to experience exhilarating, yet safe, world-class obstacles they won't find anywhere else",
          "distance": "19K",
          "fb_url": "https://www.facebook.com/toughmudder",
          "hosts": "Tough Mudder",
          "id": 8,
          "imgs": [
            "/static/img/runTempl/toughmudder1.jpg",
            "/static/img/runTempl/toughmudder2.jpg",
            "/static/img/runTempl/toughmudder3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/toughmudderLanding.jpg",
          "loc": 3,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3322.038929257956!2d-84.7159338!3d33.6302326!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f4d91a281b01bf%3A0x5e4b7c6398a7c91e!2s10045+Cedar+Grove+Rd%2C+Fairburn%2C+GA+30213!5e0!3m2!1sen!2sus!4v1428532369676",
          "name": "Tough Mudder",
          "price": "Before May 2nd: $185\nMay 2nd: $185",
          "quotes": [
            "The teamwork and camaraderie out there was amazing.",
            "The idea of Tough Mudder is not to win... but to have a story to tell.",
            "Tough Mudder is a culture and community of taking on challenges and supporting each other."
          ],
          "short": "Get through 12 miles of military-style obstacles!",
          "sponsors": "Toyo Tires, Cellucor, Shock-Top, MET-Rx, Oberto, Radisson, Wheaties, Under Armour",
          "themes": [
            1,
            4,
            5
          ],
          "video_url": "https://www.youtube.com/embed/Jim-ksScOoc",
          "website": "https://toughmudder.com/"
        },
        {
          "address": "Sunday River Ski Resort\n15 S Ridge Rd.\nNewry, ME 04261",
          "challenges": [
            0,
            3,
            5,
            7,
            11,
            12
          ],
          "charities": "N/A",
          "city": "Newry, Maine",
          "description": "Carry your wife to the finish and win her weight in beer! The course at Sunday River is built to international specifications at 278 yards in length, with two dry obstacles and one water obstacle.",
          "distance": "278yd",
          "fb_url": "https://www.facebook.com/sundayriver",
          "hosts": "Sunday River",
          "id": 11,
          "imgs": [
            "/static/img/runTempl/wifecarry1.jpg",
            "/static/img/runTempl/wifecarry2.jpg",
            "/static/img/runTempl/wifecarry3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/wifecarryLanding.jpg",
          "loc": 5,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2847.0332106871697!2d-70.856894!3d44.473492!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cb3dd81009e321b%3A0xd2eb7c1aecb4af6e!2sSunday+River+Ski+Resort!5e0!3m2!1sen!2sus!4v1428532505050",
          "name": "North American Wife Carrying Championship",
          "price": "N/A",
          "quotes": [
            "It was a very cool event! Sunday River does a good job with it!",
            "I'm wicked strong and she's wicked small!",
            "Hardly fair playing field but fun to watch none the less."
          ],
          "short": "Carry your wife and win her weight in beer!",
          "sponsors": "BudLight, Bethel Inn Resort",
          "themes": [
            4,
            5
          ],
          "video_url": "https://player.vimeo.com/video/112507533",
          "website": "http://www.sundayriver.com/events-and-activities/events-calendar/north-american-wife-carrying-championship"
        }
      ]
    }))
		self.assertEqual(response_object, expected)

	def test_challenge_run_1 (self) :
		url = server_address + '/api/challenges/1/funruns'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "funruns": [
        {
          "address": "Cleveland Public Square\nCleveland, OH 44113",
          "challenges": [
            1,
            2
          ],
          "charities": "A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects",
          "city": "Cleveland, Ohio",
          "description": "The movie producers must have been runners, because the distance between the former Higbee's Department Store and the A Christmas Story House and Museum is about 5K.  Ralphie's dad, The Old Man must have used the 1938 Oldsmobile to track the distance, since there was no GPS in the 1940's.  To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.",
          "distance": "5K, 10K",
          "fb_url": "https://www.facebook.com/AChristmasStoryRun",
          "hosts": "A Christmas Story House & Museum",
          "id": 1,
          "imgs": [
            "/static/img/runTempl/christmasstory1.jpg",
            "/static/img/runTempl/christmasstory2.jpg",
            "/static/img/runTempl/christmasstory3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/christmasStoryRunLanding.jpg",
          "loc": 2,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2988.260792402495!2d-81.694473!3d41.498622999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830f07e4562d241%3A0x94e8396bc5227630!2sRenaissance+Cleveland+Hotel!5e0!3m2!1sen!2sus!4v1427230544965",
          "name": "A Christmas Story Run",
          "price": "Before September 30th: $45\nOctober 1st - December 5th: $55",
          "quotes": [
            "I was so excited to get my finisher medal and enjoy a well deserved Christmas Ale.",
            "Despite the crowds, it was so much fun seeing everyone in costume celebrating the movie and our city.",
            "All in all Pepper gives this fun run an A+!"
          ],
          "short": "Experience the classic movie \"A Christmas Story\" in person.",
          "sponsors": "Ovaltine, Renaissance Hotels, Dannon, Walmart, McDonalds, The Home Depot",
          "themes": [
            0,
            2,
            3
          ],
          "video_url": "https://www.youtube.com/embed/uPiN-_p7q2k",
          "website": "http://achristmasstoryrun.com/"
        },
        {
          "address": "City Hall Plaza\n500 Marilla St.\nDallas, TX 75201",
          "challenges": [
            1,
            2
          ],
          "charities": "The Y Community Programs",
          "city": "Dallas, Texas",
          "description": "The Dallas Turkey Trot really proves that everything's bigger in Texas. One of the largest multi-event races in the country, this trot attracts elite runners and regular ol' birds alike. In fact, in 2011, it set a world record for the largest gathering of people dressed as turkeys.",
          "distance": "5K, 8mi",
          "fb_url": "https://www.facebook.com/DallasYMCATrot",
          "hosts": "YMCA, Capital One Bank",
          "id": 2,
          "imgs": [
            "/static/img/runTempl/dallasturkey1.jpg",
            "/static/img/runTempl/dallasturkey2.jpg",
            "/static/img/runTempl/dallasturkey3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/dallasTurkeyTrotLanding.jpg",
          "loc": 1,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13418.251274220785!2d-96.79709!3d32.777333!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc83854fdfdad6162!2sDallas+City+Hall!5e0!3m2!1sen!2sus!4v1427228610474",
          "name": "Dallas Turkey Trot",
          "price": "Before September 30th: $30\nSeptember 31st - November 25th: $35\nNovember 26th: $45",
          "quotes": [
            "This will be the sixth year my wife and I have run the Dallas Turkey Trot. We began running this race the first year we got married and have kept it a tradition every year. Love this race!",
            "This event is by far the best family friendly event that takes place in Dallas each year!",
            "I had a blast running the Turkey Trot this year. Even though it's my first time doing it, I will definitely make it a tradition every year"
          ],
          "short": "Run in the largest Thanksgiving Day event of its kind.",
          "sponsors": "The Dallas Morning News, Brand Keepers, City of Dallas, Kroger, Nike, The Dallas Cowboys",
          "themes": [
            0,
            2
          ],
          "video_url": "https://www.youtube.com/embed/qdnzjhWgCOg",
          "website": "http://thetrot.org/"
        },
        {
          "address": "Main St & Howard St\nSan Francisco, CA 94105",
          "challenges": [
            1,
            3,
            6
          ],
          "charities": "Mo'MAGIC, United Way of the Bay Area, National Kidney Foundation",
          "city": "San Francisco, California",
          "description": "The Zappos.com Bay to Breakers 12K race runs west through the city and finishes at the Great Highway along the Pacific Coasts Ocean Beach. Participants run up the iconic Hayes Street Hill, along the Panhandle and through Golden Gate Park, while the city of San Francisco cheers them on.",
          "distance": "12K",
          "fb_url": "https://www.facebook.com/zapposbaytobreakers",
          "hosts": "Zappos.com",
          "id": 3,
          "imgs": [
            "/static/img/runTempl/baytobreakers1.jpg",
            "/static/img/runTempl/baytobreakers2.jpg",
            "/static/img/runTempl/baytobreakers3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/baytobreakersLanding.jpg",
          "loc": 6,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3152.984846292559!2d-122.39335585211597!3d37.79039490045594!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064dca37cb7%3A0x3509f87b15b8eae5!2s219+Howard+St%2C+San+Francisco%2C+CA+94105!5e0!3m2!1sen!2sus!4v1428532134914",
          "name": "Bay To Breakers",
          "price": "Adult: $59\nChild: $29.50\nVIP: $139\nGroup/Centipede: $54",
          "quotes": [
            "Bay to Breakers is a direct route to the city's heart and soul.",
            "This 12k seriously looks like a party!",
            "This is an amazing experience that will last forever. It is not only a race, but an incredible party throughout the streets of San Francisco."
          ],
          "short": "Explore SF from the bay to the Ocean Beach breakers.",
          "sponsors": "Under Armour, MapMyRun, Geico, Hyatt Regency, TomTom, Kron4, Kettle Brand, Big 5 Sporting Goods, Hangzhou, Mio",
          "themes": [
            2,
            5
          ],
          "video_url": "https://www.youtube.com/embed/NVEVGSEJmOc",
          "website": "http://zapposbaytobreakers.com/"
        },
        {
          "address": "3186 DPH 4-H Camp\nSound Avenue\nRiverhead, NY 11901",
          "challenges": [
            1,
            4,
            10,
            12,
            14
          ],
          "charities": "Local Charities",
          "city": "Riverhead, New York",
          "description": "Join us at ZOMBIE RACE! A 5k & 15k run infested with zombies. From the moment the humans leave the start line, theyll be running, crawling, and fleeing in horror from the hordes of undead whose only mission is to devour them alive! Don't let the zombies pull your flags!",
          "distance": "5K, 15K",
          "fb_url": "https://www.facebook.com/zombieracellc",
          "hosts": "Great Vision Productions LLC",
          "id": 4,
          "imgs": [
            "/static/img/runTempl/zombierun1.jpg",
            "/static/img/runTempl/zombierun2.jpg",
            "/static/img/runTempl/zombierun3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/zombierunLanding.jpg",
          "loc": 7,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d48208.84256933457!2d-72.7160401!3d40.9584252!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e861d37b7288b9%3A0x67dff709a1d00494!2sNassau+County+4H+Camp!5e0!3m2!1sen!2sus!4v1428532216187",
          "name": "Zombie Run",
          "price": "5K Prices\nBefore February 6th: $55\nFebruary 7th - February 27th: $65\nFebruary 28th - March 27th: $75\nMarch 28th - April 17th: $85\nApril 18th - May 1st: $95\n15K Prices\nBefore February 6th: $75\nFebruary 7th - February 27th: $85\nFebruary 28th - March 27th: $95\nMarch 28th - April 17th: $105\nApril 18th - May 1st: $155\nZombie Price\nBefore February 6th: $20\nFebruary 7th - February 27th: $25\nFebruary 28th - March 27th: $30\nMarch 28th - April 17th: $35\nApril 18th - May 1st: $40",
          "quotes": [
            "They don't like fast food",
            "Run like zombies are chasing you!",
            "This is one of the funnest events I've ever attended!"
          ],
          "short": "Escape the zombies and get to the finish line!",
          "sponsors": "WholeSale Halloween Costumes",
          "themes": [
            1,
            2,
            9
          ],
          "video_url": "https://www.youtube.com/embed/yhrC2CO9gKM",
          "website": "http://www.zombierace.co/index.php"
        },
        {
          "address": "The Long Center Grounds\n701 W Riverside Dr.\nAustin, TX 78704",
          "challenges": [
            1,
            2
          ],
          "charities": "Capital Area Food Bank of Texas",
          "city": "Austin, Texas",
          "description": "Slip into your weirdest costume, slap on your favorite light up running shoes and throw your timer into Lady Bird Lake! This is the slowest 5K on the planet - the wildest, weirdest and most memorable!",
          "distance": "5K",
          "fb_url": "https://www.facebook.com/pages/Keep-Austin-Weird-Festival-5K/121126484577639",
          "hosts": "The Long Center",
          "id": 10,
          "imgs": [
            "/static/img/runTempl/keepAustinWeird1.jpg",
            "/static/img/runTempl/keepAustinWeird2.jpg",
            "/static/img/runTempl/keepAustinWeird3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/keepAustinWeirdLanding.jpg",
          "loc": 4,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3446.1964982159493!2d-97.751079!3d30.259982!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b504ea2084d7%3A0xa8a514235a56453e!2s701+W+Riverside+Dr%2C+Austin%2C+TX+78704!5e0!3m2!1sen!2sus!4v1428532467708",
          "name": "Keep Austin Weird 5K",
          "price": "VIP: $75\nAdults: $22.50\nKids: $12",
          "quotes": [
            "So much fun! Drove down from Oklahoma City to attend!",
            "So well done! Loads of fun!",
            "It was our first time attending the fest and we had a blast! I will be back next year for sure!"
          ],
          "short": "Make Austin weird in the slowest race ever!",
          "sponsors": "HotSchedules, AT&T U-verse, Amy's Ice Cream, Babyearth, Beatbox Beverages",
          "themes": [
            2,
            3,
            8
          ],
          "video_url": "https://www.youtube.com/embed/9sL-B1D7v34",
          "website": "http://keepaustinweirdfest.com/festival/"
        }
      ]
    }))
		self.assertEqual(response_object, expected)

	def test_challenge_run_2 (self) :
		self.maxDiff = None
		url = server_address + '/api/challenges/2/funruns'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	json.loads(json.dumps({
      "funruns": [
        {
          "address": "Cleveland Public Square\nCleveland, OH 44113",
          "challenges": [
            1,
            2
          ],
          "charities": "A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects",
          "city": "Cleveland, Ohio",
          "description": "The movie producers must have been runners, because the distance between the former Higbee's Department Store and the A Christmas Story House and Museum is about 5K.  Ralphie's dad, The Old Man must have used the 1938 Oldsmobile to track the distance, since there was no GPS in the 1940's.  To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.",
          "distance": "5K, 10K",
          "fb_url": "https://www.facebook.com/AChristmasStoryRun",
          "hosts": "A Christmas Story House & Museum",
          "id": 1,
          "imgs": [
            "/static/img/runTempl/christmasstory1.jpg",
            "/static/img/runTempl/christmasstory2.jpg",
            "/static/img/runTempl/christmasstory3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/christmasStoryRunLanding.jpg",
          "loc": 2,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2988.260792402495!2d-81.694473!3d41.498622999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830f07e4562d241%3A0x94e8396bc5227630!2sRenaissance+Cleveland+Hotel!5e0!3m2!1sen!2sus!4v1427230544965",
          "name": "A Christmas Story Run",
          "price": "Before September 30th: $45\nOctober 1st - December 5th: $55",
          "quotes": [
            "I was so excited to get my finisher medal and enjoy a well deserved Christmas Ale.",
            "Despite the crowds, it was so much fun seeing everyone in costume celebrating the movie and our city.",
            "All in all Pepper gives this fun run an A+!"
          ],
          "short": "Experience the classic movie \"A Christmas Story\" in person.",
          "sponsors": "Ovaltine, Renaissance Hotels, Dannon, Walmart, McDonalds, The Home Depot",
          "themes": [
            0,
            2,
            3
          ],
          "video_url": "https://www.youtube.com/embed/uPiN-_p7q2k",
          "website": "http://achristmasstoryrun.com/"
        },
        {
          "address": "City Hall Plaza\n500 Marilla St.\nDallas, TX 75201",
          "challenges": [
            1,
            2
          ],
          "charities": "The Y Community Programs",
          "city": "Dallas, Texas",
          "description": "The Dallas Turkey Trot really proves that everything's bigger in Texas. One of the largest multi-event races in the country, this trot attracts elite runners and regular ol' birds alike. In fact, in 2011, it set a world record for the largest gathering of people dressed as turkeys.",
          "distance": "5K, 8mi",
          "fb_url": "https://www.facebook.com/DallasYMCATrot",
          "hosts": "YMCA, Capital One Bank",
          "id": 2,
          "imgs": [
            "/static/img/runTempl/dallasturkey1.jpg",
            "/static/img/runTempl/dallasturkey2.jpg",
            "/static/img/runTempl/dallasturkey3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/dallasTurkeyTrotLanding.jpg",
          "loc": 1,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13418.251274220785!2d-96.79709!3d32.777333!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc83854fdfdad6162!2sDallas+City+Hall!5e0!3m2!1sen!2sus!4v1427228610474",
          "name": "Dallas Turkey Trot",
          "price": "Before September 30th: $30\nSeptember 31st - November 25th: $35\nNovember 26th: $45",
          "quotes": [
            "This will be the sixth year my wife and I have run the Dallas Turkey Trot. We began running this race the first year we got married and have kept it a tradition every year. Love this race!",
            "This event is by far the best family friendly event that takes place in Dallas each year!",
            "I had a blast running the Turkey Trot this year. Even though it's my first time doing it, I will definitely make it a tradition every year"
          ],
          "short": "Run in the largest Thanksgiving Day event of its kind.",
          "sponsors": "The Dallas Morning News, Brand Keepers, City of Dallas, Kroger, Nike, The Dallas Cowboys",
          "themes": [
            0,
            2
          ],
          "video_url": "https://www.youtube.com/embed/qdnzjhWgCOg",
          "website": "http://thetrot.org/"
        },
        {
          "address": "Bouckaert Farm\n10045 Cedar Grove\nFairburn, GA 30213",
          "challenges": [
            0,
            2,
            3,
            5,
            7,
            8,
            9,
            10,
            11,
            12,
            13
          ],
          "charities": "Wounded Warrior Project, U.S. Army",
          "city": "Fairburn, Georgia",
          "description": "Tough Mudder is a team-oriented obstacle course designed to test physical strength and mental grit. It puts camaraderie over finisher rankings and is not a timed race but a team challenge that allows participants to experience exhilarating, yet safe, world-class obstacles they won't find anywhere else",
          "distance": "19K",
          "fb_url": "https://www.facebook.com/toughmudder",
          "hosts": "Tough Mudder",
          "id": 8,
          "imgs": [
            "/static/img/runTempl/toughmudder1.jpg",
            "/static/img/runTempl/toughmudder2.jpg",
            "/static/img/runTempl/toughmudder3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/toughmudderLanding.jpg",
          "loc": 3,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3322.038929257956!2d-84.7159338!3d33.6302326!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f4d91a281b01bf%3A0x5e4b7c6398a7c91e!2s10045+Cedar+Grove+Rd%2C+Fairburn%2C+GA+30213!5e0!3m2!1sen!2sus!4v1428532369676",
          "name": "Tough Mudder",
          "price": "Before May 2nd: $185\nMay 2nd: $185",
          "quotes": [
            "The teamwork and camaraderie out there was amazing.",
            "The idea of Tough Mudder is not to win... but to have a story to tell.",
            "Tough Mudder is a culture and community of taking on challenges and supporting each other."
          ],
          "short": "Get through 12 miles of military-style obstacles!",
          "sponsors": "Toyo Tires, Cellucor, Shock-Top, MET-Rx, Oberto, Radisson, Wheaties, Under Armour",
          "themes": [
            1,
            4,
            5
          ],
          "video_url": "https://www.youtube.com/embed/Jim-ksScOoc",
          "website": "https://toughmudder.com/"
        },
        {
          "address": "The Long Center Grounds\n701 W Riverside Dr.\nAustin, TX 78704",
          "challenges": [
            1,
            2
          ],
          "charities": "Capital Area Food Bank of Texas",
          "city": "Austin, Texas",
          "description": "Slip into your weirdest costume, slap on your favorite light up running shoes and throw your timer into Lady Bird Lake! This is the slowest 5K on the planet - the wildest, weirdest and most memorable!",
          "distance": "5K",
          "fb_url": "https://www.facebook.com/pages/Keep-Austin-Weird-Festival-5K/121126484577639",
          "hosts": "The Long Center",
          "id": 10,
          "imgs": [
            "/static/img/runTempl/keepAustinWeird1.jpg",
            "/static/img/runTempl/keepAustinWeird2.jpg",
            "/static/img/runTempl/keepAustinWeird3.jpg"
          ],
          "landing_img": "/static/img/landing/funruns/keepAustinWeirdLanding.jpg",
          "loc": 4,
          "map_url": "https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3446.1964982159493!2d-97.751079!3d30.259982!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b504ea2084d7%3A0xa8a514235a56453e!2s701+W+Riverside+Dr%2C+Austin%2C+TX+78704!5e0!3m2!1sen!2sus!4v1428532467708",
          "name": "Keep Austin Weird 5K",
          "price": "VIP: $75\nAdults: $22.50\nKids: $12",
          "quotes": [
            "So much fun! Drove down from Oklahoma City to attend!",
            "So well done! Loads of fun!",
            "It was our first time attending the fest and we had a blast! I will be back next year for sure!"
          ],
          "short": "Make Austin weird in the slowest race ever!",
          "sponsors": "HotSchedules, AT&T U-verse, Amy's Ice Cream, Babyearth, Beatbox Beverages",
          "themes": [
            2,
            3,
            8
          ],
          "video_url": "https://www.youtube.com/embed/9sL-B1D7v34",
          "website": "http://keepaustinweirdfest.com/festival/"
        }
      ]
    }))
		self.assertEqual(response_object, expected)

	def test_challenge_themes_0 (self) :
		url = server_address + '/api/challenges/0/themes'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps(	{
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
    }))
		self.assertEqual(response_object, expected)

	def test_challenge_themes_1 (self) :
		url = server_address + '/api/challenges/1/themes'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps(	{
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
    }))
		self.assertEqual(response_object, expected)

	def test_challenge_themes_2 (self) :
		url = server_address + '/api/challenges/2/themes'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps(	{
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
    }))
		self.assertEqual(response_object, expected)


	def test_locations (self) :
		url = server_address + '/api/locations'
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
										    }
										  ]
										}))
		self.assertEqual(response_object, expected)

	def test_locations_by_id_0 (self) :
		url = server_address + '/api/locations/0'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
      "locations": {
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
    }))
		self.assertEqual(response_object, expected)

	def test_locations_by_id_1 (self) :
		url = server_address + '/api/locations/1'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
      "locations": {
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
    }))
		self.assertEqual(response_object, expected)

	def test_locations_by_id_2 (self) :
		url = server_address + '/api/locations/2'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
      "locations": {
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
      }
    }))
		self.assertEqual(response_object, expected)

	def test_locations_by_id_3 (self) :
		url = server_address + '/api/locations/3'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = json.loads(json.dumps({
      "locations": {
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
    }))
		self.assertEqual(response_object, expected)

if __name__ == "__main__" :
    main()