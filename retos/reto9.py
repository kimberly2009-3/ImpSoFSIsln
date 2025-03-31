#!/usr/bin/env python
# coding: utf-8

# In[3]:


def fizzbuzz(max_num):
    three_mul = 'fizz'
    five_mul = 'buzz'
    num1 = 3
    num2 = 5 
    
    for i in range(1,max_num):
        if i % num1 ==0 and i % num2 == 0:
            print(i,three_mul+five_mul)
        elif i%num1 == 0:
            print(i,three_mul)
        elif i%num2 == 0:
            print(i,five_mul)

#----START OF SCRIPT
if __name__=='__main__':
    fizzbuzz(100)

