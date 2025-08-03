#!/usr/bin/env python3
import requests

url = 'https://kernel.org/'
urls_list = []
is_followed = {}
urls_list.append(url)

def check_url_list (url) -> bool:
    if url in urls_list:
        return True
    else:
        return False

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
                    parsed_url = sliced[sliced.index(start):sliced.index(end)]
                else:
                    parsed_url = sliced
                if check_url_list(parsed_url) == False:
                    urls_list.append (parsed_url)
            except:
                continue

print (urls_list)