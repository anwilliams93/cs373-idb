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
	print("///////////////////////////////////////////// OPEN API OUTPUT FILE /////////////////////////////////////////////")
	# oldStdOut = sys.stdout
	catch_api_output = open('api/test_output.txt', "w")
	print("///////////////////////////////////////////// LOAD API TESTS /////////////////////////////////////////////")

	# catch_api_output = StringIO()
	api_tests = unittest.TestLoader().loadTestsFromTestCase(TestAPI)
	print("///////////////////////////////////////////// RUN API TESTS /////////////////////////////////////////////")

	unittest.TextTestRunner(stream=catch_api_output, verbosity=2).run(api_tests)
	print("///////////////////////////////////////////// CLOSE API OUTPUT FILE /////////////////////////////////////////////")

	# catch_api_output.write("hello")
	# sys.stdout = oldStdOut
	# print("Hi" + catch_api_output.getvalue())
	catch_api_output.close()

	# return catch_api_output.getvalue()

	print("///////////////////////////////////////////// OPEN MODELS OUTPUT FILE /////////////////////////////////////////////")
	# Models
	catch_model_output = open('models/test_output.txt', "w")
	print("///////////////////////////////////////////// LOAD MODELS TESTS /////////////////////////////////////////////")

	model_tests = unittest.TestLoader().loadTestsFromTestCase(TestDBModels)
	print("///////////////////////////////////////////// RUN MODELS TESTS /////////////////////////////////////////////")

	unittest.TextTestRunner(stream=catch_model_output, verbosity=2).run(model_tests)
	print("///////////////////////////////////////////// CLOSE MODELS OUTPUT FILE /////////////////////////////////////////////")

	catch_model_output.close()
	print("///////////////////////////////////////////// TESTS DONE /////////////////////////////////////////////")	


if __name__ == '__main__':
	runTests()