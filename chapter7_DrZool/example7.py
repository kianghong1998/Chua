import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

nyc = pd.read_csv('ave_hi_nyc_jan_1895-2018.csv')


print (nyc.head())
print (nyc.tail())

nyc.columns = ['Date', 'Temperature', 'Anomaly']
nyc.Date = nyc.Date.floordiv(100)
linear_regression = stats.linregress (x=nyc.Date, y=nyc.Temperature)
print (linear_regression.slope)
print (linear_regression.intercept)

axes = sns.regplot (x=nyc.Date, y=nyc.Temperature)
sns.set_style('whitegrid')
axes.set_ylim(5,80)
plt.show()
