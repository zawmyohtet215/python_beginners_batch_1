#!/usr/bin/env python
# coding: utf-8

# In[25]:


# Step1.Request data from the URL
#Step2.Create Beautifulsoup object
#Step3. Find info tags using find_all
#Step4.Extract data for each info tag


# In[26]:


#pip install beautifulsoup4
#pip install requests


# In[27]:


#pip install beautifulsoup4


# In[1]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[2]:


# define url
url="https://unique.com.mm/collections/dell-notebook"


# In[3]:


#set header to pretend as a browswer
headers_attributes = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers_attributes)
print(response.text)


# In[4]:


#   convert as beautifulsoup object
soup=BeautifulSoup(response.text,'html.parser')


# In[5]:


# extract all tags from soup object
info_tags_list = soup.find_all('div', class_='product-item__info')


# In[6]:


############### change as function ###################

# extract title function
def extract_title(i_tag):
    # extract title tag
  
  #  title_tag = i_tag.find('div', class_='product-item__info-inner')
    title_tag = i_tag.find('a', class_='product-item__title text--strong link')
    # extract text
    title_text = title_tag.get_text()
    # use strip() to remove newlines
    title_text2 = title_text.strip()
    # replace new line character with - by using replace() method
    if '\n' in title_text2:
        title_text3 = title_text2.replace('\n', '')
    else:
        title_text3 = title_text2
    # change variable name
    final_title_text = title_text3
    
    return final_title_text


# In[7]:


extract_title(info_tags_list[2])


# In[8]:


# extract price function
def extract_price(t_tag):
    #extract price tag
    price_text = t_tag.find('div', class_='product-item__price-list price-list')
   # extract price text using get_text() method
    price_text2=price_text.get_text()
    #remove,
    price_text3=price_text2.replace(',','')
     #estract old price if there is a discount price
    if '\n' in price_text3:
        price_text3=price_text3.split('\n')[1]
    else:
        price_text3=price_text3
    #remove 'Ks'
    price_text4 = float(price_text3.replace('K',''))
    # change variable name
    final_price_text = price_text4
    return final_price_text


# In[9]:


def extract_inv(i_tag):
    #extract inventory tag
    inv_text=i_tag.find('span',class_='product-item__inventory inventory')
    if inv_text is not None:
        #extract price text using get_text() method
        inv_text2=inv_text.get_text()
         #remove,
        inv_text3=inv_text2.replace('\'','')
        final_inv_text=inv_text3
    else :
        final_inv_text="Element not found"
    return final_inv_text
        


# In[10]:


extract_title(info_tags_list[2])


# In[11]:


extract_price(info_tags_list[2])


# In[12]:


extract_inv(info_tags_list[2])


# In[13]:


# extract all tags from soup object
info_tags_list = soup.find_all('div', class_='product-item__info')


# In[14]:


title_list=[]
price_list=[]
inv_list=[]
count=0
for info_tag in (info_tags_list):
    title = extract_title(info_tag)
    price = extract_price(info_tag)
    inv = extract_inv(info_tag)
    
   # print(title)
   # print(price)
   # print(inv)
   # print('\n')
    count=count+1
   # print(count)
    #insert extra data to lists
    title_list.append(title)
    price_list.append(price)
    inv_list.append(inv)


  


# In[15]:


df = pd.DataFrame({
    'Product': title_list,
    'Price': price_list,
    'Stock': inv_list
})


# In[16]:


#df.to_excel(r'D:\Python_Beginner\Final_Project\final_project_MZP.xlsx', index=False, sheet_name='Sheet1')


# In[ ]:





# In[19]:


df.to_excel('Dell Laptops - May Zin Phyo.xlsx', index=False, sheet_name='Sheet1')


# In[20]:


df


# In[ ]:




