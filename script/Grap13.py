import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar todos los archivos CSV y Excel
mod_1_df = pd.read_csv('mnt\data\Mod_1_DF.csv')
mod_2_df = pd.read_csv('mnt\data\Mod_2_DF.csv')
mod_3_df = pd.read_csv('mnt\data\Mod_3_DF.csv')
mod_4_df = pd.read_csv('mnt\data\Mod_4_DF.csv')
datos_modificados_ve = pd.read_excel('mnt\data\Datos_Modificados VE(SYD).xlsx')

# Filtrar las columnas relevantes del archivo "Datos_Modificados VE(SYD).xlsx"
datos_modificados_ve = datos_modificados_ve[['Empresa', 'Model', 'Current Price', 'Initial Price']]

# Reorganizar los DataFrames para hacer la comparación, usando melt para convertir las columnas en filas
mod_1_melted = mod_1_df.melt(id_vars=['Empresa'], var_name='Model', value_name='Estimated Price Mod 1').dropna()
mod_2_melted = mod_2_df.melt(id_vars=['Empresa'], var_name='Model', value_name='Estimated Price Mod 2').dropna()
mod_3_melted = mod_3_df.melt(id_vars=['Empresa'], var_name='Model', value_name='Estimated Price Mod 3').dropna()
mod_4_melted = mod_4_df.melt(id_vars=['Empresa'], var_name='Model', value_name='Estimated Price Mod 4').dropna()

# Convertir los años del modelo a enteros para la comparación
mod_1_melted['Model'] = mod_1_melted['Model'].astype(int)
mod_2_melted['Model'] = mod_2_melted['Model'].astype(int)
mod_3_melted['Model'] = mod_3_melted['Model'].astype(int)
mod_4_melted['Model'] = mod_4_melted['Model'].astype(int)

# Unir los datos reales con los resultados estimados de los cuatro métodos
merged_data = datos_modificados_ve.merge(mod_1_melted, on=['Empresa', 'Model'], how='left') \
                                 .merge(mod_2_melted, on=['Empresa', 'Model'], how='left') \
                                 .merge(mod_3_melted, on=['Empresa', 'Model'], how='left') \
                                 .merge(mod_4_melted, on=['Empresa', 'Model'], how='left')

# Calcular los errores absolutos entre los datos reales y las estimaciones de cada método
merged_data['Error Mod 1'] = abs(merged_data['Current Price'] - merged_data['Estimated Price Mod 1'])
merged_data['Error Mod 2'] = abs(merged_data['Current Price'] - merged_data['Estimated Price Mod 2'])
merged_data['Error Mod 3'] = abs(merged_data['Current Price'] - merged_data['Estimated Price Mod 3'])
merged_data['Error Mod 4'] = abs(merged_data['Current Price'] - merged_data['Estimated Price Mod 4'])

# Calcular valores mínimos y máximos individuales para las visualizaciones
min_value_mod1 = merged_data['Error Mod 1'].min()
max_value_mod1 = merged_data['Error Mod 1'].max()

min_value_mod2 = merged_data['Error Mod 2'].min()
max_value_mod2 = merged_data['Error Mod 2'].max()

min_value_mod3 = merged_data['Error Mod 3'].min()
max_value_mod3 = merged_data['Error Mod 3'].max()

min_value_mod4 = merged_data['Error Mod 4'].min()
max_value_mod4 = merged_data['Error Mod 4'].max()

# Crear una figura con 4 subplots, uno para cada matriz de error
fig, axs = plt.subplots(1, 4, figsize=(28, 8), gridspec_kw={'width_ratios': [1, 1, 1, 1]})
cmap = 'coolwarm'

# Función para agregar texto sobre la matriz de calor
def add_text(matrix, ax):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            value = matrix.iloc[i, j]
            if not pd.isna(value):  # Solo agregar texto si no es NaN
                ax.text(j, i, f'{value:.0f}', ha='center', va='center', color='black', fontsize=10)

