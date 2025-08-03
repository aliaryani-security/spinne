#!/usr/bin/env python3
import requests

url = 'https://wikipedia.org'
urls_list = []
is_followed = {}
urls_list.append(url)

def check_url_list (url) -> bool:
    if url in urls_list:
        return True
    else:
        return False
def check_follow (url) -> bool:
    for entry in is_followed.keys():
        if url != entry:
            return False
        else:
            if is_followed[url]:
                return True
            else:
                return False

start = "http"
end = ''
try:
    for URL in urls_list:
        if check_follow(URL) != True:
            try:
                page = requests.get (URL)
            except:
                continue
            is_followed[URL] = True
        for line in page.text.split('\n'):
            if "http" in line:
                if "wikipedia.org" in line:
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
                            is_followed[parsed_url] = False
                    except:
                        continue
finally:
    for url in urls_list:
        print (url)