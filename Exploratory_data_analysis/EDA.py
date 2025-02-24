# -*- coding: utf-8 -*-

# Loading the data and importing necessary libaries and modules
from google.colab import files
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_excel("data_sales.xlsx")

#Basic Understanding and EDA of the dataset
df.head(5)
df.info()
df.shape
df.describe()
df.columns
df.isnull().sum()

#Display sales vs year graph
sns.set_style("white")
sns.set_palette("husl")
sns.set_palette("Reds")
f, ax = plt.subplots(figsize=(15, 10))
ax=sns.despine(f, left=True, bottom=True)
ax=sns.lineplot(data=df,x="Year of Transaction Date",y="Sales")
plt.title("Sales over the Years")
plt.show()

#Display histogram on individual sales by sales reps
f, ax = plt.subplots(figsize=(15, 10))
ax= sns.hist(data=df,x="Sales Rep")
plt.show()

#There are dozens of Sale Rep thereofre histogram is not useful
df["Sales Rep"].unique()

df["Country"].unique()

fig = plt.figure(figsize = (10, 5))
plt.bar(df["Country"],df["Sales"], color ='maroon',
        width = 0.4)
plt.show()
