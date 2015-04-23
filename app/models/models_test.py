
from models.models import db, Location, FunRun, Theme, Challenge
import os
#import sql_db
import unittest
import tempfile

class TestDBModels(unittest.TestCase):

	def test_funrun(self):
		print("TESTING1")
		result = db.session.query(FunRun.id).count()
		self.assertEqual(result, 12)

	def test_themes(self):
		print("TESTING2")
		result = db.session.query(Theme.id).count()
		self.assertEqual(result, 10)

	def test_challenges(self):
		print("TESTING3")
		result = db.session.query(Challenge.id).count()
		self.assertEqual(result, 16)

	def test_location(self):
		print("TESTING4")
		result = db.session.query(Location.id).count()
		self.assertEqual(result, 10)

	def test_add_funrun(self):
		print("TESTING5")
		frun1 = FunRun(id = 13, name = 'testing')
		db.session.add(frun1)
		result = db.session.query(FunRun.id).count()
		self.assertEqual (result, 13)
		db.session.delete(frun1)
		db.session.flush()
		result = db.session.query(FunRun.id).count()
		self.assertEqual (result, 12)
		db.session.close()		

	def test_add_themes(self):
		print("TESTING6")
		theme1 = Theme(id = 11, name = 'testing')
		db.session.add(theme1)
		result = db.session.query(Theme.id).count()
		self.assertEqual (result, 11)
		db.session.delete(theme1)
		db.session.flush()
		result = db.session.query(Theme.id).count()
		self.assertEqual (result, 10)
		db.session.close()		

	def test_add_challenge(self):
		print("TESTING7")
		chal1 = Challenge(id = 17, name = 'testing')
		db.session.add(chal1)
		result = db.session.query(Challenge.id).count()
		self.assertEqual (result, 17)
		db.session.delete(chal1)
		db.session.flush()
		result = db.session.query(Challenge.id).count()
		self.assertEqual (result, 16)
		db.session.close()

	def test_add_location(self):
		print("TESTING8")
		location1 = Location(id = 11, name = 'testing')
		db.session.add(location1)
		result = db.session.query(Location.id).count()
		self.assertEqual (result, 11)
		db.session.delete(location1)
		db.session.flush()
		result = db.session.query(Location.id).count()
		self.assertEqual (result, 10)
		db.session.close()		

	def test_fun_location_relationship_1(self):
		print("TESTING9")
		results = db.session.query(FunRun).order_by(FunRun.id)
		self.assertEqual(results[0].location_id,  1)

	def test_fun_location_relationship_2(self):
		print("TESTING10")
		results = db.session.query(FunRun).order_by(FunRun.id)
		self.assertEqual(results[1].location_id,  3)

	def test_fun_location_relationship_3(self):
		print("TESTING11")
		results = db.session.query(FunRun).order_by(FunRun.id)
		self.assertEqual(results[2].location_id,  2)

	def test_fun_location_relationship_4(self):
		print("TESTING12")
		results = db.session.query(FunRun).order_by(FunRun.id)
		self.assertEqual(results[3].location_id,  7)

	def test_fun_theme_relationship_1(self):
		print("TESTING13")
		results = db.session.query(FunRun).order_by(FunRun.id)
		theme = db.session.query(Theme).order_by(Theme.id)
		self.assertEqual(results[0].funRun_theme[0], theme[1])

	def test_fun_theme_relationship_2(self):
		print("TESTING14")
		results = db.session.query(FunRun).order_by(FunRun.id)
		theme = db.session.query(Theme).order_by(Theme.id)
		self.assertEqual(results[1].funRun_theme[0], theme[0])

	def test_fun_theme_relationship_3(self):
		print("TESTING15")
		results = db.session.query(FunRun).order_by(FunRun.id)
		theme = db.session.query(Theme).order_by(Theme.id)
		self.assertEqual(results[2].funRun_theme[0], theme[0])

	def test_fun_theme_relationship_4(self):
		print("TESTING16")
		results = db.session.query(FunRun).order_by(FunRun.id)
		theme = db.session.query(Theme).order_by(Theme.id)
		self.assertEqual(results[2].funRun_theme[1], theme[2])

	def test_fun_challenge_relationship_1(self):
		print("TESTING17")
		results = db.session.query(FunRun).order_by(FunRun.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		self.assertEqual(results[7].funRun_challenge[0], challenge[6])

	def test_fun_challenge_relationship_2(self):
		print("TESTING18")
		results = db.session.query(FunRun).order_by(FunRun.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		self.assertEqual(results[0].funRun_challenge[1], challenge[3])

	def test_fun_challenge_relationship_3(self):
		print("TESTING19")
		results = db.session.query(FunRun).order_by(FunRun.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		self.assertEqual(results[1].funRun_challenge[0], challenge[1])

	def test_fun_challenge_relationship_3(self):
		print("TESTING20")
		results = db.session.query(FunRun).order_by(FunRun.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		self.assertEqual(results[2].funRun_challenge[0], challenge[1])

	def test_theme_challenge_relationship_1(self):
		print("TESTING21")
		results = db.session.query(Theme).order_by(Theme.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		self.assertEqual(results[0].theme_challenge[0], challenge[1])
	
	def test_theme_challenge_relationship_2(self):
		print("TESTING22")
		results = db.session.query(Theme).order_by(Theme.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		self.assertEqual(results[0].theme_challenge[1], challenge[2])

	def test_theme_challenge_relationship_3(self):
		print("TESTING23")
		results = db.session.query(Theme).order_by(Theme.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		self.assertEqual(results[3].theme_challenge[0], challenge[3])

	def test_theme_challenge_relationship_4(self):
		print("TESTING24")
		results = db.session.query(Theme).order_by(Theme.id)
		challenge = db.session.query(Challenge).order_by(Challenge.id)
		self.assertEqual(results[2].theme_challenge[0], challenge[1])

if __name__ == '__main__':
	unittest.main()