#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
def factorial(n):
    r = 1
    for i in range(1, n+1):
        r = r * i
    return r

def e_v_stepeni_x(x):
    a = 0
    for s in range(0, 30):
        a = a + (x**s)/(factorial(s))
    return a
print(e_v_stepeni_x(2))   #Проверил на единице и двойке, все работает👍🏻👍🏻


# In[ ]:





# In[ ]:




