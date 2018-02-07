
# coding: utf-8

# In[3]:


def cost(b):
    return (b-4)**2


# In[4]:


cost(0)


# In[5]:


def num_slope(b):
    h= 0.0001
    return (cost(b+h)-cost(b))/h


# In[7]:


num_slope(3)


# In[8]:


def slope(b):
    return 2*(b-4)


# In[9]:


slope(3)


# In[10]:


slope(5)


# In[11]:


b = 8


# In[12]:


b=b-.1*slope(b)
print(b)


# In[14]:


for i in range(3):
    print (i)


# In[17]:


for i in range(1000):
    b=b-.1*slope(b)
    print(b)
