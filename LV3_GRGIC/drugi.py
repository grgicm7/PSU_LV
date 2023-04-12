import pandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')

mpg_by_cyl = mtcars.groupby('cyl')['mpg'].mean()
plt.bar(mpg_by_cyl.index, mpg_by_cyl.values, color = 'orchid')
plt.xlabel('broj cilindara')
plt.ylabel('mpg')
plt.show()


boxplot= mtcars.boxplot(by='cyl', column=['wt'], color='purple', boxprops=dict(color='violet'))
plt.show()


colors1=['purple', 'violet']
x_labels = ['Automatski', 'Rucni']
ax = mtcars.groupby(['am']).mpg.mean().plot.bar(stacked=True, title='Potrosnja s obzirom na mjenjac', ylabel='mpg', xlabel='Mjenjac', rot=0, color = colors1)
ax.set_xticklabels(x_labels)
plt.show()