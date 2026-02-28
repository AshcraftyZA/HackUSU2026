import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm
import os

print("Current directory:", os.getcwd())
print("Files in directory:", os.listdir())
#Reads in the data
MaxDif = pd.read_csv("DataResults1.csv")
#Drops some of the unessicary columns
maxdif = MaxDif.drop(columns=[
    'Record ID',
    'MaxDiff1_Fit (RLH)',
    'Model fit relative quality'
])
#calculates the mean
mean = maxdif.mean().sort_values(ascending=True)
print("Means calculated")
#Defines the size of the figure
plt.figure(figsize=(10,12))
#Tell what type of graph
mean.plot(kind="barh")

#Naming the x label
plt.xlabel("Average Utility Score")
#Naming the chart
plt.title("MaxDiff Results: Average Preferences")

plt.tight_layout()
#creates the pdf
plt.savefig("maxdiff_plot.png")
#lets the user know the graph is created
print("Plot saved successfully.")