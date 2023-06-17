#!/usr/bin/env python
# coding: utf-8

# # Submission by:SREESHWAN JAGEER
# # UNEMPLOYMENT ANALYSIS WITH PYTHON
# # Data science
# # Task 2

# In[1]:


#importing requried libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[2]:


#reading datasets
data=pd.read_csv("Unemployment in India.csv")
data=pd.read_csv("Unemployment_Rate_upto_11_2020 (1).csv")
data.head(5)


# In[3]:


#checking is there any null values are present in our dataset
data.isnull().sum()


# In[4]:


#changing columns 
data.columns = ['States', 'Date', 'Frequency', 'Estimated Unemployment Rate',
                'Estimated Employed', 'Estimated Labour Participation Rate',
                'Region', 'longitude', 'latitude']
data.head(5)


# In[5]:


#checking how many  rows and columns are present in our dataset
data.shape


# In[6]:


#describtion about statistical analysis
data.describe()


# In[7]:


#checking number states
data.States.unique()


# In[8]:


#checking number of Regions
data.Region.unique()


# In[9]:


#checking Estimated Employed rate of india
data.columns=['States', 'Date', 'Frequency', 'Estimated Unemployment Rate',
                'Estimated Employed', 'Estimated Labour Participation Rate',
                'Region', 'longitude', 'latitude']
plt.figure(figsize=(7,6))
plt.title("Estimated Employed Rate of India")
sns.histplot(x="Estimated Employed", hue="Region", data=data)
plt.show()


# In[10]:


#Estimated Labour Participation Rate based on Regions of Indian
plt.figure(figsize=(7,6))
plt.title("Estimated Labour Participation Rate based on Regions of Indian ")
sns.histplot(x="Estimated Labour Participation Rate", hue="Region", data=data)
plt.show()


# In[11]:


#estimating Labour Participation Rate for each region and states
fig = px.histogram(data, x='Estimated Labour Participation Rate',y='States' ,color='Region')
fig.show()


# In[12]:


#checking unemployment rate according to different regions of India
data.columns=['States', 'Date', 'Frequency', 'Estimated Unemployment Rate',
                'Estimated Employed', 'Estimated Labour Participation Rate',
                'Region', 'longitude', 'latitude']
plt.figure(figsize=(7, 6))
plt.title("Unemployment Rate According to Different Regions of Indian ")
sns.histplot(x="Estimated Unemployment Rate", hue="Region", data=data)
plt.show()


# In[13]:


#Avg Estimated Unemployment Rate for each state and region 
plot_Estimated_Unemployment = data[['Estimated Unemployment Rate','States']]
Estimated_Unemployment_Rate= plot_Estimated_Unemployment.groupby('States').mean().reset_index()
Estimated_Unemployment_Rate = Estimated_Unemployment_Rate.sort_values('Estimated Unemployment Rate')
fig = px.scatter(Estimated_Unemployment_Rate, x='States',y='Estimated Unemployment Rate',color='States',title='Average Estimated Unemployment Rate in each state',template='plotly')
fig.show()


# In[14]:


#estimating average empolyed rate in each state
plot_Estimated_Employed = data[['Estimated Employed','States']]
Estimated_Employed= plot_Estimated_Employed .groupby('States').mean().reset_index()
Estimated_Employed = Estimated_Employed.sort_values('Estimated Employed')
fig = px.histogram(Estimated_Employed, x='States',y='Estimated Employed',color='States',title='Average Estimated Employed in each state',template='plotly')
fig.show()




