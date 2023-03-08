from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ninetyData.csv', index_col = 'LDPC_2021')
#print(df.describe)

scaler = StandardScaler
print(df.describe())

#df['LDPC_2021_T', 'LDPC_2020_T', 'LDPC_2019_T', 'LDPC_2018_T', 'LDPC_2017_T'] = scaler.fit_transform(df['LDPC_2021', 'LDPC_2020', 'LDPC_2019', 'LDPC_2018', 'LDPC_2017'])
#print(df[LDPC_2021_T, LDPC_2020_T, LDPC_2019_T, LDPC_2018_T, LDPC_2017_T])

kmeans = KMeans(n_clusters=5)
kmeans.fit(df[['LDPP_2018','Latitude']])
df['kmeansVal'] = kmeans.labels_


plt.scatter(x=df['LDPP_2018'], y=df['Latitude'], c = df['kmeansVal'])
plt.show()
