#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Artista :
    genero = 'rok'
    escula = 'teatro'
    def __init__(self ,nombre,pais):
        print(f"creado Artista {nombre}, {pais}")
        self.nombre =nombre
        self.pais = pais

artista=Artista("brian may","londres")

