import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import os, sys

tau0 = 0.0    # initialize tau0
tau = 0.0     # ditto for tau
maxDeltatau = 0.8 # maximum duration to plot
nebins = 200  # fix this somehow
ebins = np.arange(0,2.0,0.01)

dirname = os.path.dirname(sys.argv[1])

#====================================================================================
def get_ncols(filename):
    with open(filename) as f:
        n_cols = len(f.readline().split())
    f.close()
    return n_cols

#====================================================================================
def load_file(filename, i):
    global tau0, tau
    if tau - tau0 > maxDeltatau:
        return np.array([])
    data = np.loadtxt( filename, usecols=tuple([2,6,7,8]+list(range(9, get_ncols(filename)))) )
    tau = data[0,0]
    if i==0:
        tau0 = tau
    print('Processing tau =', tau)
    #print(data.shape)
    #print(data[:,2:].shape)
    #print(np.amax(data[:,2:], axis=1).shape)
    data = np.c_[ data[:,0], 0.197327*data[:,1],
                  np.amin(data[:,4:], axis=1), np.amax(data[:,4:], axis=1),
                  data[:,2], data[:,3] ]
    data = data[np.where( (data[:,4]==1) & (data[:,5]==1) )]
    data[:,3] = np.array(list(map(lambda x : np.max([x,0.0]), data[:,3])))
    # max violation histogram
    hist0, bins0 = np.histogram(data[:,1], bins=ebins, weights=np.ones(data[:,1].size))
    w = np.sqrt(data[:,3])-1.0
    hist, bins = np.histogram(data[:,1], bins=ebins, weights=w*np.heaviside(w,0.0))
    #print(bins.size)
    #print(hist.size)
    return np.c_[ data[0,0]*np.ones(hist.size), 0.5*(bins[:-1]+bins[1:]), hist/(hist0+1e-100), hist, hist0 ]
    
#====================================================================================
if __name__ == "__main__":
    #dataToPlot = np.array([load_file(filename) for filename in sys.argv[1:81]])
    dataToPlot = np.array([load_file(filename,i) for i, filename in enumerate(sys.argv[1:81])])
    #(lambda x : x[np.where(np.array(list(map(len,x)))!=0)].astype(float))(np.array([f(x) for x in range(10)],dtype=object))
    #print(dataToPlot.shape)
    #print(dataToPlot.size)
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    psm = ax.pcolormesh(dataToPlot[:,:,0], dataToPlot[:,:,1], dataToPlot[:,:,2], \
                        shading='nearest', vmin = 0.0, vmax = 0.20)
    #x = dataToPlot[:,:,0]
    #y = dataToPlot[:,:,1]
    #extent = np.min(x), np.max(x), np.min(y), np.max(y)
    #m = dataToPlot[:,:,2]
    #psm = plt.imshow(m.T, interpolation='bilinear', extent=extent)
    cbar = fig.colorbar(psm, ax=ax)
    cbar.set_label(r'$v_{\mathrm{char}}/c$', fontsize=16)

    
    #print(dataToPlot.shape)
    #print(len(dataToPlot))
    newLen=dataToPlot.size
    #print(newLen)
    #print(newLen/3)
    toSave = dataToPlot.reshape([int(newLen/5),5])
    np.savetxt(dirname + '/../charvel_density.dat', toSave, fmt='%12.8f')
    
    ax.set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
    ax.set_ylabel(r'$e$ (GeV/fm$^3$)', fontsize=16)
    
    #plt.show()
    outfilename = dirname + '/../charvel_density_plot.png'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

    
        