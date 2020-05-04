import requests

from services.url_generator import UrlGenerator

url_generator = UrlGenerator()

class MarketplaceClient:

    def get_all_items(self):
        url = url_generator.get_url(api_key='GET_ITEMS')
        headers = {'Accept': 'application/json'}
        response = requests.get(url=url, headers=headers)
        return response, response.json()

    def create_item(self, name, price, store_id):
        url = url_generator.get_url('POST_ITEM') % name
        headers  = dict()
        headers['Accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        payload = {'price': price,'store_id': store_id}
        response = requests.post(url=url, headers=headers, json=payload)
        return response, response.json()

    def create_store(self, name):
        url = url_generator.get_url('POST_STORE') % name
        headers  = dict()
        headers['Accept'] = 'application/json'
        response = requests.post(url=url, headers=headers)
        return response, response.json()
