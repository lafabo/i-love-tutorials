from nose.tools import *
import re

def assert_responce(resp, contains=None, mathces=None, headers=None, status='200'):

	assert status in resp.status, "Expected response %r not in %r" % (status, resp.status)

	if status == '200':
		assert resp.data, 'Response data is empty'

	if contains:
		assert contains in resp.data, "Response does not contain %r" % contains

	if mathces:
		reg = re.compile(mathces)
		assert  reg.matches(resp.data), "Response does not match %r" % mathces

	if headers:
		assert _equal(resp.headers, headers)