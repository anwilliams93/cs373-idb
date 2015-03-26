import os
import api
import unittest
import tempfile

class ApiTestCase(unittest.TestCase):

    #def setUp(self):
        #self.db_fd, api.app.config['DATABASE'] = tempfile.mkstemp()
        #api.app.config['TESTING'] = True
        #self.app = api.app.test_client()
        #api.init_db()

   # def tearDown(self):
    #    os.close(self.db_fd)
    #   os.unlink(api.app.config['DATABASE'])

    def test_empty_db(self):
    	rv = self.get_run_themes(0)
    	assert list({
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
			    }) == list(rv)


if __name__ == '__main__':
    unittest.main()