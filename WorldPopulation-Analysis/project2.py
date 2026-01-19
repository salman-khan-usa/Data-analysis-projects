import matplotlib.pyplot as plt
import pandas as pd


df = pd.read_csv('world_population.csv')
# print(df.columns)
# print(df.shape)
# print(df.head)

df.drop(['CCA3','Rank'],axis=1,inplace=True)
print(df)

#Changing Name 
df.loc[221,'Country/Territory'] = 'USA'
print(df)




#Top 10 Most Populated countries
top10  = df.nlargest(10,'2022 Population')
print(top10[['Country/Territory','2022 Population','World Population Percentage']])


#Ploting A Bar chart
plt.bar(top10['Country/Territory'],top10['2022 Population'],color='Green')
plt.xticks(rotation=25)
plt.xlabel('Countries')
plt.ylabel('Population 2022 (Billion)')
plt.title('Top 10 Populated Countries (2022)')
plt.tight_layout
plt.show()




#Comapre Top 5 Countries with 2000 vs 2022
countries = ['China','India','USA','Indonesia' ,'Pakistan']
subset = df[df['Country/Territory'].isin(countries)][['Country/Territory','2000 Population','2022 Population']]
subset.plot(x='Country/Territory',kind='bar')
plt.ylabel('Population in Billion')
plt.xticks(rotation = 25)
plt.title('Camparison of 2022 vs 2000')
plt.show()



#Continents camparison
continent = df.groupby('Continent')['2022 Population'].sum()
plt.pie(continent,labels=continent.index,autopct="%1.1f%%",colors=['Red','blue','yellow','purple','green','grey'])
plt.title('Continent Population Distribution Of 2022')
plt.show()
