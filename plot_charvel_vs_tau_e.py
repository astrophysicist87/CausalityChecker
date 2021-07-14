import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import os, sys

tau0 = 0.0    # initialize tau0
tau = 0.0     # ditto for tau
maxDeltatau = 0.05 # maximum duration to plot
nebins = 200  # fix this somehow
nTbins = 80
ebins = np.arange(0,2.0,0.01)
Tbins = np.arange(0,400.0,5.0)

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
        return np.array([[]])
    data = np.loadtxt( filename, usecols=tuple([2,5,6,7,8]+list(range(9, get_ncols(filename)))) )
    tau = data[0,0]
    if i==0:
        tau0 = tau
    print('Processing tau =', tau)
    #print(data.shape)
    #print(data[:,2:].shape)
    #print(np.amax(data[:,2:], axis=1).shape)
    data = np.c_[ data[:,0], 197.327*data[:,1], 0.197327*data[:,2],
                  np.amin(data[:,5:], axis=1), np.amax(data[:,5:], axis=1),
                  data[:,3], data[:,4] ]
    data = data[np.where( (data[:,5]==1) & (data[:,6]==1) )] # where causality analysis succeeded
    data[:,4] = np.array(list(map(lambda x : np.max([x,0.0]), data[:,4])))
    # max violation histogram
    hist0, bins0 = np.histogram(data[:,1], bins=Tbins, weights=np.ones(data[:,1].size))
    w = np.sqrt(data[:,4])-1.0
    hist, bins = np.histogram(data[:,1], bins=Tbins, weights=w*np.heaviside(w,0.0))
    #print(bins.size)
    #print(hist.size)
    #print(np.c_[ data[0,0]*np.ones(hist.size), 0.5*(bins[:-1]+bins[1:]), hist/(hist0+1e-100), hist, hist0 ].shape)
    return np.c_[ data[0,0]*np.ones(hist.size), 0.5*(bins[:-1]+bins[1:]), hist/(hist0+1e-100), hist, hist0 ]
    
#====================================================================================
if __name__ == "__main__":
    #dataToPlot = np.array([load_file(filename) for filename in sys.argv[1:81]])
    dataToPlot = np.array([load_file(filename,i) for i, filename in enumerate(sys.argv[1:])])
    #print(dataToPlot)
    #print(np.array(list(map(len,dataToPlot))))
    print(np.where(np.array(list(map(len,dataToPlot)))>1))
    print(dataToPlot[np.where(np.array(list(map(len,dataToPlot)))>1)])
    dataToPlot = np.asarray(dataToPlot[np.where(np.array(list(map(len,dataToPlot)))>1)])
    #(lambda x : x[np.where(np.array(list(map(len,x)))!=0)].astype(float))(np.array([f(x) for x in range(10)],dtype=object))
    #print(dataToPlot.shape)
    #print(dataToPlot.size)
    print(dataToPlot.shape)
    print("Also check:")
    for dataThing in dataToPlot:
        print(dataThing.shape)
    fig, ax = plt.subplots( nrows=1, ncols=1 )
    psm = ax.pcolormesh(dataToPlot[:,:,0], dataToPlot[:,:,1], 1.0+dataToPlot[:,:,2], \
                        shading='nearest', vmin = 1.0, vmax = 1.20)
    #x = dataToPlot[:,:,0]
    #y = dataToPlot[:,:,1]
    #extent = np.min(x), np.max(x), np.min(y), np.max(y)
    #m = dataToPlot[:,:,2]
    #psm = plt.imshow(m.T, interpolation='bilinear', extent=extent)
    cbar = fig.colorbar(psm, ax=ax)
    cbar.set_label(r'$v_{\mathrm{char}}/c$', size=16)

    
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
    #outfilename = dirname + '/../charvel_density_plot.png'
    outfilename = './charvel_density_plot.png'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

    
        