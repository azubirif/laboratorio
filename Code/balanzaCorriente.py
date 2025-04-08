import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.stats import linregress

datos = pd.read_excel("../BalanzaCorriente.ods", engine="odf")
x = datos.iloc[:5, 3]
y = datos.iloc[:5, 2]
errores_x = [0.0001] * 5
errores_y = [0.01*10**-3] * 5

plt.scatter(x, y)

for xi, yi, ex, ey in zip(x, y, errores_x, errores_y):
    plt.hlines(yi, xi - ex, xi + ex, color='red', linestyles='solid')  # Barras en x
    plt.vlines(xi, yi - ey, yi + ey, color='green', linestyles='solid')  # Barras en y

plt.xlabel('Longitud (m)')
plt.ylabel('Fuerza normal (N)')
plt.title('Balanza de corriente - Intensidad constante')
plt.grid(True)
plt.savefig('images/f_n_contra_l.png', dpi=300)

resultado = linregress(list(x), list(y))

print(f"Pendiente: {resultado.slope:.4f} ± {resultado.stderr:.4f}")
print(f"Intercepto: {resultado.intercept:.4f} ± {resultado.intercept_stderr:.4f}")
print(f"Correlación: {resultado.rvalue:.4f}")
