import requests
from bs4 import BeautifulSoup as bs
import sys

r_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
OG = {
    'OG type  :':"og:type",
    'OG URL   :':"og:url",
    'OG title :':"og:title",
    'OG descr :':"og:description",
    'OG image :':"og:image",
    'Twi card  :':"twitter:card",
    'Twi URL   :':"twitter:url",
    'Twi title :':"twitter:title",
    'Twi descr :':"twitter:description",
    'Twi image :':"twitter:image"
}

def Sec_header(h_name):
    l = ""
    for i in range(0, len(h_name)):
        l = l + "="
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
# url = "https://startpagetest.lp.goit.global/ua/"
# url = "https://softryzen.goit.global/test-quiz/" - strange webpage, unusual behavior on run

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
# data = soup.find('link', rel='canonical').get('href')
data = soup.find('link', attrs={'rel': 'canonical'})
try:
    data = data.get('href')
except:
    data = None
print('Webpage   : ' + url)
print('Canonical : ' + str(data))

print('')

# <title> checking
data = soup.find('title').text
print('<title>   : ' + data)

print('')

# <meta description> checking
data = soup.find('meta', attrs={'name': 'description'})
try:
    data = data.get('content')
except:
    data = None
print('<meta description> tag : ' + str(data))

print('')

# <meta robots> checking
data = soup.find('meta', attrs={'name': 'robots'})
try:
    data = data.get('content')
except:
    data = None
print('Robots : ' + str(data))

print('')

# Open Graph markup checking
Sec_header('Open Graph markup')
# for i in OG.keys():
#     print(i, soup.find('meta', property=OG.get(i)).get('content'))
for i in OG.keys():
    data = soup.find('meta', attrs={'property': OG.get(i)})
    try:
        data = data.get('content')
    except:
        data = None
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
    alt = Trunc_str(alt, 31)
    # if len(alt) > 31:
    #     alt = alt[:-(len(alt) - 31)]
    #     alt += '>'
    src = i.get('src')
    srcset = i.get('srcset')
    count += 1
    print(format % (str(w), str(h), str(lazy), str(alt), str(src)))
    print(format % (' ', ' ', ' ', ' ', str(srcset)))
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
    text = Trunc_str(text, 17)
    aria = Trunc_str(str(aria), 17)
    print(format % (text, aria, str(rel), str(target), str(href)))
    count += 1
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
    text = Trunc_str(text, 27)
    aria = Trunc_str(str(aria), 27)
    print(format % (text, aria, str(type)))
    count += 1
total_count(str(count))

print('')

# print(r.content)

# soup = bs(r.text, 'lxml')

# data = soup.find_all('div', class_="w-full rounded border")

# for i in data:
#     name = i.find('h4').text.replace("\n", "")
#     price = i.find('h5').text
#     url_img = "https://scrapingclub.com" + i.find('img', class_='card-img-top img-fluid').get('src')

#     print('\n' + name + '\n' + price + '\n' + url_img + '\n')

