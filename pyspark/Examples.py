#!/usr/bin/env python
# coding: utf-8

# # PySpark Examples 

# ## Basic Examples

# In[1]:


import pyspark
from pyspark import SparkContext, SparkConf


# In[2]:


conf = SparkConf(master="local[*]", )
sc = SparkContext(conf=conf)


# In[3]:



words = ["Hello", "this", "is", "an", "example"]
# Collect
print(sc.parallelize(words).map(lambda w: w).collect())
# Count
print(sc.parallelize(words).map(lambda w: w).count())
# flatmap
print(sc.parallelize(words).flatMap(lambda w: w).collect())
# appending the words into a sentence
def form_sentence(words):
    result = ""
    for entry in words:
        result += entry
        result += " "
    return result
print(sc.parallelize(words).map(form_sentence).collect())


# ## ML Examples

# ### Basic Statistics

# In[ ]:


"""
Basic Statistics impemented here are as follows:
1. Correlation - linear relationship(statistical association) of two variables
        This attribute is mainly used to measure the type of relationship 
        between two variables. Either positive or negative. 
2. Hypothesis Testing - 
3. Summarizer - 
"""

