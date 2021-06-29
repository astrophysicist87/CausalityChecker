import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import cm
#from scipy import interpolate
import os, sys

hbarc = 0.19733     # GeV*fm

# fix command-line arguments
#path = "C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/"
scale = float(sys.argv[1])
minFrameNumber = int(sys.argv[2])
maxFrameNumber = int(sys.argv[3])
inpath = sys.argv[4]
outpath = sys.argv[5]
'''scale=10
minFrameNumber=0
maxFrameNumber=40
inpath="C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/frames"
outpath="C:/Users/Christopher Plumberg/Desktop/Research/UIUC/HydroCausalityChecks/slides"'''


tau = 0.6   #initial tau (fm/c), overwritten by value in file
#dx = 0.1
#dy = 0.1
dxy = float(sys.argv[7])
dx = dxy
dy = dxy
scalex = scale
scaley = scale
nxbins = int(np.round(1.0+2.0*scalex/dx))
nybins = int(np.round(1.0+2.0*scaley/dx))

energyCutOff = True
eDec = float(sys.argv[6])/hbarc  # impose cut off in fm^{-4}

colorsToUseAcausal = ['black','red','purple','blue','green','orange']
colorsToUseParabolic = ['black','red','purple','blue','green','orange']

#===============================================================================
def colorFunction_acausal(entry):
    x = np.max(entry[9:])
    if entry[6] < eDec or entry[7] != 1 or entry[8] != 1:
        return -0.5
    elif x >= 1.0:
        return x
    else:
        return 0.5

#===============================================================================
def colorFunction_parabolic(entry):
    x = np.min(entry[9:])
    if x < 0.0:           # if basic hydro assumptions failed
        return x
    else:                      # else if necessary conditions are violated
        return 1

#===============================================================================
def generate_frame(frameNumber):
    # load data to plot
    global tau
    frameData = np.loadtxt(inpath + '/frame%(frame)04d.dat' % {'frame': frameNumber})
    if frameData.size != 0:
        tau = frameData[0,2]
        frameData = np.unique(frameData, axis=0)
        print('shape(1) =', frameData.shape)
        #if energyCutOff:
        #    frameData = frameData[np.where((frameData[:,6] >= eDec) \
        #                                   & (frameData[:,7] == 1)\
        #                                   & (frameData[:,8] == 1))]
        print('shape(2) =', frameData.shape)
            
    if frameData.size == 0:
        frameData = np.zeros((2,21), dtype=int)
        
    dataToPlot = frameData[:,[3,4]]     # swap x and y to get correct orientation

    fig, ax = plt.subplots( nrows=1, ncols=1 )
    
    '''
    # histogram with each entry weighted by causality conditions
    vals = np.array([colorFunction(entry) for entry in frameData])
    H, xedges, yedges = np.histogram2d(dataToPlot[:,0], dataToPlot[:,1], \
                        bins=(nxbins, nybins), weights=vals, \
                        range=[[-scalex-0.5*dx,scalex+0.5*dx],
                               [-scaley-0.5*dy,scaley+0.5*dy]])
        
    H = H.T
    ax.imshow(H.astype(int), interpolation='nearest', origin='low', \
                  extent=[-scalex-0.5*dx,scalex+0.5*dx,-scaley-0.5*dy,scaley+0.5*dy], \
                  cmap=ListedColormap(colorsToUse), vmin=0, vmax=(len(colorsToUse)-1))
    '''
    
    print('nxbins =', nxbins)
    print('nybins =', nybins)
    print('shape =', frameData.shape)
    print('shape =', np.max(frameData[:,9:], axis=1).shape)
    psm = ax.pcolormesh(np.array(list(map(colorFunction_acausal,frameData))).reshape((nxbins-1,nybins-1)),
                        cmap=cm.get_cmap('viridis'), vmin=0.0, vmax=10.0)
    fig.colorbar(psm, ax=ax)
                  
    plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
            {'color': 'white', 'fontsize': 12}, transform=ax.transAxes,
            horizontalalignment='left', verticalalignment='top')
            
    ax.set_xlabel(r'$x$ (fm)', fontsize=16)
    ax.set_ylabel(r'$y$ (fm)', fontsize=16)
    
    #plt.show()
    outfilename = outpath + '/slide%(frame)04d.png' % {'frame': frameNumber}
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)
    
    greenFraction = len(vals[np.where(vals==4)])/len(vals)
    blueFraction = len(vals[np.where(vals==3)])/len(vals)
    redFraction = len(vals[np.where(vals==1)])/len(vals)
    
    return np.array([tau, greenFraction, blueFraction, redFraction])



#===============================================================================
if __name__ == "__main__":
    # generate frames one by one
    fractionTimeDependence = None
    for loop, frameNumber in enumerate(range(minFrameNumber, maxFrameNumber)):
        print('Generating frame =', frameNumber, ';', \
               maxFrameNumber - frameNumber, 'frames remaining')
        fractions = generate_frame(frameNumber)
        if loop==0:
            fractionTimeDependence = fractions
        else:
            fractionTimeDependence = np.c_[ fractionTimeDependence, fractions ]
        generate_frame_wRegulation(frameNumber)

    fractionTimeDependence = fractionTimeDependence.T
    
    # export to file in case plotting fails
    np.savetxt( outpath + '/cell_fractions_tau_dependence.dat', fractionTimeDependence )
    
    generate_fraction_time_dependence( fractionTimeDependence )

