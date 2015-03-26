from io       import StringIO
from unittest import main, TestCase
import urllib.request, codecs, json

server_address = 'http://104.239.139.43:8000'

def http_response_to_json_object (response) :
	reader = codecs.getreader("utf-8")
	return json.load(reader(response))

class TestAPI (TestCase) :

	def test_root_1 (self) :
		url = server_address + '/api'
		response = urllib.request.urlopen(url)
		response_object = http_response_to_json_object(response)
		expected = 	{'urls':	{
			              		"funruns_url": "/funruns",
			                	"themes_url": "/themes",
			                	"challenges_url": "/challenges"
			            		}
					}
		self.assertEqual(list(response_object), list(expected))

if __name__ == "__main__" :
    main()