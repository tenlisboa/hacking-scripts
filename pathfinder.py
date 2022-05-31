import sys
import requests

def open_file(filename):
    with open(filename) as file:
        file = file.read()
        file_content = file.strip().split('\n')
        return file_content

def get_headers(token = None):
    headers = {'Content-Type': 'application/json'}

    if (token):
        headers['authorization'] = 'Bearer {}'.format(token)

    return headers

def check_if_is_valid(url, path, headers):
    full_path = url+path
    if url[-1] != '/':
        full_path = url+'/'+path
    print('Checking {}'.format(path))
    for method in ['get', 'post', 'put', 'patch', 'delete']:
        response = getattr(requests, method)(full_path, headers=headers)
        if response.status_code != 404:
            print('Method: {}, Route: {}'.format(method, full_path))
            print('Response: {}'.format(response.content or response.text))

if (len(sys.argv) < 3):
    print('You must provide a wordlist file and a target url')
    print('Ex: {} wordlist.txt https://api.com'.format(sys.argv[0]))
else:
    wordlist = sys.argv[1]
    target = sys.argv[2]
    token = None
    if (len(sys.argv) > 3):
        token = sys.argv[3]

    paths = open_file(wordlist)

    for path in paths:
        check_if_is_valid(target, path, get_headers(token))
