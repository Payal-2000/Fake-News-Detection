import pandas as pd
df = pd.read_csv("fake1.csv", usecols = ['date'])
print(df.loc[5][0])