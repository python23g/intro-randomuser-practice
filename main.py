import requests 
import json
from pprint import pprint

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

# print(get_content_type(url))

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

# print(get_text(url))


def text_to_dict(text: str) -> dict:
    '''convert text to dict
    
    Args:
        text (str): text of response
    
    Returns:
        str: dict
    '''
    response = requests.get(url)
    text = response.text

    return json.loads(text)

# print(text_to_dict(get_text(url)))


def get_data(url: str) -> dict:
    '''get data of response. use method json()
    
    Args:
        url (str): api url
    
    Returns:
        dict: data
    '''
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# print(get_data(url))

def get_user(url: str) -> dict:
    '''get user
    
    Args:
        url (str): api url
    
    Returns:
        dict: user
    '''
    data = get_data(url)
    return data['results'][0]

# pprint(get_user(url))

def get_users(url: str, n: int) -> list:
    '''get user
    
    Args:
        url (str): api url
        n (int): number of users
    
    Returns:
        list: list of users
    '''
    users = []
    for _ in range(n):
        user = get_user(url)
        users.append(user)

    return users

users = get_users(url, 5)

with open('users.json', 'w') as f:
    json.dump(users, f, indent=4)
    