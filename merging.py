import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(r'/Users/marrionmac/PycharmProjects/bda_594/triage.csv')
df2 = pd.read_csv(r'/Users/marrionmac/PycharmProjects/bda_594/diagnosis.csv')

# inner join tables using subject_id
merged_inner = df.merge(right=df2, how='inner', on='subject_id')
df = pd.DataFrame(merged_inner)

# Remove irrelevant columns
df = df.drop(['icd_title', 'icd_version', 'icd_code', 'chiefcomplaint', 'seq_num', 'stay_id_y', 'subject_id', 'stay_id_x'], axis=1)

# Identify rows with Null values
is_NaN = df.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = df[row_has_NaN]

#print("Rows in total:", df.shape)
#print("Rows with missing values:", rows_with_NaN.shape)

# Drop rows with missing values (is this a good idea?..)
df = df.dropna(axis=0)
#print("Remaining rows without missing values:", df.shape)

# Correlation Matrix
corrMatrix = round(df.corr(),2)
#sn.heatmap(corrMatrix, annot=True)
#plt.show() # no significant ( > 0.8) correlations yay!

# label dependent/independent variables
# acuity considered the classifier, 1=most severe, 2:5=not as severe
dv = df.acuity # dependent variable
ivs = df.loc[:, df.columns != 'acuity'] # all other columns as independent variables

# histograms of all numerical variables
# df['temperature'].hist(bins=15, figsize=(15,6))

sn.scatterplot(x=df['temperature'], y=dv)
plt.show()






