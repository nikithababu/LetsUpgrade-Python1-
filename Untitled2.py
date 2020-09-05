#!/usr/bin/env python
# coding: utf-8

# # tuples

# In[14]:


tuple1=(1, 2, 3,4,3)
tuple2=(4, 5, 6,1)
print(len(tuple2))
print(len(tuple1))


# In[9]:


print(max(tuple1))


# In[12]:


print(min(tuple2))


# In[16]:


print( tuple(tuple1))


# In[18]:


atuple=print( "tuple 1:",tuple(tuple1))


# In[37]:


print((1, 2, 3) + (4, 5, 6))


# In[38]:


print(3 in (1, 2, 3))


# # dictionaries

# In[21]:


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict1['Age'] = 8;
dict1['School'] = "srmjv School"; 

print ("dict['Age']: ", dict1['Age'])
print ("dict['School']: ", dict1['School'])


# In[23]:


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
del dict1['Name']
print("dict1:",dict1)


# In[ ]:


dict1.clear();
print("dict1:",dict1)


# In[26]:


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("dict1:",dict1)


# In[27]:


del dict1 ; 
print("dict1:",dict1)


# In[32]:


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict2 = {'Name': 'Mahnaz', 'Age': 27};
print ("Length :",len (dict1))
print ("Length :",len (dict2))


# In[35]:


dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print("String : ",str (dict1))


# In[36]:


print (" Type :",type (dict))


# In[39]:


dict3= {'Name': 'Zara', 'Age': 7};
print("Start Len :",len(dict))
dict.clear()
print("End Len : ",len(dict))


# In[43]:


dict4 = dict1.copy()
print("New Dictionary :",str(dict4))


# In[47]:


seq1= ('name', 'age', 'sex')
dict5 = dict.fromkeys(seq1)
print ("New Dictionary :",str(dict5))
dict5 = dict.fromkeys(seq1, 10)
print ("New Dictionary :",str(dict5))


# In[71]:


dict0 = {'Name': 'Zabra', 'Age': 7}
print ("Value :",dict0.get('Age'))
print ("Value : ",dict0.get('Education',"Never"))
print ("Value :",dict0.values())
dict0.setdefault('Sex', "F")
print(dict0)


# In[69]:


dict8 = {'class':'IT-B', 'roll no.': 58 }
dict0.update(dict8)
print(dict0)


# In[70]:


print(dict0.keys())


# # string

# In[73]:


var1 = 'Hello World!'
var2 = "Python Programming"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])


# In[76]:


str="Hi sir!! this is nikitha"
print("str.capitalize() : ", str.capitalize())


# In[77]:


str.upper()


# In[79]:


str.title()


# In[80]:


str.swapcase()


# In[82]:


print(str.isdecimal())


# In[85]:


str = ("THIS IS STRING EXAMPLE....WOW!!!");
print(str.lower())


# In[93]:


print(str.isupper())
str = ("THIS IS STRING EXAMPLE....wow!!!");
print(str.isupper())
str = ("THIS IS STRING EXAMPLE....WOW!!!");
print(str.isupper())


# In[95]:


s = "-";
seq = ("n", "c", "c");
print(s.join( seq ))


# In[97]:


str = "this2009";  
print(str.isalnum())
str = "this is string example....wow!!!";
print(str.isalnum())


# In[99]:


str1 = "this is string example....wow!!!";
str2 = "exam";
print (str1.find(str2))
print (str1.find(str2, 10))
print (str1.find(str2, 40))


# # sets

# In[100]:


Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)


# In[105]:


DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
#union
AllDays = DaysA|DaysB
print(AllDays)
#intersection
AllDays = DaysA & DaysB
print(AllDays)
#difference
AllDays = DaysA - DaysB
print(AllDays)


# In[115]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft","cherry", "apple"}
z = x.union(y)
print(z)


# In[111]:


x.update(y)
print(x)


# In[114]:


z = x.symmetric_difference(y)
print(z)


# In[116]:


x.discard("banana")

print(x)


# In[117]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft","cherry", "apple"}
z = x.isdisjoint(y) 
print(z)


# In[118]:


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft"}
z = x.isdisjoint(y) 
print(z)

