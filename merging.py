import pandas as pd
import seaborn as sn
import csv
import matplotlib.pyplot as plt
import numpy as np
import sklearn
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

df = pd.read_csv(r'triage.csv')
df2 = pd.read_csv(r'diagnosis.csv')

# inner join tables using subject_id
merged_inner = df.merge(right=df2, how='inner', on='subject_id')
df = pd.DataFrame(merged_inner)

# Remove irrelevant columns
df = df.drop(['icd_title', 'icd_version', 'icd_code', 'chiefcomplaint', 'seq_num', 'stay_id_y', 'subject_id', 'stay_id_x'], axis=1)

# Identify rows with Null values
is_NaN = df.isnull()
row_has_NaN = is_NaN.any(axis=1)
rows_with_NaN = df[row_has_NaN]

print("Rows in total:", df.shape)
print("Rows with missing values:", rows_with_NaN.shape)

# Drop rows with missing values (is this a good idea?..)
df = df.dropna(axis=0)
print("Remaining rows without missing values:", df.shape)

# Correlation Matrix
corrMatrix = round(df.corr(),2)
sn.heatmap(corrMatrix, annot=True)
#plt.show() # no significant ( > 0.8) correlations yay!

# recoding dependent variable 'acuity'
# acuity considered the classifier, 1:2=need medical attention, 3:5=not as severe
df["acuity"].replace({2: 1, 3: 0, 4: 0, 5: 0}, inplace=True)

# check if dependent variable is impartial
total_count = df.shape[0]
not_severe = df[df.acuity == 0].shape[0]
severe = df[df.acuity == 1].shape[0]
severe_Ratio = severe/total_count
not_severe_Ratio = not_severe/total_count
print("Ratio of severe:", severe_Ratio)
print("Ratio of not severe:", not_severe_Ratio)
print("Total count:", total_count)
print("Total rows:", df.shape)

# count outliers for observations
# pain_hi_outliers = df[df.pain > 10]
# pain_lo_outliers = df[df.pan < 0]
# print(pain_hi_outliers)
# print(pain_lo_outliers)

# temp_hi_outliers = df[df.temperature > 108]
# temp_lo_outliers = df[df.temperature < 75]
# print(len(temp_hi_outliers))
# print(len(temp_lo_outliers))

# df.to_csv(r'cleaned_data.csv')











