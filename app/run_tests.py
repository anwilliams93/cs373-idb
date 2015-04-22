from api.api_test import TestAPI
from models.models_test import TestDBModels
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
	catch_api_output = open('api/test_output.txt', "w")
	print("****************************** TESTS RUNNING ******************************")

	# catch_api_output = StringIO()
	api_tests = unittest.TestLoader().loadTestsFromTestCase(TestAPI)
	print("****************************** TESTS RUNNING ******************************")

	unittest.TextTestRunner(stream=catch_api_output, verbosity=2).run(api_tests)
	print("****************************** TESTS RUNNING ******************************")

	# catch_api_output.write("hello")
	# sys.stdout = oldStdOut
	# print("Hi" + catch_api_output.getvalue())
	catch_api_output.close()
	print("****************************** TESTS RUNNING ******************************")

	# return catch_api_output.getvalue()


	# Models
	catch_model_output = open('models/test_output.txt', "w")
	print("****************************** TESTS RUNNING ******************************")

	model_tests = unittest.TestLoader().loadTestsFromTestCase(TestDBModels)
	print("****************************** TESTS RUNNING ******************************")

	unittest.TextTestRunner(stream=catch_model_output, verbosity=2).run(model_tests)
	print("****************************** TESTS RUNNING ******************************")

	catch_model_output.close()
	print("****************************** TESTS DONE ******************************")	


if __name__ == '__main__':
	runTests()