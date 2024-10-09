# Importar las bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Cargar los datos
file_path = 'mnt\data\Datos_Modificados VE(SYD).xlsx'
data_dt = pd.read_excel(file_path, sheet_name='DT')

# Asegurarse de que la columna de depreciación esté calculada correctamente
if 'Depreciation' not in data_dt.columns:
    data_dt['Depreciation'] = data_dt['Initial Price'] - data_dt['Current Price']

# Convertir las columnas relevantes a formato numérico para evitar errores
data_dt['Current Price'] = pd.to_numeric(data_dt['Current Price'], errors='coerce')
data_dt['Initial Price'] = pd.to_numeric(data_dt['Initial Price'], errors='coerce')
data_dt['Model'] = pd.to_numeric(data_dt['Model'], errors='coerce')
data_dt['Accumulated kilometers'] = pd.to_numeric(data_dt['Accumulated kilometers'], errors='coerce')
data_dt['Depreciation'] = pd.to_numeric(data_dt['Depreciation'], errors='coerce')

# Limpiar los datos, eliminando filas con NaN
data_dt_cleaned = data_dt[['Current Price', 'Initial Price', 'Model', 'Accumulated kilometers', 'Depreciation']].dropna()

# Establecer un estilo profesional
sns.set(style='whitegrid', palette='muted', font_scale=1.2)

# Crear la figura y los subgráficos
plt.figure(figsize=(14, 10))

# Gráfico 1: Relación entre Precio Inicial y Precio Actual con línea de regresión
plt.subplot(2, 2, 1)
sns.regplot(x='Initial Price', y='Current Price', data=data_dt_cleaned, scatter_kws={'alpha':0.6}, line_kws={"color": "red"})
plt.title('(a)', fontsize=14, fontweight='bold') # Relación entre Precio Inicial y Precio Actual - Relationship Between Initial Price and Current Price
plt.xlabel('Initial Price', fontsize=12)
plt.ylabel('Current Price', fontsize=12)

# Gráfico 2: Relación entre Año del Modelo y Kilometraje Acumulado
plt.subplot(2, 2, 2)
sns.scatterplot(x='Model', y='Accumulated kilometers', data=data_dt_cleaned, alpha=0.6, color='green')
plt.title('(b)', fontsize=14, fontweight='bold') # Relación entre Año del Modelo y Kilometraje Acumulado - Relationship Between Model Year and Accumulated Mileage
plt.xlabel('Model Year', fontsize=12)
plt.ylabel('Accumulated kilometers', fontsize=12)

# Gráfico 3: Relación entre Precio Inicial y Depreciación con línea de regresión
plt.subplot(2, 2, 3)
sns.regplot(x='Initial Price', y='Depreciation', data=data_dt_cleaned, scatter_kws={'alpha':0.6}, line_kws={"color": "red"})
plt.title('(c)', fontsize=14, fontweight='bold') # Relación entre Precio Inicial y Depreciación - Relationship Between Initial Price and Depreciation
plt.xlabel('Initial Price', fontsize=12)
plt.ylabel('Depreciation', fontsize=12)

# Gráfico 4: Relación entre Kilometraje Acumulado y Depreciación con línea de regresión
plt.subplot(2, 2, 4)
sns.regplot(x='Accumulated kilometers', y='Depreciation', data=data_dt_cleaned, scatter_kws={'alpha':0.6}, line_kws={"color": "red"})
plt.title('(d)', fontsize=14, fontweight='bold') # Relación entre Kilometraje Acumulado y Depreciación - Relationship Between Accumulated Mileage and Depreciation
plt.xlabel('Accumulated kilometers', fontsize=12)
plt.ylabel('Depreciation', fontsize=12)

# Ajustar el diseño
plt.tight_layout()

# Guardar la figura en alta resolución para publicación
plt.savefig('figures\Fig07.png', bbox_inches='tight', dpi=300)
plt.savefig('figures\Fig07.pdf', bbox_inches='tight', dpi=300)

# Mostrar el gráfico
plt.show()

