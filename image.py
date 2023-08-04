import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft2, ifft2, fftshift

# Cargar la imagen en escala de grises
imagen = cv2.imread('messi.jpeg')

# Calcular la transformada de Fourier 2D de la imagen
transformada = fft2(imagen)

# Mover el componente de frecuencia cero al centro del espectro
transformada_desplazada = fftshift(transformada)

# Calcular el espectro de amplitud
espectro_amplitud = np.abs(transformada_desplazada)

# Aplicar un filtro para resaltar los contornos en el espectro de amplitud
# Por ejemplo, podemos aplicar un umbral para eliminar las frecuencias de baja amplitud y conservar las de alta amplitud.
umbral = 0.0000001
espectro_amplitud[espectro_amplitud < umbral] = 0

# Recuperar la transformada original deshaciendo el desplazamiento
transformada_filtrada = fftshift(transformada_desplazada * (espectro_amplitud > 0))

# Calcular la transformada inversa para obtener la imagen filtrada
imagen_filtrada = np.abs(ifft2(transformada_filtrada))

# Visualizar la imagen original y la imagen filtrada
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(imagen_filtrada, cmap='gray')
plt.title('Imagen Filtrada')
plt.axis('off')

plt.show()
