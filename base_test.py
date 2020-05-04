import requests
from nose.tools import assert_true
from http import HTTPStatus as http

class BaseTest:
    """This class deals with setting the environment to the initial state"""

    def setup(self):
        """
        Delete all items and stores before tests start
        :return: None
        """
        url = 'http://127.0.0.1:5000/items'
        headers = {'Accept': 'application/json'}
        response = requests.delete(url=url, headers=headers)
        assert_true(response.status_code == http.OK, "Recived {} instead of {}".format(response.status_code, http.OK))

        url = 'http://127.0.0.1:5000/stores'
        headers = {'Accept': 'application/json'}
        response = requests.delete(url=url, headers=headers)
        assert_true(response.status_code == http.OK, "Recived {} instead of {}".format(response.status_code, http.OK))
