#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns 


# In[16]:


df = pd.read_csv('C:/Users/ekinc/OneDrive/Desktop/youtube_dataset.csv')


# In[17]:


df.head()


# In[4]:


def slice_data (df, number_of_rows):
    return df.iloc[:number_of_rows]
first_1000 = slice_data(df, 1000)


# In[5]:


hist = {}

def dist(t):
    for x in t:
        hist[x] = hist.get(x,0) + 1

distrubition = dist(first_1000.channeltype)


# In[6]:


hist


# In[12]:


new_hist= pd.DataFrame(list(hist.items()),columns = ['ChannelType','Count']) 
new_hist


# In[13]:


plt.figure(figsize=(15,10))
sns.barplot(x='ChannelType', 
            y='Count', 
            data=new_hist, 
            order=new_hist.sort_values('Count',ascending = False).ChannelType)

plt.xlabel("Channel Type", size= 15)
plt.ylabel("Count", size=15)
plt.title("Distribution of Channel type from the top 1000 records including NAs", size=18)
plt.tight_layout()
plt.savefig("Distribution of Channel type from the top 1000 records including NAs", dpi=100)


# In[14]:


first_1000.to_csv(r'C:/Users/ekinc/OneDrive/Desktop/youtube1000.csv', index = False)


# In[15]:


df_1000 = pd.read_csv('C:/Users/ekinc/OneDrive/Desktop/youtube1000.csv')


# In[11]:


df_1000.head(10)


# In[ ]:




