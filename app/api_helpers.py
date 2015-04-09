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
			                            u'Such a blast! Let\'s do it again next year!'
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
			                            0, 3, 5, 8, 9, 11, 12, 13
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
			        'loc':			2,
			        'imgs':         [
			                            u'/static/img/runTempl/christmasstory1.jpg',
			                            u'/static/img/runTempl/christmasstory2.jpg',
			                            u'/static/img/runTempl/christmasstory3.jpg'
			                        ],
			        'themes':       [
			                            0, 2, 3
			                        ],
			        'challenges':   [
			                            1, 2
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
			        'loc':			1,
			        'imgs':         [
			                            u'/static/img/runTempl/dallasturkey1.jpg',
			                            u'/static/img/runTempl/dallasturkey2.jpg',
			                            u'/static/img/runTempl/dallasturkey3.jpg'
			                        ],
			        'themes':       [
			                            0, 2
			                        ],
			        'challenges':   [
			                            1, 2
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
			        'description':  u'The Zappos.com Bay to Breakers 12K race runs west through the city and finishes at the Great Highway along the Pacific Coasts Ocean Beach. Participants run up the iconic Hayes Street Hill, along the Panhandle and through Golden Gate Park, while the city of San Francisco cheers them on.',
			        'short':		u'Explore SF from the bay to the Ocean Beach breakers.',
			        'quotes':       [
			                            u'Bay to Breakers is a direct route to the city\'s heart and soul.',
			                            u'This 12k seriously looks like a party!',
			                            u'This is an amazing experience that will last forever. It is not only a race, but an incredible party throughout the streets of San Francisco.'
			                        ],
			        'website':      u'http://zapposbaytobreakers.com/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3152.984846292559!2d-122.39335585211597!3d37.79039490045594!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064dca37cb7%3A0x3509f87b15b8eae5!2s219+Howard+St%2C+San+Francisco%2C+CA+94105!5e0!3m2!1sen!2sus!4v1428532134914',
			        'video_url':    u'https://www.youtube.com/embed/NVEVGSEJmOc',
			        'fb_url':       u'https://www.facebook.com/zapposbaytobreakers',
			        'landing_img':	u'/static/img/landing/funruns/baytobreakersLanding.jpg',
			        'loc':			6,
			        'imgs':         [
			                            u'/static/img/runTempl/baytobreakers1.jpg',
			                            u'/static/img/runTempl/baytobreakers2.jpg',
			                            u'/static/img/runTempl/baytobreakers3.jpg'
			                        ],
			        'themes':       [
			                            2, 5
			                        ],
			        'challenges':   [
			                            1, 3, 6
			                        ]
			    },
			    	{
			        'id':           4,
			        'name':         u'Zombie Run',
			        'city':         u'Riverhead, New York',
			        'address':      u'3186 DPH 4-H Camp\nSound Avenue\nRiverhead, NY 11901',
			        'date':         u'May 10th, 2015',
			        'distance':     u'5K, 15K',
			        'price':        u'5K Prices\nBefore February 6th: $55\nFebruary 7th - February 27th: $65\nFebruary 28th - March 27th: $75\nMarch 28th - April 17th: $85\nApril 18th - May 1st: $95\n15K Prices\nBefore February 6th: $75\nFebruary 7th - February 27th: $85\nFebruary 28th - March 27th: $95\nMarch 28th - April 17th: $105\nApril 18th - May 1st: $155\nZombie Price\nBefore February 6th: $20\nFebruary 7th - February 27th: $25\nFebruary 28th - March 27th: $30\nMarch 28th - April 17th: $35\nApril 18th - May 1st: $40',
			        'hosts':        u'Great Vision Productions LLC',
			        'sponsors':     u'WholeSale Halloween Costumes',
			        'charities':    u'Local Charities',
			        'description':  u'Join us at ZOMBIE RACE! A 5k & 15k run infested with zombies. From the moment the humans leave the start line, theyll be running, crawling, and fleeing in horror from the hordes of undead whose only mission is to devour them alive! Don\'t let the zombies pull your flags!',
			        'short':		u'Escape the zombies and get to the finish line!',
			        'quotes':       [
			                            u'They don\'t like fast food',
			                            u'Run like zombies are chasing you!',
			                            u'This is one of the funnest events I\'ve ever attended!'
			                        ],
			        'website':      u'http://www.zombierace.co/index.php',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d48208.84256933457!2d-72.7160401!3d40.9584252!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e861d37b7288b9%3A0x67dff709a1d00494!2sNassau+County+4H+Camp!5e0!3m2!1sen!2sus!4v1428532216187',
			        'video_url':    u'https://www.youtube.com/embed/yhrC2CO9gKM',
			        'fb_url':       u'https://www.facebook.com/zombieracellc',
			        'landing_img':	u'/static/img/landing/funruns/zombierunLanding.jpg',
			        'loc':			7,
			        'imgs':         [
			                            u'/static/img/runTempl/zombierun1.jpg',
			                            u'/static/img/runTempl/zombierun2.jpg',
			                            u'/static/img/runTempl/zombierun3.jpg'
			                        ],
			        'themes':       [
			                            1, 2, 9
			                        ],
			        'challenges':   [
			                            1, 4, 10, 12, 14
			                        ]
			    },
					{
			        'id':           5,
			        'name':         u'Blacklight Run',
			        'city':         u'Memphis, Tennessee',
			        'address':      u'Memphis International Raceway\n5500 Victory Ln\nMillington, TN 38053',
			        'date':         u'May 9th, 2015',
			        'distance':     u'5K',
			        'price':        u'Standard Registration\nBefore April 8th: $20\nApril 8th - May 9th: $40\nVIP Registration\nBefore April 8th: $45\nApril 8th - May 9th: $75',
			        'hosts':        u'Blacklight Run Corporate',
			        'sponsors':     u'Local Sponsors',
			        'charities':    u'Children\'s Hospital',
			        'description':  u'Blacklight Run is a unique night 5K fun run focused less on speed and more on UV Neon Glowing fun with friends and family. Glowing participants come from all different ages, shapes, sizes, and speeds; every participant will get Glowed and will have the time of their life!',
			        'short':		u'Get going and get glowing with this neon powder run!',
			        'quotes':       [
			                            u'Survived another 5k! Finished the Blacklight Run - I love fun runs because there\'s less pressure and the obstacles make the race that much more challenging!',
			                            u'I loved tonight\'s run at Qualcomm stadium in San Diego! California knows how to party! Can\'t wait to have you guys here again and do it again!',
			                            u'This run leaves runners looking like they fell into a Ghost Buster\'s movie (minus the slime).'
			                        ],
			        'website':      u'http://www.blacklightrun.com/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3256.9248763636133!2d-89.9476!3d35.282993999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x887f7ec1c0a48aa5%3A0x7ef6ea23d0ad044a!2sMemphis+International+Raceway!5e0!3m2!1sen!2sus!4v1428532262614',
			        'video_url':    u'https://www.youtube.com/embed/TgMgEtXjSUk',
			        'fb_url':       u'https://www.facebook.com/BlacklightRun',
			        'landing_img':	u'/static/img/landing/funruns/blacklightrunLanding.jpg',
			        'loc':			8,
			        'imgs':         [
			                            u'/static/img/runTempl/blacklight1.jpg',
			                            u'/static/img/runTempl/blacklight2.jpg',
			                            u'/static/img/runTempl/blacklight3.jpg'
			                        ],
			        'themes':       [
			                            4, 8
			                        ],
			        'challenges':   [
			                            5, 15
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
			        'description':  u'Electric Run is the ultimate nighttime 5k run/walk adventure, where the participants are an integrated part of the show. Featuring immersive "Lands" of light and sound that transport the participant into an electric wonderland.',
			        'short':		u'Become part of the electric run in this nighttime adventure.',
			        'quotes':       [
			                            u'You\'ve GOT to bring The Electric Run back to ATLANTA!',
			                            u'I loved the event last year!',
			                            u'It was a blast! Can\'t wait for this year!',
			                        ],
			        'website':      u'http://electricrun.com/seatac',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d21692.65452180003!2d-122.3073378!3d47.1856237!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5490fc035e7af37d%3A0x5fb822881e1b0c46!2sWashington+State+Fair!5e0!3m2!1sen!2sus!4v1428532299643',
			        'video_url':    u'https://www.youtube.com/embed/R0uhmZI1yy4',
			        'fb_url':       u'https://www.facebook.com/electricrun',
			        'landing_img':	u'/static/img/landing/funruns/electricrunLanding.jpg',
			        'loc':			9,
			        'imgs':         [
			                            u'/static/img/runTempl/electricrun1.jpg',
			                            u'/static/img/runTempl/electricrun2.jpg',
			                            u'/static/img/runTempl/electricrun3.jpg'
			                        ],
			        'themes':       [
			                            4, 8
			                        ],
			        'challenges':   [
			                            5, 15
			                        ]
			    },
			    {
			        'id':           7,
			        'name':         u'Brew Mile',
			        'city':         u'Dallas, Texas',
			        'address':      u'Fair Park Dallas\n1300 Robert B Cullum Boulevard\nDallas, TX 78210',
			        'date':         u'May 1st, 2015',
			        'distance':     u'5K',
			        'price':        u'February 1st - March 12th: $55\nMarch 13th - April 9th: $65\nApril 10th - April 30th: $75\nMay 1st: $80',
			        'hosts':        u'Blacklight Run Corporate',
			        'sponsors':     u'Upslope Brewing Co, TwinPeaks Brewing Co, Nine Band Brewing Co, Pedernales Brewing Co, Saint Arnold Brewing Co',
			        'charities':    u'Local Breweries, Local Food, Local Music',
			        'description':  u'The Brew Mile is your chance to combine your love of running with the finest beverage on the face of this good green earth  BEER. Finally an event that tests your liver as much as it tests your lungs, and is followed by one of the best parties of the year!',
			        'short':		u'Take on a mile while chugging beer!',
			        'quotes':       [
			                            u'Super excited for us to do this run.',
			                            u'Drinking a beer after a run is freaking awesome.',
			                            u'I HAVE NEVER BEEN SO EXCITED TO RUN A MILE.'
			                        ],
			        'website':      u'http://brewmile.com/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3354.4074902321736!2d-96.76173600000001!3d32.781453!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x864e9897a14862d7%3A0x64277dc82ee9144!2sFair+Park!5e0!3m2!1sen!2sus!4v1428532340130',
			        'video_url':    u'https://www.youtube.com/embed/cXrafhIBdlI',
			        'fb_url':       u'https://www.facebook.com/brewmileseries',
			        'landing_img':	u'/static/img/landing/funruns/brewrunLanding.jpg',
			        'loc':			1,
			        'imgs':         [
			                            u'/static/img/runTempl/brewmile1.jpg',
			                            u'/static/img/runTempl/brewmile2.jpg',
			                            u'/static/img/runTempl/brewmile3.jpg'
			                        ],
			        'themes':       [
			                            6
			                        ],
			        'challenges':   [
			                            6
			                        ]
			    },
			    {
			        'id':           8,
			        'name':         u'Tough Mudder',
			        'city':         u'Fairburn, Georgia',
			        'address':      u'Bouckaert Farm\n10045 Cedar Grove\nFairburn, GA 30213',
			        'date':         u'May 2nd, 2015',
			        'distance':     u'19K',
			        'price':        u'Before May 2nd: $185\nMay 2nd: $185',
			        'hosts':        u'Tough Mudder',
			        'sponsors':     u'Toyo Tires, Cellucor, Shock-Top, MET-Rx, Oberto, Radisson, Wheaties, Under Armour',
			        'charities':    u'Wounded Warrior Project, U.S. Army',
			        'description':  u'Tough Mudder is a team-oriented obstacle course designed to test physical strength and mental grit. It puts camaraderie over finisher rankings and is not a timed race but a team challenge that allows participants to experience exhilarating, yet safe, world-class obstacles they won\'t find anywhere else',
			        'short':		u'Get through 12 miles of military-style obstacles!', 
			        'quotes':       [
			                            u'The teamwork and camaraderie out there was amazing.',
			                            u'The idea of Tough Mudder is not to win... but to have a story to tell.',
			                            u'Tough Mudder is a culture and community of taking on challenges and supporting each other.'
			                        ],
			        'website':      u'https://toughmudder.com/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3322.038929257956!2d-84.7159338!3d33.6302326!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f4d91a281b01bf%3A0x5e4b7c6398a7c91e!2s10045+Cedar+Grove+Rd%2C+Fairburn%2C+GA+30213!5e0!3m2!1sen!2sus!4v1428532369676',
			        'video_url':    u'https://www.youtube.com/embed/Jim-ksScOoc',
			        'fb_url':       u'https://www.facebook.com/toughmudder',
			        'landing_img':	u'/static/img/landing/funruns/toughmudderLanding.jpg',
			        'loc':			3,
			        'imgs':         [
			                            u'/static/img/runTempl/toughmudder1.jpg',
			                            u'/static/img/runTempl/toughmudder2.jpg',
			                            u'/static/img/runTempl/toughmudder3.jpg'
			                        ],
			        'themes':       [
			                            1, 4, 5
			                        ],
			        'challenges':   [
			                            0, 2, 3, 5, 7, 8, 9, 10, 11, 12, 13
			                        ]
			    },
			    {
			        'id':           9,
			        'name':         u'Fit Foodie 5K',
			        'city':         u'Austin, Texas',
			        'address':      u'Browning Hangar\n4550 Mueller Blvd.\nAustin, TX 78723',
			        'date':         u'June 13th, 2015',
			        'distance':     u'5K',
			        'price':        u'Before June 13th: $55\nJune 13th: $60',
			        'hosts':        u'Cooking Light & Health',
			        'sponsors':     u'Cooking Light, Health, Aveeno, Hawaiian Host, Fabletics, Rove, Sartori, Tom\'s, Mueller, Fast Forward Ventures',
			        'charities':    u'Make A Film Foundation, American Diabetes Association',
			        'description':  u'Cooking Light & Health\'s The Fit Foodie 5K Race is the ultimate celebration of food, fitness, and fun. Put those running shoes to work as you navigate your way around a beautiful 5K course.',
			        'short':		u'Cruise to the finish and food away!',
			        'quotes':       [
			                            u'The race was great, but the festivities after were even greater!',
			                            u'It\'s more than a race, it is a fitness and culinary experience.',
			                            u'Where delicious meets fitness.'
			                        ],
			        'website':      u'http://fitfoodierun.com/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3444.8924904757855!2d-97.7073052!3d30.297122100000003!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b5f84578082f%3A0x42afd5562f2f2df1!2s4550+Mueller+Blvd%2C+Austin%2C+TX+78723!5e0!3m2!1sen!2sus!4v1428532415527',
			        'video_url':    u'https://www.youtube.com/embed/cVG9FATjIyk',
			        'fb_url':       u'https://www.facebook.com/pages/The-Fit-Foodie-Race-Series/177814812394419',
			        'landing_img':	u'/static/img/landing/funruns/fitfoodieLanding.jpg',
			        'loc':			4,
			        'imgs':         [
			                            u'/static/img/runTempl/fitfoodie1.jpg',
			                            u'/static/img/runTempl/fitfoodie2.jpg',
			                            u'/static/img/runTempl/fitfoodie3.jpg'
			                        ],
			        'themes':       [
			                            7
			                        ],
			        'challenges':   [
			                            6
			                        ]
			    },
			    {
			        'id':           10,
			        'name':         u'Keep Austin Weird 5K',
			        'city':         u'Austin, Texas',
			        'address':      u'The Long Center Grounds\n701 W Riverside Dr.\nAustin, TX 78704',
			        'date':         u'June 27th, 2015',
			        'distance':     u'5K',
			        'price':        u'VIP: $75\nAdults: $22.50\nKids: $12',
			        'hosts':        u'The Long Center',
			        'sponsors':     u'HotSchedules, AT&T U-verse, Amy\'s Ice Cream, Babyearth, Beatbox Beverages',
			        'charities':    u'Capital Area Food Bank of Texas',
			        'description':  u'Slip into your weirdest costume, slap on your favorite light up running shoes and throw your timer into Lady Bird Lake! This is the slowest 5K on the planet - the wildest, weirdest and most memorable!',
			        'short':		u'Make Austin weird in the slowest race ever!',
			        'quotes':       [
			                            u'So much fun! Drove down from Oklahoma City to attend!',
			                            u'So well done! Loads of fun!',
			                            u'It was our first time attending the fest and we had a blast! I will be back next year for sure!'
			                        ],
			        'website':      u'http://keepaustinweirdfest.com/festival/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3446.1964982159493!2d-97.751079!3d30.259982!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b504ea2084d7%3A0xa8a514235a56453e!2s701+W+Riverside+Dr%2C+Austin%2C+TX+78704!5e0!3m2!1sen!2sus!4v1428532467708',
			        'video_url':    u'https://www.youtube.com/embed/9sL-B1D7v34',
			        'fb_url':       u'https://www.facebook.com/pages/Keep-Austin-Weird-Festival-5K/121126484577639',
			        'landing_img':	u'/static/img/landing/funruns/keepAustinWeirdLanding.jpg',
			        'loc':			4,
			        'imgs':         [
			                            u'/static/img/runTempl/keepAustinWeird1.jpg',
			                            u'/static/img/runTempl/keepAustinWeird2.jpg',
			                            u'/static/img/runTempl/keepAustinWeird3.jpg'
			                        ],
			        'themes':       [
			                            2, 3, 8
			                        ],
			        'challenges':   [
			                            1, 2
			                        ]
			    },
			    {
			        'id':           11,
			        'name':         u'North American Wife Carrying Championship',
			        'city':         u'Newry, Maine',
			        'address':      u'Sunday River Ski Resort\n15 S Ridge Rd.\nNewry, ME 04261',
			        'date':         u'October 10th, 2015',
			        'distance':     u'278yd',
			        'price':        u'N/A',
			        'hosts':        u'Sunday River',
			        'sponsors':     u'BudLight, Bethel Inn Resort',
			        'charities':    u'N/A',
			        'description':  u'Carry your wife to the finish and win her weight in beer! The course at Sunday River is built to international specifications at 278 yards in length, with two dry obstacles and one water obstacle.',
			        'short':		u'Carry your wife and win her weight in beer!',
			        'quotes':       [
			                            u'It was a very cool event! Sunday River does a good job with it!',
			                            u'I\'m wicked strong and she\'s wicked small!',
			                            u'Hardly fair playing field but fun to watch none the less.'
			                        ],
			        'website':      u'http://www.sundayriver.com/events-and-activities/events-calendar/north-american-wife-carrying-championship',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2847.0332106871697!2d-70.856894!3d44.473492!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cb3dd81009e321b%3A0xd2eb7c1aecb4af6e!2sSunday+River+Ski+Resort!5e0!3m2!1sen!2sus!4v1428532505050',
			        'video_url':    u'https://player.vimeo.com/video/112507533',
			        'fb_url':       u'https://www.facebook.com/sundayriver',
			        'landing_img':	u'/static/img/landing/funruns/wifecarryLanding.jpg',
			        'loc':			5,
			        'imgs':         [
			                            u'/static/img/runTempl/wifecarry1.jpg',
			                            u'/static/img/runTempl/wifecarry2.jpg',
			                            u'/static/img/runTempl/wifecarry3.jpg'
			                        ],
			        'themes':       [
			                            4, 5
			                        ],
			        'challenges':   [
			                            0, 3, 5, 7, 11, 12
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
			        'challenges':   [
			                            1, 2
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
			        'challenges':   [
			                            0, 2, 3, 4, 7, 8, 9, 10, 11, 12, 13, 14
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
			        'challenges':   [
			                            1
			                        ]
			    },
			    {
			        'id':           3,
			        'name':         u'Location',
			        'buzzwords':    u'Landmarks, Rivers, Downtown, Parks, Lakes, Views',
			        'description':  u'Whether it is an excuse to travel and exercise, or a good distraction from the aches and pains of running, the location of a race is a great factor in deciding which run works for you!',
			        'short':		u'Enjoy the scenic views while getting in some exercise.',
			        'landing_img':	u'/static/img/landing/themes/location1.jpg',
			        'imgs':         [
			                            u'/static/img/themeTempl/location1.jpg',
			                            u'/static/img/themeTempl/location2.jpg',
			                            u'/static/img/themeTempl/location3.jpg',
			                            u'/static/img/themeTempl/location4.jpg',
			                            u'/static/img/themeTempl/location5.jpg',
			                            u'/static/img/themeTempl/location6.jpg',
			                            u'/static/img/themeTempl/location7.jpg',
			                            u'/static/img/themeTempl/location8.jpg'
			                        ],
			        'challenges':   [
			                            3
			                        ]
			    },
			    {
			        'id':           4,
			        'name':         u'Dirty',
			        'buzzwords':    u'Mud, Color Paint, Wet',
			        'description':  u'Want to run through mud pits, climb walls, and get blasted with paint? Challenge yourself with these get down-and-dirty runs.',
			        'short':		u'Get ready to take a long shower afterwards.',
			        'landing_img':	u'/static/img/landing/themes/dirty1.jpg',
			        'imgs':         [
			                            u'/static/img/themeTempl/dirty1.jpg',
			                            u'/static/img/themeTempl/dirty2.jpg',
			                            u'/static/img/themeTempl/dirty3.jpg',
			                            u'/static/img/themeTempl/dirty4.jpg',
			                            u'/static/img/themeTempl/dirty5.jpg',
			                            u'/static/img/themeTempl/dirty6.jpg',
			                            u'/static/img/themeTempl/dirty7.jpg',
			                            u'/static/img/themeTempl/dirty8.jpg'
			                        ],
			        'challenges':   [
			                            0, 5, 8, 9, 10, 11, 12, 13, 15
			                        ]
			    },
			    {
			        'id':           5,
			        'name':         u'Team',
			        'buzzwords':    u'Group, Partner(s), Family',
			        'description':  u'You don\'t have to run a race by yourself. Instead, put together a team of your friends and take part in one of these races.',
			        'short':		u'Share the fun with a group or that special someone',
			        'landing_img':	u'/static/img/landing/themes/team1.jpg',
			        'imgs':         [
			                            u'/static/img/themeTempl/team1.jpg',
			                            u'/static/img/themeTempl/team2.jpg',
			                            u'/static/img/themeTempl/team3.jpg',
			                            u'/static/img/themeTempl/team4.jpg',
			                            u'/static/img/themeTempl/team5.jpg',
			                            u'/static/img/themeTempl/team6.jpg',
			                            u'/static/img/themeTempl/team7.jpg',
			                            u'/static/img/themeTempl/team8.jpg'
			                        ],
			        'challenges':   [
			                            7, 12
			                        ]
			    },
			    {
			        'id':           6,
			        'name':         u'Drink',
			        'buzzwords':    u'Beer, beer, and more beer',
			        'description':  u'Ever try keeping down a couple of drinks while running long distances? These runs test your endurance and bladder',
			        'short':			u'Hold yourself together while being part ofthese runs.',
			        'landing_img':	u'/static/img/landing/themes/drink1.jpg',
			        'imgs':         [
			                            u'/static/img/themeTempl/drink1.jpg',
			                            u'/static/img/themeTempl/drink2.jpg',
			                            u'/static/img/themeTempl/drink3.jpg',
			                            u'/static/img/themeTempl/drink4.jpg',
			                            u'/static/img/themeTempl/drink5.jpg',
			                            u'/static/img/themeTempl/drink6.jpg',
			                            u'/static/img/themeTempl/drink7.jpg',
			                            u'/static/img/themeTempl/drink8.jpg'
			                        ],
			        'challenges':   [
			                            6, 7
			                        ]
			    },
			    {
			        'id':           7,
			        'name':         u'Food',
			        'buzzwords':    u'Sweet, sour, healthy',
			        'description':  u'Forget bananas and postrace barbecues. In these races, chowing down is part of the competition.',
			        'short':		u'Enjoy a nice meal with these runs.',
			        'landing_img':	u'/static/img/landing/themes/food1.jpg',
			        'imgs':         [
			                            u'/static/img/themeTempl/food1.jpg',
			                            u'/static/img/themeTempl/food2.jpg',
			                            u'/static/img/themeTempl/food3.jpg',
			                            u'/static/img/themeTempl/food4.jpg',
			                            u'/static/img/themeTempl/food5.jpg',
			                            u'/static/img/themeTempl/food6.jpg',
			                            u'/static/img/themeTempl/food7.jpg',
			                            u'/static/img/themeTempl/food8.jpg'
			                        ],
			        'challenges':   [
			                            6, 7
			                        ]
			    },
			    {
			        'id':           8,
			        'name':         u'Music',
			        'buzzwords':    u'Rhythm, Dance, Banger',
			        'description':  u'No need for a pre-workout for these runs. The music will get you pumped and ready to hit the ground running.',
			        'short':		u'Jam out to some tunes during these runs.',
			        'landing_img':	u'/static/img/landing/themes/music1.jpg',
			        'imgs':         [
			                            u'/static/img/themeTempl/music1.jpg',
			                            u'/static/img/themeTempl/music2.jpg',
			                            u'/static/img/themeTempl/music3.jpg',
			                            u'/static/img/themeTempl/music4.jpg',
			                            u'/static/img/themeTempl/music5.jpg',
			                            u'/static/img/themeTempl/music6.jpg',
			                            u'/static/img/themeTempl/music7.jpg',
			                            u'/static/img/themeTempl/music8.jpg'
			                        ],
			        'challenges':   [
			                            1, 5, 15
			                        ]
			    },
			    {
			        'id':           9,
			        'name':         u'Fantasy',
			        'buzzwords':    u'Dreams, Monsters, Supernatural',
			        'description':  u'These runs will make your imagination run wild with their supernatural sights and experiences.',
			        'short':		u'Run through your wildest fantasies.',
			        'landing_img':	u'/static/img/landing/themes/fantasy1.jpg',
			        'imgs':         [
			                            u'/static/img/themeTempl/fantasy1.jpg',
			                            u'/static/img/themeTempl/fantasy2.jpg',
			                            u'/static/img/themeTempl/fantasy3.jpg',
			                            u'/static/img/themeTempl/fantasy4.jpg',
			                            u'/static/img/themeTempl/fantasy5.jpg',
			                            u'/static/img/themeTempl/fantasy6.jpg',
			                            u'/static/img/themeTempl/fantasy7.jpg',
			                            u'/static/img/themeTempl/fantasy8.jpg'
			                        ],
			        'challenges':   [
			                            1, 4, 14
			                        ]
			    }
			]
	return themes

def retrieve_challenges():
	challenges = [
				    {
				        'id':           0,
				        'name':         u'Stepping On Awkward Ground',
				        'difficulty':   60,
				        'flavors':      u'Ice, Inflatable Balls, Mud',
				        'description':  u'Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.',
				        'landing_img':	u'/static/img/landing/challenges/oddGround1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/oddGround1.jpg',
				                            u'/static/img/challengeTempl/oddGround2.jpg',
				                            u'/static/img/challengeTempl/oddGround3.jpg'
				                        ]
				    },
				    {
				        'id':           1,
				        'name':         u'Moving In A Costume',
				        'difficulty':   20,
				        'flavors':      u'Mascots, Nude, Speedos, Costumes',
				        'description':  u'Ideally, running should be done in comfortable shorts and shirt. Instead, some dare to run in costumes - or a lack of costume - in self expression and, oftentimes, silliness.',
				        'landing_img':	u'/static/img/landing/challenges/costume1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/costume1.jpg',
				                            u'/static/img/challengeTempl/costume2.jpg',
				                            u'/static/img/challengeTempl/costume3.jpg'
				                        ]
				    },
				    {
				        'id':           2,
				        'name':         u'Enduring Extreme Temperatures',
				        'difficulty':   80,
				        'flavors':      u'Snow, Ice, Fire, Heat',
				        'description':  u'Take on extreme temps fearlessly with fun runs in less than ideal temperatures. Will the icy winds or intense heat get to you or will you make it to the finish line and prevail?',
				        'landing_img':	u'/static/img/landing/challenges/extremetemp1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/extremetemp1.jpg',
				                            u'/static/img/challengeTempl/extremetemp2.jpg',
				                            u'/static/img/challengeTempl/extremetemp3.jpg'
				                        ]
				    },
				    {
				        'id':           3,
				        'name':         u'Going Over Hills',
				        'difficulty':   30,
				        'flavors':      u'High Elevation, Inclines, Steep Roads',
				        'description':  u'Fight against gravity and prepare to go over steep hills in runs with hilly landscape. Feel those legs burn as you scale those inclines to the very end!',
				        'landing_img':	u'/static/img/landing/challenges/hill1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/hill1.jpg',
				                            u'/static/img/challengeTempl/hill2.jpg',
				                            u'/static/img/challengeTempl/hill3.jpg'
				                        ]
				    },
				    {
				        'id':           4,
				        'name':         u'Getting Chased',
				        'difficulty':   70,
				        'flavors':      u'Pursued, Zombies, Capture The Flag',
				        'description':  u'You don\'t have to outrun your pursuers, you just have to outrun the other people being chased! Don\'t let yourself get caught in hardcore survival runs where it\'s kill... or be killed.',
				        'landing_img':	u'/static/img/landing/challenges/chased1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/chased1.jpg',
				                            u'/static/img/challengeTempl/chased2.jpg',
				                            u'/static/img/challengeTempl/chased3.jpg'
				                        ]
				    },
				    {
				        'id':           5,
				        'name':         u'Getting Covered in Stuff',
				        'difficulty':   10,
				        'flavors':      u'Foam, Bubbles, Mud, Water, Powder',
				        'description':  u'Want to run through a waterfall of bubbles and foam? Or would you rather stay away from the suds and go for the muds!? Either way, this stuff is going to make you feel ',
				        'landing_img':	u'/static/img/landing/challenges/covered1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/covered1.jpg',
				                            u'/static/img/challengeTempl/covered2.jpg',
				                            u'/static/img/challengeTempl/covered3.jpg'
				                        ]
				    },
				    {
				        'id':           6,
				        'name':         u'Consuming',
				        'difficulty':   30,
				        'flavors':      u'Food, Drink, Quick Consumption',
				        'description':  u'',
				        'landing_img':	u'/static/img/landing/challenges/consuming1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/consuming1.jpg',
				                            u'/static/img/challengeTempl/consuming2.jpg',
				                            u'/static/img/challengeTempl/consuming3.jpg'
				                        ]
				    },
				    {
				        'id':           7,
				        'name':         u'Carrying an Object',
				        'difficulty':   70,
				        'flavors':      u'Sandbags, Other People, Logs',
				        'description':  u'',
				        'landing_img':	u'/static/img/landing/challenges/carry1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/carry1.jpg',
				                            u'/static/img/challengeTempl/carry2.jpg',
				                            u'/static/img/challengeTempl/carry3.jpg'
				                        ]
				    },
				    {
				        'id':           8,
				        'name':         u'Scaling a Wall',
				        'difficulty':   70,
				        'flavors':      u'Wooden Walls, Rope Walls, Chains, Rope Ladders',
				        'description':  u'',
				        'landing_img':	u'/static/img/landing/challenges/scaling1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/scaling1.jpg',
				                            u'/static/img/challengeTempl/scaling2.jpg',
				                            u'/static/img/challengeTempl/scaling3.jpg'
				                        ]
				    },
				    {
				        'id':           9,
				        'name':         u'Sliding Down Slopes',
				        'difficulty':   10,
				        'flavors':      u'Large Inflatable Slides, Mud Slides, Foam Slides',
				        'description':  u'',
				        'landing_img':	u'/static/img/landing/challenges/sliding1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/sliding1.jpg',
				                            u'/static/img/challengeTempl/sliding2.jpg',
				                            u'/static/img/challengeTempl/sliding3.jpg'
				                        ]
				    },
				    {
				        'id':           10,
				        'name':         u'Crawling Underneath Obstacles',
				        'difficulty':   40,
				        'flavors':      u'Barbed Wire, Tunnels, Electrical Wiring',
				        'description':  u'',
				        'landing_img':	u'/static/img/landing/challenges/crawling1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/crawling1.jpg',
				                            u'/static/img/challengeTempl/crawling2.jpg',
				                            u'/static/img/challengeTempl/crawling3.jpg'
				                        ]
				    },
				    {
				        'id':           11,
				        'name':         u'Being Suspended',
				        'difficulty':   60,
				        'flavors':      u'Monkey Bars, Rope Swings, Metal Swings',
				        'description':  u'',
				        'landing_img':	u'/static/img/landing/challenges/suspended1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/suspended1.jpg',
				                            u'/static/img/challengeTempl/suspended2.jpg',
				                            u'/static/img/challengeTempl/suspended3.jpg'
				                        ]
				    },
				    {
				        'id':           12,
				        'name':         u'Staying Balanced',
				        'difficulty':   70,
				        'flavors':      u'Balance beams, wooden beams, inflated walkways',
				        'description':  u'',
				        'landing_img':	u'/static/img/landing/challenges/balance1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/balance1.jpg',
				                            u'/static/img/challengeTempl/balance2.jpg',
				                            u'/static/img/challengeTempl/balance3.jpg'
				                        ]
				    },
				    {
				        'id':           13,
				        'name':         u'Getting Hit by Objects',
				        'difficulty':   80,
				        'flavors':      u'Inflated Bulldozer Balls, Thrown Items',
				        'description':  u'',
				        'landing_img':	u'/static/img/landing/challenges/gettinghit1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/gettinghit1.jpg',
				                            u'/static/img/challengeTempl/gettinghit2.jpg',
				                            u'/static/img/challengeTempl/gettinghit3.jpg'
				                        ]
				    },
				    {
				        'id':           14,
				        'name':         u'Performing Urban Parkour',
				        'difficulty':   60,
				        'flavors':      u'Buildings, Construction Areas, Urban Areas',
				        'description':  u'',
				        'landing_img':	u'/static/img/landing/challenges/parkour1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/parkour1.jpg',
				                            u'/static/img/challengeTempl/parkour2.jpg',
				                            u'/static/img/challengeTempl/parkour3.jpg'
				                        ]
				    },
				    {
				        'id':           15,
				        'name':         u'Running with Limited Visibility',
				        'difficulty':   40,
				        'flavors':      u'Darkness, Face Powder, Fog',
				        'description':  u'',
				        'landing_img':	u'/static/img/landing/challenges/visibility1.jpg',
				        'imgs':         [
				                            u'/static/img/challengeTempl/visibility1.jpg',
				                            u'/static/img/challengeTempl/visibility2.jpg',
				                            u'/static/img/challengeTempl/visibility3.jpg'
				                        ]
				    }
				]
	return challenges

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
					},
					{
					    'id':                   3,
					    'name':             	u'Fairburn, Georgia',
					    'nickname':				u'A City Among the Hills',
					    'winter_avgTemp':       44,
					    'spring_avgTemp':       61,
					    'summer_avgTemp':       77,
					    'fall_avgTemp':         63,
					    'winter_avgHumidity':   65,
					    'spring_avgHumidity':   78,
					    'summer_avgHumidity':   83,
					    'fall_avgHumidity':     78,
					    'altitude':             u'1,027ft',
					    'annual_rainfall':      u'52.06in',
					    'landmarks':            u'Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center',
					    'website_url':			u'http://www.fairburn.com/',
					    'description':			u'Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.',
					    'landing_img':			u'/static/img/landing/locations/fairburnGALanding.jpg',
					    'img':					u'/static/img/locationTempl/fairburn1.jpg'	
					},
					{
					    'id':                   4,
					    'name':             	u'Austin, Texas',
					    'nickname':				u'Live Music Capital of the World',
					    'winter_avgTemp':       51,
					    'spring_avgTemp':       67,
					    'summer_avgTemp':       83,
					    'fall_avgTemp':         69,
					    'winter_avgHumidity':   77,
					    'spring_avgHumidity':   86,
					    'summer_avgHumidity':   76,
					    'fall_avgHumidity':     70,
					    'altitude':             u'489ft',
					    'annual_rainfall':      u'34.53in',
					    'landmarks':            u'Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo',
					    'website_url':			u'http://www.austintexas.org/',
					    'description':			u'Austin is the capital of Texas.  It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.',
					    'landing_img':			u'/static/img/landing/locations/austinTXLanding.jpg',
					    'img':					u'/static/img/locationTempl/austin1.jpg'	
					},
					{
					    'id':                   5,
					    'name':             	u'Newry, Maine',
					    'nickname':				u'Sunday River Plantation',
					    'winter_avgTemp':       16,
					    'spring_avgTemp':       38,
					    'summer_avgTemp':       62,
					    'fall_avgTemp':         43,
					    'winter_avgHumidity':   84,
					    'spring_avgHumidity':   74,
					    'summer_avgHumidity':   82,
					    'fall_avgHumidity':     80,
					    'altitude':             u'712ft',
					    'annual_rainfall':      u'42.13in',
					    'landmarks':            u'Artists\' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park',
					    'website_url':			u'http://www.newrymaine.org/',
					    'description':			u'Newry is a town in Oxfor County, Maine.  It is the home of Sunday River Ski Resort and has a proportionately large population during winter.',
					    'landing_img':			u'/static/img/landing/locations/newryMELanding.jpg',
					    'img':					u'/static/img/locationTempl/newry1.jpg'	
					},
					{
					    'id':                   6,
					    'name':             	u'San Francisco, California',
					    'nickname':				u'The Golden Gate City',
					    'winter_avgTemp':       58,
					    'spring_avgTemp':       63,
					    'summer_avgTemp':       66,
					    'fall_avgTemp':         68,
					    'winter_avgHumidity':   77,
					    'spring_avgHumidity':   71,
					    'summer_avgHumidity':   79,
					    'fall_avgHumidity':     73,
					    'altitude':             u'52ft',
					    'annual_rainfall':      u'23.64in',
					    'landmarks':            u'Chinatown, Golden Gate Bridge, Golden Gate Park',
					    'website_url':			u'http://www.sanfrancisco.travel/',
					    'description':			u'San Francisco is home to a little bit of everything. Whether you\'re a first time visitor or a long-time local. This is the place to find out about all things San Francisco.',
					    'landing_img':			u'/static/img/landing/locations/sanfranciscoCALanding.jpg',
					    'img':					u'/static/img/locationTempl/sanfrancisco1.jpg'	
					},
					{
					    'id':                   7,
					    'name':             	u'Riverhead, New York',
					    'nickname':				u'Strong Island',
					    'winter_avgTemp':       41,
					    'spring_avgTemp':       59,
					    'summer_avgTemp':       81,
					    'fall_avgTemp':         64,
					    'winter_avgHumidity':   78,
					    'spring_avgHumidity':   84,
					    'summer_avgHumidity':   90,
					    'fall_avgHumidity':     82,
					    'altitude':             u'13ft',
					    'annual_rainfall':      u'47.8in',
					    'landmarks':            u'Long Island Aquarium and Exhibition Center, Splish Splash',
					    'website_url':			u'http://www.townofriverheadny.gov/',
					    'description':			u'Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.',
					    'landing_img':			u'/static/img/landing/locations/riverheadNYLanding.jpg',
					    'img':					u'/static/img/locationTempl/riverhead1.jpg'	
					},
					{
					    'id':                   8,
					    'name':             	u'Memphis, Tennessee',
					    'nickname':				u'Home of the Blues',
					    'winter_avgTemp':       52,
					    'spring_avgTemp':       73,
					    'summer_avgTemp':       91,
					    'fall_avgTemp':         74,
					    'winter_avgHumidity':   67,
					    'spring_avgHumidity':   63,
					    'summer_avgHumidity':   68,
					    'fall_avgHumidity':     68,
					    'altitude':             u'337ft',
					    'annual_rainfall':      u'53.68in',
					    'landmarks':            u'Graceland, Memphis Zoo, Stax Museum of American Soul Music',
					    'website_url':			u'http://www.memphistn.gov/',
					    'description':			u'Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.',
					    'landing_img':			u'/static/img/landing/locations/memphisTNLanding.jpg',
					    'img':					u'/static/img/locationTempl/memphis1.jpg'	
					},
					{
					    'id':                   9,
					    'name':             	u'Puyallup, Washington',
					    'nickname':				u'A Tree City USA',
					    'winter_avgTemp':       48,
					    'spring_avgTemp':       61,
					    'summer_avgTemp':       76,
					    'fall_avgTemp':         62,
					    'winter_avgHumidity':   81,
					    'spring_avgHumidity':   84,
					    'summer_avgHumidity':   75,
					    'fall_avgHumidity':     73,
					    'altitude':             u'46ft',
					    'annual_rainfall':      u'40.43in',
					    'landmarks':            u'U.S District Court, Historic Preservation, City of Tacoma',
					    'website_url':			u'http://www.cityofpuyallup.org/',
					    'description':			u'Named after the Puyallup Tribe of Native Americans, Puyallup means \'the generous people\'. Puyallup was first recognized as a Tree City USA in 2014.',
					    'landing_img':			u'/static/img/landing/locations/puyallupWALanding.jpg',
					    'img':					u'/static/img/locationTempl/puyallup1.jpg'	
					}
				]
	return locations
