
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
    	assert (result == 17)
    	db.session.delete(Location1)
    	db.session.flush()
    	result = db.session.query(Location).count()
    	assert (result == 16)




if __name__ == '__main__':
    unittest.main()