from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
from IPython.display import HTML
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

# Definir la función que genera la superficie del corazón
def corazon_3d(x, y, z):
    a = (x**2 + (9/4)*(y**2) + z**2 - 1)**3
    b = x**2*z**3
    c = (9/80)*(y**2)*(z**3)
    return a - b - c

# Función para agregar una imagen en el centro del corazón
def agregar_imagen_en_centro(ax, imagen, tamaño_imagen, posicion_imagen):
    imagen_offset = OffsetImage(imagen, zoom=0.3)
    ab = AnnotationBbox(imagen_offset, posicion_imagen,
                        xybox=(0, 0),
                        xycoords='data',
                        boxcoords="offset points",
                        pad=0.0,
                        frameon=False)
    ax.add_artist(ab)

# Crear la figura y el eje 3D
bbox=(-1.5, 1.5)
xmin, xmax, ymin, ymax, zmin, zmax = bbox*3
fig = plt.figure(figsize=(18, 18))
ax = fig.add_subplot(111, projection='3d')
ax.set_facecolor('black')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

ax.set_zlim3d(zmin, zmax)
ax.set_xlim3d(xmin, xmax)
ax.set_ylim3d(ymin, ymax)

# Inicializar la superficie del corazón
A = np.linspace(xmin, xmax, 100) 
B = np.linspace(xmin, xmax, 50)
A1, A2 = np.meshgrid(A, A)

for z in B:
    X, Y = A1, A2
    Z = corazon_3d(X, Y, z)
    cset = ax.contour(X, Y, Z+z, [z],
                      zdir='z', colors=('red'))

for y in B:
    X, Z = A1, A2
    Y = corazon_3d(X, y, Z)
    cset = ax.contour(X, Y+y, Z, [y],
                      zdir='y', colors=('red'))

for x in B:
    Y, Z = A1, A2
    X = corazon_3d(x, Y, Z)
    cset = ax.contour(X+x, Y, Z, [x],
                      zdir='x',colors=('red'))

plt.show()