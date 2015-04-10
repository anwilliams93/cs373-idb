
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

    # def test_challenges(self):
    # 	result = db.session.query(Challenge).count()
    # 	assert (result == 16)

    # def test_location(self):
    # 	result = db.session.query(Location).count()
    # 	assert (result == 10)

    # def test_add_funrun(self):
    # 	frun1 = FunRun(name = 'testing')
    # 	db.session.add(frun1)
    # 	result = db.session.query(FunRun).count()
    # 	assert (result == 13)
    # 	db.session.flush()
    # 	assert (result == 12)



if __name__ == '__main__':
    unittest.main()