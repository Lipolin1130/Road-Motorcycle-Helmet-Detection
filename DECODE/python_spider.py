from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import os

ua = UserAgent()
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183"}
# input_image = input('請輸入要下載的圖片')
response = requests.get(f'https://www.soonnet.org/albumviewPhotostream?id=112617&currentPage=1&activename=photo&currentSize=72&Sorting=&sortASC=ascending', headers=header)

# response.encoding = 'utf-8'
# print(response)
soup = BeautifulSoup(response.text, 'lxml')
print(soup)
# results = soup.find_all('img', {'lazy':'loaded'}, limit=72)
results = soup.find_all('img')
# print(results)

image_link = [result.get('src') for result in results]


# for index, link in enumerate(image_link):
#     img = requests.get(link)
    
#     if not os.path.exists('images'):
#         os.mkdir('images')
        
#     img = requests.get(link)
    
#     with open('images\\' + str(index + 1) + '.jpg', 'wb') as file:
#         file.write(img.content)