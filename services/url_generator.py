class UrlGenerator:

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
        if api_key not in self.urls_map:
            raise Exception(f"API alias {api_key} is not registered in known endpoints")

        endpoint = self.urls_map[api_key]
        url = f'http://127.0.0.1:5000/{endpoint}'
        return url.format(*args)
