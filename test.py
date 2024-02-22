import requests
from bs4 import BeautifulSoup as bs
import sys

r_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
OG = {
    'OG type      :':"og:type",
    'OG title     :':"og:title",
    'OG descr     :':"og:description",
    'OG URL       :':"og:url",
    'OG Site Name :':"og:site_name",
    'OG Locale    :':"og:locale",
    'OG image     :':"og:image"
}
TWI = {
    'Twitter card        :':"twitter:card",
    'Twitter title       :':"twitter:title",
    'Twitter descr       :':"twitter:description",
    'Twitter image       :':"twitter:image",
    'Twitter image width :':"twitter:image:width",
    'Twitter image heigh :':"twitter:image:heigh",
    'Twitter image alt   :':"twitter:image:alt",
    'Twitter URL         :':"twitter:url"
}

# Return the get_attr value from name tag with attr
# 
def get_tag(name, attr, get_attr):
    data = soup.find(name, attrs=attr)
    try:
        data = data.get(get_attr)
    except:
        data = None
    return(data)

# Return the get_attr value from name tag with attr
# 
def get_text(name):
    # data = soup.find('title').text
    data = soup.find(name)
    try:
        data = data.text
    except:
        data = None
    return(data)

def Sec_header(h_name):
    l = ""
    for i in range(0, len(h_name)):
        l += "="
    print(h_name)
    print(l)

def Trunc_str(str, length):
    if len(str) > length:
        str = str[:-(len(str) - length)]
        str += '>'
    return(str)

def total_count(count):
    print('-------------------\nTotal : ', str(count))

#Getting the URL from 1st parameter of the command string
try:
    url = sys.argv[1]
except IndexError:
    print('\n' + 'Usage : python parser_land.py <URL>' + '\n')
    quit()

print(' ')

# Getting the webpage code
r = requests.get(url, headers=r_headers)
Sec_header('Response code : ' + str(r.status_code))

# Formatting the webpage code
soup = bs(r.text, 'lxml')

# Canonical string checking
data = get_tag('link', {'rel': 'canonical'}, 'href')
print('Webpage   : ' + url)
print('Canonical : ' + str(data))

print('')

# <title> checking
# data = soup.find('title').text
data = get_text('title')
print('<title>   : ' + str(data))

print('')

# <meta description> checking
data = get_tag('meta', {'name': 'description'}, 'content')
print('<meta description> tag : ' + str(data))

print('')

# <meta robots> checking
data = get_tag('meta', {'name': 'robots'}, 'content')
print('<meta robots> tag : ' + str(data))

print('')

# Sandbox area:



