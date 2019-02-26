from ptest.plogger import preporter
from ptest.assertion import assert_equals




def assert_response_status(response, expected_status):
    preporter.info("Checking for response status====== " + str(expected_status))
    assert_equals(response.status_code, expected_status, response.text)
