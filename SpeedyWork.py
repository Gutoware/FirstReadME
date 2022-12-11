import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Written to import the csv file and to show the columns in the dataset
df = pd.read_csv(r'forbes2013.csv')
print(df)
df.info()

#Sorting the dataset by biggest sales to be able to accurately label and recall during the presentation
df2 = df.sort_values(by=['Sales'], ascending=False)
print(df2)

#Counting the frequency of companies and the country they are based in
print(df['Country'].value_counts())

#Creating charts to be used in the presentation. 'Country' was listed out to add lables to the proceeding chart data
country=df['Country'].value_counts().tolist()
country=country[0:5]
Countryname=['United States', 'Japan', 'China', 'United Kingdom', 'Canada']
print(country)


plt.bar(Countryname, country)
plt.ylabel('Frequency')
plt.title('Top 5 Countries according to Forbes 2013')
plt.show()

