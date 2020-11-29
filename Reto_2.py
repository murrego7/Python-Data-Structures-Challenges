#!/usr/bin/env python
# coding: utf-8

# # Solución Código # 

# In[2]:


def answer_one():  
    import pandas as pd
    counts = dict()
    neruda = """Puedo escribir los versos más tristes esta noche.
            Yo la quise, y a veces ella también me quiso.
            En las noches como ésta la tuve entre mis brazos.
            La besé tantas veces bajo el cielo infinito.
            
            Ella me quiso, a veces yo también la quería.
            Cómo no haber amado sus grandes ojos fijos.""".lower() 

    words = neruda.split()

    for word in words:
        counts[word] = counts.get(word,0) + 1
    #counts
    df = pd.DataFrame.from_dict(counts, orient = 'index').reset_index().rename(columns={"index": "Words", "0": "count"})
    return df
answer_one()


# In[ ]:




