import pandas as pd
df = pd.read_csv(r'/Users/marrionmac/PycharmProjects/bda_594/triage.csv')
df2 = pd.read_csv(r'/Users/marrionmac/PycharmProjects/bda_594/diagnosis.csv')

# inner join tables using subject_id
merged_inner = pd.merge(left=df, right=df2, left_on='subject_id', right_on='subject_id')
df = merged_inner

# data w wrangling
print(df.head)
