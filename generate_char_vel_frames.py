import numpy as np
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
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
    if entry[6] < eDec or entry[7] != 1 or entry[8] != 1:
        return 0.0
    else:
        return np.max(entry[9:])

#===============================================================================
def colorFunction_acausal2(entry):
    x = np.max(entry[9:])
    if entry[6] < eDec or entry[7] != 1 or entry[8] != 1 or x < 1.0:
        return 1.0
    else:
        return x

#===============================================================================
def colorFunction_causal(entry):
    x = np.max(entry[9:])
    if entry[6] < eDec or entry[7] != 1 or entry[8] != 1 or x >= 1.0:
        return 0.0
    else:
        return 0.999999

#===============================================================================
def colorFunction_parabolic(entry):
    #x = np.min(entry[9:])
#    if x < 0.0:           # if basic hydro assumptions failed
#        return x
#    else:                      # else if necessary conditions are violated
#        return 1
    if entry[6] < eDec or entry[7] != 1 or entry[8] != 1:
        return 1.0
    else:
        return np.min(entry[9:])

#===============================================================================
def generate_frame(frameNumber):
    # load data to plot
    global tau
    frameData = np.loadtxt(inpath + '/frame_w_char_vel%(frame)04d.dat' % {'frame': frameNumber})
    if frameData.size != 0:
        tau = frameData[0,2]
        #frameData = np.unique(frameData, axis=0)
        print('shape(1) =', frameData.shape)
        #if energyCutOff:
        #    frameData = frameData[np.where((frameData[:,6] >= eDec) \
        #                                   & (frameData[:,7] == 1)\
        #                                   & (frameData[:,8] == 1))]
        print('shape(2) =', frameData.shape)
            
    if frameData.size == 0:
        frameData = np.zeros((2,21), dtype=int)
        
    dataToPlot = frameData[:,[3,4]]     # swap x and y to get correct orientation

    fig, axs = plt.subplots( nrows=1, ncols=2, figsize=(15,6) )
    
    vmin, vmax = 0.0, 1.25
    black = np.array([0/256, 0/256, 0/256, 1])
    blue = np.array([0/256, 0/256, 256/256, 1])
    red = np.array([256/256, 0/256, 0/256, 1])
    green = np.array([0/256, 128/256, 0/256, 1])
    orange = np.array([255/256, 165/256, 0])
    purple = np.array([154/256, 18/256, 179/256, 1])
    yellow = np.array([233/256, 212/256, 96/256, 1])
    transparent = np.array([0/256, 0/256, 0/256, 0])
    acausal_cmap = LinearSegmentedColormap.from_list('acausal_cmap',\
             [(0.0, black), (1e-6, blue), ((1.0-vmin)/(vmax-vmin), blue),
              ((1.00001-vmin)/(vmax-vmin), yellow), (1.0, red)])
    causal_cmap = LinearSegmentedColormap.from_list('causal_cmap', [(0.0, black), (1.0, blue)])
    parabolic_cmap = LinearSegmentedColormap.from_list('parabolic_cmap', \
                     [(0.0, orange), (0.49999, orange), (0.5, blue), (0.99999, blue), (1.0, black)])
    
    
    print('nxbins =', nxbins)
    print('nybins =', nybins)
    print('shape =', frameData.shape)
    print('shape =', np.max(frameData[:,9:], axis=1).shape)
    
    
    
    # comment this block out if not worrying about colorbar
    '''
    acausal_vmin, acausal_vmax = 1.0, 1.25
    acausal_cmap = LinearSegmentedColormap.from_list('acausal_cmap', \
                   [(0.0, transparent), (9.99e-7, transparent), (1e-6, yellow), (1.0, red)])
    causalDataToPlot = np.array(list(map(colorFunction_causal, frameData)))
    squareLength = int(np.round(np.sqrt(len(causalDataToPlot))))
    # this step accommodates different grid definitions in VISHNU vs. MUSIC
    xpts   = np.linspace(-scalex, scalex, squareLength, endpoint=bool(squareLength%2==1))
    ypts   = np.linspace(-scaley, scaley, squareLength, endpoint=bool(squareLength%2==1))
    causalDataToPlot = causalDataToPlot.reshape((squareLength, squareLength))
    #psm = axs[0].pcolormesh(xpts, ypts, np.sqrt(causalDataToPlot), cmap=causal_cmap,
    #                        vmin=vmin, vmax=vmax, shading='auto')
    dataToPlot = np.array(list(map(colorFunction_acausal2, frameData)))
    squareLength = int(np.round(np.sqrt(len(dataToPlot))))
    dataToPlot = dataToPlot.reshape((squareLength, squareLength))
    psm = axs[0].pcolormesh(xpts, ypts, np.sqrt(dataToPlot), cmap=acausal_cmap,
                            vmin=acausal_vmin, vmax=acausal_vmax, shading='auto')
    '''
    
    # the real plotting starts here
    dataToPlot = np.array(list(map(colorFunction_acausal, frameData)))
    squareLength = int(np.round(np.sqrt(len(dataToPlot))))
    # this step accommodates different grid definitions in VISHNU vs. MUSIC
    xpts   = np.linspace(-scalex, scalex, squareLength, endpoint=bool(squareLength%2==1))
    ypts   = np.linspace(-scaley, scaley, squareLength, endpoint=bool(squareLength%2==1))
    dataToPlot = dataToPlot.reshape((squareLength, squareLength))
    # use this dummy block to plot desired colormap range, then plot on top of it to get actual figure
    # BEGIN DUMMY STATEMENTS HERE
    acausal_vmin, acausal_vmax = 1.0, 1.25
    acausal_cmap = LinearSegmentedColormap.from_list('acausal_cmap', [(0.0, yellow), (1.0, red)])
    psm = axs[0].pcolormesh(xpts, ypts, 0.0*dataToPlot+0.5*(acausal_vmin+acausal_vmax), cmap=acausal_cmap,
                            vmin=acausal_vmin, vmax=acausal_vmax, shading='auto')
    fig.colorbar(psm, ax=axs[0])
    # END DUMMY STATEMENTS HERE
    # redefine acausal_cmap
    acausal_cmap = LinearSegmentedColormap.from_list('acausal_cmap',\
             [(0.0, black), (1e-6, blue), ((1.0-vmin)/(vmax-vmin), blue),
              ((1.00001-vmin)/(vmax-vmin), yellow), (1.0, red)])
    psm = axs[0].pcolormesh(xpts, ypts, np.sqrt(dataToPlot), cmap=acausal_cmap, vmin=vmin, vmax=vmax, shading='auto')
                  
    plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
            {'color': 'white', 'fontsize': 12}, transform=axs[0].transAxes,
            horizontalalignment='left', verticalalignment='top')
            
    axs[0].set_xlabel(r'$x$ (fm)', fontsize=16)
    axs[0].set_ylabel(r'$y$ (fm)', fontsize=16)
    
    dataToPlot = np.array(list(map(colorFunction_parabolic, frameData)))
    squareLength = int(np.round(np.sqrt(len(dataToPlot))))
    # this step accommodates different grid definitions in VISHNU vs. MUSIC
    xpts   = np.linspace(-scalex, scalex, squareLength, endpoint=bool(squareLength%2==1))
    ypts   = np.linspace(-scaley, scaley, squareLength, endpoint=bool(squareLength%2==1))
    dataToPlot = dataToPlot.reshape((squareLength, squareLength))
    psm = axs[1].pcolormesh(xpts, ypts, dataToPlot, cmap=parabolic_cmap, vmin=-1.0, vmax=1.0, shading='auto')
    #fig.colorbar(psm, ax=axs[1])
                  
    plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
            {'color': 'white', 'fontsize': 12}, transform=axs[0].transAxes,
            horizontalalignment='left', verticalalignment='top')
            
    plt.text(0.5, 0.1, r'Sub-luminality', \
            {'color': 'white', 'fontsize': 12}, transform=axs[0].transAxes,
            horizontalalignment='center', verticalalignment='top')
            
    plt.text(0.5, 0.1, r'Hyperbolicity', \
            {'color': 'white', 'fontsize': 12}, transform=axs[1].transAxes,
            horizontalalignment='center', verticalalignment='top')
            
    axs[1].set_xlabel(r'$x$ (fm)', fontsize=16)
    axs[1].set_ylabel(r'$y$ (fm)', fontsize=16)
    
    plt.show()
    #outfilename = outpath + '/slide_w_char_vel%(frame)04d.png' % {'frame': frameNumber}
    #print('Saving to', outfilename)
    #fig.savefig(outfilename, bbox_inches='tight')
    #plt.close(fig)
    #
    #greenFraction = len(vals[np.where(vals==4)])/len(vals)
    #blueFraction = len(vals[np.where(vals==3)])/len(vals)
    #redFraction = len(vals[np.where(vals==1)])/len(vals)
    #
    #return np.array([tau, greenFraction, blueFraction, redFraction])
    return None


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

    #fractionTimeDependence = fractionTimeDependence.T
    
    # export to file in case plotting fails
    #np.savetxt( outpath + '/cell_fractions_tau_dependence.dat', fractionTimeDependence )
    
    #generate_fraction_time_dependence( fractionTimeDependence )

