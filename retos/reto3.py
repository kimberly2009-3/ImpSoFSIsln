#!/usr/bin/env python
# coding: utf-8

# In[9]:


def fizzbuzz(max_num):
   
    for i in range(1,max_num):
        
        if i % 3 == 0 and i % 5 == 0:
            print(i,"fizzbuzz")
        elif i % 3 == 0:
            print(i,"fizz")
        elif i % 5 == 0:
            print(i,"Buzz")

#----Iniciar el script
if __name__=='__main__':
    fizzbuzz(100)

