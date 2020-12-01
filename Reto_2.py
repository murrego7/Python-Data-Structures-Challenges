#!/usr/bin/env python
# coding: utf-8

# # Solución Código # 

# In[29]:


def generar_dataframe_palabras(text):
    import pandas
    counts = dict()

    words = text.split()

    for word in words:
        counts[word] = counts.get(word,0) + 1
    #counts
    df = pandas.DataFrame.from_dict(counts, orient = 'index').reset_index().rename(columns={"index": "Words", "0": "count"})
    return df

neruda = """Puedo escribir los versos más tristes esta noche.
            Yo la quise, y a veces ella también me quiso.
            En las noches como ésta la tuve entre mis brazos.
            La besé tantas veces bajo el cielo infinito.
            
            Ella me quiso, a veces yo también la quería.
            Cómo no haber amado sus grandes ojos fijos.""".lower()  # lower hace que todas las letras sean minúsculas.

if __name__ == '__main__':
    d = generar_dataframe_palabras(neruda)
    assert isinstance(d, pandas.DataFrame), "Aun no generas un Dataframe, verifica tu algoritmo!"
    print("Excelente, has convertido un poema en un Dataframe para trabajar con el!")


# In[ ]:




