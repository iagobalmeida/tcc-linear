import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

def req(method, url, params=None, json=None, data=None):
    try:
        full_url = f'{BASE_URL}/{url}'
        request = requests.request(method=method, url=full_url, json=json, data=data, params=params)
        response = request.json()
        return response
    except:
        return None

def get(url, params=None):
    return req(method='GET', url=url, params=params)
