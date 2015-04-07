# -*- coding: utf-8 -*-

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
	funruns = 	[
			    {
			        'id':           0,
			        'name':         u'Wipeout Run',
			        'city':         u'Baltimore, Maryland',
			        'address':      u'Camden Yards\n333 W Camden St.\nBaltimore, MD 21201',
			        'date':         u'June 6th, 2015',
			        'distance':     u'5K',
			        'price':        u'March 6th - April 9th: $56\nApril 10th - May 7th: $61\nMay 8th - May 21st: $66\nMay 22nd - June 5th: $71\nJune 6th: $81',
			        'hosts':        u'Ridiculous Obstacle Challenge Race LLC, Endemol USA Inc.',
			        'sponsors':     u'VaVi Sport & Social',
			        'charities':    u'N/A',
			        'description':  u'Crash, smash, and splash your way through a 5k course with larger-than-life obstacles and elements inspired by the hit TV show Wipeout! Take on the infamous Big Balls, Sweeper, Wrecking Balls, and Happy Endings! Hilarious thrills and magnificent spills await!',
			        'short':		u'Try out the obstacles from the hit TV show "Wipeout"!',
			        'quotes':       [
			                            u'Seriously, best race I\'ve done. So much fun. Thanks for coming to Dallas! Hope to see you here in the future!',
			                            u'Had a great time participating in the WIPEOUTRUN!',
			                            u'Such a blast!! Let\'s do it again next year!!'
			                        ],
			        'website':      u'http://wipeoutrun.com/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12352.756020060675!2d-76.621608!3d39.283964!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x2428d93f0397c539!2sOriole+Park+at+Camden+Yards!5e0!3m2!1sen!2sus!4v1427230426235',
			        'video_url':    u'https://www.youtube.com/embed/1uOII9K5c0c',
			        'fb_url':       u'https://www.facebook.com/WIPEOUTRUN',
			        'landing_img':	u'/static/img/landing/funruns/wipeoutLanding.jpg',
			        'loc':			0,
			        'imgs':         [
			                            u'/static/img/runTempl/wipeout1.jpg',
			                            u'/static/img/runTempl/wipeout2.jpg',
			                            u'/static/img/runTempl/wipeout3.jpg'
			                        ],
			        'themes':       [
			                            1
			                        ],
			        'challenges':   [
			                            0
			                        ]
			    },  
			    {
			        'id':           1,
			        'name':         u'A Christmas Story Run',
			        'city':         u'Cleveland, Ohio',
			        'address':      u'Cleveland Public Square\nCleveland, OH 44113',
			        'date':         u'December 5th, 2015',
			        'distance':     u'5K, 10K',
			        'price':        u'Before September 30th: $45\nOctober 1st - December 5th: $55',
			        'hosts':        u'A Christmas Story House & Museum',
			        'sponsors':     u'Ovaltine, Renaissance Hotels, Dannon, Walmart, McDonalds, The Home Depot',
			        'charities':    u'A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects',
			        'description':  u'The movie producers must have been runners, because the distance between the former Higbee\'s Department Store and the A Christmas Story House and Museum is about 5K.  Ralphie\'s dad, The Old Man must have used the 1938 Oldsmobile to track the distance, since there was no GPS in the 1940\'s.  To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.',
			        'short':		u'Experience the classic movie "A Christmas Story" in person.',
			        'quotes':       [
			                            u'I was so excited to get my finisher medal and enjoy a well deserved Christmas Ale.',
			                            u'Despite the crowds, it was so much fun seeing everyone in costume celebrating the movie and our city.',
			                            u'All in all Pepper gives this fun run an A+!'
			                        ],
			        'website':      u'http://achristmasstoryrun.com/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2988.260792402495!2d-81.694473!3d41.498622999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830f07e4562d241%3A0x94e8396bc5227630!2sRenaissance+Cleveland+Hotel!5e0!3m2!1sen!2sus!4v1427230544965',
			        'video_url':    u'https://www.youtube.com/embed/uPiN-_p7q2k',
			        'fb_url':       u'https://www.facebook.com/AChristmasStoryRun',
			        'landing_img':	u'/static/img/landing/funruns/christmasStoryRunLanding.jpg',
			        'loc':			1,
			        'imgs':         [
			                            u'/static/img/runTempl/christmasstory1.jpg',
			                            u'/static/img/runTempl/christmasstory2.jpg',
			                            u'/static/img/runTempl/christmasstory3.jpg'
			                        ],
			        'themes':       [
			                            0
			                        ],
			        'challenges':   [
			                            2
			                        ]
			    },
			    {
			        'id':           2,
			        'name':         u'Dallas Turkey Trot',
			        'city':         u'Dallas, Texas',
			        'address':      u'City Hall Plaza\n500 Marilla St.\nDallas, TX 75201',
			        'date':         u'November 26th, 2015',
			        'distance':     u'5K, 8mi',
			        'price':        u'Before September 30th: $30\nSeptember 31st - November 25th: $35\nNovember 26th: $45',
			        'hosts':        u'YMCA, Capital One Bank',
			        'sponsors':     u'The Dallas Morning News, Brand Keepers, City of Dallas, Kroger, Nike, The Dallas Cowboys',
			        'charities':    u'The Y Community Programs',
			        'description':  u'The Dallas Turkey Trot really proves that everything\'s bigger in Texas. One of the largest multi-event races in the country, this trot attracts elite runners and regular ol\' birds alike. In fact, in 2011, it set a world record for the largest gathering of people dressed as turkeys.',
			        'short':		u'Run in the largest Thanksgiving Day event of its kind.',
			        'quotes':       [
			                            u'This will be the sixth year my wife and I have run the Dallas Turkey Trot. We began running this race the first year we got married and have kept it a tradition every year. Love this race!',
			                            u'This event is by far the best family friendly event that takes place in Dallas each year!',
			                            u'I had a blast running the Turkey Trot this year. Even though it\'s my first time doing it, I will definitely make it a tradition every year'
			                        ],
			        'website':      u'http://thetrot.org/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13418.251274220785!2d-96.79709!3d32.777333!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc83854fdfdad6162!2sDallas+City+Hall!5e0!3m2!1sen!2sus!4v1427228610474',
			        'video_url':    u'https://www.youtube.com/embed/qdnzjhWgCOg',
			        'fb_url':       u'https://www.facebook.com/DallasYMCATrot',
			        'landing_img':	u'/static/img/landing/funruns/dallasTurkeyTrotLanding.jpg',
			        'loc':			2,
			        'imgs':         [
			                            u'/static/img/runTempl/dallasturkey1.jpg',
			                            u'/static/img/runTempl/dallasturkey2.jpg',
			                            u'/static/img/runTempl/dallasturkey3.jpg'
			                        ],
			        'themes':       [
			                            2
			                        ],
			        'challenges':   [
			                            1,
			                            2
			                        ]
			    },
					{
			        'id':           3,
			        'name':         u'Bay To Breakers',
			        'city':         u'San Francisco, California',
			        'address':      u'Main St & Howard St\nSan Francisco, CA 94105',
			        'date':         u'May 17th, 2015',
			        'distance':     u'12K',
			        'price':        u'Adult: $59\nChild: $29.50\nVIP: $139\nGroup/Centipede: $54',
			        'hosts':        u'Zappos.com',
			        'sponsors':     u'Under Armour, MapMyRun, Geico, Hyatt Regency, TomTom, Kron4, Kettle Brand, Big 5 Sporting Goods, Hangzhou, Mio',
			        'charities':    u'Mo\'MAGIC, United Way of the Bay Area, National Kidney Foundation',
			        'description':  u'The Zappos.com Bay to Breakers 12K race runs west through the city and finishes at the Great Highway along the Pacific Coast’s Ocean Beach. Participants run up the iconic Hayes Street Hill, along the Panhandle and through Golden Gate Park, while the city of San Francisco cheers them on.',
			        'short':		u'Explore SF from the bay to the Ocean Beach breakers.',
			        'quotes':       [
			                            u'Bay to Breakers is a direct route to the city\'s heart and soul.',
			                            u'This 12k seriously looks like a party!',
			                            u'This is an amazing experience that will last forever. It is not only a race, but an incredible party throughout the streets of San Francisco.'
			                        ],
			        'website':      u'http://zapposbaytobreakers.com/',
			        'map_url':      u'https://www.google.com/maps/place/219+Howard+St,+San+Francisco,+CA+94105/@37.7905136,-122.3935597,17z/data=!3m1!4b1!4m2!3m1!1s0x80858064dca37cb7:0x3509f87b15b8eae5',
			        'video_url':    u'https://www.youtube.com/embed/NVEVGSEJmOc',
			        'fb_url':       u'https://www.facebook.com/zapposbaytobreakers',
			        'landing_img':	u'/static/img/landing/funruns/baytobreakersLanding.jpg',
			        'imgs':         [
			                            u'/static/img/runTempl/baytobreakers1.jpg',
			                            u'/static/img/runTempl/baytobreakers2.jpg',
			                            u'/static/img/runTempl/baytobreakers3.jpg'
			                        ],
			        'themes':       [
			                            2
			                        ],
			        'challenges':   [
			                            1
			                        ]
			    },
			    	{
			        'id':           4,
			        'name':         u'Zombie Run',
			        'city':         u'Riverhead, New York',
			        'address':      u'3186 DPH 4-H Camp\nSound Avenue\nRiverhead, New York 11901',
			        'date':         u'May 10th, 2015',
			        'distance':     u'5K, 15k',
			        'price':        u'Before February 6th: $55\nFebruary 7th - February 27th: $65\nFebruary 28th - March 27th: $75\nMarch 28th - April 17th: $85\nApril 18th - May 1st: $95',
			        'hosts':        u'Great Vision Productions LLC',
			        'sponsors':     u'WholeSale Halloween Costumes',
			        'charities':    u'Local charities',
			        'description':  u'We have obstacles but we aren\'t going to tell you what they are! The element of surprise makes the race more fun. Zombie Race is offering a 3.1 mile race and a 9.3 mile race in the Long Island area.',
			        'short':		u'There will be zombie on the course attempting to steal your health flags and eat your brains! Where will they be? You won\'t know until race weekend.!',
			        'quotes':       [
			                            u'They don\'t like fast food',
			                            u'Run like zombies are chasing you!',
			                            u'This is one of the funnest events I\'ve ever attended!'
			                        ],
			        'website':      u'http://www.zombierace.co/index.php',
			        'map_url':      u'https://www.google.com/maps/place/Nassau+County+4H+Camp/@40.9584252,-72.7160401,13z/data=!4m2!3m1!1s0x89e861d37b7288b9:0x67dff709a1d00494',
			        'video_url':    u'https://www.youtube.com/embed/yhrC2CO9gKM',
			        'fb_url':       u'https://www.facebook.com/zombieracellc',
			        'landing_img':	u'/static/img/landing/funruns/zombierunLanding.jpg',
			        'imgs':         [
			                            u'/static/img/runTempl/zombierun1.jpg',
			                            u'/static/img/runTempl/zombierun2.jpg',
			                            u'/static/img/runTempl/zombierun3.jpg'
			                        ],
			        'themes':       [
			                            1
			                        ],
			        'challenges':   [
			                            0
			                        ]
			    },
					{
			        'id':           5,
			        'name':         u'Blacklight Run',
			        'city':         u'Memphis, Tennessee',
			        'address':      u'Memphis International Raceway\n5500 Victory Ln\nMillington, TN 38053',
			        'date':         u'May 9th, 2015',
			        'distance':     u'5K',
			        'price':        u'Before April 8th: $55\nAfter April 8th: $40',
			        'hosts':        u'Blacklight Run Corporate',
			        'sponsors':     u'Local sponsors',
			        'charities':    u'Children\'s Hospital',
			        'description':  u'Blacklight Run™ is a unique night 5K fun run focused less on speed and more on UV Neon Glowing fun with friends and family.Glowing participants come from all different ages, shapes, sizes, and speeds; every participant will get Glowed and will have the time of their life!',
			        'short':		u'The 3 miles of the Blacklight Run course will have you glowing and waiting for the next one!',
			        'quotes':       [
			                            u'Survived another 5k! Finished the Blacklight Run - I love fun runs because there\'s less pressure and the obstacles make the race that much more challenging!',
			                            u'I loved tonight\'s run at Qualcomm stadium in San Diego! California knows how to party! Can\'t wait to have you guys here again and do it again!',
			                            u'This run leaves runners looking like they fell into a Ghost Buster\'s movie (minus the slime).'
			                        ],
			        'website':      u'http://www.blacklightrun.com/',
			        'map_url':      u'https://www.google.com/maps/place/Memphis+International+Raceway/@35.282994,-89.9476,17z/data=!3m1!4b1!4m2!3m1!1s0x887f7ec1c0a48aa5:0x7ef6ea23d0ad044a',
			        'video_url':    u'https://www.youtube.com/embed/TgMgEtXjSUk',
			        'fb_url':       u'https://www.facebook.com/BlacklightRun',
			        'landing_img':	u'/static/img/landing/funruns/blacklightrunLanding.jpg',
			        'imgs':         [
			                            u'/static/img/runTempl/blacklight1.jpg',
			                            u'/static/img/runTempl/blacklight2.jpg',
			                            u'/static/img/runTempl/blacklight3.jpg'
			                        ],
			        'themes':       [
			                            1
			                        ],
			        'challenges':   [
			                            0
			                        ]
			    },
		    	{
			        'id':           6,
			        'name':         u'Electric Run',
			        'city':         u'Puyallup, Washington',
			        'address':      u'Washington State Fair Events Center\n110 9th Avenue\nPuyallup, WA 98371',
			        'date':         u'May 23rd, 2015',
			        'distance':     u'5K',
			        'price':        u'Before April 15th: $45\nApril 16th - May 1st: $50',
			        'hosts':        u'Washington State Fair Events Center',
			        'sponsors':     u'WholeSale Halloween Costumes',
			        'charities':    u'Mary Bridge Children\'s Foundation',
			        'description':  u'Electric Run is the ultimate nighttime 5k run/walk adventure, where the participants are an integrated part of the show',
			        'short':		u'Come join the electric movement and dive into an unforgettable experience for the mind, body, and soul.',
			        'quotes':       [
			                            u'You\'ve GOT to bring The Electric Run back to ATLANTA!',
			                            u' I loved the event last year!',
			                            u'It was a blast! Can\'t wait for this year!',
			                        ],
			        'website':      u'http://electricrun.com/seatac',
			        'map_url':      u'https://www.google.com/maps/place/Washington+State+Fair/@47.1856237,-122.3073378,14z/data=!4m2!3m1!1s0x5490fc035e7af37d:0x5fb822881e1b0c46',
			        'video_url':    u'https://www.youtube.com/embed/R0uhmZI1yy4',
			        'fb_url':       u'https://www.facebook.com/electricrun',
			        'landing_img':	u'/static/img/landing/funruns/electricrunLanding.jpg',
			        'imgs':         [
			                            u'/static/img/runTempl/electricrun1.jpg',
			                            u'/static/img/runTempl/electricrun2.jpg',
			                            u'/static/img/runTempl/electricrun3.jpg'
			                        ],
			        'themes':       [
			                            1
			                        ],
			        'challenges':   [
			                            0
			                        ]
			    },
			    {
			        'id':           7,
			        'name':         u'Brew Mile',
			        'city':         u'Dallas, Texas',
			        'address':      u'1300 Robert B Cullum Boulevard\nDallas, Texas\n78210',
			        'date':         u'May 1st, 2015',
			        'distance':     u'5K',
			        'price':        u'Before May 1st: $75\nOn May 1st: $80',
			        'hosts':        u'Blacklight Run Corporate',
			        'sponsors':     u'Local breweries, food, music organizations',
			        'charities':    u'Local charities',
			        'description':  u'The Brew Mile is your chance to combine your love of running with the finest beverage on the face of this good green earth – BEER. Finally an event that tests your liver as much as it tests your lungs, and is followed by one of the best parties of the year!',
			        'short':		u'Run a mile while chugging beer!',
			        'quotes':       [
			                            u'Super excited for us to do this run.',
			                            u'Drinking a beer after a run is freakin awesome.',
			                            u'I HAVE NEVER BEEN SO EXCITED TO RUN A MILE'
			                        ],
			        'website':      u'http://brewmile.com/',
			        'map_url':      u'https://www.google.com/maps/place/Fair+Park/@32.781453,-96.761736,17z/data=!3m1!4b1!4m2!3m1!1s0x864e9897a14862d7:0x64277dc82ee9144',
			        'video_url':    u'https://www.youtube.com/embed/cXrafhIBdlI',
			        'fb_url':       u'https://www.facebook.com/brewmileseries',
			        'landing_img':	u'/static/img/landing/funruns/brewrunLanding.jpg',
			        'imgs':         [
			                            u'/static/img/runTempl/brewmile1.jpg',
			                            u'/static/img/runTempl/brewmile2.jpg',
			                            u'/static/img/runTempl/brewmile3.jpg'
			                        ],
			        'themes':       [
			                            1
			                        ],
			        'challenges':   [
			                            0
			                        ]
			    },
			    {
			        'id':           8,
			        'name':         u'Tough Mudder',
			        'city':         u'Fairburn, Georgia',
			        'address':      u'10045 Cedar Grove\nFairburn, Georgia\n30213',
			        'date':         u'May 2nd & 3rd, 2015',
			        'distance':     u'19K',
			        'price':        u'$185-$195',
			        'hosts':        u'Tough Mudder',
			        'sponsors':     u'Toyo Tires, Cellucor, Shock-Top, MET-Rx, Oberto, Radisson, Wheaties, Under Armour',
			        'charities':    u'Wounded Warrior Project, U.S. Army',
			        'description':  u'Tough Mudder is a team-oriented obstacle course designed to test physical strength and mental grit. It puts camaraderie over finisher rankings and is not a timed race but a team challenge that allows participants to experience exhilarating, yet safe, world-class obstacles they won\'t find anywhere else',
			        'short':		u'Run through a 12 mile course filled with military-style obstacles', 'quotes':       [
			                            u'The teamwork and camaraderie out there was amazing.',
			                            u'The idea of Tough Mudder is not to win..but to have a story to tell.',
			                            u'Tough Mudder is a culture and Community of taking on challenges and supporting each other.'
			                        ],
			        'website':      u'https://toughmudder.com/',
			        'map_url':      u'https://www.google.com/maps?q=10045+Cedar+Grove+Rd,+Fairburn,+GA,+30213,+us',
			        'video_url':    u'https://www.youtube.com/embed/Jim-ksScOoc',
			        'fb_url':       u'https://www.facebook.com/toughmudder',
			        'landing_img':	u'/static/img/landing/funruns/toughmudderLanding.jpg',
			        'imgs':         [
			                            u'/static/img/runTempl/toughmudder1.jpg',
			                            u'/static/img/runTempl/toughmudder2.jpg',
			                            u'/static/img/runTempl/toughmudder3.jpg'
			                        ],
			        'themes':       [
			                            1
			                        ],
			        'challenges':   [
			                            0
			                        ]
			    },
			    {
			        'id':           9,
			        'name':         u'Fit Foodie 5K',
			        'city':         u'Austin, Texas',
			        'address':      u'Browning Hangar\n4550 Mueller Blvd.\nAustin, TX\n78723',
			        'date':         u'June 12-14th, 2015',
			        'distance':     u'5K',
			        'price':        u'$55',
			        'hosts':        u'Cooking Light & Health',
			        'sponsors':     u'Fast Forward Event Productions',
			        'charities':    u'N/A',
			        'description':  u'Cooking Light & Health\'s The Fit Foodie 5K Race is the ultimate celebration of food, fitness and fun. Put those running shoes to work as you navigate your way around a beautiful 5K course.',
			        'short':		u'Cruise across the finish line and get ready to celebrate your success with delicious, healthy food.',
			        'quotes':       [
			                            u'The race was great, but the festivities after were even greater!',
			                            u'It\'s more than a race, it is a fitness and culinary experience.',
			                            u'Where delicious meets fitness.'
			                        ],
			        'website':      u'http://fitfoodierun.com/',
			        'map_url':      u'https://www.google.com/maps/place/4550+Mueller+Blvd,+Austin,+TX+78723/data=!4m2!3m1!1s0x8644b5f84578082f:0x42afd5562f2f2df1?sa=X&ei=WDEjVeWaF9fsoAS45IGwAw&ved=0CB4Q8gEwAA',
			        'video_url':    u'https://www.youtube.com/embed/cVG9FATjIyk',
			        'fb_url':       u'https://www.facebook.com/pages/The-Fit-Foodie-Race-Series/177814812394419',
			        'landing_img':	u'/static/img/landing/funruns/fitfoodieLanding.jpg',
			        'imgs':         [
			                            u'/static/img/runTempl/fitfoodie1.jpg',
			                            u'/static/img/runTempl/fitfoodie2.jpg',
			                            u'/static/img/runTempl/fitfoodie3.jpg'
			                        ],
			        'themes':       [
			                            1
			                        ],
			        'challenges':   [
			                            0
			                        ]
			    },
			    {
			        'id':           10,
			        'name':         u'Keep Austin Weird 5K',
			        'city':         u'Austin, Texas',
			        'address':      u'The Long Center Grounds\n701 W Riverside Dr.\nAustin, TX\n78704',
			        'date':         u'June 27th, 2015',
			        'distance':     u'5K',
			        'price':        u'Adults: $22.50\nKids: $12',
			        'hosts':        u'The Long Center',
			        'sponsors':     u'HotSchedules, AT&T U-verse, Amy\'s Ice Cream, Babyearth, Beatbox Beverages',
			        'charities':    u'Capital Area Food Bank of Texas',
			        'description':  u'Slip into your weirdest costume, slap on your favorite light up running shoes and throw your timer into Lady Bird Lake!',
			        'short':		u'This is the slowest 5K on the planet!',
			        'quotes':       [
			                            u'So much fun! Drove down from Oklahoma City to attend!',
			                            u'So well done! Loads of fun!',
			                            u'It was our first time attending the fest and we had a blast! I will be back next year for sure!'
			                        ],
			        'website':      u'http://keepaustinweirdfest.com/festival/',
			        'map_url':      u'https://www.google.com/maps/place/701+W+Riverside+Dr,+Austin,+TX+78704/@30.259982,-97.751079,17z/data=!3m1!4b1!4m2!3m1!1s0x8644b504ea2084d7:0xa8a514235a56453e?hl=en-US',
			        'video_url':    u'https://www.youtube.com/embed/9sL-B1D7v34',
			        'fb_url':       u'https://www.facebook.com/pages/Keep-Austin-Weird-Festival-5K/121126484577639',
			        'landing_img':	u'/static/img/landing/funruns/keepAustinWeirdLanding.jpg',
			        'imgs':         [
			                            u'/static/img/runTempl/keepAustinWeird1.jpg',
			                            u'/static/img/runTempl/keepAustinweird2.jpg',
			                            u'/static/img/runTempl/keepAustinweird3.jpg'
			                        ],
			        'themes':       [
			                            1
			                        ],
			        'challenges':   [
			                            0
			                        ]
			    },
			    {
			        'id':           11,
			        'name':         u'North American Wife Carrying Championship',
			        'city':         u'Newry, Maine',
			        'address':      u'Sunday River Ski Resort\n15 S Ridge Rd.\nNewry, ME\n04261',
			        'date':         u'October 10th, 2015',
			        'distance':     u'278yd',
			        'price':        u'N/A',
			        'hosts':        u'Sunday River',
			        'sponsors':     u'BudLight, Bethel Inn Resort',
			        'charities':    u'N/A',
			        'description':  u'Qualifying events are also held in Australia, Sweden, and Estonia. The course at Sunday River is built to international specifications at 278 yards in length;with two dry obstacles and one water obstacle.',
			        'short':		u'To prove their worth,men had to compete through a difficult course with a heavy sack (or woman grabbed from neighboring villages) on their back',
			        'quotes':       [
			                            u'It was a very cool event! Sunday River does a good job with it!',
			                            u'I\'m wicked strong and she\'s wicked small!',
			                            u'Hardly fair playing field but fun to watch none the less.'
			                        ],
			        'website':      u'http://www.sundayriver.com/events-and-activities/events-calendar/north-american-wife-carrying-championship',
			        'map_url':      u'https://www.google.com/maps/place/Sunday+River+Ski+Resort/@44.473492,-70.856894,17z/data=!3m1!4b1!4m2!3m1!1s0x4cb3dd81009e321b:0xd2eb7c1aecb4af6e',
			        'video_url':    u'https://player.vimeo.com/video/112507533',
			        'fb_url':       u'https://www.facebook.com/sundayriver',
			        'landing_img':	u'/static/img/landing/funruns/wifecarryLanding.jpg',
			        'imgs':         [
			                            u'/static/img/runTempl/wifecarry1.jpg',
			                            u'/static/img/runTempl/wifecarry2.jpg',
			                            u'/static/img/runTempl/wifecarry3.jpg'
			                        ],
			        'themes':       [
			                            1
			                        ],
			        'challenges':   [
			                            0
			                        ]
			    }

			]
	return funruns

