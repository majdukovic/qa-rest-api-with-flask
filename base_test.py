"""
Created on 4 May, 2020

author: Mate Ajdukovic
"""
from http import HTTPStatus as http

from nose.tools import assert_true

from services.marketplace_client import MarketplaceClient

marketplace_client = MarketplaceClient()


class BaseTest:
    """
    This class deals with setting the environment to the initial state
    """

    def setup(self):
        """
        Delete all items and stores before tests start
        :return: None
        """

        ''' Delete all items '''
        items = marketplace_client.delete_all_items()
        assert_true(items[0].status_code == http.OK, "Received {} instead of {}".format(items[0].status_code, http.OK))

        ''' Delete all stores '''
        stores = marketplace_client.delete_all_stores()
        assert_true(stores[0].status_code == http.OK, "Received {} instead of {}".format(items[0].status_code, http.OK))
