import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as tx
import cufflinks as cf
cf.go_offline()
#getting the data set 
data=pd.read_csv('data.csv')

#checking the types of data in dataset
data.describe()
data.info()
categorical=data.select_dtypes('object')
categorical.count()

#dropping the columns which contain urls
data=data.drop(columns=['Unnamed: 0','Photo','Flag','Club Logo'],axis=1)

#checking anomilies in columns of data  
data['Preferred Foot'].unique()
data['Work Rate'].unique()
data['Body Type'].unique()

#making a correlation matrix
corrmat= data.corr()
plt.subplots(figsize=(14,14))
sns.heatmap(corrmat, vmax=.8, square=True, annot=True, center=0 ,cmap='Accent')

#Indian players data
def country(x)
    return data[data['Nationality']=='India'].unique

#taking out the percentage of null values
total = pd.isnull(data).sum().sort_values(ascending=False)
percentage = ((pd.isnull(data).sum() / pd.isnull(data).count()).sort_values(ascending=False))*100
no_values = pd.concat([total,percentage],axis = 1, keys = ['Total', 'Percent'])
no_values.head(50)

#sum of null values to see how many of them have same number
data.isnull().sum()

#heatmap of null matrix
sns.heatmap(data.isnull(), cbar=False)
#as sum was same so checking if they are really equal or not
#Use Index. tolist() function to convert the index into a list.
missing_height=data[data['Height'].isnull()].index.tolist()
missing_weight=data[data['Weight'].isnull()].index.tolist()
if missing_height == missing_weight:
    print("They Are Same")
else:
    print("They are different")
    
#as the assupmtion was right they were same so therefore dropping that particular part   
data.drop(data.index[missing_height],inplace=True)

data.isnull().sum()

#as all of 3 have null values so dropping them out
data.drop(['Loaned From','Release Clause','Joined'],axis=1,inplace=True)

#converting milion and thousand sign to its values
def value_to_int(data_value):
    try:
        value=float(data_value[1:-1])
        suffix=data_value[-1:]
        
        if suffix == 'M':
            value=value*1000000
        elif suffix== 'K':
            value=value*1000
    except ValueError:
        value=0
    return value
data['Value']=data['Value'].apply(value_to_int)
data['Wage']=data['Wage'].apply(value_to_int)

#or by this method
for num,value in enumerate(data["Value"]):
    value=list(value)
    value.pop(0)
    if value[-1] is "M":
        x=1000000
        value.pop()
        value=("").join(value)
        data["Value"][num]=float(value)*x
    elif value[-1] is "K":
        x=1000
        value.pop()
        value=("").join(value)
        data["Value"][num]=float(value)*x
    else:
        data["Value"][num]=float(value[0])

data.head().T

#top 5 countries with highest number of players
print(data['Nationality'].value_counts().head(5))

#Total number of clubs present and top 5 clubs with highest number of players
print('Total no. of clubs Present : {0}'.format(data['Club'].nunique()))
print(data['Club'].value_counts().head(5))

data.sort_values(by="Overall")
data["Overall"].idxmax()
data.iloc[data["Overall"].idxmax()]

data.iloc[data["Wage"].idxmax()]

data.iloc[data["Value"].idxmax()]

f=data.groupby("Club").sum()["Value"].sort_values(ascending=False)[:10]
z=data.groupby("Club").sum()["Value"].sort_values(ascending=False)[:10].index

plt.figure(figsize=(14,14))
sns.lineplot(x=z,y=f)


sns.lmplot(data = data, x = 'Age', y = 'SprintSpeed',lowess=True,scatter_kws={'alpha':0.01, 's':5,'color':'green'}, 
           line_kws={'color':'red'})

sns.lmplot(x = 'BallControl', y = 'Dribbling', data = data,col = 'Preferred Foot',scatter_kws = {'alpha':0.1,'color':'orange'},
           line_kws={'color':'red'})

sns.jointplot(x=data['Dribbling'], y=data['Crossing'], kind="hex", color="#4CB391")

y.iplot()
y
sns.lmplot(x)

fig = tx.pie(data,values="Value",names="Nationality")
fig.show()
data



#MODELLING

df=pd.read_csv('data.csv')

#DROP UNNECESSARY VALUES
drop_cols = df.columns[28:54]
df = df.drop(drop_cols, axis = 1)
df = df.drop(['Unnamed: 0','ID','Photo','Flag','Club Logo','Jersey Number','Joined','Special','Loaned From','Body Type', 'Release Clause',
               'Weight','Height','Contract Valid Until','Wage','Value','Name','Club'], axis = 1)
df = df.dropna()
df.head()



#Turn Real Face into a binary indicator variable
def face_to_num(df):
    if (df['Real Face'] == 'Yes'):
        return 1
    else:
        return 0
    
#Turn Preferred Foot into a binary indicator variable
def right_footed(df):
    if (df['Preferred Foot'] == 'Right'):
        return 1
    else:
        return 0

#Create a simplified position varaible to account for all player positions
def simple_position(df):
    if (df['Position'] == 'GK'):
        return 'GK'
    elif ((df['Position'] == 'RB') | (df['Position'] == 'LB') | (df['Position'] == 'CB') | (df['Position'] == 'LCB') | (df['Position'] == 'RCB') | (df['Position'] == 'RWB') | (df['Position']=='LWB')):
        return 'DF'
    elif ((df['Position'] == 'LDM') | (df['Position'] == 'CDM') | (df['Position'] == 'RDM')):
        return 'DM'
    elif ((df['Position'] == 'LM') | (df['Position'] == 'LCM') | (df['Position'] == 'CM') | (df['Position'] == 'RCM') | (df['Position'] == 'RM')):
        return 'MF'
    elif ((df['Position'] == 'LAM') | (df['Position'] == 'CAM') | (df['Position'] == 'RAM') | (df['Position'] == 'LW') | (df['Position'] == 'RW')):
        return 'AM'
    elif ((df['Position'] == 'RS') | (df['Position'] == 'ST') | (df['Position'] == 'LS') | (df['Position'] == 'CF') | (df['Position'] == 'LF') | (df['Position'] == 'RF')):
        return 'ST'
    else:
        return df.Position
#Create a copy of the original dataframe to avoid indexing errors
df1 = df.copy()

#Apply changes to dataset to create new column
df1['Real_Face'] = df1.apply(face_to_num, axis=1)
df1['Right_Foot'] = df1.apply(right_footed, axis=1)
df1['Simple_Position'] = df1.apply(simple_position,axis = 1)

#Split ID as a Target value
target = df1.Overall
df2 = df1.drop(['Overall'], axis = 1)

#Splitting into test and train
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df2, target, test_size=0.2)

#One Hot Encoding
X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)
print(X_test.shape,X_train.shape)
print(y_test.shape,y_train.shape)

#Applying Linear Regression
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
predictions = model.predict(X_test)

#Finding the r2 score and root mean squared error
from sklearn.metrics import r2_score, mean_squared_error
print('r2 score: '+str(r2_score(y_test, predictions)))
print('RMSE : '+str(np.sqrt(mean_squared_error(y_test, predictions)))