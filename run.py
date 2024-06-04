import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from matplotlib.animation import FuncAnimation
from matplotlib import cm


def update(frames):
    (x, t) = np.meshgrid(np.linspace(0, 5, 100), np.linspace(frames, 10 + frames, 100))
    z = np.sqrt(2) * np.multiply(np.sin((n * np.pi * x) / L), np.sin((n * np.pi * c * t) / L) + theta)
    rgb = ls.shade(z,
                   cmap=cm.cool,
                   vert_exag=1.,
                   blend_mode='hsv',
                   # fraction=1.
                   )
    ax.clear()
    ax.plot_surface(x, t, z,
                    # cmap=cm.cool,
                    facecolors=rgb,
                    norm=norm)
    ax.set_title('1D Wave Equation')
    ax.set_axis_off()
    return ax,


n = 3.
L = 5.
theta = np.pi / 4.
c = np.sqrt(.5 / 1.)
norm = plt.Normalize(-1., 1.)
fig = plt.figure(figsize=(10, 10))
ax = fig.gca(projection='3d')
ls = LightSource(270, 45)

ani = FuncAnimation(fig, update, frames=150, interval=0, blit=True)
# ani.save('1d_wave_equation_visualization.mp4', fps=50)
plt.show()
