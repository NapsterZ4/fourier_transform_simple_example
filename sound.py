import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Cargar la señal de audio (por ejemplo, un archivo .wav)
sample_rate, audio_data = wavfile.read('testing-audio.wav')

# Calcular la Transformada de Fourier Discreta (DFT)
dft = np.fft.fft(audio_data)
frequencies = np.fft.fftfreq(len(dft), 1/sample_rate)

# Mostrar la señal de audio
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(audio_data)
plt.title('Señal de Audio')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.grid()

# Mostrar el espectro de amplitud (magnitud)
plt.subplot(2, 1, 2)
plt.plot(frequencies, np.abs(dft))
plt.title('Espectro de Amplitud')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Amplitud')
plt.grid()

plt.tight_layout()
plt.show()
