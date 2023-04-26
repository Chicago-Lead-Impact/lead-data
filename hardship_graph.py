import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mpld3
import mplcursors
from mpld3 import plugins

data = pd.read_excel('Chicago_Health_Atlas_Data_Download_Community_areas_3.xlsx', engine='openpyxl')
communites = data["Name"].tolist()
# Set the index to 'Name' column (assuming it represents the community name)
data.set_index("Name", inplace=True)

fig, ax = plt.subplots()

# Calculate the average lead poisoning rate over the years for each location
lead_columns = ['LDPP_2022', 'LDPP_2021', 'LDPP_2020', 'LDPP_2019', 'LDPP_2018', 'LDPP_2017']
data['avg_lead_poisoning'] = data[lead_columns].mean(axis=1)

data['exp_value'] = np.exp(data['INC_2017-2021']/10000)
print(data['exp_value'])

def set_marker_size(x, factor):
    return [x_i**factor for x_i in x]

# Explore the relationship between lead poisoning rates and other variables
# HDX - Hardship index, INC - Income, VRLE - Life expectancy
# variables_to_compare = ['HDX_2017-2021', 'VRLE_2020']
# for variable in variables_to_compare:
#     data.plot.scatter(x='avg_lead_poisoning', y=variable, s=set_marker_size(data['exp_value'], 0.5), edgecolors='black')

scatter = ax.scatter(x=data['avg_lead_poisoning'], y=data['HDX_2017-2021'], s=set_marker_size(data['exp_value'], 0.5), edgecolors='black')

labels =['{0}'.format(x) for x in communites]
tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labels)
ax.set_ylabel('Hardship Index')
ax.set_xlabel('Average Lead Poisoning %')
ax.set_title('Average Lead Poisoning % Rate Compared to Hardship Index & Income per Community')

mpld3.plugins.connect(fig, tooltip)

print(data['avg_lead_poisoning'])

# Save the HTML to test.html
mpld3.save_html(fig, 'hardship_graph.html')

# Open up the browser and show a preview.
# mpld3.show()
#mplcursors.cursor(hover=True)
# #data['Name']

mpld3.show()
# plt.show()

