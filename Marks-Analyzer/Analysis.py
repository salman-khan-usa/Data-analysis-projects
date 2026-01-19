import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Marks-Analyzer/marks.csv')
print(df)
print(df.info())

#Total Marks For each student
df['Total/400'] = df[['Physics','Chemistry','Math','Computer']].sum(axis=1)

#Percentage for each student
df['Percentage'] = df['Total/400']/400*100

#Adding Grade
def grades(g):

    if g >= 90:
        return 'A+(90)'
    elif g >= 85:
        return 'A(85)'
    elif g >= 70:
        return'B+(70)'
    elif g > 50:
        return 'C(50)'
    else:
        'F'


df['Grade'] = df['Percentage'].apply(grades)


#Subject Analysis
Average_marks = df[['Math','Physics','Chemistry','Computer']].mean()
Max_marks     = df[['Math','Physics','Chemistry','Computer']].max()
Min_marks = df[['Math','Physics','Chemistry','Computer']].min()



df.to_csv('Final_marks.csv',index=False)
