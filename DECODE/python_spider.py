from bs4 import BeautifulSoup
import requests
import os

# input_image = input('請輸入要下載的圖片')

response = requests.get(f'https://unsplash.com/s/photos/motorcycle-riders')
soup = BeautifulSoup(response.text, 'lxml')

results = soup.find_all('img', {'class':'tB6UZ a5VGX'}, limit=50)

image_link = [result.get('src') for result in results]

for index, link in enumerate(image_link):
    img = requests.get(link)
    
    if not os.path.exists('images'):
        os.mkdir('images')
        
    img = requests.get(link)
    
    with open('images\\' + str(index + 1) + '.jpg', 'wb') as file:
        file.write(img.content)
