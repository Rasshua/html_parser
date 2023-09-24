import requests
from bs4 import BeautifulSoup as bs
import sys

r_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

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

#Getting the URL from the 1st parameter of the command string
try:
    url = sys.argv[1]
except IndexError:
    print('\n' + 'Usage : python parser_land.py <URL>' + '\n')
    quit()

# url = "https://uxuidesign.m.goit.global/ua/course/2/"

# Getting the webpage code
r = requests.get(url, headers=r_headers)
print('\nResponse code : ' + str(r.status_code))
print('-------------------')

# Formatting the webpage code
soup = bs(r.text, 'lxml')

print(' ')

# Sandbox area

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
    # print(format % (text, aria, str(rel), str(target), str(href)))
    print(text, aria, str(rel), str(target), str(href))
    count += 1

    input('press enter')
total_count(str(count))

print('')

