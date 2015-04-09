from models.models import db, FunRun, Theme, Challenge, Location

def populateDatabase():
    db.reflect()
    db.drop_all()
    db.session.commit()

    db.create_all()
    db.session.commit()

    # Create the funruns
    frun1 = FunRun(id = 1, name = 'Wipeout Run', \
        address = 'Camden Yards\n333 W Camden St.\nBaltimore, MD 21201', \
        date = 'June 6th, 2015', \
        distance = '5K', \
        price = 'March 6th - April 9th: $56\nApril 10th - May 7th: $61\nMay 8th - May 21st: $66\nMay 22nd - June 5th: $71\nJune 6th: $81', \
        hosts = 'Ridiculous Obstacle Challenge Race LLC, Endemol USA Inc.', \
        sponsors = 'VaVi Sport & Social', \
        charities = 'N/A', \
        description = 'Crash, smash, and splash your way through a 5k course with larger-than-life obstacles and elements inspired by the hit TV show Wipeout! Take on the infamous Big Balls, Sweeper, Wrecking Balls, and Happy Endings! Hilarious thrills and magnificent spills await!', \
        short = 'Try out the obstacles from the hit TV show "Wipeout"!', \
        quote_1 = 'Seriously, best race I\'ve done. So much fun. Thanks for coming to Dallas! Hope to see you here in the future!', \
        quote_2 = 'Had a great time participating in the WIPEOUTRUN!', \
        quote_3 = 'Such a blast! Let\'s do it again next year!', \
        website = 'http://wipeoutrun.com/', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d12352.756020060675!2d-76.621608!3d39.283964!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0x2428d93f0397c539!2sOriole+Park+at+Camden+Yards!5e0!3m2!1sen!2sus!4v1427230426235', \
        video_url = 'https://www.youtube.com/embed/1uOII9K5c0c', \
        fb_url = 'https://www.facebook.com/WIPEOUTRUN', \
        landing_img = '/static/img/landing/funruns/wipeoutLanding.jpg', \
        location_id = 1, \
        img_1 = '/static/img/runTempl/wipeout1.jpg', \
        img_2 = '/static/img/runTempl/wipeout2.jpg', \
        img_3 = '/static/img/runTempl/wipeout3.jpg')

    frun2 = FunRun(id = 2, name = 'A Christmas Story Run', \
        address = 'Cleveland Public Square\nCleveland, OH 44113', \
        date = 'December 5th, 2015', \
        distance = '5K, 10K', \
        price = 'Before September 30th: $45\nOctober 1st - December 5th: $55', \
        hosts = 'A Christmas Story House & Museum', \
        sponsors = 'Ovaltine, Renaissance Hotels, Dannon, Walmart, McDonalds, The Home Depot', \
        charities = 'A Christmas Story House Foundation, Inc. Cleveland Home Restoration Projects', \
        description = 'The movie producers must have been runners, because the distance between the former Higbee\'s Department Store and the A Christmas Story House and Museum is about 5K.  Ralphie\'s dad, The Old Man must have used the 1938 Oldsmobile to track the distance, since there was no GPS in the 1940\'s.  To accommodate both movie locations that made this race famous, the distance for the races are approximate, and perhaps a little shorter or longer.', \
        short = 'Experience the classic movie "A Christmas Story" in person.', \
        quote_1 = 'I was so excited to get my finisher medal and enjoy a well deserved Christmas Ale.', \
        quote_2 = 'Despite the crowds, it was so much fun seeing everyone in costume celebrating the movie and our city.', \
        quote_3 = 'All in all Pepper gives this fun run an A+!', \
        website = 'http://achristmasstoryrun.com/', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2988.260792402495!2d-81.694473!3d41.498622999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8830f07e4562d241%3A0x94e8396bc5227630!2sRenaissance+Cleveland+Hotel!5e0!3m2!1sen!2sus!4v1427230544965', \
        video_url = 'https://www.youtube.com/embed/uPiN-_p7q2k', \
        fb_url = 'https://www.facebook.com/AChristmasStoryRun', \
        landing_img = '/static/img/landing/funruns/christmasStoryRunLanding.jpg', \
        location_id = 3, \
        img_1 = '/static/img/runTempl/christmasstory1.jpg', \
        img_2 = '/static/img/runTempl/christmasstory2.jpg', \
        img_3 = '/static/img/runTempl/christmasstory3.jpg')

    frun3 = FunRun(id = 3, name = 'Dallas Turkey Trot', \
        address = 'City Hall Plaza\n500 Marilla St.\nDallas, TX 75201', \
        date = 'November 26th, 2015', \
        distance = '5K, 8mi', \
        price = 'Before September 30th: $30\nSeptember 31st - November 25th: $35\nNovember 26th: $45', \
        hosts = 'YMCA, Capital One Bank', \
        sponsors = 'The Dallas Morning News, Brand Keepers, City of Dallas, Kroger, Nike, The Dallas Cowboys', \
        charities = 'The Y Community Programs', \
        description = 'The Dallas Turkey Trot really proves that everything\'s bigger in Texas. One of the largest multi-event races in the country, this trot attracts elite runners and regular ol\' birds alike. In fact, in 2011, it set a world record for the largest gathering of people dressed as turkeys.', \
        short = 'Run in the largest Thanksgiving Day event of its kind.', \
        quote_1 = 'This will be the sixth year my wife and I have run the Dallas Turkey Trot. We began running this race the first year we got married and have kept it a tradition every year. Love this race!', \
        quote_2 = 'This event is by far the best family friendly event that takes place in Dallas each year!', \
        quote_3 = 'I had a blast running the Turkey Trot this year. Even though it\'s my first time doing it, I will definitely make it a tradition every year', \
        website = 'http://thetrot.org/', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d13418.251274220785!2d-96.79709!3d32.777333!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x0%3A0xc83854fdfdad6162!2sDallas+City+Hall!5e0!3m2!1sen!2sus!4v1427228610474', \
        video_url = 'https://www.youtube.com/embed/qdnzjhWgCOg', \
        fb_url = 'https://www.facebook.com/DallasYMCATrot', \
        landing_img = '/static/img/landing/funruns/dallasTurkeyTrotLanding.jpg', \
        location_id = 2, \
        img_1 = '/static/img/runTempl/dallasturkey1.jpg', \
        img_2 = '/static/img/runTempl/dallasturkey2.jpg', \
        img_3 = '/static/img/runTempl/dallasturkey3.jpg')

    frun4 = FunRun(id = 4, name = 'Bay To Breakers', \
        address = 'Main St & Howard St\nSan Francisco, CA 94105', \
        date = 'May 17th, 2015', \
        distance = '12K', \
        price = 'Adult: $59\nChild: $29.50\nVIP: $139\nGroup/Centipede: $54', \
        hosts = 'Zappos.com', \
        sponsors = 'Under Armour, MapMyRun, Geico, Hyatt Regency, TomTom, Kron4, Kettle Brand, Big 5 Sporting Goods, Hangzhou, Mio', \
        charities = 'Mo\'MAGIC, United Way of the Bay Area, National Kidney Foundation', \
        description = 'The Zappos.com Bay to Breakers 12K race runs west through the city and finishes at the Great Highway along the Pacific Coasts Ocean Beach. Participants run up the iconic Hayes Street Hill, along the Panhandle and through Golden Gate Park, while the city of San Francisco cheers them on.', \
        short = 'Explore SF from the bay to the Ocean Beach breakers.', \
        quote_1 = 'Bay to Breakers is a direct route to the city\'s heart and soul.', \
        quote_2 = 'This 12k seriously looks like a party!', \
        quote_3 = 'This is an amazing experience that will last forever. It is not only a race, but an incredible party throughout the streets of San Francisco.', \
        website = 'http://zapposbaytobreakers.com/', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3152.984846292559!2d-122.39335585211597!3d37.79039490045594!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x80858064dca37cb7%3A0x3509f87b15b8eae5!2s219+Howard+St%2C+San+Francisco%2C+CA+94105!5e0!3m2!1sen!2sus!4v1428532134914', \
        video_url = 'https://www.youtube.com/embed/NVEVGSEJmOc', \
        fb_url = 'https://www.facebook.com/zapposbaytobreakers', \
        landing_img = '/static/img/landing/funruns/baytobreakersLanding.jpg', \
        location_id = 7, \
        img_1 = '/static/img/runTempl/baytobreakers1.jpg', \
        img_2 = '/static/img/runTempl/baytobreakers2.jpg', \
        img_3 = '/static/img/runTempl/baytobreakers3.jpg')

    frun5 = FunRun(id = 5, name = 'Zombie Run', \
        address = '3186 DPH 4-H Camp\nSound Avenue\nRiverhead, NY 11901', \
        date = 'May 10th, 2015', \
        distance = '5K, 15K', \
        price = '5K Prices\nBefore February 6th: $55\nFebruary 7th - February 27th: $65\nFebruary 28th - March 27th: $75\nMarch 28th - April 17th: $85\nApril 18th - May 1st: $95\n15K Prices\nBefore February 6th: $75\nFebruary 7th - February 27th: $85\nFebruary 28th - March 27th: $95\nMarch 28th - April 17th: $105\nApril 18th - May 1st: $155\nZombie Price\nBefore February 6th: $20\nFebruary 7th - February 27th: $25\nFebruary 28th - March 27th: $30\nMarch 28th - April 17th: $35\nApril 18th - May 1st: $40', \
        hosts = 'Great Vision Productions LLC', \
        sponsors = 'WholeSale Halloween Costumes', \
        charities = 'Local Charities', \
        description = 'Join us at ZOMBIE RACE! A 5k & 15k run infested with zombies. From the moment the humans leave the start line, theyll be running, crawling, and fleeing in horror from the hordes of undead whose only mission is to devour them alive! Don\'t let the zombies pull your flags!', \
        short = 'Escape the zombies and get to the finish line!', \
        quote_1 = 'They don\'t like fast food', \
        quote_2 = 'Run like zombies are chasing you!', \
        quote_3 = 'This is one of the funnest events I\'ve ever attended!', \
        website = 'http://www.zombierace.co/index.php', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d48208.84256933457!2d-72.7160401!3d40.9584252!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x89e861d37b7288b9%3A0x67dff709a1d00494!2sNassau+County+4H+Camp!5e0!3m2!1sen!2sus!4v1428532216187', \
        video_url = 'https://www.youtube.com/embed/yhrC2CO9gKM', \
        fb_url = 'https://www.facebook.com/zombieracellc', \
        landing_img = '/static/img/landing/funruns/zombierunLanding.jpg', \
        location_id = 8, \
        img_1 = '/static/img/runTempl/zombierun1.jpg', \
        img_2 = '/static/img/runTempl/zombierun2.jpg', \
        img_3 = '/static/img/runTempl/zombierun3.jpg')

    frun6 = FunRun(id = 6, name = 'Blacklight Run', \
        address = 'Memphis International Raceway\n5500 Victory Ln\nMillington, TN 38053', \
        date = 'May 9th, 2015', \
        distance = '5K', \
        price = 'Standard Registration\nBefore April 8th: $20\nApril 8th - May 9th: $40\nVIP Registration\nBefore April 8th: $45\nApril 8th - May 9th: $75', \
        hosts = 'Blacklight Run Corporate', \
        sponsors = 'Local Sponsors', \
        charities = 'Children\'s Hospital', \
        description = 'Blacklight Run is a unique night 5K fun run focused less on speed and more on UV Neon Glowing fun with friends and family. Glowing participants come from all different ages, shapes, sizes, and speeds; every participant will get Glowed and will have the time of their life!', \
        short = 'Get going and get glowing with this neon powder run!', \
        quote_1 = 'Survived another 5k! Finished the Blacklight Run - I love fun runs because there\'s less pressure and the obstacles make the race that much more challenging!', \
        quote_2 = 'I loved tonight\'s run at Qualcomm stadium in San Diego! California knows how to party! Can\'t wait to have you guys here again and do it again!', \
        quote_3 = 'This run leaves runners looking like they fell into a Ghost Buster\'s movie (minus the slime).', \
        website = 'http://www.blacklightrun.com/', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3256.9248763636133!2d-89.9476!3d35.282993999999995!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x887f7ec1c0a48aa5%3A0x7ef6ea23d0ad044a!2sMemphis+International+Raceway!5e0!3m2!1sen!2sus!4v1428532262614', \
        video_url = 'https://www.youtube.com/embed/TgMgEtXjSUk', \
        fb_url = 'https://www.facebook.com/BlacklightRun', \
        landing_img = '/static/img/landing/funruns/blacklightrunLanding.jpg', \
        location_id = 9, \
        img_1 = '/static/img/runTempl/blacklight1.jpg', \
        img_2 = '/static/img/runTempl/blacklight2.jpg', \
        img_3 = '/static/img/runTempl/blacklight3.jpg')

    frun7 = FunRun(id = 7, name = 'Electric Run', \
        address = 'Washington State Fair Events Center\n110 9th Avenue\nPuyallup, WA 98371', \
        date = 'May 23rd, 2015', \
        distance = '5K', \
        price = 'Before April 15th: $45\nApril 16th - May 1st: $50', \
        hosts = 'Washington State Fair Events Center', \
        sponsors = 'WholeSale Halloween Costumes', \
        charities = 'Mary Bridge Children\'s Foundation', \
        description = 'Electric Run is the ultimate nighttime 5k run/walk adventure, where the participants are an integrated part of the show. Featuring immersive "Lands" of light and sound that transport the participant into an electric wonderland.', \
        short = 'Become part of the electric run in this nighttime adventure.', \
        quote_1 = 'You\'ve GOT to bring The Electric Run back to ATLANTA!', \
        quote_2 = 'I loved the event last year!', \
        quote_3 = 'It was a blast! Can\'t wait for this year!', \
        website = 'http://electricrun.com/seatac', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d21692.65452180003!2d-122.3073378!3d47.1856237!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x5490fc035e7af37d%3A0x5fb822881e1b0c46!2sWashington+State+Fair!5e0!3m2!1sen!2sus!4v1428532299643', \
        video_url = 'https://www.youtube.com/embed/R0uhmZI1yy4', \
        fb_url = 'https://www.facebook.com/electricrun', \
        landing_img = '/static/img/landing/funruns/electricrunLanding.jpg', \
        location_id = 10, \
        img_1 = '/static/img/runTempl/electricrun1.jpg', \
        img_2 = '/static/img/runTempl/electricrun2.jpg', \
        img_3 = '/static/img/runTempl/electricrun3.jpg')

    frun8 = FunRun(id = 8, name = 'Brew Mile', \
        address = 'Fair Park Dallas\n1300 Robert B Cullum Boulevard\nDallas, TX 78210', \
        date = 'May 1st, 2015', \
        distance = '5K', \
        price = 'February 1st - March 12th: $55\nMarch 13th - April 9th: $65\nApril 10th - April 30th: $75\nMay 1st: $80', \
        hosts = 'Blacklight Run Corporate', \
        sponsors = 'Upslope Brewing Co, TwinPeaks Brewing Co, Nine Band Brewing Co, Pedernales Brewing Co, Saint Arnold Brewing Co', \
        charities = 'Local Breweries, Local Food, Local Music', \
        description = 'The Brew Mile is your chance to combine your love of running with the finest beverage on the face of this good green earth  BEER. Finally an event that tests your liver as much as it tests your lungs, and is followed by one of the best parties of the year!', \
        short = 'Take on a mile while chugging beer!', \
        quote_1 = 'Super excited for us to do this run.', \
        quote_2 = 'Drinking a beer after a run is freaking awesome.', \
        quote_3 = 'I HAVE NEVER BEEN SO EXCITED TO RUN A MILE.', \
        website = 'http://brewmile.com/', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3354.4074902321736!2d-96.76173600000001!3d32.781453!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x864e9897a14862d7%3A0x64277dc82ee9144!2sFair+Park!5e0!3m2!1sen!2sus!4v1428532340130', \
        video_url = 'https://www.youtube.com/embed/cXrafhIBdlI', \
        fb_url = 'https://www.facebook.com/brewmileseries', \
        landing_img = '/static/img/landing/funruns/brewrunLanding.jpg', \
        location_id = 2, \
        img_1 = '/static/img/runTempl/brewmile1.jpg', \
        img_2 = '/static/img/runTempl/brewmile2.jpg', \
        img_3 = '/static/img/runTempl/brewmile3.jpg')

    frun9 = FunRun(id = 9, name = 'Tough Mudder', \
        address = 'Bouckaert Farm\n10045 Cedar Grove\nFairburn, GA 30213', \
        date = 'May 2nd, 2015', \
        distance = '19K', \
        price = 'Before May 2nd: $185\nMay 2nd: $185', \
        hosts = 'Tough Mudder', \
        sponsors = 'Toyo Tires, Cellucor, Shock-Top, MET-Rx, Oberto, Radisson, Wheaties, Under Armour', \
        charities = 'Wounded Warrior Project, U.S. Army', \
        description = 'Tough Mudder is a team-oriented obstacle course designed to test physical strength and mental grit. It puts camaraderie over finisher rankings and is not a timed race but a team challenge that allows participants to experience exhilarating, yet safe, world-class obstacles they won\'t find anywhere else', \
        short = 'Get through 12 miles of military-style obstacles!', \
        quote_1 = 'The teamwork and camaraderie out there was amazing.', \
        quote_2 = 'The idea of Tough Mudder is not to win... but to have a story to tell.', \
        quote_3 = 'Tough Mudder is a culture and community of taking on challenges and supporting each other.', \
        website = 'https://toughmudder.com/', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3322.038929257956!2d-84.7159338!3d33.6302326!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x88f4d91a281b01bf%3A0x5e4b7c6398a7c91e!2s10045+Cedar+Grove+Rd%2C+Fairburn%2C+GA+30213!5e0!3m2!1sen!2sus!4v1428532369676', \
        video_url = 'https://www.youtube.com/embed/Jim-ksScOoc', \
        fb_url = 'https://www.facebook.com/toughmudder', \
        landing_img = '/static/img/landing/funruns/toughmudderLanding.jpg', \
        location_id = 4, \
        img_1 = '/static/img/runTempl/toughmudder1.jpg', \
        img_2 = '/static/img/runTempl/toughmudder2.jpg', \
        img_3 = '/static/img/runTempl/toughmudder3.jpg')

    frun10 = FunRun(id = 10, name = 'Fit Foodie 5K', \
        address = 'Browning Hangar\n4550 Mueller Blvd.\nAustin, TX 78723', \
        date = 'June 13th, 2015', \
        distance = '5K', \
        price = 'Before June 13th: $55\nJune 13th: $60', \
        hosts = 'Cooking Light & Health', \
        sponsors = 'Cooking Light, Health, Aveeno, Hawaiian Host, Fabletics, Rove, Sartori, Tom\'s, Mueller, Fast Forward Ventures', \
        charities = 'Make A Film Foundation, American Diabetes Association', \
        description = 'Cooking Light & Health\'s The Fit Foodie 5K Race is the ultimate celebration of food, fitness, and fun. Put those running shoes to work as you navigate your way around a beautiful 5K course.', \
        short = 'Cruise to the finish and food away!', \
        quote_1 = 'The race was great, but the festivities after were even greater!', \
        quote_2 = 'It\'s more than a race, it is a fitness and culinary experience.', \
        quote_3 = 'Where delicious meets fitness.', \
        website = 'http://fitfoodierun.com/', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3444.8924904757855!2d-97.7073052!3d30.297122100000003!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b5f84578082f%3A0x42afd5562f2f2df1!2s4550+Mueller+Blvd%2C+Austin%2C+TX+78723!5e0!3m2!1sen!2sus!4v1428532415527', \
        video_url = 'https://www.youtube.com/embed/cVG9FATjIyk', \
        fb_url = 'https://www.facebook.com/pages/The-Fit-Foodie-Race-Series/177814812394419', \
        landing_img = '/static/img/landing/funruns/fitfoodieLanding.jpg', \
        location_id = 5, \
        img_1 = '/static/img/runTempl/fitfoodie1.jpg', \
        img_2 = '/static/img/runTempl/fitfoodie2.jpg', \
        img_3 = '/static/img/runTempl/fitfoodie3.jpg')

    frun11 = FunRun(id = 11, name = 'Keep Austin Weird 5K', \
        address = 'The Long Center Grounds\n701 W Riverside Dr.\nAustin, TX 78704', \
        date = 'June 27th, 2015', \
        distance = '5K', \
        price = 'VIP: $75\nAdults: $22.50\nKids: $12', \
        hosts = 'The Long Center', \
        sponsors = 'HotSchedules, AT&T U-verse, Amy\'s Ice Cream, Babyearth, Beatbox Beverages', \
        charities = 'Capital Area Food Bank of Texas', \
        description = 'Slip into your weirdest costume, slap on your favorite light up running shoes and throw your timer into Lady Bird Lake! This is the slowest 5K on the planet - the wildest, weirdest and most memorable!', \
        short = 'Make Austin weird in the slowest race ever!', \
        quote_1 = 'So much fun! Drove down from Oklahoma City to attend!', \
        quote_2 = 'So well done! Loads of fun!', \
        quote_3 = 'It was our first time attending the fest and we had a blast! I will be back next year for sure!', \
        website = 'http://keepaustinweirdfest.com/festival/', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d3446.1964982159493!2d-97.751079!3d30.259982!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8644b504ea2084d7%3A0xa8a514235a56453e!2s701+W+Riverside+Dr%2C+Austin%2C+TX+78704!5e0!3m2!1sen!2sus!4v1428532467708', \
        video_url = 'https://www.youtube.com/embed/9sL-B1D7v34', \
        fb_url = 'https://www.facebook.com/pages/Keep-Austin-Weird-Festival-5K/121126484577639', \
        landing_img = '/static/img/landing/funruns/keepAustinWeirdLanding.jpg', \
        location_id = 5, \
        img_1 = '/static/img/runTempl/keepAustinWeird1.jpg', \
        img_2 = '/static/img/runTempl/keepAustinweird2.jpg', \
        img_3 = '/static/img/runTempl/keepAustinweird3.jpg')

    frun12 = FunRun(id = 12, name = 'North American Wife Carrying Championship', \
        address = 'Sunday River Ski Resort\n15 S Ridge Rd.\nNewry, ME 04261', \
        date = 'October 10th, 2015', \
        distance = '278yd', \
        price = 'N/A', \
        hosts = 'Sunday River', \
        sponsors = 'BudLight, Bethel Inn Resort', \
        charities = 'N/A', \
        description = 'Carry your wife to the finish and win her weight in beer! The course at Sunday River is built to international specifications at 278 yards in length, with two dry obstacles and one water obstacle.', \
        short = 'Carry your wife and win her weight in beer!', \
        quote_1 = 'It was a very cool event! Sunday River does a good job with it!', \
        quote_2 = 'I\'m wicked strong and she\'s wicked small!', \
        quote_3 = 'Hardly fair playing field but fun to watch none the less.', \
        website = 'http://www.sundayriver.com/events-and-activities/events-calendar/north-american-wife-carrying-championship', \
        map_url = 'https://www.google.com/maps/embed?pb=!1m14!1m8!1m3!1d2847.0332106871697!2d-70.856894!3d44.473492!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x4cb3dd81009e321b%3A0xd2eb7c1aecb4af6e!2sSunday+River+Ski+Resort!5e0!3m2!1sen!2sus!4v1428532505050', \
        video_url = 'https://player.vimeo.com/video/112507533', \
        fb_url = 'https://www.facebook.com/sundayriver', \
        landing_img = '/static/img/landing/funruns/wifecarryLanding.jpg', \
        location_id = 6, \
        img_1 = '/static/img/runTempl/wifecarry1.jpg', \
        img_2 = '/static/img/runTempl/wifecarry2.jpg', \
        img_3 = '/static/img/runTempl/wifecarry3.jpg')


    # Create the themes
    theme1 = Theme(id = 1, name = 'Holiday', \
        buzzwords = 'Christmas, Thanksgiving, Easter, Valentine\'s Day, St. Patrick\'s Day, New Year\'s, Halloween, 4th of July', \
        description = 'Instead of sitting around the fire, talking of presents and Santa, why not go for a run with the family? Holiday runs are a great way to get out and celebrate during the festivities! Often featuring thematic competitions and costumes, they\'re a sure way of making any holiday a memorable one.', \
        short = 'Celebrate the holidays with a festive run.', \
        landing_img = '/static/img/landing/themes/holiday1.jpg', \
        img_1 = '/static/img/themeTempl/holiday1.jpg', \
        img_2 = '/static/img/themeTempl/holiday2.jpg', \
        img_3 = '/static/img/themeTempl/holiday3.jpg', \
        img_4 = '/static/img/themeTempl/holiday4.jpg', \
        img_5 = '/static/img/themeTempl/holiday5.jpg', \
        img_6 = '/static/img/themeTempl/holiday6.jpg', \
        img_7 = '/static/img/themeTempl/holiday7.jpg', \
        img_8 = '/static/img/themeTempl/holiday8.jpg')

    theme2 = Theme(id = 2, name = 'Intense', \
        buzzwords = 'Training, Diet, Hardcore, Recovery, Cutthroat', \
        description = 'More interested in proving how much you can take than how much fun you\'ll actually have? Intense runs are exactly what you need - a good dose of body-numbing, soul-crushing exercise to show your stuff. See if you can survive the brutal difficulty of these events.', \
        short = 'Test your endurance in these hardcore races.', \
        landing_img = '/static/img/landing/themes/intense1.jpg', \
        img_1 = '/static/img/themeTempl/intense1.jpg', \
        img_2 = '/static/img/themeTempl/intense2.jpg', \
        img_3 = '/static/img/themeTempl/intense3.jpg', \
        img_4 = '/static/img/themeTempl/intense4.jpg', \
        img_5 = '/static/img/themeTempl/intense5.jpg', \
        img_6 = '/static/img/themeTempl/intense6.jpg', \
        img_7 = '/static/img/themeTempl/intense7.jpg', \
        img_8 = '/static/img/themeTempl/intense8.jpg')

    theme3 = Theme(id = 3, name = 'Costume', \
        buzzwords = 'Silly, Uncomfortable, Dress-Up, Make-Believe', \
        description = 'Ever run a 5K in a hot and heavy mascot uniform? How about amongst hundreds of other runners in similarly ridiculous outfits? Try a costume run to experience the unique challenge of running in something other than athletic clothes and join a hodge-podge mob of other costumed crazies!', \
        short = 'Put on your silliest outfit and get running.', \
        landing_img = '/static/img/landing/themes/costume1.jpg', \
        img_1 = '/static/img/themeTempl/costume1.jpg', \
        img_2 = '/static/img/themeTempl/costume2.jpg', \
        img_3 = '/static/img/themeTempl/costume3.jpg', \
        img_4 = '/static/img/themeTempl/costume4.jpg', \
        img_5 = '/static/img/themeTempl/costume5.jpg', \
        img_6 = '/static/img/themeTempl/costume6.jpg', \
        img_7 = '/static/img/themeTempl/costume7.jpg', \
        img_8 = '/static/img/themeTempl/costume8.jpg')

    theme4 = Theme(id = 4, name = 'Location', \
        buzzwords = 'Landmarks, Rivers, Downtown, Parks, Lakes, Views', \
        description = 'Whether it is an excuse to travel and exercise, or a good distraction from the aches and pains of running, the location of a race is a great factor in deciding which run works for you!', \
        short = 'Enjoy the scenic views while getting in some exercise.', \
        landing_img = '/static/img/landing/themes/location1.jpg', \
        img_1 = '/static/img/themeTempl/location1.jpg', \
        img_2 = '/static/img/themeTempl/location2.jpg', \
        img_3 = '/static/img/themeTempl/location3.jpg', \
        img_4 = '/static/img/themeTempl/location4.jpg', \
        img_5 = '/static/img/themeTempl/location5.jpg', \
        img_6 = '/static/img/themeTempl/location6.jpg', \
        img_7 = '/static/img/themeTempl/location7.jpg', \
        img_8 = '/static/img/themeTempl/location8.jpg')

    theme5 = Theme(id = 5, name = 'Dirty', \
        buzzwords = 'Mud, Color Paint, Wet', \
        description = 'Want to run through mud pits, climb walls, and get blasted with paint? Challenge yourself with these get down-and-dirty runs.', \
        short = 'Get ready to take a long shower afterwards.', \
        landing_img = '/static/img/landing/themes/dirty1.jpg', \
        img_1 = '/static/img/themeTempl/dirty1.jpg', \
        img_2 = '/static/img/themeTempl/dirty2.jpg', \
        img_3 = '/static/img/themeTempl/dirty3.jpg', \
        img_4 = '/static/img/themeTempl/dirty4.jpg', \
        img_5 = '/static/img/themeTempl/dirty5.jpg', \
        img_6 = '/static/img/themeTempl/dirty6.jpg', \
        img_7 = '/static/img/themeTempl/dirty7.jpg', \
        img_8 = '/static/img/themeTempl/dirty8.jpg')

    theme6 = Theme(id = 6, name = 'Team', \
        buzzwords = 'Group, Partner(s), Family', \
        description = 'You don\'t have to run a race by yourself. Instead, put together a team of your friends and take part in one of these races.', \
        short = 'Share the fun with a group or that special someone', \
        landing_img = '/static/img/landing/themes/team1.jpg', \
        img_1 = '/static/img/themeTempl/team1.jpg', \
        img_2 = '/static/img/themeTempl/team2.jpg', \
        img_3 = '/static/img/themeTempl/team3.jpg', \
        img_4 = '/static/img/themeTempl/team4.jpg', \
        img_5 = '/static/img/themeTempl/team5.jpg', \
        img_6 = '/static/img/themeTempl/team6.jpg', \
        img_7 = '/static/img/themeTempl/team7.jpg', \
        img_8 = '/static/img/themeTempl/team8.jpg')

    theme7 = Theme(id = 7, name = 'Drink', \
        buzzwords = 'Beer, beer, and more beer', \
        description = 'Ever try keeping down a couple of drinks while running long distances? These runs test your endurance and bladder', \
        short = 'Hold yourself together while being part ofthese runs.', \
        landing_img = '/static/img/landing/themes/drink1.jpg', \
        img_1 = '/static/img/themeTempl/drink1.jpg', \
        img_2 = '/static/img/themeTempl/drink2.jpg', \
        img_3 = '/static/img/themeTempl/drink3.jpg', \
        img_4 = '/static/img/themeTempl/drink4.jpg', \
        img_5 = '/static/img/themeTempl/drink5.jpg', \
        img_6 = '/static/img/themeTempl/drink6.jpg', \
        img_7 = '/static/img/themeTempl/drink7.jpg', \
        img_8 = '/static/img/themeTempl/drink8.jpg')

    theme8 = Theme(id = 8, name = 'Food', \
        buzzwords = 'Sweet, sour, healthy', \
        description = 'Forget bananas and postrace barbecues. In these races, chowing down is part of the competition.', \
        short = 'Enjoy a nice meal with these runs.', \
        landing_img = '/static/img/landing/themes/food1.jpg', \
        img_1 = '/static/img/themeTempl/food1.jpg', \
        img_2 = '/static/img/themeTempl/food2.jpg', \
        img_3 = '/static/img/themeTempl/food3.jpg', \
        img_4 = '/static/img/themeTempl/food4.jpg', \
        img_5 = '/static/img/themeTempl/food5.jpg', \
        img_6 = '/static/img/themeTempl/food6.jpg', \
        img_7 = '/static/img/themeTempl/food7.jpg', \
        img_8 = '/static/img/themeTempl/food8.jpg')

    theme9 = Theme(id = 9, name = 'Music', \
        buzzwords = 'Rhythm, Dance, Banger', \
        description = 'No need for a pre-workout for these runs. The music will get you pumped and ready to hit the ground running.', \
        short = 'Jam out to some tunes during these runs.', \
        landing_img = '/static/img/landing/themes/music1.jpg', \
        img_1 = '/static/img/themeTempl/music1.jpg', \
        img_2 = '/static/img/themeTempl/music2.jpg', \
        img_3 = '/static/img/themeTempl/music3.jpg', \
        img_4 = '/static/img/themeTempl/music4.jpg', \
        img_5 = '/static/img/themeTempl/music5.jpg', \
        img_6 = '/static/img/themeTempl/music6.jpg', \
        img_7 = '/static/img/themeTempl/music7.jpg', \
        img_8 = '/static/img/themeTempl/music8.jpg')

    theme10 = Theme(id = 10, name = 'Fantasy', \
        buzzwords = 'Dreams, Monsters, Supernatural', \
        description = 'These runs will make your imagination run wild with their supernatural sights and experiences.', \
        short = 'Run through your wildest fantasies.', \
        landing_img = '/static/img/landing/themes/fantasy1.jpg', \
        img_1 = '/static/img/themeTempl/fantasy1.jpg', \
        img_2 = '/static/img/themeTempl/fantasy2.jpg', \
        img_3 = '/static/img/themeTempl/fantasy3.jpg', \
        img_4 = '/static/img/themeTempl/fantasy4.jpg', \
        img_5 = '/static/img/themeTempl/fantasy5.jpg', \
        img_6 = '/static/img/themeTempl/fantasy6.jpg', \
        img_7 = '/static/img/themeTempl/fantasy7.jpg', \
        img_8 = '/static/img/themeTempl/fantasy8.jpg')


    # Create the challenges
    chal1 = Challenge(id = 1, \
        name = 'Running On Awkward Ground', \
        difficulty = 60, \
        flavors = 'Ice, Inflatable Balls, Mud', \
        description = 'Think running is hard enough? Try running on mud, inflatable balls, or slippery surfaces! Just be ready for the fall - and to get back up again to keep trying.', \
        landing_img = '/static/img/landing/challenges/oddGround1.jpg', \
        img_1 = '/static/img/challengeTempl/oddGround1.jpg', \
        img_2 = '/static/img/challengeTempl/oddGround2.jpg', \
        img_3 = '/static/img/challengeTempl/oddGround3.jpg')

    chal2 = Challenge(id = 2, \
        name = 'Running In A Costume', \
        difficulty = 40, \
        flavors = 'Mascots, Nude, Speedos, Costumes', \
        description = 'Ideally, running should be done in comfortable shorts and shirt. Instead, some dare to run in costumes - or a lack of costume - in self expression and, oftentimes, silliness.', \
        landing_img = '/static/img/landing/challenges/costume1.jpg', \
        img_1 = '/static/img/challengeTempl/costume1.jpg', \
        img_2 = '/static/img/challengeTempl/costume2.jpg', \
        img_3 = '/static/img/challengeTempl/costume3.jpg')

    chal3 = Challenge(id = 3, \
        name = 'Running In Cold Weather', \
        difficulty = 80, \
        flavors = 'Snow, Ice, Freezing Temperatures', \
        description = 'Take on the cold fearlessly with fun runs in less than ideal temperatures. Will the icy winds get to you or will you make it to the finish line and prevail?', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal4 = Challenge(id = 4, \
        name = 'Going Over Hills', \
        difficulty = 70, \
        flavors = 'High elevation, Incline, Steep', \
        description = 'Fight against gravity and prepare to go over steep hills in these runs', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal5 = Challenge(id = 5, \
        name = 'Getting Chased', \
        difficulty = 60, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal6 = Challenge(id = 6, \
        name = 'Getting Covered in Stuff', \
        difficulty = 40, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal7 = Challenge(id = 7, \
        name = 'Consuming', \
        difficulty = 40, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal8 = Challenge(id = 8, \
        name = 'Carrying an Object', \
        difficulty = 70, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal9 = Challenge(id = 9, \
        name = 'Scaling a Wall', \
        difficulty = 80, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal10 = Challenge(id = 10, \
        name = 'Sliding Down Slopes', \
        difficulty = 50, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal11 = Challenge(id = 11, \
        name = 'Crawling Underneath Obstacles', \
        difficulty = 60, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal12 = Challenge(id = 12, \
        name = 'Being Suspended', \
        difficulty = 70, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal13 = Challenge(id = 13, \
        name = 'Staying Balanced', \
        difficulty = 70, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal14 = Challenge(id = 14, \
        name = 'Getting Hit by Objects', \
        difficulty = 80, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal15 = Challenge(id = 15, \
        name = 'Performing Urban Parkouring', \
        difficulty = 70, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')

    chal16 = Challenge(id = 16, \
        name = 'Running with Limited Visibility', \
        difficulty = 60, \
        flavors = 'Pursued, Zombies', \
        description = '', \
        landing_img = '/static/img/landing/challenges/cold1.jpg', \
        img_1 = '/static/img/challengeTempl/cold1.jpg', \
        img_2 = '/static/img/challengeTempl/cold2.jpg', \
        img_3 = '/static/img/challengeTempl/cold3.jpg')


    # Create the locations
    loc1 = Location(id = 1, \
        name = 'Baltimore, Maryland', \
        nickname = 'The Charm City', \
        winter_avgTemp = 45, \
        spring_avgTemp = 65, \
        summer_avgTemp = 87, \
        fall_avgTemp = 69, \
        winter_avgHumidity = 63, \
        spring_avgHumidity = 61, \
        summer_avgHumidity = 69, \
        fall_avgHumidity = 69, \
        altitude = '33ft', \
        annual_rainfall = '40.72in', \
        landmarks = 'National Aquarium in Baltimore, Fort McHenry', \
        website_url = 'http://www.baltimorecity.gov/', \
        description = 'Baltimore is the largest city in the State of Maryland, the largest independent city in the United States, and the 26th-most populous city in the country.', \
        landing_img = '/static/img/landing/locations/baltimoreMDLanding.jpg', \
        img = '/static/img/locationTempl/baltimore1.jpg')

    loc2 = Location(id = 2, \
        name = 'Dallas, Texas', \
        nickname = 'Home of the Cowboys', \
        winter_avgTemp = 59, \
        spring_avgTemp = 77, \
        summer_avgTemp = 95, \
        fall_avgTemp = 78, \
        winter_avgHumidity = 52, \
        spring_avgHumidity = 49, \
        summer_avgHumidity = 44, \
        fall_avgHumidity = 47, \
        altitude = '430ft', \
        annual_rainfall = '40.55in', \
        landmarks = 'Sixth Floor Museum at Dealey Plaza, Dallas World Aquarium', \
        website_url = 'http://dallascityhall.com/Pages/default.aspx', \
        description = 'Dallas is a major city in Texas and is the largest urban center of the fourth most populous metropolitan area in the United States. The city proper ranks ninth in the U.S. and third in Texas after Houston and San Antonio.', \
        landing_img = '/static/img/landing/locations/dallasTXLanding.jpg', \
        img = '/static/img/locationTempl/dallas1.jpg')

    loc3 = Location(id = 3, \
        name = 'Cleveland, Ohio', \
        nickname = 'The Forest City', \
        winter_avgTemp = 37, \
        spring_avgTemp = 58, \
        summer_avgTemp = 81, \
        fall_avgTemp = 72, \
        winter_avgHumidity = 71, \
        spring_avgHumidity = 59, \
        summer_avgHumidity = 55, \
        fall_avgHumidity = 58, \
        altitude = '653ft', \
        annual_rainfall = '39.12in', \
        landmarks = 'Rock and Roll Hall of Fame, Cleveland Metroparks Zoo', \
        website_url = 'http://www.city.cleveland.oh.us/CityofCleveland/Home', \
        description = 'Cleveland is a city in the state of Ohio and is the county seat of Cuyahoga County, the most populous county in the state.', \
        landing_img = '/static/img/landing/locations/clevelandOHLanding.jpg', \
        img = '/static/img/locationTempl/cleveland1.jpg')

    loc4 = Location(id = 4, \
        name = 'Fairburn, Georgia', \
        nickname = 'A City Among the Hills', \
        winter_avgTemp = 44, \
        spring_avgTemp = 61, \
        summer_avgTemp = 77, \
        fall_avgTemp = 63, \
        winter_avgHumidity = 65, \
        spring_avgHumidity = 78, \
        summer_avgHumidity = 83, \
        fall_avgHumidity = 78, \
        altitude = '1,027ft', \
        annual_rainfall = '52.06in', \
        landmarks = 'Cochran Mill Park, Camp Creek MarketPlace, Georgia International Convention Center', \
        website_url = 'http://www.fairburn.com/', \
        description = 'Fairburn is located just 25 minutes south of Atlanta and is a city of historic homes, buildings and places of worship with a thriving business community.', \
        landing_img = '/static/img/landing/locations/fairburnGALanding.jpg', \
        img = '/static/img/locationTempl/fairburn1.jpg')

    loc5 = Location(id = 5, \
        name = 'Austin, Texas', \
        nickname = 'Live Music Capital of the World', \
        winter_avgTemp = 51, \
        spring_avgTemp = 67, \
        summer_avgTemp = 83, \
        fall_avgTemp = 69, \
        winter_avgHumidity = 77, \
        spring_avgHumidity = 86, \
        summer_avgHumidity = 76, \
        fall_avgHumidity = 70, \
        altitude = '489ft', \
        annual_rainfall = '34.53in', \
        landmarks = 'Bob Bullock Texas State History Museum, Zilker Park, Hamilton Pool, Austin Zoo', \
        website_url = 'http://www.austintexas.org/', \
        description = 'Austin is the capital of Texas.  It has vibrant entertainment and culture, inspiring cuisine and stunning outdoor settings.', \
        landing_img = '/static/img/landing/locations/austinTXLanding.jpg', \
        img = '/static/img/locationTempl/austin1.jpg')

    loc6 = Location(id = 6, \
        name = 'Newry, Maine', \
        nickname = 'Sunday River Plantation', \
        winter_avgTemp = 16, \
        spring_avgTemp = 38, \
        summer_avgTemp = 62, \
        fall_avgTemp = 43, \
        winter_avgHumidity = 84, \
        spring_avgHumidity = 74, \
        summer_avgHumidity = 82, \
        fall_avgHumidity = 80, \
        altitude = '712ft', \
        annual_rainfall = '42.13in', \
        landmarks = 'Artists\' Covered Bridge, Step Falls Preserve, Sunday River Ski Resort, Grafton Notch State Park', \
        website_url = 'http://www.newrymaine.org/', \
        description = 'Newry is a town in Oxfor County, Maine.  It is the home of Sunday River Ski Resort and has a proportionately large population during winter.', \
        landing_img = '/static/img/landing/locations/newryMELanding.jpg', \
        img = '/static/img/locationTempl/newry1.jpg')

    loc7 = Location(id = 7, \
        name = 'San Francisco, California', \
        nickname = 'The Golden Gate City', \
        winter_avgTemp = 58, \
        spring_avgTemp = 63, \
        summer_avgTemp = 66, \
        fall_avgTemp = 68, \
        winter_avgHumidity = 77, \
        spring_avgHumidity = 71, \
        summer_avgHumidity = 79, \
        fall_avgHumidity = 73, \
        altitude = '52ft', \
        annual_rainfall = '23.64in', \
        landmarks = 'Chinatown, Golden Gate Bridge, Golden Gate Park', \
        website_url = 'http://www.sanfrancisco.travel/', \
        description = 'San Francisco is home to a little bit of everything. Whether you\'re a first time visitor or a long-time local. This is the place to find out about all things San Francisco.', \
        landing_img = '/static/img/landing/locations/sanfranciscoCALanding.jpg', \
        img = '/static/img/locationTempl/sanfrancisco1.jpg')

    loc8 = Location(id = 8, \
        name = 'Riverhead, New York', \
        nickname = 'Strong Island', \
        winter_avgTemp = 41, \
        spring_avgTemp = 59, \
        summer_avgTemp = 81, \
        fall_avgTemp = 64, \
        winter_avgHumidity = 78, \
        spring_avgHumidity = 84, \
        summer_avgHumidity = 90, \
        fall_avgHumidity = 82, \
        altitude = '13ft', \
        annual_rainfall = '47.8in', \
        landmarks = 'Long Island Aquarium and Exhibition Center, Splish Splash', \
        website_url = 'http://www.townofriverheadny.gov/', \
        description = 'Riverhead is on the mouth of the Peconic River, for which the town is named. The town has a total area of 201.3 square miles, of which 133.9 square miles(66.53%) is water.', \
        landing_img = '/static/img/landing/locations/riverheadNYLanding.jpg', \
        img = '/static/img/locationTempl/riverhead1.jpg')

    loc9 = Location(id = 9, \
        name = 'Memphis, Tennessee', \
        nickname = 'Home of the Blues', \
        winter_avgTemp = 52, \
        spring_avgTemp = 73, \
        summer_avgTemp = 91, \
        fall_avgTemp = 74, \
        winter_avgHumidity = 67, \
        spring_avgHumidity = 63, \
        summer_avgHumidity = 68, \
        fall_avgHumidity = 68, \
        altitude = '337ft', \
        annual_rainfall = '53.68in', \
        landmarks = 'Graceland, Memphis Zoo, Stax Museum of American Soul Music', \
        website_url = 'http://www.memphistn.gov/', \
        description = 'Memphis is the largest city on the Mississippi River. It is the third largest city in the greater Southeastern United States, and the 20th largest in the United States.', \
        landing_img = '/static/img/landing/locations/memphisTNLanding.jpg', \
        img = '/static/img/locationTempl/memphis1.jpg')

    loc10 = Location(id = 10, \
        name = 'Puyallup, Washington', \
        nickname = 'A Tree City USA', \
        winter_avgTemp = 48, \
        spring_avgTemp = 61, \
        summer_avgTemp = 76, \
        fall_avgTemp = 62, \
        winter_avgHumidity = 81, \
        spring_avgHumidity = 84, \
        summer_avgHumidity = 75, \
        fall_avgHumidity = 73, \
        altitude = '46ft', \
        annual_rainfall = '40.43in', \
        landmarks = 'U.S District Court, Historic Preservation, City of Tacoma', \
        website_url = 'http://www.cityofpuyallup.org/', \
        description = 'Named after the Puyallup Tribe of Native Americans, Puyallup means \'the generous people\'. Puyallup was first recognized as a Tree City USA in 2014.', \
        landing_img = '/static/img/landing/locations/puyallupWALanding.jpg', \
        img = '/static/img/locationTempl/puyallup1.jpg')


    # Add relationships
    frun1.funRun_theme.append(theme2)
    frun1.funRun_challenge.append(chal1)
    frun1.funRun_challenge.append(chal4)
    frun1.funRun_challenge.append(chal6)
    frun1.funRun_challenge.append(chal9)
    frun1.funRun_challenge.append(chal10)
    frun1.funRun_challenge.append(chal12)
    frun1.funRun_challenge.append(chal13)
    frun1.funRun_challenge.append(chal14)
    frun2.funRun_theme.append(theme1)
    frun2.funRun_theme.append(theme3)
    frun2.funRun_theme.append(theme4)
    frun2.funRun_challenge.append(chal2)
    frun2.funRun_challenge.append(chal3)
    frun3.funRun_theme.append(theme1)
    frun3.funRun_theme.append(theme3)
    frun3.funRun_challenge.append(chal2)
    frun3.funRun_challenge.append(chal3)
    frun4.funRun_theme.append(theme3)
    frun4.funRun_theme.append(theme6)
    frun4.funRun_challenge.append(chal2)
    frun4.funRun_challenge.append(chal4)
    frun4.funRun_challenge.append(chal7)
    frun5.funRun_theme.append(theme2)
    frun5.funRun_theme.append(theme3)
    frun5.funRun_theme.append(theme10)
    frun5.funRun_challenge.append(chal2)
    frun5.funRun_challenge.append(chal5)
    frun5.funRun_challenge.append(chal11)
    frun5.funRun_challenge.append(chal13)
    frun5.funRun_challenge.append(chal15)
    frun6.funRun_theme.append(theme5)
    frun6.funRun_theme.append(theme9)
    frun6.funRun_challenge.append(chal6)
    frun6.funRun_challenge.append(chal16)
    frun7.funRun_theme.append(theme5)
    frun7.funRun_theme.append(theme9)
    frun7.funRun_challenge.append(chal6)
    frun7.funRun_challenge.append(chal16)
    frun8.funRun_theme.append(theme7)
    frun8.funRun_challenge.append(chal7)
    frun9.funRun_theme.append(theme2)
    frun9.funRun_theme.append(theme5)
    frun9.funRun_theme.append(theme6)
    frun9.funRun_challenge.append(chal1)
    frun9.funRun_challenge.append(chal3)
    frun9.funRun_challenge.append(chal4)
    frun9.funRun_challenge.append(chal6)
    frun9.funRun_challenge.append(chal8)
    frun9.funRun_challenge.append(chal9)
    frun9.funRun_challenge.append(chal10)
    frun9.funRun_challenge.append(chal11)
    frun9.funRun_challenge.append(chal12)
    frun9.funRun_challenge.append(chal13)
    frun9.funRun_challenge.append(chal14)
    frun10.funRun_theme.append(theme8)
    frun10.funRun_challenge.append(chal7)
    frun11.funRun_theme.append(theme3)
    frun11.funRun_theme.append(theme4)
    frun11.funRun_theme.append(theme9)
    frun11.funRun_challenge.append(chal2)
    frun11.funRun_challenge.append(chal3)
    frun12.funRun_theme.append(theme5)
    frun12.funRun_theme.append(theme6)
    frun12.funRun_challenge.append(chal1)
    frun12.funRun_challenge.append(chal4)
    frun12.funRun_challenge.append(chal6)
    frun12.funRun_challenge.append(chal8)
    frun12.funRun_challenge.append(chal12)
    frun12.funRun_challenge.append(chal13)
    theme1.theme_challenge.append(chal2)
    theme1.theme_challenge.append(chal3)
    theme2.theme_challenge.append(chal1)
    theme2.theme_challenge.append(chal3)
    theme2.theme_challenge.append(chal4)
    theme2.theme_challenge.append(chal5)
    theme2.theme_challenge.append(chal8)
    theme2.theme_challenge.append(chal9)
    theme2.theme_challenge.append(chal10)
    theme2.theme_challenge.append(chal11)
    theme2.theme_challenge.append(chal12)
    theme2.theme_challenge.append(chal13)
    theme2.theme_challenge.append(chal14)
    theme2.theme_challenge.append(chal15)
    theme3.theme_challenge.append(chal2)
    theme4.theme_challenge.append(chal4)
    theme5.theme_challenge.append(chal1)
    theme5.theme_challenge.append(chal6)
    theme5.theme_challenge.append(chal9)
    theme5.theme_challenge.append(chal10)
    theme5.theme_challenge.append(chal11)
    theme5.theme_challenge.append(chal12)
    theme5.theme_challenge.append(chal13)
    theme5.theme_challenge.append(chal14)
    theme5.theme_challenge.append(chal16)
    theme6.theme_challenge.append(chal8)
    theme6.theme_challenge.append(chal13)
    theme7.theme_challenge.append(chal7)
    theme7.theme_challenge.append(chal8)
    theme8.theme_challenge.append(chal7)
    theme8.theme_challenge.append(chal8)
    theme9.theme_challenge.append(chal2)
    theme9.theme_challenge.append(chal6)
    theme9.theme_challenge.append(chal16)
    theme10.theme_challenge.append(chal2)
    theme10.theme_challenge.append(chal5)
    theme10.theme_challenge.append(chal15)

    # Populate the funruns
    db.session.add(frun1)
    db.session.add(frun2)
    db.session.add(frun3)
    db.session.add(frun4)
    db.session.add(frun5)
    db.session.add(frun6)
    db.session.add(frun7)
    db.session.add(frun8)
    db.session.add(frun9)
    db.session.add(frun10)
    db.session.add(frun11)
    db.session.add(frun12)

    # Populate the themes
    db.session.add(theme1)
    db.session.add(theme2)
    db.session.add(theme3)
    db.session.add(theme4)
    db.session.add(theme5)
    db.session.add(theme6)
    db.session.add(theme7)
    db.session.add(theme8)
    db.session.add(theme9)
    db.session.add(theme10)

    # Populate the challenges
    db.session.add(chal1)
    db.session.add(chal2)
    db.session.add(chal3)
    db.session.add(chal4)
    db.session.add(chal5)
    db.session.add(chal6)
    db.session.add(chal7)
    db.session.add(chal8)
    db.session.add(chal9)
    db.session.add(chal10)
    db.session.add(chal11)
    db.session.add(chal12)
    db.session.add(chal13)
    db.session.add(chal14)
    db.session.add(chal15)
    db.session.add(chal16)

    # Populate the locations
    db.session.add(loc1)
    db.session.add(loc2)
    db.session.add(loc3)
    db.session.add(loc4)
    db.session.add(loc5)
    db.session.add(loc6)
    db.session.add(loc7)
    db.session.add(loc8)
    db.session.add(loc9)
    db.session.add(loc10)


    db.session.commit()

    print (frun1.id)
    print (chal1.id)
    print (loc1.id)
    print (theme1.id)

if __name__ == '__main__':
    populateDatabase()