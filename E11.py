import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
df=pd.read_csv(r"D:\New folder\Diode_IV_Temperature.csv")
plt.figure(figsize=(10, 6)) # a new window, 10 x 6 inches
for i, group in df.groupby('T (C)'):
     plt.plot(
 group['V (V)'], # x data
 group['I (mA)'], # y data
 marker='o', # a dot at every measured point
 linewidth=2,label=f'$V_{{D}}$ = {i} V') # thicker line
plt.xlabel('Diode voltage')
plt.ylabel('Diode current I_D (mA)')
plt.savefig('Diode_I_V.png',
dpi=350)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()