def retrieve_themes():
	themes = [
			    {
			        'id':           0,
			        'name':         u'Holiday', 
			        'buzzwords':    u'Christmas, Thanksgiving, Easter, Valentine\'s Day, St. Patrick\'s Day, New Year\'s, Halloween, 4th of July',
			        'description':  u'Instead of sitting around the fire, talking of presents and Santa, why not go for a run with the family? Holiday runs are a great way to get out and celebrate during the festivities! Often featuring thematic competitions and costumes, they\'re a sure way of making any holiday a memorable one.',
			        'short':		u'Celebrate the holidays with a festive run.',
			        'landing_img':	u'/static/img/landing/themes/holiday1.jpg',
			        'imgs':         [
			                            u'/static/img/themeTempl/holiday1.jpg',
			                            u'/static/img/themeTempl/holiday2.jpg',
			                            u'/static/img/themeTempl/holiday3.jpg',
			                            u'/static/img/themeTempl/holiday4.jpg',
			                            u'/static/img/themeTempl/holiday5.jpg',
			                            u'/static/img/themeTempl/holiday6.jpg',
			                            u'/static/img/themeTempl/holiday7.jpg',
			                            u'/static/img/themeTempl/holiday8.jpg'
			                        ],
			        'funruns':         [
			                            1
			                        ],
			        'challenges':   [
			                            0,
			                            2
			                        ]
			    },
			    {
			        'id':           1,
			        'name':         u'Intense',
			        'buzzwords':    u'Training, Diet, Hardcore, Recovery, Cutthroat',
			        'description':  u'More interested in proving how much you can take than how much fun you\'ll actually have? Intense runs are exactly what you need - a good dose of body-numbing, soul-crushing exercise to show your stuff. See if you can survive the brutal difficulty of these events.',
			        'short':		u'Test your endurance in these hardcore races.',
			        'landing_img':	u'/static/img/landing/themes/intense1.jpg',
			        'imgs':         [
			                            u'/static/img/themeTempl/intense1.jpg',
			                            u'/static/img/themeTempl/intense2.jpg',
			                            u'/static/img/themeTempl/intense3.jpg',
			                            u'/static/img/themeTempl/intense4.jpg',
			                            u'/static/img/themeTempl/intense5.jpg',
			                            u'/static/img/themeTempl/intense6.jpg',
			                            u'/static/img/themeTempl/intense7.jpg',
			                            u'/static/img/themeTempl/intense8.jpg'
			                        ],
			        'funruns':         [
			                            0
			                        ],
			        'challenges':   [
			                            0,
			                            2
			                        ]
			    },
			    {
			        'id':           2,
			        'name':         u'Costume',
			        'buzzwords':    u'Silly, Uncomfortable, Dress-Up, Make-Believe',
			        'description':  u'Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!',
			        'short':		u'Put on your silliest outfit and get running.',
			        'landing_img':	u'/static/img/landing/themes/costume1.jpg',
			        'imgs':         [
			                            u'/static/img/themeTempl/costume1.jpg',
			                            u'/static/img/themeTempl/costume2.jpg',
			                            u'/static/img/themeTempl/costume3.jpg',
			                            u'/static/img/themeTempl/costume4.jpg',
			                            u'/static/img/themeTempl/costume5.jpg',
			                            u'/static/img/themeTempl/costume6.jpg',
			                            u'/static/img/themeTempl/costume7.jpg',
			                            u'/static/img/themeTempl/costume8.jpg'
			                        ],
			        'funruns':         [
			                            2
			                        ],
			        'challenges':   [
			                            1
			                        ]
			    # },
			    # {
			    #     'id':           3,
			    #     'name':         u'Location',
			    #     'buzzwords':    u'Landmarks, Rivers, Downtown, Parks, Lakes, Views',
			    #     'description':  u'Whether it is an excuse to travel and exercise, or a good distraction from the aches and pains of running, the location of a race is a great factor in deciding which run works for you!',
			    #     'short':		u'Enjoy the scenic views while getting in some exercise.',
			    #     'landing_img':	u'/static/img/landing/themes/location1.jpg',
			    #     'imgs':         [
			    #                         u'/static/img/themeTempl/location1.jpg',
			    #                         u'/static/img/themeTempl/location2.jpg',
			    #                         u'/static/img/themeTempl/location3.jpg',
			    #                         u'/static/img/themeTempl/location4.jpg',
			    #                         u'/static/img/themeTempl/location5.jpg',
			    #                         u'/static/img/themeTempl/location6.jpg',
			    #                         u'/static/img/themeTempl/location7.jpg',
			    #                         u'/static/img/themeTempl/location8.jpg'
			    #                     ],
			    #     'funruns':         [
			    #                         2
			    #                     ],
			    #     'challenges':   [
			    #                         1
			    #                     ]
			    # },
			    # {
			    #     'id':           4,
			    #     'name':         u'Dirty',
			    #     'buzzwords':    u'Silly, Uncomfortable, Dress-Up, Make-Believe',
			    #     'description':  u'Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!',
			    #     'short':		u'Put on your silliest outfit and get running',
			    #     'landing_img':	u'/static/img/landing/themes/dirty1.jpg',
			    #     'imgs':         [
			    #                         u'/static/img/themeTempl/dirty1.jpg',
			    #                         u'/static/img/themeTempl/dirty2.jpg',
			    #                         u'/static/img/themeTempl/dirty3.jpg',
			    #                         u'/static/img/themeTempl/dirty4.jpg',
			    #                         u'/static/img/themeTempl/dirty5.jpg',
			    #                         u'/static/img/themeTempl/dirty6.jpg',
			    #                         u'/static/img/themeTempl/dirty7.jpg',
			    #                         u'/static/img/themeTempl/dirty8.jpg'
			    #                     ],
			    #     'funruns':         [
			    #                         2
			    #                     ],
			    #     'challenges':   [
			    #                         1
			    #                     ]
			    # },
			    # {
			    #     'id':           5,
			    #     'name':         u'Team',
			    #     'buzzwords':    u'Silly, Uncomfortable, Dress-Up, Make-Believe',
			    #     'description':  u'Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!',
			    #     'short':		u'Put on your silliest outfit and get running',
			    #     'landing_img':	u'/static/img/landing/themes/team1.jpg',
			    #     'imgs':         [
			    #                         u'/static/img/themeTempl/team1.jpg',
			    #                         u'/static/img/themeTempl/team2.jpg',
			    #                         u'/static/img/themeTempl/team3.jpg',
			    #                         u'/static/img/themeTempl/team4.jpg',
			    #                         u'/static/img/themeTempl/team5.jpg',
			    #                         u'/static/img/themeTempl/team6.jpg',
			    #                         u'/static/img/themeTempl/team7.jpg',
			    #                         u'/static/img/themeTempl/team8.jpg'
			    #                     ],
			    #     'funruns':         [
			    #                         2
			    #                     ],
			    #     'challenges':   [
			    #                         1
			    #                     ]
			    # },
			    # {
			    #     'id':           6,
			    #     'name':         u'Drink',
			    #     'buzzwords':    u'Silly, Uncomfortable, Dress-Up, Make-Believe',
			    #     'description':  u'Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!',
			    #     'short':		u'Put on your silliest outfit and get running',
			    #     'landing_img':	u'/static/img/landing/themes/drink1.jpg',
			    #     'imgs':         [
			    #                         u'/static/img/themeTempl/drink1.jpg',
			    #                         u'/static/img/themeTempl/drink2.jpg',
			    #                         u'/static/img/themeTempl/drink3.jpg',
			    #                         u'/static/img/themeTempl/drink4.jpg',
			    #                         u'/static/img/themeTempl/drink5.jpg',
			    #                         u'/static/img/themeTempl/drink6.jpg',
			    #                         u'/static/img/themeTempl/drink7.jpg',
			    #                         u'/static/img/themeTempl/drink8.jpg'
			    #                     ],
			    #     'funruns':         [
			    #                         2
			    #                     ],
			    #     'challenges':   [
			    #                         1
			    #                     ]
			    # },
			    # {
			    #     'id':           7,
			    #     'name':         u'Food',
			    #     'buzzwords':    u'Silly, Uncomfortable, Dress-Up, Make-Believe',
			    #     'description':  u'Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!',
			    #     'short':		u'Put on your silliest outfit and get running',
			    #     'landing_img':	u'/static/img/landing/themes/food1.jpg',
			    #     'imgs':         [
			    #                         u'/static/img/themeTempl/food1.jpg',
			    #                         u'/static/img/themeTempl/food2.jpg',
			    #                         u'/static/img/themeTempl/food3.jpg',
			    #                         u'/static/img/themeTempl/food4.jpg',
			    #                         u'/static/img/themeTempl/food5.jpg',
			    #                         u'/static/img/themeTempl/food6.jpg',
			    #                         u'/static/img/themeTempl/food7.jpg',
			    #                         u'/static/img/themeTempl/food8.jpg'
			    #                     ],
			    #     'funruns':         [
			    #                         2
			    #                     ],
			    #     'challenges':   [
			    #                         1
			    #                     ]
			    # },
			    # {
			    #     'id':           8,
			    #     'name':         u'Music',
			    #     'buzzwords':    u'Silly, Uncomfortable, Dress-Up, Make-Believe',
			    #     'description':  u'Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!',
			    #     'short':		u'Put on your silliest outfit and get running',
			    #     'landing_img':	u'/static/img/landing/themes/music1.jpg',
			    #     'imgs':         [
			    #                         u'/static/img/themeTempl/music1.jpg',
			    #                         u'/static/img/themeTempl/music2.jpg',
			    #                         u'/static/img/themeTempl/music3.jpg',
			    #                         u'/static/img/themeTempl/music4.jpg',
			    #                         u'/static/img/themeTempl/music5.jpg',
			    #                         u'/static/img/themeTempl/music6.jpg',
			    #                         u'/static/img/themeTempl/music7.jpg',
			    #                         u'/static/img/themeTempl/music8.jpg'
			    #                     ],
			    #     'funruns':         [
			    #                         2
			    #                     ],
			    #     'challenges':   [
			    #                         1
			    #                     ]
			    # },
			    # {
			    #     'id':           9,
			    #     'name':         u'Fantasy',
			    #     'buzzwords':    u'Silly, Uncomfortable, Dress-Up, Make-Believe',
			    #     'description':  u'Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!',
			    #     'short':		u'Put on your silliest outfit and get running',
			    #     'landing_img':	u'/static/img/landing/themes/fantasy1.jpg',
			    #     'imgs':         [
			    #                         u'/static/img/themeTempl/fantasy1.jpg',
			    #                         u'/static/img/themeTempl/fantasy2.jpg',
			    #                         u'/static/img/themeTempl/fantasy3.jpg',
			    #                         u'/static/img/themeTempl/fantasy4.jpg',
			    #                         u'/static/img/themeTempl/fantasy5.jpg',
			    #                         u'/static/img/themeTempl/fantasy6.jpg',
			    #                         u'/static/img/themeTempl/fantasy7.jpg',
			    #                         u'/static/img/themeTempl/fantasy8.jpg'
			    #                     ],
			    #     'funruns':         [
			    #                         2
			    #                     ],
			    #     'challenges':   [
			    #                         1
			    #                     ]
			    }
			]
	return themes

