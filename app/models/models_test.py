
from models.models import db, Location, FunRun, Theme, Challenge
import os
#import sql_db
import unittest
import tempfile

class TestDBModels(unittest.TestCase):


	def test_funrun(self):
		result = db.session.query(FunRun).count()
		assert (result == 12)

	def test_themes(self):
		result = db.session.query(Theme).count()
		assert (result == 10)

	def test_challenges(self):
		result = db.session.query(Challenge).count()
		assert (result == 16)

	def test_location(self):
		result = db.session.query(Location).count()
		assert (result == 10)

	def test_add_funrun(self):
		frun1 = FunRun(id = 13, name = 'testing')
		db.session.add(frun1)
		result = db.session.query(FunRun).count()
		assert (result == 13)
		db.session.delete(frun1)
		db.session.flush()
		result = db.session.query(FunRun).count()
		assert (result == 12)

	def test_add_themes(self):
		theme1 = Theme(id = 11, name = 'testing')
		db.session.add(theme1)
		result = db.session.query(Theme).count()
		assert (result == 11)
		db.session.delete(theme1)
		db.session.flush()
		result = db.session.query(Theme).count()
		assert (result == 10)

	def test_add_challenge(self):
		chal1 = Challenge(id = 17, name = 'testing')
		db.session.add(chal1)
		result = db.session.query(Challenge).count()
		assert (result == 17)
		db.session.delete(chal1)
		db.session.flush()
		result = db.session.query(Challenge).count()
		assert (result == 16)

	def test_add_location(self):
		location1 = Location(id = 11, name = 'testing')
		db.session.add(location1)
		result = db.session.query(Location).count()
		assert (result == 11)
		db.session.delete(location1)
		db.session.flush()
		result = db.session.query(Location).count()
		assert (result == 10)

	def test_fun_location_relationship_1(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		assert(results[0].location_id ==  1)

	def test_fun_location_relationship_2(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		assert(results[1].location_id ==  3)

	def test_fun_location_relationship_3(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		assert(results[2].location_id ==  2)

	def test_fun_location_relationship_4(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		assert(results[3].location_id ==  7)

	def test_fun_theme_relationship_1(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		theme = db.session.query(Theme).order_by(Theme.id)
		assert(results[0].funRun_theme[0] == theme[1])

	def test_fun_theme_relationship_2(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		theme = db.session.query(Theme).order_by(Theme.id)
		assert(results[1].funRun_theme[0] == theme[0])

	def test_fun_theme_relationship_3(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		theme = db.session.query(Theme).order_by(Theme.id)
		assert(results[2].funRun_theme[0] == theme[0])

	def test_fun_theme_relationship_4(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		theme = db.session.query(Theme).order_by(Theme.id)
		assert(results[2].funRun_theme[1] == theme[2])

	def test_fun_challenge_relationship_1(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		assert(results[7].funRun_challenge[0] == challenge[6])

	def test_fun_challenge_relationship_2(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		assert(results[0].funRun_challenge[1] == challenge[3])

	def test_fun_challenge_relationship_3(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		assert(results[1].funRun_challenge[0] == challenge[1])

	def test_fun_challenge_relationship_3(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		assert(results[2].funRun_challenge[0] == challenge[1])

	def test_theme_challenge_relationship_1(self):
		results = db.session.query(Theme).order_by(Theme.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		assert(results[0].theme_challenge[0] == challenge[1])
	
	def test_theme_challenge_relationship_2(self):
		results = db.session.query(Theme).order_by(Theme.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		assert(results[0].theme_challenge[1] == challenge[2])

	def test_theme_challenge_relationship_3(self):
		results = db.session.query(Theme).order_by(Theme.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		assert(results[3].theme_challenge[0] == challenge[3])

	def test_theme_challenge_relationship_4(self):
		results = db.session.query(Theme).order_by(Theme.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		assert(results[2].theme_challenge[0] == challenge[1])

if __name__ == '__main__':
	unittest.main()