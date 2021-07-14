import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
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
#eDec = 0.3/hbarc  # impose cut off in fm^{-4}
eDec = float(sys.argv[6])/hbarc

colorsToUse = ['black','red','purple','blue','green','orange']

#===============================================================================
def colorFunction(entry):
    if entry[-2]==0:           # if basic hydro assumptions failed
        return 5
    elif entry[-1]==0:         # else if diagonalization of pimunu failed
        return 4
    elif entry[1]==11111111:   # else if sufficient conditions are satisfied
        return 3
    elif entry[0]==111111:     # else if necessary conditions are satisfied
        return 2
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
        if energyCutOff:
            frameData = frameData[np.where(frameData[:,6] >= eDec)]
            
    if frameData.size == 0:
        frameData = np.array([[0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0]])
        
    dataToPlot = frameData[:,[3,4]]     # swap x and y to get correct orientation

    fig, ax = plt.subplots( nrows=1, ncols=1 )
    
    # histogram with each entry weighted by causality conditions
    vals = np.array([colorFunction(entry) for entry in frameData])
    H, xedges, yedges = np.histogram2d(dataToPlot[:,0], dataToPlot[:,1], \
                        bins=(nxbins, nybins), weights=vals, \
                        range=[[-scalex-0.5*dx,scalex+0.5*dx],
                               [-scaley-0.5*dy,scaley+0.5*dy]])
        
    #print 'Total:', vals.shape
    #print 'Good:', vals[np.where(vals==3)].shape
    #print 'Iffy:', vals[np.where(vals==2)].shape
    #print 'Bad:', vals[np.where(vals==1)].shape
    
    H = H.T
    ax.imshow(H.astype(int), interpolation='nearest', origin='low', \
                  extent=[-scalex-0.5*dx,scalex+0.5*dx,-scaley-0.5*dy,scaley+0.5*dy], \
                  cmap=ListedColormap(colorsToUse), vmin=0, vmax=(len(colorsToUse)-1))
                  
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
    
    orangeFraction = len(vals[np.where(vals==5)])/len(vals)
    greenFraction = len(vals[np.where(vals==4)])/len(vals)
    blueFraction = len(vals[np.where(vals==3)])/len(vals)
    purpleFraction = len(vals[np.where(vals==2)])/len(vals)
    redFraction = len(vals[np.where(vals==1)])/len(vals)
    
    return np.array([tau, orangeFraction, greenFraction, blueFraction, \
                     purpleFraction, redFraction])

#===============================================================================
#def identify_violations(piViolations, BulkPiViolations):
#    # convert pi to make it easier to process
#    piViolation[:,1] = int(np.round(1000.0*piViolation[:,1]))
    
#===============================================================================
def get_value(point, x, y, z):
    return z[ np.where( np.isclose(x,point[0]) & np.isclose(y,point[1]) ) ]

