# requests module

working with requests

## install requests
```bash
pip install requests
```

## working with requests module

`/main.py`

### import module and url
```python
import requests

url = 'https://randomuser.me/api/'
```

### get_version()
```python
def get_version():
    '''get requests module'''
    pass
```

### get_status_code()
```python
def get_status_code(url: str) -> int:
    '''get status code of response
    
    Args:
        url (str): api url
    
    Returns:
        str: status code of response
    '''
    pass
```

### get_headers()
```python
def get_headers(url: str) -> dict:
    '''get headers of response
    
    Args:
        url (str): api url
    
    Returns:
        str: headers of response
    '''
    pass
```

### get_content_type()
```python
def get_content_type(url: str) -> str:
    '''get content type of response
    
    Args:
        url (str): api url
    
    Returns:
        str: content type of response
    '''
    pass
```

### get_text()
```python
def get_text(url: str) -> str:
    '''get text of response
    
    Args:
        url (str): api url
    
    Returns:
        str: text of response
    '''
    pass
```

### text_to_dict()
```python
def text_to_dict(text: str) -> dict:
    '''convert text to dict
    
    Args:
        text (str): text of response
    
    Returns:
        str: dict
    '''
    pass
```

### get_data()
```python
def get_data(url: str) -> dict:
    '''get data of response. use method json()
    
    Args:
        url (str): api url
    
    Returns:
        dict: data
    '''
    pass
```

### get_user()
```python
def get_user(url: str) -> dict:
    '''get user
    
    Args:
        url (str): api url
    
    Returns:
        dict: user
    '''
    pass
```

### get_users()
```python
def get_users(url: str, n: int) -> list:
    '''get user
    
    Args:
        url (str): api url
        n (int): number of users
    
    Returns:
        list: list of users
    '''
    pass
```