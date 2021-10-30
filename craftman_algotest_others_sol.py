import base64
import itertools
import requests  # install request to make this work "pip install requests"

# base64 encoded randomly indexed array, splitted after every 50 char.
url = ["LmNvbQ",
       "aGFpYjk3NDclNDBnbWFpbC5jb20tTnpnazl2ZVM5bGRvYnlPVS",
       "ZlbnRyeS4xOTU0MDUwMzA0PXByby5zYWhhaWI5NzQ3QGdtYWls",
       "50cnkuMTAxMzkwOTE1PVpHdHNtaXkweUZiUnhPSmYtcHJvLnNh",
       "lwUUxTZS1nQUx1eFBKanJPVEZ2MnpCX0FSQVFBbEtGRHlYdTVS",
       "aHR0cHM6Ly9kb2NzLmdvb2dsZS5jb20vZm9ybXMvZC9lLzFGQU",
       "b2xHcGxablNvLUw2akFBL3ZpZXdmb3JtP3VzcD1wcF91cmwmZW"]


def decoder(item):
    """ this function will return decoded text from base64"""
    item += '=='
    item = base64.b64decode(item).decode('latin-1')
    return item


# dict of urls to make permutations
urls = {
    'a': url[0],
    'b': url[1],
    'c': url[2],
    'd': url[3],
    'e': url[4],
    'f': url[5],
    'g': url[6]
}

# make permutaions
combo = itertools.permutations([
    urls['a'],
    urls['b'],
    urls['c'],
    urls['d'],
    urls['e'],
    urls['f'],
    urls['g']
])

# filter all the linkes by the root url, root url is: f(manually checked)
# before filtering there will 5000+ rows, after filtering it will be around 720rows.

filtered_urls = []

for ur in combo:
    url = ''.join(ur)

    if urls['f'] == url[:50]:
        filtered_urls.append(url)

# validating process
count = 1
for data in filtered_urls:
    url = decoder(data)  # decode
    if not url.endswith("pro.sahaib9747@gmail.com"):
        continue
    # send request to check that is it valid link or not
    res = requests.get(url)
    if res.ok:
        print(f"Correct Decoded URL: {url}")
        print(res.status_code)
        print(f"Response URL: {res.url}")
        break
    else:
        print(f"Invalid ID: {count} url: {url}\n")

    count += 1
