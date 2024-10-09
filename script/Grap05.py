# Importar bibliotecas necesarias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos del archivo Excel
file_path = 'mnt\data\Datos_Modificados VE(SYD).xlsx'
data_dt = pd.read_excel(file_path, sheet_name='DT')

# Establecer el estilo de Seaborn para darle un aspecto más profesional
sns.set(style='whitegrid', palette='muted', font_scale=1.2)

# Crear la figura y los subgráficos
plt.figure(figsize=(14, 10))

# Gráfico 1: Distribución del Precio Actual
plt.subplot(2, 2, 1)
sns.histplot(data_dt['Current Price'], bins=20, kde=True, color='#1f77b4')
plt.title('(a)', fontsize=14, fontweight='bold') # Distribución del Precio Actual
plt.xlabel('Current Price', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(True)

# Gráfico 2: Distribución del Precio Inicial
plt.subplot(2, 2, 2)
sns.histplot(data_dt['Initial Price'], bins=20, kde=True, color='#2ca02c')
plt.title('(b)', fontsize=14, fontweight='bold') # Distribución del Precio Inicial
plt.xlabel('Initial Price', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(True)

# Gráfico 3: Distribución del Año del Modelo
plt.subplot(2, 2, 3)
sns.histplot(data_dt['Model'], bins=10, kde=False, color='#9467bd')
plt.title('(c)', fontsize=14, fontweight='bold') # Distribución del Año del Modelo
plt.xlabel('Model', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(True)

# Gráfico 4: Distribución del Kilometraje Acumulado
plt.subplot(2, 2, 4)
sns.histplot(data_dt['Accumulated kilometers'], bins=20, kde=True, color='#d62728')
plt.title('(d)', fontsize=14, fontweight='bold') # Distribución del Kilometraje Acumulado
plt.xlabel('Accumulated kilometers', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.grid(True)

# Ajustar el diseño para mejorar la visibilidad y estética
plt.tight_layout()

# Guardar la figura en alta resolución para publicación
plt.savefig('figures\Fig05.png', bbox_inches='tight', dpi=300)
plt.savefig('figures\Fig05.pdf', bbox_inches='tight', dpi=300)

# Mostrar el gráfico
plt.show()
