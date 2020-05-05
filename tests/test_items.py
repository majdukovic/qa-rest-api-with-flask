"""
Created on 4 May, 2020

author: Mate Ajdukovic
"""
from http import HTTPStatus as http

from nose.tools import assert_true

from base_test import BaseTest
from services.marketplace_client import MarketplaceClient

marketplace_client = MarketplaceClient()


class TestItems(BaseTest):
    """
    This class deals with Item tests
    """

    def test_create_item(self):
        """ Verify user can create an item """

        ''' Item data '''
        item_name = 'piano'
        item_price = 339.99
        store_id = 1

        ''' Create an item'''
        item = marketplace_client.create_item(name=item_name, price=item_price, store_id=store_id)

        ''' Verify item is created and data is correct '''
        assert_true(item[0].status_code == http.CREATED,
                    "Item is not created. Received status code {} instead of {}.".format(item[0].status_code, http.CREATED))
        assert_true(item[1]['name'] == item_name, "Item name is incorrect.")
        assert_true(item[1]['price'] == item_price, "Item price is incorrect.")

    def test_get_item(self):
        """ Verify user can retrieve created item """

        ''' Item data '''
        item_name = 'chair'
        item_price = 21.99
        store_id = 1

        ''' Create an item'''
        item = marketplace_client.create_item(name=item_name, price=item_price, store_id=store_id)

        ''' Verify item is created '''
        assert_true(item[0].status_code == http.CREATED,
                    "Item is not created. Received status code {} instead of {}.".format(item[0].status_code, http.CREATED))

        item = marketplace_client.get_item(name=item_name)

        ''' Verify item is returned and data is correct '''
        assert_true(item[0].status_code == http.OK,
                    "Item is not returned. Received status code {} instead of {}.".format(item[0].status_code, http.OK))
        assert_true(item[1]['name'] == item_name, "Item name is incorrect.")
        assert_true(item[1]['price'] == item_price, "Item price is incorrect.")
