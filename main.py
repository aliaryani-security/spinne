#!/usr/bin/env python3
import requests

url = 'http://192.168.1.101'
urls_list = []
urls_list.append(url)

page = requests.get (url)
print (page.text)