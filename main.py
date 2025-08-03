#!/usr/bin/env python3
import requests

url = 'http://192.168.1.101'
urls_list = []
is_followed = {}
urls_list.append(url)

page = requests.get (url)
is_followed[url] = True

for line in page.text.split('\n'):
    if "http" in line:
        print (line)
