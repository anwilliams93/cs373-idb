from test.tests import TestAPI
import unittest
from io import StringIO

def runTests():
	stream = StringIO()
	runner = unittest.TextTestRunner(stream = stream)
	result = runner.run(unittest.makeSuite(TestAPI))
	stream.seek(0)
	return stream.read()