# Graficar el Error Mod 1
error_mod1_matrix = merged_data.pivot_table(values='Error Mod 1', index='Empresa', columns='Model', aggfunc=np.mean)
heatmap1 = axs[0].imshow(error_mod1_matrix, cmap=cmap, vmin=min_value_mod1, vmax=max_value_mod1, aspect='auto')
axs[0].set_title('(a)', fontsize=14, weight='bold') # Straight-Line Method (SLM)
axs[0].set_yticks(np.arange(len(error_mod1_matrix.index)))
axs[0].set_yticklabels(error_mod1_matrix.index, fontsize=12)
axs[0].set_xticks(np.arange(len(error_mod1_matrix.columns)))
axs[0].set_xticklabels(error_mod1_matrix.columns, rotation=45, ha='right', fontsize=12)
axs[0].grid(False)
fig.colorbar(heatmap1, ax=axs[0], fraction=0.046, pad=0.04).set_label('Absolute Error', fontsize=12)
add_text(error_mod1_matrix, axs[0])

# Graficar el Error Mod 2
error_mod2_matrix = merged_data.pivot_table(values='Error Mod 2', index='Empresa', columns='Model', aggfunc=np.mean)
heatmap2 = axs[1].imshow(error_mod2_matrix, cmap=cmap, vmin=min_value_mod2, vmax=max_value_mod2, aspect='auto')
axs[1].set_title('(b)', fontsize=14, weight='bold') # Declining Balance Method
axs[1].set_xticks(np.arange(len(error_mod2_matrix.columns)))
axs[1].set_xticklabels(error_mod2_matrix.columns, rotation=45, ha='right', fontsize=12)
axs[1].set_yticks([])  # Ocultar etiquetas del eje Y para las matrices 2, 3 y 4
axs[1].grid(False)
fig.colorbar(heatmap2, ax=axs[1], fraction=0.046, pad=0.04).set_label('Absolute Error', fontsize=12)
add_text(error_mod2_matrix, axs[1])

# Graficar el Error Mod 3
error_mod3_matrix = merged_data.pivot_table(values='Error Mod 3', index='Empresa', columns='Model', aggfunc=np.mean)
heatmap3 = axs[2].imshow(error_mod3_matrix, cmap=cmap, vmin=min_value_mod3, vmax=max_value_mod3, aspect='auto')
axs[2].set_title('(c)', fontsize=14, weight='bold') # Sum-of-Years Digits (SYD)
axs[2].set_xticks(np.arange(len(error_mod3_matrix.columns)))
axs[2].set_xticklabels(error_mod3_matrix.columns, rotation=45, ha='right', fontsize=12)
axs[2].set_yticks([])  
axs[2].grid(False)
fig.colorbar(heatmap3, ax=axs[2], fraction=0.046, pad=0.04).set_label('Absolute Error', fontsize=12)
add_text(error_mod3_matrix, axs[2])

# Graficar el Error Mod 4
error_mod4_matrix = merged_data.pivot_table(values='Error Mod 4', index='Empresa', columns='Model', aggfunc=np.mean)
heatmap4 = axs[3].imshow(error_mod4_matrix, cmap=cmap, vmin=min_value_mod4, vmax=max_value_mod4, aspect='auto')
axs[3].set_title('(d)', fontsize=14, weight='bold') # Depreciation method by perception of asymmetric information
axs[3].set_xticks(np.arange(len(error_mod4_matrix.columns)))
axs[3].set_xticklabels(error_mod4_matrix.columns, rotation=45, ha='right', fontsize=12)
axs[3].set_yticks([])  
axs[3].grid(False)
fig.colorbar(heatmap4, ax=axs[3], fraction=0.046, pad=0.04).set_label('Absolute Error', fontsize=12)
add_text(error_mod4_matrix, axs[3])

# Ajustar el diseño
plt.tight_layout()

# Guardar la figura en alta resolución para publicación
plt.savefig('figures\Fig13.png', bbox_inches='tight', dpi=300)
plt.savefig('figures\Fig13.pdf', bbox_inches='tight', dpi=300)

# Mostrar la gráfica final
plt.show()