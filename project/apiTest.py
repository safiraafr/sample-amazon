from pprint import pprint
import requests


# endpoint get all products
class Test_getAll:
    base_url = 'https://fakestoreapi.com/products'

    responseFetch = requests.get(base_url)
    statusFetch = responseFetch.status_code
    print(statusFetch)

    if statusFetch == 200:
        pprint(responseFetch.json())
        assert len(responseFetch.json()) > 1

    else:
        print("False")

# endpoint get single product by id
class Test_getOne:
    id = 1
    base_url = 'https://fakestoreapi.com/products'
    response = requests.get(f'{base_url}/{id}')
    pprint(response.json())