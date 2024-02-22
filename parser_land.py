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
    'Twitter image height:':"twitter:image:height",
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

# url = "https://uxuidesign.m.goit.global/ua/course/2/"
# url = "https://test-qa.softryzen.com/" - from my test task, lot of errors
# url = "https://startpagetest.lp.goit.global/ua/dev/"
# url = "https://doctor-voitsitskyi.com.ua/uk"


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

# Open Graph markup checking
Sec_header('Open Graph markup')
for i in OG.keys():
    data = get_tag('meta', {'property': OG.get(i)}, 'content')
    print(i, str(data))
print('------------')
for i in TWI.keys():
    data = get_tag('meta', {'name': TWI.get(i)}, 'content')
    print(i, str(data))

print('')

# Content image checking
Sec_header('Content image checking')
format = '%-4s %-4s %-5s %-32s %-30s'
print(format % ('W', 'H', 'Lazy', 'Alt', 'Src'))
print('                                                 Srcset   ')
print('----------------------------------------------------------')
data = soup.find_all('img')
count = 0
for i in data:
    w = i.get('width')
    h = i.get('height')
    lazy = i.get('loading')
    alt = i.get('alt')
    alt = Trunc_str(str(alt), 31)
    src = i.get('src')
    srcset = i.get('srcset')
    print(format % (str(w), str(h), str(lazy), str(alt), str(src)))
    print(format % (' ', ' ', ' ', ' ', str(srcset)))
    # print ('')
    count += 1
if count == 0:
    print('     << No content images on the webpage >>')
total_count(str(count))

print('')

# Checking of links
Sec_header('Link review')
format = '%-18s %-18s %-40s %-8s %-25s'
print(format % ('Text','aria-label=', 'rel=', 'target=', 'href='))
print('---------------------------------------------------------------------------------------------')
data = soup.find_all('a')
count = 0
for i in data:
    text = i.text
    aria = i.get('aria-label')
    rel = i.get('rel')
    target = i.get('target')
    href = i.get('href')
    text = Trunc_str(str(text), 17)
    aria = Trunc_str(str(aria), 17)
    print(format % (text, aria, str(rel), str(target), str(href)))
    count += 1
if count == 0:
    print('     << No links on the webpage >>')
total_count(str(count))

print('')

# Checking of buttons
Sec_header('Button review')
format = '%-28s %-28s %-40s'
print(format % ('Text','aria-label=', 'type='))
print('-----------------------------------------------------------')
data = soup.find_all('button')
count = 0
for i in data:
    text = i.text
    aria = i.get('aria-label')
    type = i.get('type')
    text = Trunc_str(str(text), 27)
    aria = Trunc_str(str(aria), 27)
    print(format % (text, aria, str(type)))
    count += 1
if count == 0:
    print('     << No buttons on the webpage >>')
total_count(str(count))

print('')

