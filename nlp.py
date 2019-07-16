#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Group id : 9133
#Sanjay Kumar K.K.R. 
#Sayee Mulay 
#Suraj Takur
# competition code AC01
#https://buildmedia.readthedocs.org/media/pdf/newspaper/latest/newspaper.pdf
# this is considered the best way to buil nlp models 


# In[2]:


from newspaper import Article


# In[3]:


url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'


# In[4]:


article = Article(url)


# In[5]:


article.download()
article.html


# In[15]:


article.parse()


# In[16]:


article.title


# In[17]:


article.authors


# In[18]:


import nltk
nltk.download()


# In[19]:


article.publish_date


# In[20]:


article.movies


# In[21]:


article.nlp()


# In[22]:


article.keywords


# In[14]:


article.summary


# In[23]:


import newspaper


# In[24]:


newspaper.languages()


# In[ ]:




