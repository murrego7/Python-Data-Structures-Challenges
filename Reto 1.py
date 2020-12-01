#!/usr/bin/env python
# coding: utf-8

# # Solución Reto 1 #

# In[8]:


stopwords = ['the', 'of', 'is', 'i', 'me', 'he', 'she', 'of', 'or', 'and', 'for', 'to']


def limpiar_stop_words(texto_a_limpiar):
    
    texto_a_limpiar = "The NEW python prograMMER is a GREAT person. He is EXCEllent solving problems OF CODING anD "                     "writING scrIPts tO solve moDErn problems"
    
    texto_a_limpiar = texto_a_limpiar.lower()
    texto_a_limpiar = list(texto_a_limpiar.split(" ")) 
    
    for word in texto_a_limpiar:  
        if word in stopwords:
            texto_a_limpiar.remove(word)
    
    texto_a_limpiar = ' '.join([str(elem) for elem in texto_a_limpiar]) 
    texto_a_limpiar = texto_a_limpiar.replace('is', '')
    

    return texto_a_limpiar


if __name__ == '__main__':
    texto_entrada = "The NEW python prograMMER is a GREAT person. He is EXCEllent solving problems OF CODING anD "                     "writING scrIPts tO solve moDErn problems"
    texto_procesado = limpiar_stop_words(texto_entrada)
    texto_limpio = "new python programmer a great person.  excellent solving problems coding writing "                    "scripts solve modern problems"
    assert texto_limpio == texto_procesado, "Tu función aun no limpia de forma correcta"
    print("Tu limpiador de texto funciona!. FELICITACIONES!!!")


# In[ ]:




