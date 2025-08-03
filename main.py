#!/usr/bin/env python3
import requests

url = 'https://kernel.org/'
urls_list = []
is_followed = {}
urls_list.append(url)

page = requests.get (url)
is_followed[url] = True
start = "http"
end = ''
for line in page.text.split('\n'):
    if "http" in line:
        if "kernel.org" in line:
            if '">' in line:
                end = '">'
            else:
                end = '" '
            try:
                sliced = line[line.index(start):line.index(end)]
                if '"' in sliced:
                    end = '"'
                    print (sliced[sliced.index(start):sliced.index(end)])
                else:
                    print (sliced)
            except:
                continue
