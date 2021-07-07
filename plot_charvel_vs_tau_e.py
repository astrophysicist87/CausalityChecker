import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import os, sys

nebins = 10  # fix this somehow
ebins = np.arange(0,1*nebins,1)

#====================================================================================
def get_ncols(filename):
    with open(filename) as f:
        n_cols = len(f.readline().split())
    f.close()
    return n_cols

#====================================================================================
def load_file(filename):
    data = np.loadtxt( filename, usecols=tuple([2,6]+list(range(9, get_ncols(filename)))) )
    print(data.shape)
    print(data[:,2:].shape)
    print(np.amax(data[:,2:], axis=1).shape)
    data = np.c_[ data[:,0], 0.197327*data[:,1],
                  np.amin(data[:,2:], axis=1), np.amax(data[:,2:], axis=1) ]
    # max violation histogram
    hist0, bins0 = np.histogram(data[:,1], bins=ebins, weights=np.ones(data[:,1].size))
    w = np.sqrt(data[:,3])-1.0
    hist, bins = np.histogram(data[:,1], bins=ebins, weights=w*np.heaviside(w,0.0))
    #tmp = np.c_[ data[:,0], data[:,1], data[:,3], np.heaviside(np.sqrt(data[:,3])-1.0,0.0) ]
    #print(tmp[np.where(tmp[:,1]>400.0)])
    #print(bins.size)
    #print(hist.size)
    return np.c_[ data[0,0]*np.ones(hist.size), 0.5*(bins[:-1]+bins[1:]), hist/(hist0+1e-100) ]
    
#====================================================================================
if __name__ == "__main__":
    dataToPlot = np.array([load_file(filename) for filename in sys.argv[1:11]])
    print(dataToPlot.shape)
    print(dataToPlot.size)
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    psm = ax.pcolormesh(dataToPlot[:,:,0], dataToPlot[:,:,1], dataToPlot[:,:,2], shading='nearest')
    fig.colorbar(psm, ax=ax)
    
    #print(dataToPlot.shape)
    #print(len(dataToPlot))
    newLen=dataToPlot.size
    #print(newLen)
    #print(newLen/3)
    toSave = dataToPlot.reshape([int(newLen/3),3])
    np.savetxt('./charvel_density.dat', toSave, fmt='%12.8f')
    
    #plt.show()
    outfilename = './charvel_density_plot.png'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

    
        