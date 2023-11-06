"""
Max(Z) = 2*x1 + x2

x1 + x2 <= 8
3x1 + x2 <= 18

"""

import matplotlib.pyplot as plt
import numpy as np

# Definimos los rangos de x1 y x2.
x1 = np.linspace(0, 10, 400)
x2 = np.linspace(0, 10, 400)

# Creamos la malla de puntos.
X1, X2 = np.meshgrid(x1, x2)

# Calculamos las inecuaciones.
ineq1 = X1 + X2 <= 8
ineq2 = 3*X1 + X2 <= 18

# Definimos los rangos de x1 y x2 para el segundo cuadrante.
x1_neg = np.linspace(-10, 0, 400)

# Creamos la malla de puntos para el segundo cuadrante.
X1_neg, X2 = np.meshgrid(x1_neg, x2)

# Calculamos las inecuaciones simétricas para el segundo cuadrante.
ineq1_neg = -X1_neg + X2 <= 8
ineq2_neg = -3*X1_neg + X2 <= 18

# Definimos los rangos de x1 y x2 para el tercer y cuarto cuadrante.
x1_neg = np.linspace(-10, 0, 400)
x2_neg = np.linspace(-10, 0, 400)

# Creamos la malla de puntos para el tercer y cuarto cuadrante.
X1_neg, X2_neg = np.meshgrid(x1_neg, x2_neg)

# Calculamos las inecuaciones simétricas para el tercer y cuarto cuadrante.
ineq1_neg_neg = -X1_neg + -X2_neg <= 8
ineq2_neg_neg = -3*X1_neg + -X2_neg <= 18
# Creamos la malla de puntos para el cuarto cuadrante usando las variables x1 y x2_neg.
X1, X2_neg = np.meshgrid(x1, x2_neg)

# Calculamos las inecuaciones simétricas para el cuarto cuadrante.
ineq1_pos_neg = X1 + -X2_neg <= 8
ineq2_pos_neg = 3*X1 + -X2_neg <= 18

# Graficamos las regiones que cumplen las inecuaciones en todos los cuadrantes nuevamente.
plt.figure(figsize=(8,8))
plt.imshow(((ineq1) & (ineq2)).astype(int), 
           extent=(X1.min(), X1.max(), X2.min(), X2.max()), 
           origin="lower", cmap="Greys", alpha = 0.3)
plt.imshow(((ineq1_neg) & (ineq2_neg)).astype(int), 
           extent=(X1_neg.min(), X1_neg.max(), X2.min(), X2.max()), 
           origin="lower", cmap="Greys", alpha = 0.3)
plt.imshow(((ineq1_neg_neg) & (ineq2_neg_neg)).astype(int), 
           extent=(X1_neg.min(), X1_neg.max(), X2_neg.min(), X2_neg.max()), 
           origin="lower", cmap="Greys", alpha = 0.3)
plt.imshow(((ineq1_pos_neg) & (ineq2_pos_neg)).astype(int), 
           extent=(X1.min(), X1.max(), X2_neg.min(), X2_neg.max()), 
           origin="lower", cmap="Greys", alpha = 0.3)

# Graficamos las líneas de las inecuaciones para todos los cuadrantes.
#Ejes cartesianos
plt.axhline(0, color='black')
plt.axvline(0, color='black')
#Inecuaciones
plt.plot(x1, 8 - x1)
plt.plot(x1, 18 - 3*x1)
plt.plot(x1_neg, 8 + x1_neg)
plt.plot(x1_neg, 18 + 3*x1_neg)
plt.plot(x1_neg, -8 - x1_neg)
plt.plot(x1_neg, -18 - 3*x1_neg)
plt.plot(x1, -18 + 3*x1)
plt.plot(x1, -8 + x1)

# Añadimos detalles al gráfico.
plt.xlim((-10, 10))
plt.ylim((-10, 10))
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')

# Añadimos la leyenda.
plt.legend()

# Mostramos la gráfica.
plt.show()
