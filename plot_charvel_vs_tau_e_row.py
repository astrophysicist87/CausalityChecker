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
    fig, axs = plt.subplots( nrows=1, ncols=nFiles, figsize=(17.5,5) )
    plt.subplots_adjust( hspace=-0.01, wspace=0.025 )
    
    # loop over all histograms to plot together
    for i in range(nFiles):
        dataDimsFile = sys.argv[2*i+1]
        print('Loading', dataDimsFile)
        dim0, dim1, dim2, tau0, tau, TFO = np.loadtxt(dataDimsFile)
        dataFile = sys.argv[2*(i+1)]
        print('Loading', dataFile)
        dataToPlot = np.loadtxt(dataFile).reshape([int(d) for d in (dim0,dim1,dim2)])

        psm = axs[i].pcolormesh(dataToPlot[:,:,0], dataToPlot[:,:,1], 1.0+dataToPlot[:,:,2], \
                            shading='gouraud', vmin = 1.0, vmax = 1.20, cmap=plt.get_cmap('magma'))

        xpts = np.linspace(np.min(dataToPlot[:,:,0]), np.max(dataToPlot[:,:,0]), 3)
        axs[i].plot(xpts, 0.0*xpts+TFO, color='white', ls='--')

        axs[i].tick_params(axis='both', which='major', labelsize=14)
        axs[i].set_xticks(np.arange(tau0, tau, 0.1))
        axs[i].set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
    
    #axs[0].tick_params( axis='y', which='both', left=False, right=False, labelleft=False )
    axs[1].tick_params( axis='y', which='both', left=False, right=False, labelleft=False )
    axs[2].tick_params( axis='y', which='both', left=False, right=False, labelleft=False )
    axs[0].set_ylabel(r'$T$ (MeV)', fontsize=16)

    cbar = fig.colorbar(psm, ax=axs)
    cbar.set_label(r'$v_{\mathrm{char}}/c$', size=16)
    cbar.ax.tick_params(labelsize=14)

    outfilename = "charvel_density_combined.png"
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

    
        