def retrieve_challenges():
	challenges = [
				    {
				        'id':           0,
				        'name':         u'Running On Awkward Ground',
				        'difficulty':   60,
				        'flavors':      u'Ice, Inflatable Balls, Mud',
				        'description':  u'Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.',
				        'landing_img':	u'/static/img/landing/challenges/oddGround1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/oddGround1.jpg',
				                            u'/static/img/challengeTempl/oddGround2.jpg',
				                            u'/static/img/challengeTempl/oddGround3.jpg'
				                        ],
				        'funruns':      [
				                            0
				                        ],
				        'themes':       [
				                            0,
				                            1
				                        ]
				    },
				    {
				        'id':           1,
				        'name':         u'Running In A Costume',
				        'difficulty':   40,
				        'flavors':      u'Mascots, Nude, Speedos, Costumes',
				        'description':  u'Ideally, running should be done in comfortable shorts and shirt. Instead, some dare to run in costumes - or a lack of costume - in self expression and, oftentimes, silliness.',
				        'landing_img':	u'/static/img/landing/challenges/costume1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/costume1.jpg',
				                            u'/static/img/challengeTempl/costume2.jpg',
				                            u'/static/img/challengeTempl/costume3.jpg'
				                        ],
				        'funruns':      [
				                            2
				                        ],
				        'themes':       [
				                            2
				                        ]
				    },
				    {
				        'id':           2,
				        'name':         u'Running In Cold Weather',
				        'difficulty':   80,
				        'flavors':      u'Snow, Ice, Freezing Temperatures',
				        'description':  u'Take on the cold fearlessly with fun runs in less than ideal temperatures. Will the icy winds get to you or will you make it to the finish line and prevail?',
				        'landing_img':	u'/static/img/landing/challenges/cold1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/cold1.jpg',
				                            u'/static/img/challengeTempl/cold2.jpg',
				                            u'/static/img/challengeTempl/cold3.jpg'
				                        ],
				        'funruns':      [
				        					1,
				                            2
				                        ],
				        'themes':       [
				                            0,
				                            1
				                        ]
				    }
				]
	return challenges

