"""
Created on 5 May, 2020

author: Mate Ajdukovic
"""
import requests

from services.url_generator import UrlGenerator

url_generator = UrlGenerator()


class MarketplaceClient:
    """
    Client class to deal with Marketplace REST API.
    """

    def get_all_items(self):
        """
        Get all available items.
        :return: Response - http items response, json
        """
        url = url_generator.get_url(api_key='GET_ITEMS')
        headers = {'Accept': 'application/json'}
        response = requests.get(url=url, headers=headers)
        return response, response.json()

    def get_item(self, name):
        """
        Get specific item.
        :return: Response - http item response, json
        """
        url = url_generator.get_url(api_key='GET_ITEM') % name
        headers = {'Accept': 'application/json'}
        response = requests.get(url=url, headers=headers)
        return response, response.json()

    def create_item(self, name, price, store_id):
        """
        Create item with name, price and store id
        :param name: string - name of the item
        :param price: float - price of the item
        :param store_id: int - store id
        :return: Response - http item response, json
        """
        url = url_generator.get_url('POST_ITEM') % name
        headers = dict()
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        payload = {'price': price, 'store_id': store_id}
        response = requests.post(url=url, headers=headers, json=payload)
        return response, response.json()

    def create_store(self, name):
        """
        Create store
        :param name: string - name of the store
        :return: Response - http store response, json
        """
        url = url_generator.get_url('POST_STORE') % name
        headers = dict()
        headers['Accept'] = 'application/json'
        response = requests.post(url=url, headers=headers)
        return response, response.json()

    def delete_all_items(self):
        """
        Delete all items
        :return: Response - http, json
        """
        url = url_generator.get_url(api_key='DELETE_ITEMS')
        headers = {'Accept': 'application/json'}
        response = requests.delete(url=url, headers=headers)
        return response, response.json()

    def delete_all_stores(self):
        """
        Delete all stores
        :return: Response - http, json
        """
        url = url_generator.get_url(api_key='DELETE_STORES')
        headers = {'Accept': 'application/json'}
        response = requests.delete(url=url, headers=headers)
        return response, response.json()
