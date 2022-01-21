import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,LabelEncoder
from sklearn.cluster import KMeans
#load data
data = pd.read_csv("hospital.csv")
print(data)

#data preprocessing
nan=data.iloc[:,3:5]
print(nan)
data= data.drop(nan,axis=1)
data= data.dropna(subset=["Score","Sample"])
print(data)

data.dtypes
data.columns
pd.unique(data['ProviderNumber'])
print(data['City'].value_counts())
data['Score'].describe()

data=data.drop([43,327,332,374,536,628,674,889,919],axis=0)
print(data)
data=data.drop([51,157,350,389,410,492,797,866,921],axis=0)
print(data)
data=data.drop([318,564,579,809],axis=0)
print(data)
data=data.drop([418,653],axis=0)
data=data.drop(["Address1","City","State","ZipCode","CountyName","PhoneNumber"],axis=1)
print(data)
data=data.drop_duplicates(subset=["MeasureCode","Stateavg"])
print(data)
data['EmergencyService']=data.iloc[:,10:11].values
print(data['EmergencyService'])

#data encoding

le=LabelEncoder()
data['EmergencyService'] = le.fit_transform(data['EmergencyService'])
print(data['EmergencyService'])

df=data.iloc[:,9:12]
print(df)

HospitalOwner = df.iloc[:,0:1].values
print(HospitalOwner)
condition=df.iloc[:,2:].values
emergency_services=df['EmergencyService'].values

ohe=OneHotEncoder()
condition=ohe.fit_transform(condition).toarray()
print(condition)
ohe=OneHotEncoder()
HospitalOwner=ohe.fit_transform(HospitalOwner).toarray()
print(HospitalOwner)

ca

