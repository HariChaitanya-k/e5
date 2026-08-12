import pandas as pd
df=pd.read_csv("D:/New folder/MOSFET_ID_VDS.csv")
print(df.columns)
print(df.shape)
print(df.describe())