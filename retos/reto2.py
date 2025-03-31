#!/usr/bin/env python
# coding: utf-8

# In[5]:


def fizzbuzz(max_num):
    "Este metodo implementa FizzBuzz"
    
    tres_mul = 'fizz'
    cinco_mul = 'buzz'
    num1 = 3
    num2 = 5 

    # Busca en Google 'range in python' para ver su funcionamiento
    for i in range(1,max_num):
        # % o modulo
        if i % 3 == 0 and i % 5 == 0:
            print(i,"fizzbuzz")
        elif i % 3 == 0:
            print(i,"fizz")
        elif i % 5 == 0:
            print(i,"buzz")

#----Iniciar el script
if __name__=='__main__':
    fizzbuzz(101)

