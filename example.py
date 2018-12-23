import os
import numpy as np
import matplotlib.pyplot as plt

from one_euro_filter import OneEuroFilter


frames = 100
t = np.linspace(0, 4*np.pi, frames)
x = np.sin(t) + np.random.normal(scale=0.1, size=len(t))
x_hat = np.zeros_like(x)
x_hat[0] = x[0]
# TODO: tune coefficients
one_euro_filter = OneEuroFilter(
    t[0], x[0],
    min_cutoff=0.004,
    beta=0.005
)
for i in range(1, len(t)):
    x_hat[i] = one_euro_filter(t[i], x[i])


# The figure
# https://eli.thegreenplace.net/2016/drawing-animated-gifs-with-matplotlib/
fig, ax = plt.subplots()
fig.set_tight_layout(True)
signal, _ = ax.plot(t[0], x[0], 'o')
filtered, _ = ax.plot(t[0], x_hat[0], '-')

def update(i):
    print(i)
    signal.set_data(t[0:i], x[0:i])
    filtered.set_data(t[0:i], x_hat[0:t])
    return signal, filtered


if __name__ == '__main__':
    # FuncAnimation will call the 'update' function for each frame; here
    # animating over 10 frames, with an interval of 200ms between frames.
    anim = FuncAnimation(fig, update, frames=np.arange(0, frames), interval=20)
    if len(sys.argv) > 1 and sys.argv[1] == 'save':
        anim.save('signal.gif', dpi=80, writer='imagemagick')
    else:
        # plt.show() will just loop the animation forever.
        plt.show()
