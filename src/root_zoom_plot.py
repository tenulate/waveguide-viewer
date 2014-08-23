''' used to plot bessel function roots. Inherits all ZoomPlot
    features, but changes the plotted range '''
    
from interactive_plot import ZoomPlot
from errors import NotNumpyArray

import numpy as np

class RootZoomPlot(ZoomPlot):
        
    def get_ylim(self):
        ''' Used for plotting Bessel functions nicely
            As Bessel functions diverge for x->0, this finds maximum value of Y range to plot.'''
        
        # convenience variable
        y = self.y
                
        # return +1 or -1 for each y value of the plotted line
        ysign = np.sign(y)
        
        # Go through fsign array from beginning, and get index of first sign change
        N = ysign.size # number of elements
        current_sign = False # holds the current sign value
        index = -1
        for i in range(1,N):
            if current_sign == False:
                current_sign = ysign[i]
                continue
            elif current_sign*ysign[i]==-1:
                index = i
                break
            
        # if no sign change is found, index = -1, and we'll just use a standard range
        # likewise if sign change occurs on last element
        if index==-1 or index==(N-1):
            return y.min(),y.max()
        else:   
            max = np.abs(y[index:-1]).max()
            return -1.1*max, 1.1*max
        
    def plot(self, color='blue', linewidth=1):
        ''' plot the function being studied '''
        # set the line properties
        self.line.set_color(color)
        self.line.set_linewidth(linewidth)
        
        # set the axis range/domain
        x_min, x_max = self.get_xlim()
        self.set_xlim(x_min, x_max)
        y_min, y_max = self.get_ylim()
        self.set_ylim(y_min, y_max)
        
        # draw it
        self.canvas.draw()

def get_plot_dimensions(N, Ncols):
    # find out how many rows and columns are necessary to make a subplot with N plots, and Ncols columns
    Nrows = np.floor(N/Ncols)
    # if there is a remainder after dividing, add an extra row
    if N%Ncols!=0:
        Nrows+=1
    # if there are less subplots then columns, just make 1 row, N columns
    if Ncols > N:
        Ncols = N
        Nrows = 1
    
    return int(Nrows), int(Ncols)

if __name__ == '__main__':
    pass
