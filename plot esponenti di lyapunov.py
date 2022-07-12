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
lyapunov = np.zeros(m)
for i in range(iterations):
    x = logistic(r, x)
    # calcoliamo la somma parziale dell'
    # Esponente di Lyapunov.
    lyapunov += np.log(abs(r - 2 * r * x))
# mostriamo l'esponente di Lyapunov.
# linea orizzontale.
ax1.axhline(0, color='k', lw=.5, alpha=.5)
# esponente di Lyapunov negativo.
ax1.plot(r[lyapunov < 0],
         lyapunov[lyapunov < 0] / iterations,
         '.k', alpha=.5, ms=.5)
# esponente di Lyapunov positivo.
ax1.plot(r[lyapunov >= 0],
         lyapunov[lyapunov >= 0] / iterations,
         '.r', alpha=.5, ms=.5)
ax1.set_xlim(r_min, r_max)
ax1.set_ylim(-2, 1)
ax1.set_title("Esponente di Lyapunov")
plt.tight_layout()
plt.show()