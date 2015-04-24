from api.api_test import TestAPI
from api.api_sorting_challenges_test import TestChallengesSort
from api.api_sorting_locations_test import TestLocationsSort
from api.api_filtering_themes_test import TestThemesFilter
from api.api_filtering_challenges_test import TestChallengeFilter
from api.loc_filter_test import TestLocationFilter
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

def run_challenges_sort_tests():
	catch_api_output = StringIO()	
	api_tests = unittest.TestLoader().loadTestsFromTestCase(TestChallengesSort)
	unittest.TextTestRunner(stream=catch_api_output, verbosity=2).run(api_tests)
	return catch_api_output

def run_locations_sort_tests():
	catch_api_output = StringIO()	
	api_tests = unittest.TestLoader().loadTestsFromTestCase(TestLocationsSort)
	unittest.TextTestRunner(stream=catch_api_output, verbosity=2).run(api_tests)
	return catch_api_output	

def run_filtering_sort_tests():
	catch_api_output = StringIO()	
	api_tests = unittest.TestLoader().loadTestsFromTestCase(TestThemesFilter)
	unittest.TextTestRunner(stream=catch_api_output, verbosity=2).run(api_tests)
	return catch_api_output	

def run_filtering_challenges_tests():
	catch_api_output = StringIO()	
	api_tests = unittest.TestLoader().loadTestsFromTestCase(TestChallengeFilter)
	unittest.TextTestRunner(stream=catch_api_output, verbosity=2).run(api_tests)
	return catch_api_output

def run_filtering_locations_tests():
	catch_api_output = StringIO()	
	api_tests = unittest.TestLoader().loadTestsFromTestCase(TestLocationFilter)
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