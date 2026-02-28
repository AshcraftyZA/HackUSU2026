import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
import statsmodels.api as sm
from statsmodels.stats.anova import anova_lm

MaxDif = pd.read_csv("/workspaces/HackUSU2026/DataResults1.csv")

# print(MaxDif.head())

# print(MaxDif.info())
# print(MaxDif.describe())
print(MaxDif['Milkshake Mixes'].head())

