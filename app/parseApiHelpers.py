from api_helpers import retrieve_funruns, retrieve_themes, retrieve_challenges, retrieve_locations
# Creates a file called create_database.py with commands to populate
# all of the data we have stored in api_helpers.py


def dealWithEscapedNLandApost(s) :
	newS = ""
	for char in s :
		if char == '\n' :
			newS += "\\n"
		elif char == '\'' :
			newS += "\\'"
		else :
			newS += char
	return newS

def funRunsParser(run) :
	return ("frun" + str(run['id'] + 1) + " = FunRun(" + "id = " + str(run['id'] + 1) + ", "\
	 + "name = '" + dealWithEscapedNLandApost(run['name']) + "', " + "\\\n\t"\
	 + "address = '" + dealWithEscapedNLandApost(run['address']) + "', " + "\\\n\t"\
	 + "date = '" + dealWithEscapedNLandApost(run['date']) + "', " + "\\\n\t"\
	 + "distance = '" + dealWithEscapedNLandApost(run['distance']) + "', " + "\\\n\t"\
	 + "price = '" + dealWithEscapedNLandApost(run['price']) + "', " + "\\\n\t"\
	 + "hosts = '" + dealWithEscapedNLandApost(run['hosts']) + "', " + "\\\n\t"\
	 + "sponsors = '" + dealWithEscapedNLandApost(run['sponsors']) + "', " + "\\\n\t"\
	 + "charities = '" + dealWithEscapedNLandApost(run['charities']) + "', " + "\\\n\t"\
	 + "description = '" + dealWithEscapedNLandApost(run['description']) + "', " + "\\\n\t"\
	 + "short = '" + dealWithEscapedNLandApost(run['short']) + "', " + "\\\n\t"\
	 + "quote_1 = '" + dealWithEscapedNLandApost(run['quotes'][0]) + "', " + "\\\n\t"\
	 + "quote_2 = '" + dealWithEscapedNLandApost(run['quotes'][1]) + "', " + "\\\n\t"\
	 + "quote_3 = '" + dealWithEscapedNLandApost(run['quotes'][2]) + "', " + "\\\n\t"\
	 + "website = '" + dealWithEscapedNLandApost(run['website']) + "', " + "\\\n\t"\
	 + "map_url = '" + dealWithEscapedNLandApost(run['map_url']) + "', " + "\\\n\t"\
	 + "video_url = '" + dealWithEscapedNLandApost(run['video_url']) + "', " + "\\\n\t"\
	 + "fb_url = '" + dealWithEscapedNLandApost(run['fb_url']) + "', " + "\\\n\t"\
	 + "landing_img = '" + dealWithEscapedNLandApost(run['landing_img']) + "', \\\n\t"\
	 + "location_id = " + str(run['loc'] + 1) + ", " + "\\\n\t"\
	 + "img_1 = '" + dealWithEscapedNLandApost(run['imgs'][0]) + "', " + "\\\n\t"\
	 + "img_2 = '" + dealWithEscapedNLandApost(run['imgs'][1]) + "', " + "\\\n\t"\
	 + "img_3 = '" + dealWithEscapedNLandApost(run['imgs'][2]) + "')\n\n")

def themesParser(theme) :
	return ("theme" + str(theme['id'] + 1) + " = Theme(" + "id = " + str(theme['id'] + 1)\
	+ ", " + "name = '" + theme['name'] + "', " + "\\\n\t"\
	+ "buzzwords = '" + dealWithEscapedNLandApost(theme['buzzwords']) + "', " + "\\\n\t"\
	+ "description = '" + dealWithEscapedNLandApost(theme['description']) + "', " + "\\\n\t"\
	+ "short = '" + dealWithEscapedNLandApost(theme['short']) + "', " + "\\\n\t"\
	+ "landing_img = '" + dealWithEscapedNLandApost(theme['landing_img']) + "', " + "\\\n\t"\
	+ "img_1 = '" + dealWithEscapedNLandApost(theme['imgs'][0]) + "', " + "\\\n\t"\
	+ "img_2 = '" + dealWithEscapedNLandApost(theme['imgs'][1]) + "', " + "\\\n\t"\
	+ "img_3 = '" + dealWithEscapedNLandApost(theme['imgs'][2]) + "', " + "\\\n\t"\
	+ "img_4 = '" + dealWithEscapedNLandApost(theme['imgs'][3]) + "', " + "\\\n\t"\
	+ "img_5 = '" + dealWithEscapedNLandApost(theme['imgs'][4]) + "', " + "\\\n\t"\
	+ "img_6 = '" + dealWithEscapedNLandApost(theme['imgs'][5]) + "', " + "\\\n\t"\
	+ "img_7 = '" + dealWithEscapedNLandApost(theme['imgs'][6]) + "', " + "\\\n\t"\
	+ "img_8 = '" + dealWithEscapedNLandApost(theme['imgs'][7]) + "')\n\n")

