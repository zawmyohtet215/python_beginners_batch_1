#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd 


# In[2]:


def extract_title(i_tag):
    title_tag = i_tag.find('a', class_='product-item__title')
    title_text = title_tag.get_text() 
    title_text2 = title_text.strip()
    Product_name = title_text2 
    
    return Product_name 

def extract_price(i_tag):
    price_text = i_tag.find('div', class_='product-item__price-list')
    price_text2 = price_text.get_text() 
    if '\n' in price_text2:
        price_text2 = price_text2.split('\n')[1]
    else:
        price_text2 = price_text2 
    price_text3 = price_text2.replace(',', '') 
    price_text4 = float(price_text3.replace('K', '')) 
    Total_price = price_text4 
    
    return Total_price 


# In[3]:


url = "https://unique.com.mm/collections/dell-notebook"  


# In[4]:


headers_attributes = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers_attributes)


# In[5]:


soup = BeautifulSoup(response.text, 'html.parser') 


# In[6]:


info_tags_list = soup.find_all('div', class_='product-item__info-inner') 


# In[7]:


name_list = []
price_list = [] 
for i in info_tags_list:
    title = extract_title(i)  
    price = extract_price(i) 
    
    name_list.append(title) 
    price_list.append(price)   
    


# In[8]:


df = pd.DataFrame({'Prdouct Name': name_list,
                  'Original Price' : price_list})  


# In[9]:


# df.to_excel('myaeemyaeehtweaung_finalproject_.xlsx', index=False)     


# In[10]:


df.to_excel('Dell Laptops - Myae Myae Htwe Aung.xlsx', index=False)


# In[11]:


df

