"""
Created on 4 May, 2020

author: Mate Ajdukovic
"""


class UrlGenerator:
    """
    This class build URLs based on the specified endpoint
    """

    # urls_map contains all endpoints
    urls_map = {
        'POST_ITEM': 'item/%s',
        'PUT_ITEM': 'item/%s',
        'GET_ITEM': 'item/%s',
        'GET_ITEMS': 'items',
        'DELETE_ITEM': 'item/%s',
        'DELETE_ITEMS': 'items',
        'POST_STORE': 'store/%s',
        'PUT_STORE': 'store/%s',
        'GET_STORE': 'store/%s',
        'GET_STORES': 'stores',
        'DELETE_STORE': 'store/%s',
        'DELETE_STORES': 'stores',
    }

    def get_url(self, api_key, *args):
        """
        Return the url based on the provided api_key and arguments.
        Arguments are used to format URL with item/store name.
        :param api_key: string - used for getting correct endpoint from urls_map
        :param args: string - name of the item or store, defaults to None
        :return: URL string
        """
        if api_key not in self.urls_map:
            raise Exception(f"API alias {api_key} is not registered in known endpoints")

        endpoint = self.urls_map[api_key]
        url = f'http://127.0.0.1:5000/{endpoint}'
        return url.format(*args)
