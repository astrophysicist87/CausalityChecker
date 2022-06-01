import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import os, sys

tau0 = 0.0    # initialize tau0
tau = 0.0     # ditto for tau
maxDeltatau = 0.75 # maximum duration to plot
#nebins = 200  # fix this somehow
#nTbins = 50
ebins = np.arange(0,2.0,0.01)
Tbins = np.arange(125.0,225.0,1.0)
nebins = len(ebins)
nTbins = len(Tbins)

TFOs = [151.0, 143.26]

VISHNUorMUSICmode = int(sys.argv[1])  # 0 == VISHNU, 1 == MUSIC
dirname = os.path.dirname(sys.argv[2])

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
        return (np.zeros((nTbins-1,5))-1000.0)
    data = np.loadtxt( filename, usecols=tuple([2,5,6,7,8]+list(range(9, get_ncols(filename)))) )
    tau = data[0,0]
    if i==0:
        tau0 = tau
    print('Processing tau =', tau, flush=True)

    data = np.c_[ data[:,0], 197.327*data[:,1], 0.197327*data[:,2],
                  np.amin(data[:,5:], axis=1), np.amax(data[:,5:], axis=1),
                  data[:,3], data[:,4] ]
    data = data[np.where( (data[:,5]==1) & (data[:,6]==1) )] # where causality analysis succeeded
    data[:,4] = np.array(list(map(lambda x : np.max([x,0.0]), data[:,4])))

    # max violation histogram
    w = np.sqrt(data[:,4])-1.0
    hist0, bins0 = np.histogram(data[:,1], bins=Tbins, weights=np.ones(data[:,1].size)*np.heaviside(w,0.0))
    hist, bins = np.histogram(data[:,1], bins=Tbins, weights=w*np.heaviside(w,0.0))
    return np.c_[ data[0,0]*np.ones(hist.size), 0.5*(bins[:-1]+bins[1:]), hist/(hist0+1e-100), hist, hist0 ]
    
#====================================================================================
if __name__ == "__main__":
    dataToPlot = np.array([load_file(filename,i) for i, filename in enumerate(sys.argv[2:])])
    dims = dataToPlot.shape
    dataToPlot = dataToPlot.reshape((dims[0]*dims[1],dims[2]))
    dataToPlot = dataToPlot[np.where(dataToPlot[:,0]>0)]
    dims2 = dataToPlot.shape

    dataToPlot = dataToPlot.reshape((dims2[0]//dims[1],dims[1],dims[2]))

    fig, ax = plt.subplots( nrows=1, ncols=1 )
    psm = ax.pcolormesh(dataToPlot[:,:,0], dataToPlot[:,:,1], 1.0+dataToPlot[:,:,2], \
                        shading='gouraud', vmin = 1.0, vmax = 1.20, cmap=plt.get_cmap('magma'))

    cbar = fig.colorbar(psm, ax=ax)
    cbar.set_label(r'$v_{\mathrm{char}}/c$', size=16)
    cbar.ax.tick_params(labelsize=12)
    cbar.set_ticks([1.0,1.05,1.1,1.15,1.2])

    xpts = np.linspace(np.min(dataToPlot[:,:,0]), np.max(dataToPlot[:,:,0]), 3)
    ax.plot(xpts, 0.0*xpts+TFOs[VISHNUorMUSICmode], color='white', ls='--')
    
    newLen=dataToPlot.size
    toSave = dataToPlot.reshape([int(newLen/5),5])
    np.savetxt(dirname + '/../charvel_density_check.dat', toSave, fmt='%12.8f')

    ax.tick_params(axis='both', which='major', labelsize=12)
    ax.set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
    ax.set_ylabel(r'$T$ (MeV)', fontsize=16)
    
    #plt.show()
    outfilename = dirname + '/../charvel_density_plot_check.png'
    #outfilename = './charvel_density_plot.png'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

    
        