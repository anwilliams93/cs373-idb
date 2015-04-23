from api.api_test import TestAPI
from models.models_test import TestDBModels
import unittest
import sys
import threading
from io import StringIO

def run_api_tests():
	catch_api_output = StringIO()

	print("///////////////////////////////////////////// LOAD API TESTS /////////////////////////////////////////////")

	api_tests = unittest.TestLoader().loadTestsFromTestCase(TestAPI)
	print("///////////////////////////////////////////// RUN API TESTS /////////////////////////////////////////////")

	unittest.TextTestRunner(stream=catch_api_output, verbosity=2).run(api_tests)

	return catch_api_output

def run_models_tests():
	catch_model_output = StringIO()
	print("///////////////////////////////////////////// LOAD MODELS TESTS /////////////////////////////////////////////")

	model_tests = unittest.TestLoader().loadTestsFromTestCase(TestDBModels)
	print("///////////////////////////////////////////// RUN MODELS TESTS /////////////////////////////////////////////")

	unittest.TextTestRunner(stream=catch_model_output, verbosity=2).run(model_tests)

	print("///////////////////////////////////////////// TESTS DONE /////////////////////////////////////////////")	

	return catch_model_output

if __name__ == '__main__':
	runTests()