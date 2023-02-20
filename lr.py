#import numpy as np
#import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('../results.xlsx')
data.head()

plt.figure(figsize=(10,10))
#plt.scatter(data['Initial'],data['Sequential'])
plt.title('Test')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()