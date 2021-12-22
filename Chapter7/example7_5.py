import matplotlib.pyplot as plt
import numpy as np
import random
import seaborn as sns
import sys

# use lisd comprehension to create a list of rolls of a six-sided die
rolls = [random.randrange(1,7) for i in range(int(sys.argv[1]))]

# NumPy uniqie function returns unique faces and frequency of each face
values, frequencies = np.unique(rolls, return_counts=True)

#title = f'Rolling a Six-Sided Die {len(rolls):,} Times'
sns.set_style('whitegrid')
axes = sns.barplot(values, frequencies, palette='bright')
#axes.set_title(title) # set graph title
axes.set(xlabel="Die Value", ylabel='Frequency')

# scale y-axis by 10% to make room for test above bars
axes.set_ylim(top=max(frequencies)*1.10)

# display frequency & percentage above each patch (bar)
for bar, frequency in zip(axes.patches, frequencies):
    text_x = bar.get_x() + bar.get_width() / 2.0
    text_y = bar.get_height()
    axes.text (text_x, text_y, text_y,
               fontsize=11, ha='center', va='bottom')
               
plt.show() #display graph
