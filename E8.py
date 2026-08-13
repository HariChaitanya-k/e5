import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
df=pd.read_csv("D:/New folder/MOSFET_ID_VDS.csv")
plt.figure(2, figsize=(10, 6)) # a SECOND, separate window
for v_gs, group in df.groupby('V_GS (V)'):
    v_ds = group['V_DS (V)']
    i_d = group['I_D (mA)']
    did_dvds = np.gradient(i_d, v_ds) # mA / V = mS
    plt.plot(v_ds, did_dvds, marker='s', linestyle='--', linewidth=2,
    label=f'$V_{{GS}}$ = {v_gs} V')
    # Insert this directly below your loop block
    highest_group = df[df['V_GS (V)'] == df['V_GS (V)'].max()].sort_values('V_DS (V)')
    g_d_sat = np.gradient(highest_group['I_D (mA)'], highest_group['V_DS (V)'])[-1]
    r_o = 1 / g_d_sat
print(f"Resistance r_o in saturation: {r_o:.2f} kΩ")


plt.title('Differential Output Conductance $g_d = dI_D/dV_{DS}$',
fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Drain-to-Source Voltage, $V_{DS}$ (V)', fontsize=12, labelpad=10)
plt.ylabel('Conductance, $g_d$ (mS)', fontsize=12, labelpad=10)
plt.legend(title='Gate-Source Voltage', loc='upper right', fontsize='10')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.savefig('Coundutance.png',
dpi=300)
plt.show()