import csv
import plotly.express as px
import pandas as pd 

df = pd.read_csv('data.csv')

studentMean = df.groupby(['student_id','level'], as_index=False)['attempt'].mean()
figure = px.scatter(studentMean,x='student_id',y='level', size='attempt', color='attempt')
print(studentMean)
figure.show()
