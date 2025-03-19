#!/usr/bin/env python
# coding: utf-8

# In[13]:


class Padre:
    mama = "madre"
    papa = "padre"

class hijo(Padre):
    __hijo1 = "jovany"
    def calificacion(self):
        print("10")

class hijo2(Padre):
    __hijo2 = "jesus"
    def calificacion(self):
        print("8")


la_calificacion = hijo()
segundo = hijo2()
print(segundo.calificacion())
print(la_calificacion.calificacion())

