#!/usr/bin/env python
# coding: utf-8

# ### Final Project By Yaminn Nge

# In[1]:


# import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


# define functions
# Define functions
def extract_title(i_tag):
    """Extract title function"""
    # Extract title tag
    title_tag = i_tag.find('a', class_='product-item__title')
    if title_tag:
        # Extract text and clean it up
        title_text = title_tag.get_text().strip()
        # Replace newlines with hyphens (if any)
        final_title_text = title_text.replace('\n', '-')
        return final_title_text
    return None  # Return None if title_tag is not found


def extract_price(i_tag):
    """Extract price function"""
    
    # Extract price tag
    price_text = i_tag.find('div', class_='product-item__price-list price-list')
    # Extract price text using get_text() method
    price_text2 = price_text.get_text()
    
    # Extract old price if there is a discount price
    if '\n' in price_text2:
        price_text2 = price_text2.split('\n')[1]
    
    # Remove unwanted characters, keep only numbers and period
    price_text3 = ''.join(filter(lambda x: x.isdigit() or x == '.', price_text2))
    
    # Convert to float
    final_price_text = float(price_text3)
    
    return final_price_text


# In[3]:


# Step 2: Send a request to the website
url = "https://unique.com.mm/collections/dell-notebook"


# #### Step 1 : Request Data

# In[4]:


#set header to pretend as a browswer
headers_attributes = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

response = requests.get(url, headers=headers_attributes)


# #### Step 2 : Create a Beautiful Object

# In[5]:


# convert as beautifulsoup object
soup = BeautifulSoup(response.text, 'html.parser')


# #### Step 3 : Find info tag.

# In[6]:


info_tags_list = soup.find_all('div', class_='product-item__info-inner')


# #### Setp 4 : Extract Data from each tag.

# In[7]:


title_list = []
price_list = []
supplier_list = []
count = 0;
for info_tag in info_tags_list:
    title = extract_title(info_tag)
    price = extract_price(info_tag)
    
    print(title)
    print(price)
    count = count + 1;
    print(count)
    
    # insert extracted data into lists
    title_list.append(title)
    price_list.append(price)


# #### Step 5 : Export Data as a excel file.

# In[8]:


# create dataframe
df = pd.DataFrame({'Product Name':title_list,
                  'Original Price':price_list})


# In[9]:


#df.to_excel(r'D:\IT\02. Python\Final_proj\Export Data\Dell_Notebooks.xlsx', index=False)
#df.to_excel('Output.xlsx', index=False)


# In[10]:


#print(info_tags_list)


# In[11]:


df.to_excel('Dell Laptops - Yamin Nge.xlsx', index=False)


# In[12]:


df

