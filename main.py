import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

data = pd.read_csv("DatasetL5_2.csv")

sns.scatterplot(data=data, x="sex", y="val")
plt.show()
sns.histplot(data=data['val'], bins=20)
plt.show()
sns.histplot(data['val'])
plt.show()
sns.jointplot(x='upper', y='val', data=data, kind='reg')
plt.show()
sns.pairplot(data, hue='val')
plt.show()
x = data['val']
y = data['upper']
fig = px.scatter(x=x, y=y)
fig.update_layout(
    legend_orientation="h",
    legend=dict(x=0.5, xanchor='center'),
    title='Plot Title',
    xaxis_title='val',
    yaxis_title='upper',
    margin=dict(l=0, r=0, t=30, b=0)
)
fig.show()
