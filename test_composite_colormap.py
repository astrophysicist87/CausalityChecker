import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

vmin, vmax = -4.0, 4.0

def plot_examples(colormaps):
    """
    Helper function to plot data with associated colormap.
    """
    np.random.seed(19680801)
    data = np.random.randn(30, 30)
    n = len(colormaps)
    fig, axs = plt.subplots(1, n, figsize=(n * 2 + 2, 3),
                            constrained_layout=True, squeeze=False)
    for [ax, cmap] in zip(axs.flat, colormaps):
        psm = ax.pcolormesh(data, cmap=cmap, rasterized=True, vmin=vmin, vmax=vmax)
        fig.colorbar(psm, ax=ax)
    plt.show()
    
viridis = cm.get_cmap('viridis', 256)
newcolors = viridis(np.linspace(0, 1, 256))
dataNodes = np.linspace(vmin, vmax, 256)
pink = np.array([248/256, 24/256, 148/256, 1])
newcolors[np.where(dataNodes <= 1), :] = pink
newcmp = ListedColormap(newcolors)

plot_examples([viridis, newcmp])