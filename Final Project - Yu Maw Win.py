#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


# define functions

# extract title function
def extract_title(i_tag):
    # extract title tag list
    title_tag = i_tag.find("a", class_= "product-item__title text--strong link")
    # extract text from soup
    title_tag2 = title_tag.get_text()
    # extract product name
    title_tag3 = title_tag2.split(" (")[0]
    # change variable name
    final_title_tag = title_tag3

    return final_title_tag

# extract price function
def extract_price(i_tag):
    # find price list 
    price_tag = i_tag.find("span", class_= "price")
    # extract text from soup
    price_tag2 = price_tag.get_text()
    # remove comma
    price_tag3 = price_tag2.replace(",", "")
    # remove K
    price_tag4 = price_tag3.replace("K", "")
    # change variable name
    final_price_tag = price_tag4

    return final_price_tag


# In[3]:


# define url
url = "https://unique.com.mm/collections/dell-notebook"


# ### Step 1. Request Data

# In[4]:


response = requests.get(url)
response


# ### Step 2. Create BeautifulSoup object

# In[5]:


# covert beautifulsoup object
soup = BeautifulSoup(response.text, "html.parser")
soup


# ### Step 3. Find info tags

# In[6]:


# extract all tags from soup object
info_tags_list = soup.find_all("div", class_= "product-item__info-inner")
info_tags_list


# ### Step 4. Extract data from each tag

# In[7]:


title_list = []
price_list = []

for info_tag in info_tags_list:
    title = extract_title(info_tag)
    price = extract_price(info_tag)

# extract insert data into lists
    title_list.append(title)
    price_list.append(price)


# In[8]:


title_list


# In[9]:


price_list


# ### Step 5. Export data as an excel file

# In[10]:


# create a dictionary to combine the lists into column
df = pd.DataFrame({"Product Name" : title_list, "Price" : price_list})


# In[11]:


df


# In[12]:


# export as excel
# df.to_excel("dell_notebooks.xlsx", index = False)


# In[13]:


df.to_excel("Dell Laptops - Yu Maw Win.xlsx", index = False)