### NOTE: I CHANGED LOCATION TO NAME ON ATTRIBUTES AND STRINGS TO INTS
def retrieve_locations():
	locations = [
					{
					    'id':                   0,
					    'name':      	      	u'Baltimore, Maryland',
					    'nickname':				u'The Charm City',
					    'winter_avgTemp':       45,
					    'spring_avgTemp':       65,
					    'summer_avgTemp':       87,
					    'fall_avgTemp':         69,
					    'winter_avgHumidity':   63,
					    'spring_avgHumidity':   61,
					    'summer_avgHumidity':   69,
					    'fall_avgHumidity':     69,
					    'altitude':             u'33ft',
					    'annual_rainfall':      u'40.72in',
					    'landmarks':            u'National Aquarium in Baltimore, Fort McHenry',
					    'website_url':			u'http://www.baltimorecity.gov/',
					    'description':			u'Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.',
					    'landing_img':			u'/static/img/landing/locations/baltimoreMDLanding.jpg',
					    'img':					u'/static/img/locationTempl/baltimore1.jpg'
					},
					{
					    'id':                   1,
					    'name':      	      	u'Dallas, Texas',
					    'nickname':				u'Home of the Cowboys',
					    'winter_avgTemp':	    59,
					    'spring_avgTemp':       77,
					    'summer_avgTemp':       95,
					    'fall_avgTemp':         78,
					    'winter_avgHumidity':   52,
					    'spring_avgHumidity':   49,
					    'summer_avgHumidity':   44,
					    'fall_avgHumidity':     47,
					    'altitude':             u'430ft',
					    'annual_rainfall':      u'40.55in',
					    'landmarks':            u'Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium',
					    'website_url':			u'http://dallascityhall.com/Pages/default.aspx',
					    'description':			u'Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.',
					    'landing_img':			u'/static/img/landing/locations/dallasTXLanding.jpg',
					    'img':					u'/static/img/locationTempl/dallas1.jpg'
					},
					{
					    'id':                   2,
					    'name':             	u'Cleveland, Ohio',
					    'nickname':				u'The Forest City',
					    'winter_avgTemp':       37,
					    'spring_avgTemp':       58,
					    'summer_avgTemp':       81,
					    'fall_avgTemp':         72,
					    'winter_avgHumidity':   71,
					    'spring_avgHumidity':   59,
					    'summer_avgHumidity':   55,
					    'fall_avgHumidity':     58,
					    'altitude':             u'653ft',
					    'annual_rainfall':      u'39.12in',
					    'landmarks':            u'Rock and Roll Hall of Fame, Cleveland Metroparks Zoo',
					    'website_url':			u'http://www.city.cleveland.oh.us/CityofCleveland/Home',
					    'description':			u'Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.',
					    'landing_img':			u'/static/img/landing/locations/clevelandOHLanding.jpg',
					    'img':					u'/static/img/locationTempl/cleveland1.jpg'	
					}
				]
	return locations

