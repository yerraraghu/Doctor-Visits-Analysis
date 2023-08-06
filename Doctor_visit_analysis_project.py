#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# # Loading dataset

# In[5]:


df=pd.read_excel("DoctorVisits.xlsx")


# In[6]:


df


# In[5]:


df.head(10)


# In[6]:


df.tail(10)


# # Information of data set

# In[7]:


df.info()


# # Checking data contain null values or not

# In[8]:


df.isnull().sum()


# In[9]:


#  No Null values are there in the given data set


# # Accessing  columns

# In[7]:


df["illness"]


# #  Finding the Mean,Min,Max values

# In[11]:


df.describe()


# # Finding total no of people based on their count of illness

# In[8]:


df["illness"].value_counts()


# # Representing percentage of patient and age using pie-chart

# In[13]:


age_count=df['age'].value_counts()
age_count=age_count.sort_index()
plt.figure(figsize =(10,10))
plt.pie(age_count, labels=age_count.index, autopct='%1.1f%%')
plt.title('age distribution')
plt.show()


# # Representing income using histogram

# In[14]:


plt.figure(figsize =(10,8))
df["income"].plot(kind='hist')


# # Representing percentage of male and female using piechart

# In[75]:


plt.figure(figsize =(10,10))
df.groupby('illness')['gender'].value_counts().unstack().plot(kind='bar', stacked=True)


# # visualize and analyse the maximum,minimum and medium income

# In[42]:


df["income"].describe()


# In[46]:


a=list(df.income)
plt.boxplot(a)
plt.show()


# # Finding the age of people who are more likely of getting illness

# In[45]:


res=dict(df['age'].value_counts())
max(res, key=lambda k: res[k])


# ## Finding the no of days of reduced activity of male and female seperately due to illness
# 

# In[51]:


df.groupby(['gender','reduced']).mean()


# # Visualising is any missing values in the dataset based on heat map

# In[14]:


sns.heatmap(df.isnull(),cbar=False,cmap='viridis')


# ### Finding the corelation between variables in the given dataset correlation between different variables
# 

# In[54]:


plt.figure(figsize=(7,7))
sns.heatmap(df.corr(),cbar=True,annot=True)


# # Analyse how the income of a patient affects the no of visits to the hospital
# 

# In[55]:


plt.figure(figsize=(10,10))
plt.scatter(x='income',y='visits',data=df)
plt.xlabel('income')
plt.ylabel('visits')
plt.show()


# # visualising  the number of males and females affected by illness

# In[18]:


sns.histplot(df['gender'], bins=2)
gender_counts = df['gender'].value_counts()
for i, count in enumerate(gender_counts):
    plt.annotate(str(count), xy=(i, count), ha='center', va='bottom')
plt.xlabel('Gender')
plt.title('Gender Distribution')
plt.show()


# ## visualize the percentage of people getting govt health insurance due to low income, due to old age and also the percentage of people having private health insurance
# 

# In[82]:


label=['yes','no']
y=df[df['freepoor']=='yes']
n=df[df['freepoor']=='no']
x=[y.shape[0],n.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label, autopct='%1.1f%%')
plt.title('Percentage of people getting govt health insurance due to low income')
plt.show()


# In[83]:


label=['yes','no']
y=df[df['private']=='yes']
n=df[df['private']=='no']
x=[y.shape[0],n.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label,autopct='%1.1f%%')
plt.title('Percentage of people having private health insurance')
plt.show()


# In[84]:


label=['yes','no']
y=df[df['freerepat']=='yes']
n=df[df['freerepat']=='no']
x=[y.shape[0],n.shape[0]]
plt.figure(figsize=(5,5))
plt.pie(x,labels=label,autopct='%1.1f%%')
plt.title('Percentage of people getting govt insurance due to old age,disability or veteran status')
plt.show()


# # Bar Chart to analyze the days of activity due to illness based on gender
# 

# In[19]:


db=df.groupby('gender')['reduced'].sum().to_frame().reset_index()
plt.bar(db['gender'],db['reduced'],color=['red','green'])
plt.title('Bar Chart')
plt.xlabel('gender')
plt.ylabel('reduced activity')
plt.show()

