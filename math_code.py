import sympy as sp
import matplotlib.pyplot as plt

# Definir la variable simbólica n para la muestra en el tiempo discreto
n = sp.Symbol('n', integer=True)

# Definir la señal de ejemplo (puedes cambiar esta señal según tus necesidades)
# Ejemplo: señal periódica con dos componentes frecuenciales
frecuencia_1 = 5  # Hz
frecuencia_2 = 10  # Hz
amplitud_1 = 2
amplitud_2 = 3
muestras = 100
señal = amplitud_1 * sp.sin(2 * sp.pi * frecuencia_1 * n / muestras) + \
         amplitud_2 * sp.sin(2 * sp.pi * frecuencia_2 * n / muestras)

# Definir la Transformada de Fourier Discreta (DFT)
def dft(signal):
    N = len(signal) # Total de puntos de la señal
    n_values = range(N) # Se crea una lista con los indices de la señal, tiempo o posición de cada señal
    return [sum(signal[k] * sp.exp(-2*sp.pi*sp.I*k*n/N) for k in n_values) for n in n_values]

# Calcular la DFT de la señal
dft_result = dft([señal.subs(n, i) for i in range(muestras)])

# Mostrar la señal original y su espectro de amplitud
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(range(muestras), [señal.subs(n, i) for i in range(muestras)])
plt.title('Señal en el dominio del tiempo')
plt.xlabel('Muestra')
plt.ylabel('Amplitud')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(range(muestras), [abs(val) for val in dft_result])
plt.title('Espectro de Amplitud (DFT)')
plt.xlabel('Frecuencia')
plt.ylabel('Amplitud')
plt.grid()

plt.tight_layout()
plt.show()
