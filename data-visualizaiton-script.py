
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy


# ## Importing the dataset

# In[4]:


data = pd.read_csv("ann_arbor_temp_data.csv")
data.head()


# In[ ]:





# In[6]:


data.info()


# ## Formatting the dataset

# In[7]:


# dropping the leap 29th feb(leap year day) data for more uniformity in the visualisation

data = data[data['Date'] != '2008-02-29']
data = data[data['Date'] != '2012-02-29']
data.info()


# In[8]:


# droppinng the id column
data = data.iloc[:, 1:]
data.head()


# In[9]:


# seggregating the max and min temp data into diffrent dataframes
max_temp_data = data[data['Element'] == 'TMAX']
min_temp_data = data[data['Element'] == 'TMIN']


# In[11]:


max_temp_data.info()


# In[12]:


min_temp_data.info()


# In[14]:


# sorting the minimum and maximum temperature dataframes by date 
max_temp_data.sort_values(by = ['Date'], inplace = True)
min_temp_data.sort_values(by = ['Date'], inplace = True)


# In[16]:


max_temp_data.head()


# In[17]:


min_temp_data.head()


# In[18]:


# since data contains multiple records for all dates we collect all unique dates seprately
dates = max_temp_data['Date'].unique()


# In[20]:


# creating a datset max_min_record to store maximum and minumum temprature for all dates beteween jan 1 2005 to dec 31 2015
# initally keeping maximum and minimum temperature records to 0
max_min_temp_record = pd.DataFrame({'Date': dates, 'MaxTemp': 0, 'MinTemp': 0})
max_min_temp_record.set_index(['Date'], inplace = True)
max_min_temp_record.head()


# In[21]:


# Filling out the MaxTemp and MinTemp columsn of the max_min_temp_record dataframe using max_temp_data and min_temp_data
# This is a slow function and might take couple of minutes
for date in dates:
    temp = max_temp_data[max_temp_data['Date'] == date]['Data_Value']
    max_min_temp_record['MaxTemp'][date] = max(max_temp_data[max_temp_data['Date'] == date]['Data_Value'])
    max_min_temp_record['MinTemp'][date] = min(min_temp_data[min_temp_data['Date'] == date]['Data_Value'])


# In[22]:


temp = copy.copy(max_min_temp_record)
temp.reset_index(inplace = True)
temp.head()


# In[23]:


# this index will be used as index for year day from day1 to day365
index = np.array(range(1, 366))


# ## creating seprate records of maximum and minimum temperature data for 11 years 2005 to 2015

# In[24]:


max_min_temp_record = temp.iloc[:, 1:]
max_min_temp_record.head()


# In[26]:


max_min_temp_record.info()


# ### creating max and min temperatue data for 2005

# In[27]:


temp_record_2005 = max_min_temp_record.iloc[:365, :]
temp_record_2005.rename(columns = {'MaxTemp': '2005Max', 'MinTemp': '2005Min'}, inplace = True)
temp_record_2005['Day'] = index
temp_record_2005.set_index(['Day'], inplace = True)
temp_record_2005.head()


# ### creating max and min temperatue data for 2006

# In[28]:


temp_record_2006 = max_min_temp_record.iloc[365:365*2, :]
temp_record_2006.rename(columns = {'MaxTemp': '2006Max', 'MinTemp': '2006Min'}, inplace = True)
temp_record_2006['Day'] = index
temp_record_2006.set_index(['Day'], inplace = True)
temp_record_2006.info()


# ### creating max and min temperatue data for 2007

# In[29]:


temp_record_2007 = max_min_temp_record.iloc[365*2:365*3, :]
temp_record_2007.rename(columns = {'MaxTemp': '2007Max', 'MinTemp': '2007Min'}, inplace = True)
temp_record_2007['Day'] = index
temp_record_2007.set_index(['Day'], inplace = True)
temp_record_2007.info()


# ### creating max and min temperatue data for 2008

# In[30]:


temp_record_2008 = max_min_temp_record.iloc[365*3:365*4, :]
temp_record_2008.rename(columns = {'MaxTemp': '2008Max', 'MinTemp': '2008Min'}, inplace = True)
temp_record_2008['Day'] = index
temp_record_2008.set_index(['Day'], inplace = True)
temp_record_2008.info()


# ### creating max and min temperatue data for 2009

# In[32]:


temp_record_2009 = max_min_temp_record.iloc[365*4:365*5, :]
temp_record_2009.rename(columns = {'MaxTemp': '2009Max', 'MinTemp': '2009Min'}, inplace = True)
temp_record_2009['Day'] = index
temp_record_2009.set_index(['Day'], inplace = True)
temp_record_2009.info()


# In[ ]:





# ### creating max and min temperatue data for 2010

# In[33]:


temp_record_2010 = max_min_temp_record.iloc[365*5:365*6, :]
temp_record_2010.rename(columns = {'MaxTemp': '2010Max', 'MinTemp': '2010Min'}, inplace = True)
temp_record_2010['Day'] = index
temp_record_2010.set_index(['Day'], inplace = True)
temp_record_2010.info()


# ### creating max and min temperatue data for 2011

# In[34]:


