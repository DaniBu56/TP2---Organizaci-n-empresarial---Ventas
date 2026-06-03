import pandas as pd
import matplotlib.pyplot as plt

# Cargar dataset
df = pd.read_csv("datos/ventas.csv")

# Mostrar primeras filas para verificar
print("Primeras filas del dataset:")
print(df.head())

# Indicadores básicos
ventas_totales = df["TotalValue"].sum()
producto_mas_vendido = df["Product"].value_counts().idxmax()
ventas_por_mes = df.groupby("Date")["TotalValue"].sum()

print("\nVentas totales:", ventas_totales)
print("Producto más vendido:", producto_mas_vendido)
print("Ventas por mes:\n", ventas_por_mes)

# Gráfico
plt.figure(figsize=(10,6))
ventas_por_mes.plot(kind="line", marker="o", color="skyblue")
plt.title("Evolución de ventas por fecha")
plt.xlabel("Fecha")
plt.ylabel("Monto de ventas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")
plt.show()
