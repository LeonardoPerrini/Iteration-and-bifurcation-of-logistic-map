import math
import numpy as np
import matplotlib.pyplot as plt
r_min=float(input("inserisci il valore minimo di lambda (in genere 1): "))
r_max=float(input("inserisci il valore massimo di lambda (in genere 4): "))
m=int(input("inserisci il numero di intervalli per il range di suddivisione di lambda (10000 di solito funziona bene): "))
def logistic(r, x):
    #defnisco la funzione logistica
    return r * x * (1 - x)
r = np.linspace(r_min, r_max, m)
iterations = 1000
last = 100
x = 1e-5 * np.ones(m)
fig, ax1 = plt.subplots(1, 1)
for i in range(iterations):
    x = logistic(r, x)
    # mostriamo il diagramma a biforcazione.
    if i >= (iterations - last):
        ax1.plot(r, x, ',k', alpha=.25)
ax1.set_xlim(r_min, r_max)
ax1.set_title("Bifurcation diagram")
plt.show()