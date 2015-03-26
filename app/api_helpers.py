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
              		"runs_url": "/runs",
                	"themes_url": "/themes",
                	"challenges_url": "/challenges"
            	}
	return root_urls

def retrieve_runs():
	runs = 	[
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
			        'quotes':       [
			                            u'Seriously, best race I\'ve done. So much fun. Thanks for coming to Dallas! Hope to see you here in the future!',
			                            u'Had a great time participating in the WIPEOUTRUN!',
			                            u'Such a blast!! Let\'s do it again next year!!'
			                        ],
			        'website':      u'http://wipeoutrun.com/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12352.756020060675!2d-76.621608!3d39.283964!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x2428d93f0397c539!2sOriole+Park+at+Camden+Yards!5e0!3m2!1sen!2sus!4v1427230426235',
			        'video_url':    u'https://www.youtube.com/embed/1uOII9K5c0c',
			        'fb_url':       u'https://www.facebook.com/WIPEOUTRUN',
			        'imgs':         [
			                            u'/static/img/runTempl/wipeout1.jpg',
			                            u'/static/img/runTempl/wipeout2.jpg',
			                            u'/static/img/runTempl/wipeout3.jpg'
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
			        'sponsors':     u'Ovaltine, Renaissance HOtels, Dannon, Walmart, McDonalds, The Home Depot',
			        'charities':    u'A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects',
			        'description':  u'The movie producers must have been runners, because the distance between the former Higbee\'s Department Store and the A Christmas Story House & Museum is about 5K. Ralphie’s dad, The Old Man must have used the 1938 Oldsmobile to track the distance, since there was no GPS in the 1940\'s. To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.',
			        'quotes':       [
			                            u'I was so excited to get my finisher medal and enjoy a well deserved Christmas Ale.',
			                            u'Despite the crowds, it was so much fun seeing everyone in costume celebrating the movie and our city.',
			                            u'All in all Pepper gives this fun run an A+!'
			                        ],
			        'website':      u'http://achristmasstoryrun.com/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2988.260792402495!2d-81.694473!3d41.498622999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830f07e4562d241%3A0x94e8396bc5227630!2sRenaissance+Cleveland+Hotel!5e0!3m2!1sen!2sus!4v1427230544965',
			        'video_url':    u'https://www.youtube.com/embed/uPiN-_p7q2k',
			        'fb_url':       u'https://www.facebook.com/AChristmasStoryRun',
			        'imgs':         [
			                            u'/static/img/runTempl/christmasstory1.jpg',
			                            u'/static/img/runTempl/christmasstory2.jpg',
			                            u'/static/img/runTempl/christmasstory3.jpg'
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
			        'quotes':       [
			                            u'This will be the sixth year my wife and I have run the Dallas Turkey Trot. We began running this race the first year we got married and have kept it a tradition every year. Love this race!',
			                            u'This event is by far the best family friendly event that takes place in Dallas each year!',
			                            u'I had a blast running the Turkey Trot this year. Even though it\'s my first time doing it, I will definitely make it a tradition every year'
			                        ],
			        'website':      u'http://thetrot.org/',
			        'map_url':      u'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13418.251274220785!2d-96.79709!3d32.777333!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc83854fdfdad6162!2sDallas+City+Hall!5e0!3m2!1sen!2sus!4v1427228610474',
			        'video_url':    u'https://www.youtube.com/embed/qdnzjhWgCOg',
			        'fb_url':       u'https://www.facebook.com/DallasYMCATrot',
			        'imgs':         [
			                            u'/static/img/runTempl/dallasturkey1.jpg',
			                            u'/static/img/runTempl/dallasturkey2.jpg',
			                            u'/static/img/runTempl/dallasturkey3.jpg'
			                        ]
			    }
			]
	return runs

def retireve_themes():
	themes = [
			    {
			        'id':           0,
			        'name':         u'Holiday',
			        'buzzwords':    u'Christmas, Thanksgiving, Easter, Valentine\'s Day, St. Patrick\'s Day, New Year\'s, Halloween, 4th of July',
			        'description':  u'Instead of sitting around the fire, talking of presents and Santa, why not go for a run with the family? Holiday runs are a great way to get out and celebrate during the festivities! Often featuring thematic competitions and costumes, they\re a sure way of making any holiday a memorable one.',
			        'imgs':         [
			                            u'/static/img/themeTempl/holiday1.jpg',
			                            u'/static/img/themeTempl/holiday2.jpg',
			                            u'/static/img/themeTempl/holiday3.jpg'
			                        ]
			    },
			    {
			        'id':           1,
			        'name':         u'Intense',
			        'buzzwords':    u'Training, Diet, Hardcore, Recovery, Cutthroat',
			        'description':  u'More interested in proving how much you can take than how much fun you\'ll actually have? Intense runs are exactly what you need - a good dose of body-numbing, soul-crushing exercise to show your stuff. See if you can survive the brutal difficulty of these events.',
			        'imgs':         [
			                            u'/static/img/themeTempl/intense1.jpg',
			                            u'/static/img/themeTempl/intense2.jpg',
			                            u'/static/img/themeTempl/intense3.jpg'
			                        ]
			    },
			    {
			        'id':           2,
			        'name':         u'Costume',
			        'buzzwords':    u'Silly, Uncomfortable, Dress-Up, Make-Believe',
			        'description':  u'Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!',
			        'imgs':         [
			                            u'/static/img/themeTempl/costume1.jpg',
			                            u'/static/img/themeTempl/costume2.jpg',
			                            u'/static/img/themeTempl/costume3.jpg'
			                        ]
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
				        'imgs':         [
				                            u'/static/img/challengeTempl/cold1.jpg',
				                            u'/static/img/challengeTempl/cold2.jpg',
				                            u'/static/img/challengeTempl/cold3.jpg'
				                        ]
				    },
				    {
				        'id':           1,
				        'name':         u'Running In A Costume',
				        'difficulty':   40,
				        'flavors':      u'Mascots, Nude, Speedos, Costumes',
				        'description':  u'Ideally, running should be done in comfortable shorts and shirt. Instead, some dare to run in costumes - or a lack of costume - in self expression and, oftentimes, silliness.',
				        'imgs':         [
				                            u'/static/img/challengeTempl/costume1.jpg',
				                            u'/static/img/challengeTempl/costume2.jpg',
				                            u'/static/img/challengeTempl/costume3.jpg'
				                        ]
				    },
				    {
				        'id':           2,
				        'name':         u'Running In Cold Weather',
				        'difficulty':   80,
				        'flavors':      u'Snow, Ice, Freezing Temperatures',
				        'description':  u'Take on the cold fearlessly with fun runs in less than ideal temperatures. Will the icy winds get to you or will you make it to the finish line and prevail?',
				        'imgs':         [
				                            u'/static/img/challengeTempl/oddGround1.jpg',
				                            u'/static/img/challengeTempl/oddGround2.jpg',
				                            u'/static/img/challengeTempl/oddGround3.jpg'
				                        ]
				    }
				]
	return challenges