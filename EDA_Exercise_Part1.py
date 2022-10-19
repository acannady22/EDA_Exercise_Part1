#!/usr/bin/env python
# coding: utf-8

# In[2]:


# import the pandas library and use the alias 'pd'
get_ipython().system('pip install pandas')

import pandas as pd


# In[3]:


#create the s1 series from the list: [10,20,30,40,50]
s1 = pd.Series([10,20,30,40,50])


# In[4]:


# create a series called s_tuple from the tuple: ("apple", "banana", "cherry")
s_tuple = pd.Series(["apple", "banana", "cherry"])


# In[8]:


# create a series called s_dictionary from the dictionary: {"brand": "Ford", "model": "Mustang", "year": 1964}
#s_dictionary = pd.Series({"brand" : "Ford", "model" : "Mustang", "year" : "1964"})


# In[19]:


# fill in the blank with the series values and index values
print("The s1 series values are:", s1.values)
print("The s1 index values are:", s1.index.values)
print("\n")
print("The s_tuple series values are:", s_tuple.values)
print("The s_tuple index values are:", s_tuple.index.values)
print("\n")
#print("The s_dictionary series values are:", s_dictionary.values)
#print("The s_dictionary index values are:", s_dictionary.index.values)


# In[16]:


# create the s2 series from the list [80,93,78,85,97] and with labeled indexes ['English','Science','Social','Tamil','Maths']
s2 = pd.Series([80,93,78,85,97], index = ['English','Science','Social','Tamil','Maths'])


# In[17]:


# print the s2 series
print("The Marks obtained by student are", s2)


# In[20]:


# assign the s2 series name to be "Student Marks"
s2.name = 'Student Marks'


# In[21]:


# assign the s2 index name to be "Subject"
s2.index.name = 'Subject'


# In[22]:


# print the s2 series again to see the newly assigned name and index name
print("The Marks obtained by student - subjectwise:\n", s2)


# In[23]:


# return the first element in the s2 series
s2[0]


# In[25]:


# slicing using default integer index
s2[0:5]


# In[27]:


# return the elements starting at position one and ending with the element at index 3
s2[1:4]


# In[28]:


# Slicing using string index
# return the element associated with the index 'Tamil'
s2['Tamil']


# In[32]:


# create a dictionary of fruit names and their prices. Use the values from the article
dict_fruits = {'Orange':80,
          'Apples':210,
          'Bananas':50,
         'Grapes':90,
         'Watermelon':70}


# In[33]:


# Lets convert this dictionary into a series
fruits = pd.Series(dict_fruits)


# In[34]:


# print the series
print("Fruits and prices\n", fruits)


# In[35]:


# Slice the series and retrieve price of grapes
print("The price per kg of grapes is:", fruits['Grapes'])


# In[36]:


# create a dataframe from the s2 series
df_marks = pd.DataFrame(s2, columns=['Student1'])


# In[37]:


# print the dataframe
print("The dataframe created from series is\n",df_marks)


# In[38]:


# Create height series using [5.3, 6.2,5.8,5.0,5.5] for values, ['Person 1','Person 2','Person 3','Person 4','Person 5'] for indexes
height = pd.Series([5.3, 6.2,5.8,5.0,5.5], index=['Person 1','Person 2','Person 3','Person 4','Person 5'])


# In[39]:


# Create weight series (in kgs) using [65,89,75,60,59] for values and the same indexes as height
weight = pd.Series([65,89,75,60,59], index = ['Person 1','Person 2','Person 3','Person 4','Person 5'])


# In[40]:


# Create a dataframe from the height and weight series above
df_person = pd.DataFrame({'height': height, 'weight': weight})


# In[41]:


# print the dataframe
print("The Person table details are:\n", df_person)


# In[ ]:




