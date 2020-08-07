#!/usr/bin/env python
# coding: utf-8

# # Panda Library  and Numpy Library 
# 
# 
# 
# NumPy is a python library used for working with arrays.
# 
# In Python we have lists that serve the purpose of arrays, but they are slow to process.
# 

# In[63]:


import numpy as np
import pandas as pd


# In[64]:


##Python has a built-in module that you can use to make random numbers.
# it would generate randon new random number everytime 

arr = np.random.rand(3)
print(arr)
print(type(arr))


# In[65]:


### Print Using Index 
print(arr[0])


# # Create  Panda Series  from numpy Array 

# In[66]:


my_series  = pd.Series(arr)
print(my_series)


# In[67]:


print(type(my_series))


# In[68]:


print(my_series[0])


# In[69]:


## so does it looks like numpy array and Series is same ,Yes from above , Then why added Series as new object 
## Well reason is  , Series you could defind your own label name instead index as below 


my_series = pd.Series(arr , index=['first','second','third'])
print(my_series['first'])

## Please note you could use index 


# In[70]:


## Lets print Series now and see if instead of index 0,1,2 it print new labels we have provided
print(my_series)


# In[71]:


## Please note dtype - Means Datatype 


# # # Question 1 :  Which function is used to print labels of Panda  ??

# In[72]:


## Answerts
print(my_series.index)


# In[73]:


## Please note dtype = object in panda is anything that is not number


# So Series is Array like data with label 

# # Question 2 : How to create two dimentional array ??

# In[86]:


arr_two_dimetional = np.random.rand(3,2)
print(type(arr_two_dimetional))


# # Question 3 : How to check dimenstions of Numpy Array ?

# In[87]:


print(arr_two_dimetional.ndim)
print(arr.ndim)


# # Question 4 : How to create a DataFrame from two Dimentional array ?

# In[88]:


df = pd.DataFrame(arr_two_dimetional)


# In[89]:


print(type(df))


# In[90]:


print(df.index)


# In[91]:


print(df)


# # Question 5 : How to change column name( or Labels ) in Panda Dataframe ?

# In[97]:


print(df.columns)


# In[98]:


df.columns = ['first','second']


# In[99]:


print(df.columns)


# In[101]:


# When we select only one column from dataframe it become Series 

print(df['first'])
print(type(df['first']))


# In[ ]:





# In[ ]:




