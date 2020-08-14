#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests')


# In[2]:


import requests
from bs4 import BeautifulSoup
import smtplib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


url = "https://www.amazon.in/Test-Exclusive-544/dp/B077PWK5BY/ref=sr_1_2?dchild=1&keywords=oneplus+8+pro&qid=1597413427&sr=8-2"


# In[4]:


headers= {"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}


# In[5]:


page = requests.get(url,headers=headers)


# In[11]:


soup = BeautifulSoup(page.content,'html.parser')


# In[12]:


#title of the poge
print(soup.title)


# In[13]:


#get attributes
print(soup.title.name)


# In[14]:


#get string
print(soup.title.string)


# In[15]:


#name consists of title + string which is displayed under soup.title


# In[16]:


#beginning navigation
print(soup.title.parent.name)


# In[17]:


#getting specific value
print(soup.p)


# In[18]:


print(soup.find_all('p'))


# In[19]:


for paragraph in soup.find_all('p'):
    print(paragraph.string)
    print(str(paragraph.text))


# In[20]:


#getting every link from that page
for url in soup.find_all('a'):
    print(url.get('href'))


# In[21]:


#get all the texts from the page
print(soup.get_text())


# In[22]:


a = soup.find(id = "productTitle")
b = a.get_text()


# In[23]:


print(b.strip())


# In[24]:


s = soup.find(id ="priceblock_ourprice")
s.get_text()[2:10]


# In[25]:


price=s.get_text()[2:10]


# In[26]:


price


# In[27]:


price1=59999


# In[40]:


def send_mail():
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login("vaibhav9816@gmail.com","vaibhavanand")
    subject = "Price for the product you subscribed for has reduced"
    body = "The price for the product you subscribed for has reduced, kindly check the LINK: https://www.amazon.in/Test-Exclusive-544/dp/B077PWK5BY/ref=sr_1_2?dchild=1&keywords=oneplus+8+pro&qid=1597413427&sr=8-2"
    msg =f"Subject:{subject}\n\n{body}"
    server.sendmail(
        "vaibhavaeshu@gmail.com",
        "vaibhavaeshu@gmail.com",
        msg
    
    )      
                      
           
    print("Mail sent!")
    server.quit()


# In[42]:


if (price1<59999):
    send_mail()


# In[ ]:




