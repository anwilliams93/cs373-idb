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
	return ("frun" + str(run['id']) + " = FunRun(" + str(run['id']) + ", " + "'"\
	 + dealWithEscapedNLandApost(run['name']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['city']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['address']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['date']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['distance']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['price']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['hosts']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['sponsors']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['charities']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['description']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['short']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['quotes'][0]) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['quotes'][1]) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['quotes'][2]) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['website']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['map_url']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['video_url']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['fb_url']) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['landing_img']) + "', \\\n\t"\
	 + str(run['loc']) + ", " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['imgs'][0]) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['imgs'][1]) + "', " + "\\\n\t'"\
	 + dealWithEscapedNLandApost(run['imgs'][2]) + "')\n\n")

def themesParser(theme) :
	return ("theme" + str(theme['id']) + " = Theme(" + str(theme['id'])\
	+ ", " + "'" + theme['name'] + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['buzzwords']) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['description']) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['short']) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['landing_img']) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['imgs'][0]) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['imgs'][1]) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['imgs'][2]) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['imgs'][3]) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['imgs'][4]) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['imgs'][5]) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['imgs'][6]) + "', " + "\\\n\t'"\
	+ dealWithEscapedNLandApost(theme['imgs'][7]) + "')\n\n")

def challengesParser(challenge) :
	return ("challenge" + str(challenge['id']) + " = Challenge("\
		+ str(challenge['id']) + ", " + "\\\n\t'"\
		+ dealWithEscapedNLandApost(challenge['name']) + "', \\\n\t"\
		+ str(challenge['difficulty']) + ", " + "\\\n\t'"\
		+ dealWithEscapedNLandApost(challenge['flavors']) + "', " + "\\\n\t'"\
		+ dealWithEscapedNLandApost(challenge['description']) + "', " + "\\\n\t'"\
		+ dealWithEscapedNLandApost(challenge['landing_img']) + "', " + "\\\n\t'"\
		+ dealWithEscapedNLandApost(challenge['imgs'][0]) + "', " + "\\\n\t'"\
		+ dealWithEscapedNLandApost(challenge['imgs'][1]) + "', " + "\\\n\t'"\
		+ dealWithEscapedNLandApost(challenge['imgs'][2]) + "')\n\n")

def locationsParser(location) :
	return ("loc" + str(location['id']) + " = Location("\
		+ str(location['id']) + ", " + "\\\n\t'"\
		+ dealWithEscapedNLandApost(location['name']) + "', " + "\\\n\t'"\
		+ dealWithEscapedNLandApost(location['nickname']) + "', \\\n\t"\
		+ str(location['winter_avgTemp']) + ", \\\n\t"\
		+ str(location['spring_avgTemp']) + ", \\\n\t"\
		+ str(location['summer_avgTemp']) + ", \\\n\t"\
		+ str(location['fall_avgTemp']) + ", \\\n\t"\
		+ str(location['winter_avgHumidity']) + ", \\\n\t"\
		+ str(location['spring_avgHumidity']) + ", \\\n\t"\
		+ str(location['summer_avgHumidity']) + ", \\\n\t"\
		+ str(location['fall_avgHumidity']) + ", "+ "\\\n\t'"\
		+ dealWithEscapedNLandApost(location['altitude']) + "', "+ "\\\n\t'"\
		+ dealWithEscapedNLandApost(location['annual_rainfall']) + "', "+ "\\\n\t'"\
		+ dealWithEscapedNLandApost(location['landmarks']) + "', "+ "\\\n\t'"\
		+ dealWithEscapedNLandApost(location['website_url']) + "', "+ "\\\n\t'"\
		+ dealWithEscapedNLandApost(location['description']) + "', "+ "\\\n\t'"\
		+ dealWithEscapedNLandApost(location['landing_img']) + "', "+ "\\\n\t'"\
		+ dealWithEscapedNLandApost(location['img']) + "')\n\n")

def funRunsRelationships(run) :
	s = ""
	runName = "frun" + str(run['id'])
	for themeId in run['themes'] :
		themeName = "theme" + str(themeId)
		s += runName + ".funRun_theme.append(" + themeName + ")\n"
	for chalId in run['challenges'] :
		chalName = "chal" + str(chalId)
		s += runName + ".funRun_challenge.append(" + chalName + ")\n"
	return s

def themesRelationships(theme) :
	s = ""
	themeName = "theme" + str(theme['id'])
	for chalId in theme['challenges'] :
		chalName = "chal" + str(chalId)
		s += themeName + ".theme_challenge.append(" + chalName + ")\n"
	return s



def makeCreateDatabaseFile() :
	f = open('create_database.py', 'w')
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
		f.write("db.session.add(frun" + str(run['id']) + ")\n")

	f.write('\n# Populate the themes\n')
	for theme in themeDicList :
		f.write("db.session.add(theme" + str(theme['id']) + ")\n")

	f.write('\n# Populate the challenges\n')
	for challenge in challengeDicList :
		f.write("db.session.add(chal" + str(challenge['id']) + ")\n")

	f.write('\n# Populate the locations\n')
	for location in locationDicList :
		f.write("db.session.add(loc" + str(location['id']) + ")\n")


makeCreateDatabaseFile()