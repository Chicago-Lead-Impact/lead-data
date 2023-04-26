import pandas as pd
import matplotlib.pyplot as plt
import mpld3

#Load the Excel file
df = pd.read_excel('Chicago Health Atlas Data Download - Community areas - NO ERROR.xlsx')

#List of years and corresponding columns
years = range(2010, 2022)
columns = [f'LDPP_{year}' if year >= 2017 else f'LDPPH_{year}' for year in years]

#Create a new DataFrame with only the relevant columns and transpose it
ldpp_df = df[['Name'] + columns] # Select the relevant columns
ldpp_df = ldpp_df.set_index('Name').T # Transpose the DataFrame

#Create a line plot for each community area
plt.figure(figsize=(12, 8)) # Set the figure size
high_rates = ldpp_df.max(axis=0).sort_values(ascending=False)[:10].index # Get the names of the top 10 communities
low_rates = ldpp_df.max(axis=0).sort_values()[:10].index # Get the names of the bottom 10 communities


#Plot the top 10 communities
# plt.subplot(2, 1, 1)
fig, ax = plt.subplots()
for name in low_rates:
  plt.plot(years, ldpp_df[name], label=name)
  plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
  plt.title('Top 10 Communities with the Lowest Lead Poisoning Rates')
  plt.xlabel('Year')
  plt.ylabel('Lead Poisoning Rate (%)')
  plt.grid()

labels = [str(x) for x in years]
print(labels)
ax.set_xticklabels(labels)

#Adjust layout and display the plot
plt.tight_layout()
# plt.show()

# Save the HTML to test.html
mpld3.save_html(fig, 'low_10_communities.html')

# Open up the browser and show a preview.
mpld3.show()