temp_record_2011 = max_min_temp_record.iloc[365*6:365*7, :]
temp_record_2011.rename(columns = {'MaxTemp': '2011Max', 'MinTemp': '2011Min'}, inplace = True)
temp_record_2011['Day'] = index
temp_record_2011.set_index(['Day'], inplace = True)
temp_record_2011.info()


# ### creating max and min temperatue data for 2012

# In[35]:


temp_record_2012 = max_min_temp_record.iloc[365*7:365*8, :]
temp_record_2012.rename(columns = {'MaxTemp': '2012Max', 'MinTemp': '2012Min'}, inplace = True)
temp_record_2012['Day'] = index
temp_record_2012.set_index(['Day'], inplace = True)
temp_record_2012.info()


# ### creating max and min temperatue data for 2013

# In[36]:


temp_record_2013 = max_min_temp_record.iloc[365*8:365*9, :]
temp_record_2013.rename(columns = {'MaxTemp': '2013Max', 'MinTemp': '2013Min'}, inplace = True)
temp_record_2013['Day'] = index
temp_record_2013.set_index(['Day'], inplace = True)
temp_record_2013.info()


# ### creating max and min temperatue data for 2014

# In[37]:


temp_record_2014 = max_min_temp_record.iloc[365*9:365*10, :]
temp_record_2014.rename(columns = {'MaxTemp': '2014Max', 'MinTemp': '2014Min'}, inplace = True)
temp_record_2014['Day'] = index
temp_record_2014.set_index(['Day'], inplace = True)
temp_record_2014.info()


# ### creating max and min temperatue data for 2015

# In[38]:


temp_record_2015 = max_min_temp_record.iloc[365*10:, :]
temp_record_2015.rename(columns = {'MaxTemp': '2015Max', 'MinTemp': '2015Min'}, inplace = True)
temp_record_2015['Day'] = index
temp_record_2015.set_index(['Day'], inplace = True)
temp_record_2015.info()


# ### Concating the 11 years record into single dataframe

# In[39]:


day_wise_temp_record = pd.concat([temp_record_2005, temp_record_2006, temp_record_2007, temp_record_2008, temp_record_2009, temp_record_2010, temp_record_2011, temp_record_2012, temp_record_2013, temp_record_2014, temp_record_2015], axis=1)


# In[40]:


day_wise_temp_record.info()


# In[41]:


day_wise_temp_record.head()


# In[42]:


# creating 2 new columsn for holding maximum and minimum temperatue of all 365 days for 10 year period(2005, 2014)
day_wise_temp_record['10YearMax'] = 0
day_wise_temp_record['10YearMin'] = 0
day_wise_temp_record.head()


# In[43]:


temp2 = day_wise_temp_record.iloc[:, :20]
for ind in index:
    day_wise_temp_record['10YearMax'][ind] = max(temp2.iloc[ind-1].values)
    day_wise_temp_record['10YearMin'][ind] = min(temp2.iloc[ind-1].values)
day_wise_temp_record


# ## Plotting the line graph of maximum and minimum temprature for all 365 days during the 10 year period 2005 to 2014

# In[44]:


# setting the figure size for our plot
plt.rcParams["figure.figsize"] = [16, 8]


# In[46]:


plt.figure()
plt.plot(index, day_wise_temp_record['10YearMax'].values/10, label = 'MaxTemp')
plt.plot(index, day_wise_temp_record['10YearMin'].values/10, label = 'MinTemp')
plt.show()


# ### preparing the record of 2015 data to compare with last 10 year data

# In[47]:


max_record_of_2015 = day_wise_temp_record[day_wise_temp_record['10YearMax'] < day_wise_temp_record['2015Max']]['2015Max']


# In[48]:


min_record_of_2015 = day_wise_temp_record[day_wise_temp_record['10YearMin'] > day_wise_temp_record['2015Min']]['2015Min']


# In[49]:


min_record_of_2015


# In[50]:


type(max_record_of_2015.values)


# In[52]:


type(max_record_of_2015.index)


# ### Overlaying the line graph with scatter of all days in 2015 when temperature record was broken for either maximum or minimum temperature of last 10 year

# In[53]:


y1 = day_wise_temp_record['10YearMax'].values/10
y2 = day_wise_temp_record['10YearMin'].values/10
plt.figure()
plt.plot(index, y1, label = 'MaxTemp', color = 'orange')
plt.plot(index, y2, label = 'MinTemp', color = 'green')
plt.scatter(np.array(max_record_of_2015.index), max_record_of_2015.values/10, color = 'red', label = 'Max temp record broken in 2015')
plt.scatter(np.array(min_record_of_2015.index), min_record_of_2015.values/10, color = 'purple', label = 'Min temp record broken in 2015')
plt.gca().fill_between(range(1, len(index)+1), y2, y1, facecolor='green', alpha=0.10)
plt.xlabel("Day of the year")
plt.ylabel("temprature in degree celcius")
plt.legend()
plt.show() 


# ## Information gained from the visual

# ###### 2015 broke the record for lowest temperature attained in last 10 years a number of times indicating the major climate change
# ###### 2015 also broke the record for highest temperature achived on a particular day a quite a few times 

# In[ ]:




