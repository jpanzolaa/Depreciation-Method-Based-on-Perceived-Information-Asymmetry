import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import PercentFormatter
import pandas as pd

# Cargar el archivo proporcionado y leer los datos de la hoja "DT"
file_path = 'mnt\data\Datos_Modificados VE(SYD).xlsx'
data_dt = pd.read_excel(file_path, sheet_name='DT')

# Contar el número de ventas por empresa
sales_count = data_dt['Empresa'].value_counts()

# Extraer las marcas (empresas) y el número de ventas (frecuencia)
brands = sales_count.index.tolist()
sales = sales_count.values.tolist()

# Ordenar los datos de mayor a menor
sorted_sales = sorted(sales, reverse=True)
sorted_brands = [x for _, x in sorted(zip(sales, brands), reverse=True)]

# Calcular porcentaje acumulado para la curva de Pareto
cumulative_sales = np.cumsum(sorted_sales)
pareto_curve = cumulative_sales / cumulative_sales[-1] * 100

# Crear el gráfico de barras con los datos ordenados
fig, ax1 = plt.subplots(figsize=(10, 6), dpi=300)  # DPI alto para calidad de publicación

# Dibujar las barras con una paleta de colores más sutil
bars = ax1.bar(sorted_brands, sorted_sales, color='#4a90e2', alpha=0.85, edgecolor='gray', linewidth=0.8)
ax1.set_xlabel('Car Brands', fontsize=12, labelpad=10)
ax1.set_ylabel('Sales', fontsize=12, labelpad=10)
ax1.tick_params(axis='x', rotation=90, labelsize=10)
ax1.tick_params(axis='y', labelsize=10)
#ax1.set_title('Car Sales by Brand with Pareto Curve', fontsize=14, pad=15, fontweight='bold')

# Ocultar o mostrar los bordes de los ejes (spines) en el gráfico de barras (ax1)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)
ax1.spines['left'].set_visible(True)
ax1.spines['bottom'].set_visible(True)

# Añadir los valores encima de cada barra
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, f'{int(height)}', ha='center', va='bottom', fontsize=10)

# Crear un segundo eje y para la curva de Pareto
ax2 = ax1.twinx()
ax2.plot(sorted_brands, pareto_curve, color='#d9534f', marker='o', linestyle='-', linewidth=2, markersize=5, label='Pareto Curve')
ax2.set_ylabel('Cumulative Percentage (%)', fontsize=12, labelpad=10)
ax2.tick_params(axis='y', labelsize=10)
ax2.yaxis.set_major_formatter(PercentFormatter())

# Ocultar o mostrar los bordes de los ejes (spines) en la curva de Pareto (ax2)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(True)
ax2.spines['bottom'].set_visible(True)

# Añadir la cuadrícula sólo al eje izquierdo para las barras
ax1.grid(True, which='major', axis='both', linestyle='--', color='gray', alpha=0.7)
ax2.grid(False)

# Ajustar el diseño para que se vea mejor
plt.tight_layout()

# Añadir borde de color gris claro alrededor de la figura
fig.patch.set_edgecolor('lightgray')
fig.patch.set_linewidth(2)
fig.patch.set_facecolor('white')

# Añadir leyenda
ax2.legend(loc="center right", fontsize=10, frameon=False)

# Guardar la figura en alta resolución para publicación
plt.savefig('figures\Fig04.png', bbox_inches='tight', dpi=300)
plt.savefig('figures\Fig04.pdf', bbox_inches='tight', dpi=300)

# Mostrar el gráfico
plt.show()

