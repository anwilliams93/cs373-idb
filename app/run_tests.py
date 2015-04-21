from api.api_test import TestAPI
import unittest
import sys
from io import StringIO

def runTests():
	# Keep it ugly for now so I can figure out how to do it without a file

	# stream = StringIO()
	# runner = unittest.TextTestRunner(stream = stream)
	# result = runner.run(unittest.makeSuite(TestAPI))
	# stream.seek(0)
	# return stream.read()
	print("****************************** TESTS RUNNING ******************************")
	# oldStdOut = sys.stdout
	catchOutput = open('test_output.txt', "w")
	# catchOutput = StringIO()
	testCatcher = unittest.TestLoader().loadTestsFromTestCase(TestAPI)
	unittest.TextTestRunner(stream=catchOutput, verbosity=2).run(testCatcher)
	# catchOutput.write("hello")
	# sys.stdout = oldStdOut
	# print("Hi" + catchOutput.getvalue())
	catchOutput.close()
	# return catchOutput.getvalue()
	print("****************************** TESTS DONE ******************************")	


if __name__ == '__main__':
	runTests()