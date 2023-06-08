import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import sys
from matplotlib import cm
from mpl_toolkits.axes_grid1 import make_axes_locatable


def init():
    data = np.loadtxt(sys.argv[i+1], usecols=(1,2,5))
    nxbins = np.rint(np.sqrt(len(data[:,0])))
    nybins = np.rint(np.sqrt(len(data[:,1])))
    image = np.zeros((nxbins, nybins))
    im = plt.imshow(image)
    plt.axis('off')
    return im,


def animate(i):
    global maximum
    print('Rendering Scene ' + str(i+1) + ' of ' + str(len(sys.argv[1:])), flush=True)

    # load frame
    data = np.loadtxt(sys.argv[i+1], usecols=(1,2,5))
    
    # set grid parameters
    scalex = np.amax(data[:,0])
    scaley = np.amax(data[:,1])
    nxbins = np.rint(np.sqrt(len(data[:,0])))
    nybins = np.rint(np.sqrt(len(data[:,1])))
    dx = 2.0*scalex / (nxbins-1.0)
    dy = 2.0*scaley / (nybins-1.0)
    
    # light cone orientations
    values = np.sqrt(data[:,2])
    
    # histogram
    H, xedges, yedges = np.histogram2d(data[:,0], data[:,1], \
                    bins = (nxbins, nybins), weights=values, \
                    range = [[-scalex-0.5*dx, scalex+0.5*dx],
                             [-scaley-0.5*dy, scaley+0.5*dy]])
               
    # re-orient and plot
    H = H.T
    im = plt.imshow(H, interpolation = 'nearest', origin = 'low', \
                  extent = [ -scalex-0.5*dx,scalex+0.5*dx,
                             -scaley-0.5*dy,scaley+0.5*dy ], \
                  cmap = 'bwr', vmin = 0.8, vmax = 1.2)

    #ax = plt.gca()
    #im = ax.imshow(image, cmap=chosen_colormap)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="5%", pad=0.05)
    plt.colorbar(im, cax=cax)
    
    plt.axis('off')
    #plt.imsave(fname='old_animation_frames/frame' + str(i) + '.png', \
    #           arr=image, cmap=chosen_colormap, format='png')
    return im,



def main():

    # Plot 
    fig = plt.figure(figsize=(1,1), dpi=500)
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
        
    # Do Volume Rendering at Different Viewing Angles
    ani = animation.FuncAnimation(fig, animate, np.arange(len(sys.argv[1:])), \
                                  init_func=init, blit=True)

    f = "light_cone_movie.mp4"
    FFwriter = animation.FFMpegWriter(fps=40, extra_args=['-vcodec', 'libx264'])
    ani.save(f, writer=FFwriter)
    #f = "animation.gif" 
    #ani.save(f, writer='imagemagick', fps=10)

    return 0

  
if __name__== "__main__":
  main()

