'''
Classes, methods and variables for dealing with the waveguide modes of the 
electric and magnetic fields propagating through a coaxial/(annulus) waveguide
'''

# my errors
from errors import NotGreaterThenZero, NotGreaterThenOne, \
    NotGreaterThenOrEqualToOne                
from interactive_plot import *      # my plotting functions

# numpy stuff
from numpy import array, arange, zeros, linspace, any, all
from numpy import pi, ndarray

# plotting tools
import matplotlib.pyplot as plt

# Bessel functions and derivatives
from scipy.special import jn, yn, jvp, yvp
from scipy.optimize import newton



class TMmode:
    '''Contain a single TM wave guide mode, and methods to calculate important 
        quantitites'''
    
    mode = 'TM'
    
    def __init__(self,m,n,c):
        # make sure values are valid
        if m<0:
            raise NotGreaterThenZero, 'm must be non-negative'
        if n<1:
            raise NotGreaterThenOrEqualToOne, 'n must be >= 1'
        if c<=1:
            raise NotGreaterThenOne, 'c must be greater then 1'
        
        # save values to class variables
        self.m = m      # Bessel function order
        self.n = n      # Root number of Bessel function
        self.c = c      # Ratio of outer to inner radius
        self.root = 0   # root of equation
        self.set_root() # sets initial root to something reasonable
        self.drag = None    # information to drag root in plot
                
    def __str__(self):
        return "<%s mode>  m = %s, n = %s, c = %s" % (self.mode, self.m, self.n, self.c)
    
    def root_equation(self,m,c,x):
        'Radial root equation of Phi for TM mode'
        return yn(m,x)*jn(m,c*x)-jn(m,x)*yn(m,c*x)
    
    def chi(self,m,n,c):
        'Guess the root chi_mn for TM mode'
        return pi*n/(c-1.)
    
    def set_root(self, guess=None):
        'Set the initial guess values for the root'
        if guess is not None:
            self.root = guess
        # If no guess is provided use the Marcuvitz formula to calculate approximate root
        else:
            self.root = self.chi(self.m, self.n, self.c)
                    
    def find_root(self):
        'find root using Newton method'
        f = lambda x: self.root_equation(self.m,self.c,x)
        try:
            self.root = newton(f, self.root, maxiter=100)
        except RuntimeError:
            pass
            
    def marcuvitz(self):
        'returns a string label and value for the root form tabulated in Marcuvitz'
        label = '(c-1)*chi'
        root = (self.c-1.)*self.root
        return label, root
    
    def plot_root(self, ax=None, Npoints=500, color='red', size=6):
        'plot calculated root'
        # convenient variables
        m, n, c, root = self.m, self.n, self.c, self.root
        
        # if no axis is given, make a new plot
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111)

        # text label for root point
        label = ['$\chi_{' + str(n) + '}$']
        # plot roots
        f = lambda x: self.root_equation(m, c, x)
        root_line, = ax.plot(root, f(root), marker='o', 
                        markerfacecolor=color, markersize=size)
        # make root draggable
        self.drag = DragRoot(root_line, f, label=label)
        
    def recalculate_root(self):
        ' from the root plot retrieve the estimated root and recalculate it using '
        if self.drag is None: return
        
        new_guess = self.drag.get_xdata()
        self.set_root(guess=new_guess)
        self.find_root()
        
        # set new xdata in the plot
        new_x = self.root
        new_y = self.root_equation(self.m, self.c, new_x)
        self.drag.set_xdata(new_x)
        self.drag.set_ydata(new_y)
        
        # draw on this figure now
        self.drag.draw()
        
    def plot_root_equation(self, ax=None, Npoints=400, 
                           color='blue', width=2, bcolor='red', bwidth=2):
        # if no axis is given, make a new plot
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            
        # give a horizontal line indicating zero
        ax.axhspan(0,0, linewidth=1, linestyle='dashed')
    
        # set up root function plot to have zoom function
        f = lambda x: self.root_equation(self.m, self.c, x)
        rootplot = RootZoomPlot(ax, f, Npoints=Npoints, 
                        x_min=0, x_max=2*self.root,
                        border_width=bwidth, border_color=bcolor,
                        line_color=color, line_width=width)
        # plot the root function (plot last so as to keep pretty y range)
        rootplot.plot()
        
class TEmode(TMmode):
    
    mode = 'TE'
    
    def root_equation(self,m,c,x):
        # Radial root equation of Phi for TE mode
        return yvp(m,x,1)*jvp(m,c*x,1)-jvp(m,x,1)*yvp(m,c*x,1)
    
    def chi(self,m,n,c):
        # Guess the root chi_mn for TE mode
        if m==0:
            return pi*n/(c-1.)
        elif m!=0 and n==1:
            return 2*m/(c+1.)
        else:
            return pi*(n-1.)/(c-1.)
            
    def marcuvitz(self):
        # returns a string label and value for the root form tabulated in Marcuvitz
        if self.n==1 and self.m!=0:
            label = '(c+1)*chi'
            root = (self.c+1.)*self.root
        else:
            label = '(c-1)*chi'
            root = (self.c-1.)*self.root
        return label, root

if __name__ == '__main__':
    
    # set parameters
    Nx = 200 # number of x values to plot
    c = 3.2 # ratio of outer to inner radius
    n = 6
    m = 3
    
    z = TEmode(m, n, c)
    z.set_root()
    z.find_root()
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    z.plot_root(ax=ax)
    z.plot_root_equation(ax=ax)
        
#        # give subplot a title
#        ax.set_title('m=%s'%self.m)
#        
#        # give legend and title to figure
#        plt.figlegend([roots_line], ['roots'], 'upper right')
#        suptitle('Radial functions for %s mode\n c=%s'%(self.mode,c))
#        plt.xlabel('$x$')
    
    # show plots
    plt.show()