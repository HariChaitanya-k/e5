import pandas as pd, numpy as np, matplotlib.pyplot as plt

df=pd.read_csv("D:/New folder/MOSFET_ID_VDS.csv")# columns: V_DS (V), V_GS (V), I_D (mA)

fig, ax = plt.subplots(1, 2, figsize=(11, 4.2)) # two panels side by side

for v_ds, g in df.groupby('V_DS (V)'):
 g = g.sort_values('V_GS (V)') # ALWAYS sort the sweep axis
 gm = np.gradient(g['I_D (mA)'], g['V_GS (V)'])

 ax[0].plot(g['V_GS (V)'], g['I_D (mA)'], linewidth=2,
 label=f'$V_{{DS}}$ = {v_ds} V')
 ax[1].plot(g['V_GS (V)'], gm, linewidth=2,
label=f'$V_{{DS}}$ = {v_ds} V')

ax[0].set_title('Transfer characteristics', fontweight='bold')
ax[0].set_xlabel('$V_{GS}$ (V)'); ax[0].set_ylabel('$I_D$ (mA)')
ax[1].set_title('Transconductance $g_m = dI_D/dV_{GS}$', fontweight='bold')
ax[1].set_xlabel('$V_{GS}$ (V)'); ax[1].set_ylabel('$g_m$ (mS)')
for a in ax:
 a.grid(True, linestyle='--', alpha=0.6)
 a.legend(fontsize=9)

plt.tight_layout()
plt.savefig('gm_transfer.png', dpi=300) # save BEFORE show
plt.show()