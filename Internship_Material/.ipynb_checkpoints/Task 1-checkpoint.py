import pandas as pd
import numpy as np
import matplotlib.pyplot as mt
import seaborn as sb
df=pd.read_csv("Iris.csv")
# print(read.shape)
# print()
# print(read.head())
# print()
# print(read.columns)
# scatter=mt.scatter(read.iloc[:,0],read.iloc[:,1])
# mt.show(scatter)
# print(df.columns)
# df.plot(kind='scatter', x='SepalLengthCm', y='SepalWidthCm',hue='Species')
# sb.show()
sb.scatterplot(data=df,x="SepalLengthCm", y="SepalWidthCm",hue='Species')
mt.show()

