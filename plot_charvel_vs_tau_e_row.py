import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
from matplotlib import cm
import os, sys

tau0 = 0.0    # initialize tau0
tau = 0.0     # ditto for tau

dirname = os.path.dirname(sys.argv[1])


#====================================================================================
if __name__ == "__main__":
    # total command-line argument count must be odd
    if len(sys.argv)%2 != 1:
        print("Wrong number of arguments at command-line!")
        exit()
        
    nFiles = (len(sys.argv)-1)//2
    fig, ax = plt.subplots( nrows=1, ncols=nFiles )
    
    # loop over all histograms to plot together
    for dataFile in sys.argv[1::2]:
        dataToPlot = np.loadtxt()

        psm = ax.pcolormesh(dataToPlot[:,:,0], dataToPlot[:,:,1], 1.0+dataToPlot[:,:,2], \
                            shading='gouraud', vmin = 1.0, vmax = 1.20, cmap=plt.get_cmap('magma'))

        cbar = fig.colorbar(psm, ax=ax)
        cbar.set_label(r'$v_{\mathrm{char}}/c$', size=16)
        cbar.ax.tick_params(labelsize=14)

        xpts = np.linspace(np.min(dataToPlot[:,:,0]), np.max(dataToPlot[:,:,0]), 3)
        ax.plot(xpts, 0.0*xpts+TFOs[VISHNUorMUSICmode], color='white', ls='--')


        ax.tick_params(axis='both', which='major', labelsize=14)
        ax.set_xticks(np.arange(tau0,tau,0.1))
        ax.set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
        ax.set_ylabel(r'$T$ (MeV)', fontsize=16)
    
    plt.show()
    #outfilename = dirname + '/../charvel_density_plot.png'
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)

    
        
