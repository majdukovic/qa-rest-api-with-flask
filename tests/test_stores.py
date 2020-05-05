"""
Created on 4 May, 2020

author: Mate Ajdukovic
"""
from http import HTTPStatus as http

from nose.tools import assert_true

from base_test import BaseTest
from services.marketplace_client import MarketplaceClient

marketplace_client = MarketplaceClient()


class TestStores(BaseTest):
    """
    This class deals with Stores tests
    """

    def test_create_store(self):
        """ Verify user can create store """

        ''' Store data '''
        store_name = 'Music instruments'

        ''' Create store'''
        store = marketplace_client.create_store(name=store_name)

        ''' Verify item is created and data is correct '''
        assert_true(store[0].status_code == http.CREATED,
                    "Store is not created. Received status code {} instead of {}.".format(store[0].status_code, http.CREATED))
        assert_true(store[1]['name'] == store_name, "Store name is incorrect.")
