import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo adjunto proporcionado por el usuario
file_path = 'mnt\data\Datos_Modificados VE(SYD).xlsx'

# Leer el archivo Excel
df_vehiculos = pd.read_excel(file_path)

# Suposición: la calidad percibida está inversamente relacionada con los kilómetros acumulados.
# Usamos una escala simple donde la calidad es 100 - (kilómetros/1000)
df_vehiculos['Quality'] = 100 - (df_vehiculos['Accumulated kilometers'] / 1000)

# Función de utilidad del comprador (v(Q) - P)
def buyer_utility(quality, price):
    # La valoración percibida (v(Q)) se asume igual a la calidad
    return quality - price / 10000000  # Factor para ajustar la escala de los precios

# Función de utilidad del vendedor (P - c(Q))
def seller_utility(quality, price):
    # Costo de calidad (c(Q)) se asume inversamente proporcional a la calidad
    cost = 100 - quality
    return price / 1000000 - cost  # Factor para ajustar la escala de los precios

# Aplicar las funciones de utilidad
df_vehiculos['Buyer Utility'] = df_vehiculos.apply(lambda row: buyer_utility(row['Quality'], row['Current Price']), axis=1)
df_vehiculos['Seller Utility'] = df_vehiculos.apply(lambda row: seller_utility(row['Quality'], row['Current Price']), axis=1)

# Obtener las ecuaciones de las líneas de tendencia
z_buyer = np.polyfit(df_vehiculos['Quality'], df_vehiculos['Buyer Utility'], 1)
z_seller = np.polyfit(df_vehiculos['Quality'], df_vehiculos['Seller Utility'], 1)

equation_buyer = f"y = {z_buyer[0]:.2f}x + {z_buyer[1]:.2f}"
equation_seller = f"y = {z_seller[0]:.2f}x + {z_seller[1]:.2f}"

# Encontrar el punto de intersección entre las dos líneas
m1, b1 = z_buyer
m2, b2 = z_seller
x_intersect = (b2 - b1) / (m1 - m2)
y_intersect = m1 * x_intersect + b1

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(12, 7))

# Gráfico de utilidad del comprador (triángulo) y vendedor (círculo)
ax.scatter(df_vehiculos['Quality'], df_vehiculos['Buyer Utility'], color=(0/255, 0/255, 139/255, 150/255), 
            label='Buyer Utility', s=100, alpha=0.7, edgecolors='black', marker='^')  # Triángulo para Buyer
ax.scatter(df_vehiculos['Quality'], df_vehiculos['Seller Utility'], color=(152/255, 251/255, 152/255, 125/255), 
            label='Seller Utility', s=100, alpha=0.7, edgecolors='black', marker='o')  # Círculo para Seller

# Agregar las líneas de tendencia
p_buyer = np.poly1d(z_buyer)
p_seller = np.poly1d(z_seller)
ax.plot(df_vehiculos['Quality'], p_buyer(df_vehiculos['Quality']), color=(0/255, 0/255, 139/255, 150/255), linestyle='--', linewidth=2)
ax.plot(df_vehiculos['Quality'], p_seller(df_vehiculos['Quality']), color=(152/255, 251/255, 152/255, 125/255), linestyle='--', linewidth=2)

# Agregar el punto de intersección como un cuadrado con transparencia
ax.scatter(x_intersect, y_intersect, color='red', s=200, alpha=0.5, zorder=5, label='Intersection Point', marker='s')  # Cuadrado con 50% transparencia

# Etiquetas de ejes
ax.set_xlabel('Perceived Quality (based on accumulated kilometers)', fontsize=14)
ax.set_ylabel('Utility (scaled)', fontsize=14)

# Título y subtítulo
#ax.set_title('Buyer and Seller Utility vs. Perceived Quality of Vehicles\nMarket Analysis', fontsize=16, weight='bold')

# Mostrar leyenda
ax.legend(loc='upper left', fontsize=12)

# Agregar anotaciones explicativas
ax.text(50, 200, 'Buyer Utility', color=(0/255, 0/255, 139/255, 150/255), fontsize=12)
ax.text(70, 500, 'Seller Utility', color=(152/255, 251/255, 152/255, 125/255), fontsize=12)

# Agregar las ecuaciones de las líneas rectas y las coordenadas del punto de intersección
ax.text(10, 800, f"Buyer Utility: {equation_buyer}", color=(0/255, 0/255, 139/255, 150/255), fontsize=12, weight='bold')
ax.text(10, 750, f"Seller Utility: {equation_seller}", color=(0/255, 100/255, 0/255, 175/255), fontsize=12, weight='bold')
ax.text(10, 700, f"Intersection Point: ({x_intersect:.2f}, {y_intersect:.2f})", color='red', fontsize=12, weight='bold')

# Agregar cuadrícula
ax.grid(True)

# Configurar los bordes de los ejes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(True)
ax.spines['bottom'].set_visible(True)

# Mostrar gráfico
plt.tight_layout()

# Guardar la figura en alta resolución para publicación
plt.savefig('figures\Fig11.png', bbox_inches='tight', dpi=300)
plt.savefig('figures\Fig11.pdf', bbox_inches='tight', dpi=300)

plt.show()
