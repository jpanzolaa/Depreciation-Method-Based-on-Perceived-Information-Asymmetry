# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar los datos del archivo Excel
file_path = 'mnt\data\Datos_Modificados VE(SYD).xlsx'
data_dt = pd.read_excel(file_path, sheet_name='DT')

# Asegurarse de que la columna de depreciación esté calculada correctamente
if 'Depreciation' not in data_dt.columns:
    data_dt['Depreciation'] = data_dt['Initial Price'] - data_dt['Current Price']

# Seleccionar las variables numéricas para el análisis de correlación
data_dt_cleaned = data_dt[['Current Price', 'Initial Price', 'Model', 'Accumulated kilometers', 'Depreciation']].apply(pd.to_numeric, errors='coerce').dropna()

# Calcular la matriz de correlación
correlation_matrix = data_dt_cleaned.corr()

# Crear un mapa de calor con matplotlib
fig, ax = plt.subplots(figsize=(10, 8))  # Aumentar tamaño para mejor visualización

# Crear el mapa de calor con una paleta de colores más sutil
cax = ax.matshow(correlation_matrix, cmap='RdBu', vmin=-1, vmax=1)

# Añadir una barra de color con mejor diseño
cbar = fig.colorbar(cax, ax=ax, fraction=0.046, pad=0.04)
cbar.ax.tick_params(labelsize=12)

# Establecer las etiquetas de los ejes sin negrilla
ax.set_xticks(np.arange(len(correlation_matrix.columns)))
ax.set_yticks(np.arange(len(correlation_matrix.index)))
ax.set_xticklabels(correlation_matrix.columns, rotation=45, ha='right', fontsize=12)  # Sin negrilla
ax.set_yticklabels(correlation_matrix.index, fontsize=12)  # Sin negrilla

# Mover las etiquetas del eje x a la parte inferior
ax.xaxis.set_ticks_position('bottom')

# Añadir los valores dentro de cada celda con formato profesional
# Valores cercanos a 1 se muestran en blanco, el resto en negro
for i in range(len(correlation_matrix.columns)):
    for j in range(len(correlation_matrix.index)):
        value = correlation_matrix.iloc[i, j]
        color = 'white' if abs(value) > 0.9 else 'black'  # blanco si está cerca de 1, de lo contrario negro
        ax.text(j, i, f'{value:.2f}', 
                ha='center', va='center', color=color, fontsize=12, fontweight='medium')

# Mejorar el título del gráfico
#plt.title('Mapa de Calor de la Correlación entre Variables', fontsize=16, fontweight='bold', pad=30) # Mapa de Calor de la Correlación entre Variables

# Ajustar el diseño para evitar solapamientos
plt.tight_layout()

# Guardar la figura en alta resolución para publicación
plt.savefig('figures\Fig06.png', bbox_inches='tight', dpi=300)
plt.savefig('figures\Fig06.pdf', bbox_inches='tight', dpi=300)

# Mostrar el gráfico
plt.show()
