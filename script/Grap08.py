import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Cargar el archivo Excel proporcionado
file_path = 'mnt\data\Datos_Modificados VE(SYD).xlsx'
df = pd.read_excel(file_path, sheet_name='DT')

# Convertir las columnas relevantes a formato numérico
df['Initial Price'] = pd.to_numeric(df['Initial Price'], errors='coerce')
df['Current Price'] = pd.to_numeric(df['Current Price'], errors='coerce')
df['Model'] = pd.to_numeric(df['Model'], errors='coerce')
df['Accumulated kilometers'] = pd.to_numeric(df['Accumulated kilometers'], errors='coerce')

# Calcular la depreciación anual usando el método de línea recta (SLM)
df['Annual Depreciation'] = (df['Initial Price'] - df['Current Price']) / (2025 - df['Model'])

# Crear el nuevo dataframe con las columnas solicitadas
ndf = df[['Empresa', 'Initial Price', 'Current Price', 'Model', 'Accumulated kilometers', 'Annual Depreciation']]

# Crear una tabla pivote para tener el valor promedio de 'Annual Depreciation' en el cruce entre 'Empresa' y 'Model'
pivot_table = ndf.pivot_table(values='Annual Depreciation', index='Empresa', columns='Model', aggfunc='mean')

# Rellenar NaN con un valor adecuado para el heatmap (los NaN no serán pintados)
pivot_table_filled = pivot_table.fillna(np.nan)

# Configurar los subplots para mostrar dos gráficos en un layout de 1 fila y 2 columnas
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Subplot 1: Heatmap de Depreciación Anual Promedio por Empresa y Modelo
cmap = sns.color_palette("coolwarm", as_cmap=True)
cax = axes[0].imshow(pivot_table_filled, cmap=cmap, aspect='auto')

# Añadir la barra de color
fig.colorbar(cax, ax=axes[0])

# Configurar los ejes
axes[0].set_xticks(np.arange(len(pivot_table_filled.columns)))
axes[0].set_yticks(np.arange(len(pivot_table_filled.index)))
axes[0].set_xticklabels(pivot_table_filled.columns)
axes[0].set_yticklabels(pivot_table_filled.index)

# Rotar las etiquetas del eje x para que se vean mejor
plt.setp(axes[0].get_xticklabels(), rotation=90)

# Añadir los valores en las celdas, omitiendo NaN o ceros, y reducir el tamaño de la fuente
for (i, j), val in np.ndenumerate(pivot_table_filled.values):
    if not np.isnan(val):  # Mostrar sólo si no es NaN
        axes[0].text(j, i, f'{val:.2f}', ha='center', va='center', color='black', fontsize=6)

# Títulos y etiquetas
axes[0].set_title('(a)', fontsize=14, weight='bold') # Depreciación Anual Promedio\nPor Empresa y Modelo (Heatmap) - Average Annual Depreciation by Company and Model (Heatmap)
axes[0].set_xlabel('Model (Year)', fontsize=12)
axes[0].set_ylabel('Brand', fontsize=12)

# Configurar los bordes de los ejes para el heatmap
axes[0].spines['top'].set_visible(False)
axes[0].spines['right'].set_visible(False)
axes[0].spines['left'].set_visible(True)
axes[0].spines['bottom'].set_visible(True)

# Subplot 2: Gráfico de Barras Apiladas
pivot_table_filled.plot(kind='bar', stacked=True, ax=axes[1], color=sns.color_palette("Paired", len(pivot_table.columns)))
axes[1].set_title('(b)', fontsize=14, weight='bold') # Depreciación Anual Promedio\nPor Empresa y Modelo (Barras Apiladas) - Average Annual Depreciation by Company and Model (Stacked Bar Chart)
axes[1].set_xlabel('Brand', fontsize=12)
axes[1].set_ylabel('Average Annual Depreciation', fontsize=12)

# Configurar los bordes de los ejes para el gráfico de barras apiladas
axes[1].spines['top'].set_visible(False)
axes[1].spines['right'].set_visible(False)
axes[1].spines['left'].set_visible(True)
axes[1].spines['bottom'].set_visible(True)

# Ajustar los gráficos
plt.tight_layout()

# Guardar la figura en alta resolución para publicación
plt.savefig('figures\Fig08.png', bbox_inches='tight', dpi=300)
plt.savefig('figures\Fig08.pdf', bbox_inches='tight', dpi=300)

# Exportar la tabla pivote a un archivo CSV
csv_file_path = 'mnt\data\Mod_1_DF.csv'
pivot_table_filled.to_csv(csv_file_path)

# Mostrar el gráfico
plt.show()
