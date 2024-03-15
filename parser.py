import requests
from bs4 import BeautifulSoup

url= 'https://dedmorozural.ru/'
responce = requests.get(url)
print(responce.status_code)
#print(responce.text)

soup = BeautifulSoup(responce.text, 'html.parser')
print(soup.title)
print(type(soup.title))

print(soup.a)
print(soup.a.string)

print(soup.a.get('href'))

images_tags = soup.find_all('img')
for image_tags in images_tags:
    print(image_tags)

a_tags = soup.find_all('a')
for a_tags in a_tags:
    print(a_tags)

big_body_div = soup.find( 'div', class_ = 'modulebode1')

print(big_body_div)