
from django.shortcuts import render
from bs4 import BeautifulSoup
from splinter import Browser
import requests, csv



def home(request):
    return render(request, 'home.html')

# # Gets the website
# source = requests.get('http://coreyms.com').text 

# # converts into readable lxml format
# soup = BeautifulSoup(source, 'lxml') 

# # finds the tag
# article = soup.find('article') 

# # finds (div inside article with class) -> p -> text 
# summary = article.find('div', class_='entry-content').p.text

#  # finds (iframe inside article with class) and gets the attribute value of src
# vid_src = article.find('iframe', class_='youtube-player')['src']

# # vid_src (Output) : 
# # https://www.youtube.com/embed/-nh9rCzPJ20?version=3&rel=1&fs=1&autohide=2&
# # showsearch=0&showinfo=1&iv_load_policy=1&wmode=transparent

# # splits the src based on '/' and shows the 4th element
# vid_id = vid_src.split('/')[4] 

# # splits the src based on '?' and shows the 4th element
# vid_id = vid_id.split('?')[0]

# # Concatination
# youtube_link = f'https://youtube.com/watch?v={vid_id}'
# print(f'WATCH : {youtube_link}') 

# ////////////////////////////////////////////////////////

# source = requests.get('https://www.swiggy.com/restaurants/truffles-2nd-block-kammanahalli-kalyan-nagar-bangalore-27341').text
# soup = BeautifulSoup(source, 'lxml')

# csv_file = open('Swiggy Scrapped.csv', 'w')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Category', 'Name', 'Price', 'Type'])

# for cat in soup.find_all('div', class_='_2dS-v'):
#     print(' -------------------------')
#     cate = cat.h2.text
#     print(f' Category : {cate}')
#     print(' -------------------------')
#     for item in cat.find_all('div', class_='_2wg_t'):
#         try:
#             types = item.find('span', class_='_3x58u')
#             if types == None:
#                 types = "Veg"
#             else:
#                 types = "Non Veg"
#         except Exception as e:
#             types = 'Veg'

#         print(f' {types} : ')
#         name = item.find('div', class_='jTy8b').text
#         print(f' {name}')
#         price = item.find('span', class_='bQEAj').text
#         print(f' ₹ {price}')
#         print(' --------------')
#         csv_writer.writerow([cate, name, price, types])
# csv_file.close()

with Browser() as browser:
    url = 'https://www.swiggy.com/restaurants/truffles-2nd-block-kammanahalli-kalyan-nagar-bangalore-27341'
    browser.visit(url)
    button = browser.find_by_css('div[class="_1zVBl"]')
    button.click()