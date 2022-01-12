import pandas as pd
import matplotlib.pyplot as plt

titan = pd.read_csv('https://vincentarelbundock.github.io/Rdatasets/csv/carData/TitanicSurvival.csv')
pd.set_option('precision', 2)

print (titan.head())
print (titan.tail())
print (titan.describe())

fig = plt.figure()
plt.hist(titan['age'])
fig.suptitle('Ages of Passengers on Titanic')
plt.xlabel('Age(in Years)')
plt.ylabel('Count')
plt.show()
