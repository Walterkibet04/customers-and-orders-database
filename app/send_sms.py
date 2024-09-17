import requests

url = "https://api.sandbox.africastalking.com/version1/messaging"

headers = {'ApiKey': 'atsk_b8697ec5a31f5bfc0a6c6a771ad43dfaaaef28ef10e8a43bb40716033ea7dc59e66061f0', 
           'Content-Type': 'application/x-www-form-urlencoded',
           'Accept': 'application/json'}

data = {'username': 'sandbox',
        'from': '19977',
        'message': "Hello world !",
        'to': '+254708783067'}


def make_post_request():  
    response = requests.post( url = url, headers = headers, data = data )
    return response


print( make_post_request().json() )