#===============================================================================
def generate_frame_wRegulation(frameNumber):
    # load data to plot
    global tau
    frameData = np.loadtxt(inpath + '/frame%(frame)04d.dat' % {'frame': frameNumber})
    if frameData.size != 0:
        tau = frameData[0,2]
        frameData = np.unique(frameData, axis=0)
        if energyCutOff:
            frameData = frameData[np.where(frameData[:,6] >= eDec)]
            
    if frameData.size == 0:
        frameData = np.array([[0,0,0,-1000.0,-1000.0,0,0,0,0],\
                              [0,0,0,-1000.0,1000.0,0,0,0,0],\
                              [0,0,0,1000.0,-1000.0,0,0,0,0],\
                              [0,0,0,1000.0,1000.0,0,0,0,0]])
        
    dataToPlot = frameData[:,[3,4]]     # swap x and y to get correct orientation

    fig, axs = plt.subplots( nrows=1, ncols=2, figsize=(10,5) )
    
    # histogram with each entry weighted by causality conditions
    vals = np.array([colorFunction(entry) for entry in frameData])
    H, xedges, yedges = np.histogram2d(dataToPlot[:,0], dataToPlot[:,1], \
                        bins=(nxbins, nybins), weights=vals, \
                        range=[[-scalex-0.5*dx,scalex+0.5*dx],
                               [-scaley-0.5*dy,scaley+0.5*dy]])
                
    H = H.T
    axs[0].imshow(H.astype(int), interpolation='nearest', origin='low', \
                  extent=[-scalex-0.5*dx,scalex+0.5*dx,-scaley-0.5*dy,scaley+0.5*dy], \
                  cmap=ListedColormap(colorsToUse), vmin=0, vmax=(len(colorsToUse)-1))
    
    # load piViolation and BulkPiViolation files to track where regulator is needed
    # (assumed to be one directory level up)
    # NOTICE ALSO THAT THE FINAL COLUMN CONTAINS E DENSITY IN GEV/FM^3
    if os.path.isfile(inpath + '/../piViolation.dat'):
        piViolations = np.loadtxt(inpath + '/../piViolation.dat')
    else:
        piViolations = np.array([])
        
    if os.path.isfile(inpath + '/../BulkpiViolation.dat'):
        BulkPiViolations = np.loadtxt(inpath + '/../BulkpiViolation.dat')
    else:
        BulkPiViolations = np.array([])
    
    if piViolations.size > 0:
        piViolations = piViolations[np.where( np.isclose(piViolations[:,0], tau) \
                                & (piViolations[:,1]>0) & (piViolations[:,1]<1)
                                & (piViolations[:,-1]>=eDec*hbarc) )][:,[-3,-2]]
    if piViolations.size == 0:
        piViolations = np.array([[-1000.0,-1000.0],[-1000.0,1000.0],
                                 [1000.0,-1000.0], [1000.0,1000.0]])
    if BulkPiViolations.size > 0:
        BulkPiViolations = BulkPiViolations[np.where( np.isclose(BulkPiViolations[:,0], tau)
                                                      & (BulkPiViolations[:,-1]>=eDec*hbarc) )][:,[-3,-2]]
    if BulkPiViolations.size == 0:
        BulkPiViolations = np.array([[-1000.0,-1000.0],[-1000.0,1000.0],\
                                     [1000.0,-1000.0], [1000.0,1000.0]])
                                     
    # plot only cells above relevant eDec threshold
    dataToPlot = np.unique( np.vstack( (piViolations, BulkPiViolations) ), axis=0 )

    # to avoid throwing exceptions...
    if dataToPlot.size==0:
        dataToPlot = np.array([[-1000.0,-1000.0],[-1000.0,1000.0],\
                               [1000.0,-1000.0], [1000.0,1000.0]])

    print(dataToPlot.shape)
    H, xedges, yedges = np.histogram2d(dataToPlot[:,0], dataToPlot[:,1], \
                                    bins=(nxbins, nybins), \
                                    range=[[-scalex-0.5*dx,scalex+0.5*dx],
                                           [-scaley-0.5*dy,scaley+0.5*dy]])
        
    H = H.T
    axs[1].imshow(H.astype(int), interpolation='nearest', origin='low', \
                  extent=[-scalex-0.5*dx,scalex+0.5*dx,-scaley-0.5*dy,scaley+0.5*dy], \
                  cmap=ListedColormap(['black','white']), vmin=0, vmax=1)
                  
    plt.text(0.075, 0.925, r'$\tau = %(t)5.2f$ fm$/c$'%{'t': tau}, \
            {'color': 'white', 'fontsize': 12}, transform=axs[0].transAxes,
            horizontalalignment='left', verticalalignment='top')
            
    for ax in axs.ravel():
        ax.set_xlabel(r'$x$ (fm)', fontsize=16)
        ax.set_ylabel(r'$y$ (fm)', fontsize=16)
    
    #plt.show()
    outfilename = outpath + '/slide_wReg%(frame)04d.png' % {'frame': frameNumber}
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)
    
    
#===============================================================================
def generate_fraction_time_dependence( fractionTimeDependence ):
    fig, axs = plt.subplots( nrows=1, ncols=1, figsize=(10,10) )

    axs.plot( fractionTimeDependence[:,0], fractionTimeDependence[:,1], color='orange', lw=2 )
    axs.plot( fractionTimeDependence[:,0], fractionTimeDependence[:,2], color='green', lw=2 )
    axs.plot( fractionTimeDependence[:,0], fractionTimeDependence[:,3], color='blue', lw=2 )
    axs.plot( fractionTimeDependence[:,0], fractionTimeDependence[:,4], color='purple', lw=2 )
    axs.plot( fractionTimeDependence[:,0], fractionTimeDependence[:,5], color='red', lw=2 )
            
    axs.set_xlabel(r'$\tau$ (fm/$c$)', fontsize=16)
    axs.set_ylabel(r'Fraction', fontsize=16)
    axs.legend( loc='best' )

    #plt.show()
    outfilename = outpath + '/cell_fractions_tau_dependence.png'
    print('Saving to', outfilename)
    fig.savefig(outfilename, bbox_inches='tight')
    plt.close(fig)

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
        #generate_frame_wRegulation(frameNumber)

    fractionTimeDependence = fractionTimeDependence.T
    
    # export to file in case plotting fails
    np.savetxt( outpath + '/cell_fractions_tau_dependence.dat', fractionTimeDependence )
    
    generate_fraction_time_dependence( fractionTimeDependence )
