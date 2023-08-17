import requests
from bs4 import BeautifulSoup as bs
import sys

r_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}

def Trunc_str(str, length):
    if len(str) > length:
        str = str[:-(len(str) - length)]
        str += '>'
    return(str)

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

# <H1> checking
data = soup.find('h1')
print('<h1>   : ' + data.text)

print('')

# <meta description> checking
data = soup.find('meta', attrs={'name': 'description'}).get('content')
print('Description : ' + data)

print('')

# <meta robots> checking
data = soup.find('meta', attrs={'name': 'robots'}).get('content')
print('Robots : ' + data)

print('\n\n')

