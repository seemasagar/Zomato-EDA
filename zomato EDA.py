#!/usr/bin/env python
# coding: utf-8

# In[8]:


##Zomato Dataset EDA


# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df=pd.read_csv(r"C:\Users\seema sagar\Downloads\zomato.csv", encoding='latin-1')


# In[3]:


df.head()


# In[4]:


df.columns


# In[60]:


df.info()


# In[61]:


df.describe()


# # In data analysis what all we do
# 1. Missing Values
# 2. Explore about the numerical variables
# 3. Explore about the categorical variables
# 4. Finding relationship betwen features
# 
# 

# In[62]:


df.isnull().sum()


# In[63]:


[features for features in df.columns if df[features].isnull().sum()>0]


# In[64]:


sns.heatmap(df.isnull(),yticklabels=False,cbar=False,cmap= 'viridis')


# In[65]:


df_country=pd.read_excel(r"C:\Users\seema sagar\Downloads\country-code.xlsx")


# In[66]:


df_country.head()


# In[67]:


final_df= pd.merge(df, df_country, on="Country Code", how ='left')


# In[68]:


final_df.head()


# In[69]:


df.dtypes


# In[70]:


final_df.columns


# In[71]:


final_df.Country.value_counts()


# In[72]:


country_names=final_df.Country.value_counts().index


# In[73]:


country_value=final_df.Country.value_counts().values


# In[80]:


## Pie Chart
#top 3 countries that uses zomato

plt.pie(country_value[:3], labels=country_names[:3], autopct="%1.2f%%")


# observation:zomato maximum records are from india and after that USA and then in UK

# In[81]:


##Numerical variables

final_df.columns


# In[87]:


rating=final_df.groupby(['Aggregate rating', 'Rating color', 'Rating text']).size().reset_index().rename(columns={0:'Rating count'})


# In[88]:


rating


# ##conclusions
# 1. when rating is between 4.5 to 4.9 is excellent
# 2.when rating is between 4.0 to 4.4 is very good
# 3.when rating the is between 3.5 to 3.9 is good
# 4. when rating is between 3.0 to 3.4 is average 
# 5. when rating is between 2.5 to 2.9 is average
# 6. when rating is between 2.0 to 2.4 is poor
#  

# In[91]:


rating.head()


# In[97]:


import matplotlib
get_ipython().run_line_magic('matplotlib', 'inline')
matplotlib.rcParams['figure.figsize'] = (12, 6)
sns.barplot(x="Aggregate rating", y="Rating count", data=rating)


# In[102]:


sns.barplot(x="Aggregate rating", y="Rating count", hue='Rating color', data=rating, palette=['BLUE','red','orange','yellow','green',
                                                                                             'green'])


# OBSERVATIONS:
# 1. Not rated count is very high
# 2. Maximum number of rating are between 2.5 to 3,4

# In[103]:


#Count plot
sns.countplot(x="Rating color", data= rating, palette=['BLUE','red','orange','yellow','green','green'])


# In[116]:


#find the countries name that has given 0 rating

final_df[final_df['Rating color']=='white'].groupby('Country').size().reset_index()


# In[115]:


final_df.groupby(['Aggregate rating','Country']).size().reset_index().head(5)


# observations 
# Maximum number of 0 ratings are from Indian customers

# In[117]:


#find out which currency is used by which country?

final_df.columns


# In[119]:


final_df[['Country','Currency']].groupby(['Country','Currency']).size().reset_index()


# In[123]:


# which countries do have/ have not online delivery?

final_df[['Has Online delivery','Country']].groupby(['Has Online delivery','Country']).size().reset_index()


# In[124]:


# which countries do have online delivery?

final_df[final_df['Has Online delivery']=="Yes"].Country.value_counts()


# observations:
# 1. online deliveries are available in India and UAE

# In[131]:


##create pie chart for top 5 cities distribution?


# In[132]:


final_df.columns


# In[133]:


final_df.City.value_counts().index


# In[135]:


city_values=final_df.City.value_counts().values
city_labels=final_df.City.value_counts().index


# In[137]:


plt.pie(city_values[:5], labels=city_labels[:5], autopct="%1.2f%%")


# #Assignment
# find the top 10 couisines
# 

# In[ ]:




