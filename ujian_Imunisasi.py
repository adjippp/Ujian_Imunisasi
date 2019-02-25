import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 

df = pd.read_csv('Balita Terimunisasi BCG 1995-2017.csv',header=None,skiprows=1,na_values='n.a')
df2 = pd.read_csv('Balita Terimunisasi Campak 1995-2017.csv',header=None,skiprows=1,na_values='n.a')
df3 = pd.read_csv('Balita Terimunisasi DPT 1995-2017.csv',header=None,skiprows=1,na_values='n.a')
df4 = pd.read_csv('Balita Terimunisasi Polio 1995-2017.csv',header=None,skiprows=1,na_values='n.a')

dfbcg=df.interpolate()
dfcampak=df2.interpolate()
dfdpt=df3.interpolate()
dfpolio=df4.interpolate()
x1=dfbcg.iloc[:,0].values
y1=dfbcg.iloc[:,1].values
x2=dfcampak.iloc[:,0].values
y2=dfcampak.iloc[:,1].values
x3=dfdpt.iloc[:,0].values
y3=dfdpt.iloc[:,1].values
x4=dfpolio.iloc[:,0].values
y4=dfpolio.iloc[:,1].values

#==============================#
y1a=np.array(dfbcg.iloc[:,1].values)
y2a=np.array(dfcampak.iloc[:,1].values)
y3a=np.array(dfdpt.iloc[:,1].values)
y4a=np.array(dfpolio.iloc[:,1].values)

plt.figure('Balita Terimunisasi')

plt.subplot(221)
xtampung1=np.arange(0,len(x1))
plt.bar(xtampung1,y1,color='red')
plt.title('BCG')
plt.xticks(xtampung1,x1,rotation=90)

plt.subplot(222)
xtampung2=np.arange(0,len(x2))
plt.bar(xtampung2,y2,color='green')
plt.title('Campak')
plt.xticks(xtampung2,x2,rotation=90)

plt.subplot(223)
xtampung3=np.arange(0,len(x3))
plt.bar(xtampung3,y3,color='yellow')
plt.title('DPT')
plt.xticks(xtampung3,x3,rotation=90)

plt.subplot(224)
xtampung4=np.arange(0,len(x4))
plt.bar(xtampung4,y4,color='blue')
plt.title('Polio')
plt.xticks(xtampung4,x4,rotation=90)

plt.figure('Balita Tak Terimunisasi')

plt.subplot(221)
xtampung1=np.arange(0,len(x1))
y1hasil=100-y1a
plt.bar(xtampung1,y1hasil,color='red')
plt.title('BCG')
plt.xticks(xtampung1,x1,rotation=90)

plt.subplot(222)
xtampung2=np.arange(0,len(x2))
y2hasil=100-y2a
print(y2hasil)
plt.bar(xtampung2,y2hasil,color='green')
plt.title('Campak')
plt.xticks(xtampung2,x2,rotation=90)

plt.subplot(223)
xtampung3=np.arange(0,len(x3))
y3hasil=100-y3a
plt.bar(xtampung3,y3hasil,color='yellow')
plt.title('DPT')
plt.xticks(xtampung3,x3,rotation=90)

plt.subplot(224)
xtampung4=np.arange(0,len(x4))
y4hasil=100-y4a
plt.bar(xtampung4,y4hasil,color='blue')
plt.title('Polio')
plt.xticks(xtampung4,x4,rotation=90)
plt.show()
