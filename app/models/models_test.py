
from models import db, Location, FunRun, Theme, Challenge
import os
#import sql_db
import unittest
import tempfile

class sql_dbTestCase(unittest.TestCase):

	# def setUp(self):
	#     self.db_fd, sql_db.app.config['DATABASE'] = tempfile.mkstemp()
	#     sql_db.app.config['TESTING'] = True
	#     self.app = sql_db.app.test_client()
	#     sql_db.init_db()

	# def tearDown(self):
	#     os.close(self.db_fd)
	#     os.unlink(sql_db.app.config['DATABASE'])

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
		print(" here1 = " results[1].location_id)
		assert(results[1].location_id ==  1)

	def test_fun_location_relationship_3(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		print(" here1 = " results[2].location_id)
		assert(results[2].location_id ==  1)

	def test_fun_location_relationship_4(self):
		results = db.session.query(FunRun).order_by(FunRun.id)
		print(" here1 = " results[3].location_id)
		assert(results[3].location_id ==  1)




if __name__ == '__main__':
	unittest.main()