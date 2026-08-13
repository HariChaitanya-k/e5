import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("D:/New folder/MOSFET_ID_VDS.csv")
plt.figure(figsize=(10, 6)) # a new window, 10 x 6 inches
for v_gs, group in df.groupby('V_GS (V)'):
     plt.plot(
 group['V_DS (V)'], # x data
 group['I_D (mA)'], # y data
 marker='o', # a dot at every measured point
 linewidth=2,label=f'$V_{{GS}}$ = {v_gs} V') # thicker line
plt.xlabel('Drain-Source Voltage V_DS (V)')
plt.ylabel('Drain Current I_D (mA)')
plt.savefig('f.png',
dpi=300)
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()