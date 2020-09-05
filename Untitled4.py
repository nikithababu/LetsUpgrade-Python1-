#!/usr/bin/env python
# coding: utf-8

# # piolot problem

# In[1]:


altitude=int(input())
if(altitude<=1000):
    print("safe to land")
elif((altitude<=5000) and (altitude>1000)):
    print("Bring down to 1000")
else:
    print("turn around and try again")


# In[2]:


altitude=int(input())
if(altitude<=1000):
    print("safe to land")
elif((altitude<=5000) and (altitude>1000)):
    print("Bring down to 1000")
else:
    print("turn around and try again")


# In[3]:


altitude=int(input())
if(altitude<=1000):
    print("safe to land")
elif((altitude<=5000) and (altitude>1000)):
    print("Bring down to 1000")
else:
    print("turn around and try again")


# # prime numbers

# In[ ]:


lower = 1
upper = 200

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
    else:
        print(num)

