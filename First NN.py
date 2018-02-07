
# coding: utf-8

# In[1]:


import numpy


# In[2]:


def NN(m1, m2, w1, w2, b):
    z = m1 * w1 + m2 * w2 + b
    return sigmoid(z)

def sigmoid(x):
    return 1/(1+ numpy.exp(-x))


# In[3]:


w1 = numpy.random.randn()
w2 = numpy.random.randn()
b = numpy.random.randn()


# In[4]:


w1


# In[5]:


w2


# In[6]:


b


# In[7]:


NN(3, 1.5, w1,w2,b)


# In[8]:


NN(2,1,w1,w2,b)
