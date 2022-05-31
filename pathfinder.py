import sys
import requests

def open_file(filename):
    with open(filename) as file:
        file = file.read()
        file_content = file.strip().split('\n')
        return file_content

def check_if_is_valid(url, path):
    full_path = url+path
    if url[-1] != '/':
        full_path = url+'/'+path
    print('Checking {}'.format(path))
    for method in ['get', 'post', 'put', 'patch', 'delete']:
        response = getattr(requests, method)(full_path)
        if response.status_code != 404:
            print('Method: {}, Route: {}'.format(method, full_path))
            print('Response: {}'.format(response.content or response.text))


if (len(sys.argv) < 2):
    print('You must provide a wordlist file and a target url')
    print('Ex: {} wordlist.txt https://api.com'.format(sys.argv[0]))
else:
    wordlist = sys.argv[1]
    target = sys.argv[2]

    paths = open_file(wordlist)

    for path in paths:
        check_if_is_valid(target, path)
