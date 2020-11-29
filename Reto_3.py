#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd 
def analizar_peliculas():
    
    df = pd.read_csv('movies_metadata.csv')
    df = df[['title', 'release_date', 'budget', 'revenue', 'runtime']]
    df = df[df['revenue'] > 2000000 & (df['budget'] < 1000000)].reset_index(drop = True)
    return df
analizar_peliculas()


# In[ ]:




