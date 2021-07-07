import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import os, sys

nebins = 800  # fix this somehow
ebins = np.arange(0,nebins)

#====================================================================================
def get_ncols(filename):
    with open(filename) as f:
        n_cols = len(f.readline().split())
    f.close()
    return n_cols

#====================================================================================
def load_file(filename):
    data = np.loadtxt( filename, usecols=tuple([2,6]+list(range(9, get_ncols(filename)))) )
    data = np.c_[ data[:,0], 0.197327*data[:,1],
                  np.amin(data[:,2:], axis=1), np.amax(data[:,2:], axis=1) ]
    # max violation histogram
    hist, bins = np.histogram(data[:,1], bins=nebins, weights=data[:,3])
    result = np.c_[ data[0,0]*np.ones(hist.size), bins, hist ]
    print(result.shape)
    return result
    
#====================================================================================
if __name__ == "__main__":
    dataToPlot = np.array([load_file(filename) for filename in sys.argv[1:]])
    print(dataToPlot.shape)
    print(dataToPlot.size)
    #dataToPlot = dataToPlot.reshape( len(dataToPlot)/(3*ebins.size), ebins.size, 3 )
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    ax.pcolormesh(dataToPlot[:,:,0], dataToPlot[:,:,1], dataToPlot[:,:,2])
    
    #plt.show()
    outfilename = './charvel_density_plot.png'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

    
        