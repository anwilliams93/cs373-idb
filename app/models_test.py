import os
import sql_db
import unittest
import tempfile

class sql_dbTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, sql_db.app.config['DATABASE'] = tempfile.mkstemp()
        sql_db.app.config['TESTING'] = True
        self.app = sql_db.app.test_client()
        sql_db.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(sql_db.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()