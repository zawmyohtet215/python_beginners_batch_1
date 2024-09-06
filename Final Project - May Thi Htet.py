import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

def extract_title(i_tag):
    title_text = i_tag.find('a')
    title_text2 = title_text.get_text()
    final_title_text = title_text2
    
    return final_title_text

def extract_price(i_tag):
    price_text = i_tag.find('div', class_='product-item__price-list price-list')
    price_text2 = price_text.get_text()
    
    if '\n' in price_text2:
        price_text2 = price_text2.split('\n')[1]
    else:
        price_text2 = price_text2
        
    price_text3 = price_text2.replace('K','')
    price_text4 = price_text3.replace(',','')
    final_price_text = price_text4
    
    return final_price_text

url = "https://unique.com.mm/collections/dell-notebook"

headers_attributes = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/53'}

response = requests.get(url,headers = headers_attributes)



soup = BeautifulSoup(response.text, 'html.parser')

info_tags_list = soup.find_all('div', class_='product-item__info')


title_list = []
price_list = []

for info_tag in info_tags_list:
    title = extract_title(info_tag)
    price = extract_price(info_tag)
    title_list.append(title)
    price_list.append(price)
    

df = pd.DataFrame({
    'Product name': title_list,
    'Price': price_list
})

df.to_excel('dell_notebook_list_May_Thi_Htet.xlsx', index=False)




