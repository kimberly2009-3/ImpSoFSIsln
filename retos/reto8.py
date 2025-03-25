#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Fizz_Buzz:
    def fizzbuzz(self, max_num):  # Añadimos 'self' como primer parámetro
        three_mul = 'fizz'
        five_mul = 'buzz'
        num1 = 3
        num2 = 5

        for i in range(1, max_num + 1):  # El rango debe ir de 1 a max_num inclusive
            if i % num1 == 0 and i % num2 == 0:
                print(i, three_mul + five_mul)
            elif i % num1 == 0:
                print(i, three_mul)
            elif i % num2 == 0:
                print(i, five_mul)

# ----INICIO DEL SCRIPT
if __name__ == '__main__':
    # Inicializamos el objeto FizzBuzz
    fizzbuzz_obj = Fizz_Buzz()
    fizzbuzz_obj.fizzbuzz(100)

