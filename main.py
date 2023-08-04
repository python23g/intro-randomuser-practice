import requests 
from pprint import pprint
import json
url = 'https://randomuser.me/api/'


def get_version():
    '''get requests module'''
    return requests.__version__


def get_status_code(url: str) -> int:
    '''get status code of response
    
    Args:
        url (str): api url
    
    Returns:
        str: status code of response
    '''
    response = requests.get(url)
    
    return response.status_code

# print(get_status_code(url))


def get_content_type(url: str) -> str:
    '''get content type of response
    
    Args:
        url (str): api url
    
    Returns:
        str: content type of response
    '''
    # send request  to api
    response = requests.get(url)
    
    # get headers of response
    headers = response.headers

    # get content type of response
    return headers['Content-Type']



def get_headers(url: str) -> dict:
    '''get headers of response
    
    Args:
        url (str): api url
    
    Returns:
        str: headers of response
    '''
    response = requests.get(url)

    return response.headers


# print(get_headers(url))

def get_text(url: str) -> str:
    '''get text of response
    
    Args:
        url (str): api url
    
    Returns:
        str: text of response
    '''
    
    response = requests.get(url)
    return response.text


def text_to_dict(text: str) -> dict:
    '''convert text to dict
    
    Args:
        text (str): text of response
    
    Returns:
        str: dict
    '''
    
    response = requests.get(url)
    text = response.text
    js = json.loads(text)
    return js


def get_data(url: str) -> dict:
    '''get data of response. use method json()
    
    Args:
        url (str): api url
    
    Returns:
        dict: data
    '''
    response = requests.get(url)
    return response.json()

def get_user(url: str) -> dict:
    '''get user
    
    Args:
        url (str): api url
    
    Returns:
        dict: user
    '''
    response = requests.get(url)
    text = response.text
    js = json.loads(text)
    return js['results']

def get_users(url: str, n: int) -> list:
    '''get user
    
    Args:
        url (str): api url
        n (int): number of users
    
    Returns:
        list: list of users
    '''
    list = []
    for _ in range(n):
        response = requests.get(url)
        text = response.text
        js = json.loads(text)
        list.append(js)
    return list