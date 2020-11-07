import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#analysing the data values
dataset=pd.read_csv('rainfall in india 1901-2015.csv')
dataset.shape
numeric = dataset.select_dtypes({'int64','float64'}).columns
numeric
dataset.select_dtypes({'int64','float64'}).shape
categorical = dataset.select_dtypes({'object'}).columns
categorical
dataset.select_dtypes({'object'}).shape

#Showing the null values
total = pd.isnull(dataset).sum().sort_values(ascending=False)
percentage = ((pd.isnull(dataset).sum() / pd.isnull(dataset).count()).sort_values(ascending=False))*100
no_values = pd.concat([total,percentage],axis = 1, keys = ['Total', 'Percent'])
no_values.head(19)
#missing values bar graph
f, ax = plt.subplots(figsize=(15, 6))
plt.xticks(rotation='90')
missing_data = pd.concat([total, percentage], axis=1, keys=['Total', 'Percent'])
sns.barplot(x=missing_data.index, y=missing_data['Percent'])
plt.xlabel('Features', fontsize=15)
plt.ylabel('Percent of missing values', fontsize=15)
plt.title('Percent missing data by feature', fontsize=15)
missing_data.head()

#replacing the null values by their mean of coulumn
dataset['JAN'].fillna((dataset['JAN'].mean()),  inplace=True)
dataset['FEB'].fillna((dataset['FEB'].mean()),  inplace=True)
dataset['MAR'].fillna((dataset['MAR'].mean()),  inplace=True)
dataset['APR'].fillna((dataset['APR'].mean()),  inplace=True)
dataset['MAY'].fillna((dataset['MAY'].mean()),  inplace=True)
dataset['JUN'].fillna((dataset['JUN'].mean()),  inplace=True)
dataset['JUL'].fillna((dataset['JUL'].mean()),  inplace=True)
dataset['AUG'].fillna((dataset['AUG'].mean()),  inplace=True)
dataset['SEP'].fillna((dataset['SEP'].mean()),  inplace=True)
dataset['OCT'].fillna((dataset['OCT'].mean()),  inplace=True)
dataset['NOV'].fillna((dataset['NOV'].mean()),  inplace=True)
dataset['DEC'].fillna((dataset['DEC'].mean()),  inplace=True)
dataset['ANNUAL'].fillna((dataset['ANNUAL'].mean()),  inplace=True)
dataset['Jan-Feb'].fillna((dataset['Jan-Feb'].mean()),  inplace=True)
dataset['Mar-May'].fillna((dataset['Mar-May'].mean()),  inplace=True)
dataset['Jun-Sep'].fillna((dataset['Jun-Sep'].mean()),  inplace=True)
dataset['Oct-Dec'].fillna((dataset['Oct-Dec'].mean()),  inplace=True)

#scatter plot of annual rainfall and years
plt.figure(figsize=(1,1))
sns.jointplot(x=dataset['YEAR'].unique(),y=dataset.groupby("YEAR").mean()["ANNUAL"])
plt.xlabel('YEARS')
sns.set_style("dark")
plt.ylabel('ANNUAL RAINFALL')
plt.show()


#data interpetation
ax=dataset.groupby("YEAR").mean()['ANNUAL'].plot(ylim=(600,2200),color='b',marker='o',linestyle='-',linewidth=2,figsize=(12,8));
plt.xlabel('Year',fontsize=20)
plt.ylabel('Annual Rainfall (in mm)',fontsize=20)
plt.title('Annual Rainfall in India from Year 1901 to 2015',fontsize=25)
ax.tick_params(labelsize=15)
plt.grid()
plt.ioff()

#seasonal rainfall

dataset[['YEAR','Jan-Feb', 'Mar-May','Jun-Sep', 'Oct-Dec']].groupby("YEAR").mean().plot(figsize=(13,8));
plt.xlabel('Year',fontsize=20)
plt.ylabel('Seasonal Rainfall (in mm)',fontsize=20)
plt.title('Seasonal Rainfall from Year 1901 to 2015',fontsize=25)
ax.tick_params(labelsize=15)
plt.grid()
plt.ioff()

#season wise rainfall in india
dataset[['SUBDIVISION','Jan-Feb', 'Mar-May','Jun-Sep', 'Oct-Dec']].groupby("SUBDIVISION").mean().sort_values('Jun-Sep').plot.bar(width=0.5,edgecolor='k',align='center',stacked=True,figsize=(16,8));
plt.xlabel('Subdivision',fontsize=30)
plt.ylabel('Rainfall (in mm)',fontsize=20)
plt.title('Rainfall in Subdivisions of India',fontsize=25)
ax.tick_params(labelsize=15)
plt.grid()

#month wise rainfall
ax=dataset[['JAN', 'FEB', 'MAR', 'APR','MAY', 'JUN', 'AUG', 'SEP', 'OCT','NOV','DEC']].mean().plot.bar(width=0.5,edgecolor='k',align='center',linewidth=2,figsize=(16,8))
plt.xlabel('Month',fontsize=30)
plt.ylabel('Monthly Rainfall (in mm)',fontsize=20)
plt.title('Monthly Rainfall in India',fontsize=25)
ax.tick_params(labelsize=20)
plt.grid()

dataset.groupby("YEAR").mean()['ANNUAL'].idxmin()
