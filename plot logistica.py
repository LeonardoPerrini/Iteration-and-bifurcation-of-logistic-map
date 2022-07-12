import math
import numpy as np
import matplotlib.pyplot as plt
r=float(input("inserisci il valore di lambda: "))
def logistic(r, x):
    #defnisco la funzione logistica
    return r * x * (1 - x)
x = np.linspace(0, 1)
fig, ax = plt.subplots(1, 1)
ax.plot(x, logistic(r, x), 'k', lw=1)
plt.show()