import pandas as pd
import matplotlib.pyplot as plt
import mpld3
from mpld3 import plugins

data = pd.read_excel('Chicago Health Atlas Data Download - Community areas - NO ERROR.xlsx')

# Set the index to 'Name' column (assuming it represents the community name)
data.set_index("Name", inplace=True)

# Select the columns containing lead levels from 2017 to 2021
lead_columns = ["LDPC_2017", "LDPC_2018", "LDPC_2019", "LDPC_2020", "LDPC_2021"]
lead_data = data[lead_columns]

# Transpose the data for easier plotting
lead_data = lead_data.T

# START OF GRAPHING CODE:
# For this code, see example on mlpd3 called "Interactive Legends"
fig, ax = plt.subplots()
ax.grid(True, alpha=0.3)

for key, val in lead_data.items():
    l, = ax.plot(val.index, val.values, label=key)
    ax.fill_between(val.index,
                    0, 0,
                    color=l.get_color(), alpha=.4)

handles, labels = ax.get_legend_handles_labels() # return lines and labels
interactive_legend = plugins.InteractiveLegendPlugin(zip(handles,
                                                         ax.collections),
                                                     labels,
                                                     alpha_unsel=0.5,
                                                     alpha_over=1.5, 
                                                     start_visible=True)
plugins.connect(fig, interactive_legend)

ax.set_xlabel('Year')
# This is a hack, because I cannot figure out how to have less than 8 ticks that are labled correctly.
x_axis_labels = ['2017', '', '2018', '', '2019', '', '2020', '', '2021']
ax.set_xticklabels(x_axis_labels)

ax.set_ylabel('Lead Level')
ax.set_title('Lead Levels from 2017 to 2021')
plt.subplots_adjust(right=.8)

# Save the HTML to test.html
mpld3.save_html(fig, 'communities_leadlevels.html')

# Open up the browser and show a preview.
mpld3.show()