def challengesParser(challenge) :
	return ("chal" + str(challenge['id'] + 1) + " = Challenge(" + "id = "\
		+ str(challenge['id'] + 1) + ", " + "\\\n\t"\
		+ "name = '" + dealWithEscapedNLandApost(challenge['name']) + "', \\\n\t"\
		+ "difficulty = " + str(challenge['difficulty']) + ", " + "\\\n\t"\
		+ "flavors = '" + dealWithEscapedNLandApost(challenge['flavors']) + "', " + "\\\n\t"\
		+ "description = '" + dealWithEscapedNLandApost(challenge['description']) + "', " + "\\\n\t"\
		+ "landing_img = '" + dealWithEscapedNLandApost(challenge['landing_img']) + "', " + "\\\n\t"\
		+ "img_1 = '" + dealWithEscapedNLandApost(challenge['imgs'][0]) + "', " + "\\\n\t"\
		+ "img_2 = '" + dealWithEscapedNLandApost(challenge['imgs'][1]) + "', " + "\\\n\t"\
		+ "img_3 = '" + dealWithEscapedNLandApost(challenge['imgs'][2]) + "')\n\n")

def locationsParser(location) :
	return ("loc" + str(location['id'] + 1) + " = Location(" + "id = "\
		+ str(location['id'] + 1) + ", " + "\\\n\t"\
		+ "name = '" + dealWithEscapedNLandApost(location['name']) + "', " + "\\\n\t"\
		+ "nickname = '" + dealWithEscapedNLandApost(location['nickname']) + "', \\\n\t"\
		+ "winter_avgTemp = " + str(location['winter_avgTemp']) + ", \\\n\t"\
		+ "spring_avgTemp = " + str(location['spring_avgTemp']) + ", \\\n\t"\
		+ "summer_avgTemp = " + str(location['summer_avgTemp']) + ", \\\n\t"\
		+ "fall_avgTemp = " + str(location['fall_avgTemp']) + ", \\\n\t"\
		+ "winter_avgHumidity = " + str(location['winter_avgHumidity']) + ", \\\n\t"\
		+ "spring_avgHumidity = " + str(location['spring_avgHumidity']) + ", \\\n\t"\
		+ "summer_avgHumidity = " + str(location['summer_avgHumidity']) + ", \\\n\t"\
		+ "fall_avgHumidity = " + str(location['fall_avgHumidity']) + ", "+ "\\\n\t"\
		+ "altitude = '" + dealWithEscapedNLandApost(location['altitude']) + "', "+ "\\\n\t"\
		+ "annual_rainfall = '" + dealWithEscapedNLandApost(location['annual_rainfall']) + "', "+ "\\\n\t"\
		+ "landmarks = '" + dealWithEscapedNLandApost(location['landmarks']) + "', "+ "\\\n\t"\
		+ "website_url = '" + dealWithEscapedNLandApost(location['website_url']) + "', "+ "\\\n\t"\
		+ "description = '" + dealWithEscapedNLandApost(location['description']) + "', "+ "\\\n\t"\
		+ "landing_img = '" + dealWithEscapedNLandApost(location['landing_img']) + "', "+ "\\\n\t"\
		+ "img = '" + dealWithEscapedNLandApost(location['img']) + "')\n\n")

def funRunsRelationships(run) :
	s = ""
	runName = "frun" + str(run['id'] + 1)
	for themeId in run['themes'] :
		themeName = "theme" + str(themeId + 1)
		s += runName + ".funRun_theme.append(" + themeName + ")\n"
	for chalId in run['challenges'] :
		chalName = "chal" + str(chalId + 1)
		s += runName + ".funRun_challenge.append(" + chalName + ")\n"
	return s

def themesRelationships(theme) :
	s = ""
	themeName = "theme" + str(theme['id'] + 1)
	for chalId in theme['challenges'] :
		chalName = "chal" + str(chalId + 1)
		s += themeName + ".theme_challenge.append(" + chalName + ")\n"
	return s



def makeCreateDatabaseFile() :
	f = open('database_commands.txt', 'w')
	fRunDicList = retrieve_funruns()
	themeDicList = retrieve_themes()
	challengeDicList = retrieve_challenges()
	locationDicList = retrieve_locations()

	f.write('# Create the funruns\n')
	for run in fRunDicList :
		f.write(funRunsParser(run))

	f.write('\n# Create the themes\n')
	for theme in themeDicList :
		f.write(themesParser(theme))

	f.write('\n# Create the challenges\n')
	for challenge in challengeDicList :
		f.write(challengesParser(challenge))

	f.write('\n# Create the locations\n')
	for location in locationDicList :
		f.write(locationsParser(location))

	f.write('\n# Add relationships\n')
	for run in fRunDicList :
		f.write(funRunsRelationships(run))
	for theme in themeDicList :
		f.write(themesRelationships(theme))

	f.write('\n# Populate the funruns\n')
	for run in fRunDicList :
		f.write("db.session.add(frun" + str(run['id'] + 1) + ")\n")

	f.write('\n# Populate the themes\n')
	for theme in themeDicList :
		f.write("db.session.add(theme" + str(theme['id'] + 1) + ")\n")

	f.write('\n# Populate the challenges\n')
	for challenge in challengeDicList :
		f.write("db.session.add(chal" + str(challenge['id'] + 1) + ")\n")

	f.write('\n# Populate the locations\n')
	for location in locationDicList :
		f.write("db.session.add(loc" + str(location['id'] + 1) + ")\n")


makeCreateDatabaseFile()