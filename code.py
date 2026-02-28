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
def bar_graph (color_option, row_count):
    #calculates the mean
    mean = maxdif.mean().sort_values(ascending=True)
    #defining the rows
    mean = mean.tail(row_count)
    plt.figure(figsize=(10,12))
    #Tell what type of graph
    mean.plot(kind="barh", color = color_option)

    #Naming the x label
    plt.xlabel("Average Utility Score")
    #Naming the chart
    plt.title("MaxDiff Results: Average Preferences")

    plt.tight_layout()
    #creates the pdf
    plt.savefig("maxdiff_plot.png")
Rachael = 1
while Rachael == 1:
    while True:
        row_count = int(input("How many rows do you want to see? "))
        if row_count == -1:
            print("Exiting.")
            break
        if row_count >= 15:
            print("Max of 15 rows")
        color_option = input("What color do you want the graph? Blue, Green, or Red? Type -1 to break ")
        if color_option == "-1":
            print("Exiting.")
            break
        else:
            bar_graph(color_option, row_count)
            print("Plot saved successfully.")
            satisfaction = input("Are you satisfied? Y/N: ")
            if satisfaction == "Y":
                Rachael += 1
                break
#lets the user know the graph is created
