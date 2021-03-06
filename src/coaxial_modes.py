'''
Classes, methods and variables for dealing with the waveguide modes of the 
electric and magnetic fields propagating through a coaxial/(annulus) waveguide
'''

# my errors
from waveguide_viewer_errors import NotGreaterThenZero, NotGreaterThenOne, NotGreaterThenOrEqualToOne             
# my plotting functions
from interactive_plot import DragRoot, ZoomPlot
from root_zoom_plot import RootZoomPlot

# numpy stuff
from numpy import array, arange, zeros, linspace, any, all
from numpy import pi, ndarray, sin, cos, meshgrid, sqrt

# plotting tools
import matplotlib.pyplot as plt

# Bessel functions and derivatives
from scipy.special import jn, yn, jvp, yvp
from scipy.optimize import newton

# Wavelength of light (m)
LAMBDA = 1e-6

C = 2.99792458e8            # speed of light (m s-1)
K = 2*pi/LAMBDA             # wavenumber k (m-1)
OMEGA = C*K                 # Waveguide Frequency (s-1)
MU = 1.25663706e-6          # the magnetic constant (m kg s-2 A-2)
EPSILON = 8.85418782e-12    # permittivity of free space (m-3 kg-1 s4 A2)


class TMmode:
    '''Contain a single TM wave guide mode, and methods to calculate important 
       quantities'''
    
    def __init__(self,m,n,c):
        # make sure values are valid
        if m<0:
            raise NotGreaterThenZero, 'm must be non-negative'
        if n<1:
            raise NotGreaterThenOrEqualToOne, 'n must be >= 1'
        if c<=1:
            raise NotGreaterThenOne, 'c must be greater then 1'
        
        # save values to class variables
        self.mode = 'TM'
        self.m = m      # Bessel function order
        self.n = n      # Root number of Bessel function
        self.c = c      # Ratio of outer to inner radius 
        self.root = 0   # root of equation
        self.kz = 0     # z component of the wavenumber k
        self.set_root() # sets initial root to something reasonable
        self.drag = None    # information to drag root in plot
        
        self.E_field = None # The quiver / arrow plot of the Electric field
        self.H_field = None # "                            " Magnetic field
                        
    def __str__(self):
        return "<%s mode>  m = %s, n = %s, c = %s" % (self.mode, self.m, self.n, self.c)
    
    def root_equation(self,m,c,x):
        'Radial root equation of Phi for TM mode'
        return yn(m,x)*jn(m,c*x)-jn(m,x)*yn(m,c*x)
    
    def z(self,x):
        'Z(x) equation that keeps showing up in waveguide modes'
        m, n, chi = self.m, self.n, self.root
        return yn(m,chi)*jn(m,x)-jn(m,chi)*yn(m,x)
    
    def z_dash(self,x):
        ''' Z'(x) equation for waveguide mode '''
        m, n, chi = self.m, self.n, self.root
        # jvp(m,x,r) is the rth derivative of the bessel function of order m evaluated at x
        return yn(m,chi)*jvp(m,x,1)-jn(m,chi)*yvp(m,x,1)
    
    def update_kz(self):
        ''' wave number (2 pi lambda)^-1 in z direction '''
        # In plots we will take inner radius (b) to be 1
        # kz^2 = k^2-(chi/b)^2 = k^2-chi^2
        chi = self.root
        self.kz = sqrt(K**2 - chi**2)
    
    def E_rho(self, rho, phi):
        ''' radial component of electric field evaluated at (rho,phi) - polar coordinates '''
        m, chi, kz = self.m, self.root, self.kz
        return -1*kz*chi*self.z_dash(chi*rho)*cos(m*phi)
    
    def E_phi(self, rho, phi):
        ''' polar component of electric field evaluated at (rho,phi) - polar coordinates '''
        m, chi, kz = self.m, self.root, self.kz
        return kz*m/rho*self.z(chi*rho)*sin(m*phi)
    
    def E_z(self, rho, phi):
        ''' Z component of electric field '''
        m, chi, kz = self.m, self.root, self.kz
        return chi**2*self.z(chi*rho)*cos(m*phi)    
    
    def H_rho(self, rho, phi):
        ''' radial component of magnetic field '''
        m, chi = self.m, self.root
        return -1*OMEGA*EPSILON*m/rho*self.z(chi*rho)*sin(m*phi)
    
    def H_phi(self, rho, phi):
        ''' polar component of magnetic field '''
        m, chi = self.m, self.root
        return -1*OMEGA*EPSILON*chi*self.z_dash(chi*rho)*cos(m*phi)
    
    def H_z(self, rho, phi):
        ''' z component of magnetic field '''
        # need to return a numpy array of zeros, not just a single int 0 incase
        # rho and phi are meshgrid arrays
        
        return zeros(rho.shape)
        
    def guess_root(self,m,n,c):
        'Guess the root chi_mn for TM mode'
        return pi*n/(c-1.)
    
    def set_root(self, guess=None):
        'Set the initial guess value for the root'
        if guess is not None:
            self.root = guess
        # If no guess is provided use the Marcuvitz formula to calculate approximate root
        else:
            self.root = self.guess_root(self.m, self.n, self.c)
            
        # update the kz now that we have a new root
        self.update_kz()
                    
    def find_root(self):
        'find root using Newton method'
        f = lambda x: self.root_equation(self.m,self.c,x)
        try:
            self.root = newton(f, self.root, maxiter=100)
        except RuntimeError:
            pass
        
        # update the kz
        self.update_kz()
            
    def marcuvitz(self):
        'returns a string label and value for the root form tabulated in Marcuvitz'
        label = '(c-1)*chi'
        root = (self.c-1.)*self.root
        return label, root
    
    def plot_root(self, ax=None, color='red', size=8):
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
        # draw the root
        self.drag.draw()
        
    def recalculate_root(self):
        ''' from the root plot retrieve the estimated root and recalculate it using 
            Newton-Raphson method of finding zeros '''
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
        
    def plot_root_equation(self, ax=None, Npoints=400):
        ''' Plot the radial root equation '''
        
        # if no axis is given, make a new plot
        if ax is None:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            
        # give a horizontal line indicating zero
        ax.axhline(0,0, linewidth=1, linestyle='dashed', color='black')
    
        # set up root function plot to have zoom function
        f = lambda x: self.root_equation(self.m, self.c, x)
        self.rootplot = RootZoomPlot(f, axis=ax, Npoints=Npoints, 
                        x_min=0, x_max=2*self.root)
        # set the title for the new plot
        ax.set_title('Radial root equation for %s$_{%d,%d}$ mode (c = %.2f)'
                     %(self.mode, self.m, self.n, self.c))
        # plot the root function (plot last so as to keep pretty y range)
        self.rootplot.plot()
    
    def get_field_plot_title(self):
        ''' the title given to the vector field plot '''
        return '%s %i,%i mode'%(self.mode, self.m, self.n) 
   
    def plot_field(self, ax, 
                   E_color='blue', H_color='orange', 
                   axis_bgcolor='white', fig_facecolor='gray',
                   n_rho=15, n_phi=60):
        ''' plots H field into ax (matplotlib.Axes class) 
            n_rho = number of different rho(radial) points to use
            n_phi = number of different phi(polar angle) points to use'''
        
        # if no axis is given, make a new plot
        if ax is None:
            fig = plt.figure()
        else:
            ''' if a figure is already given need to clear it and make sure it's polar projection '''
            fig = ax.figure
            fig.clear()
        
        fig.set_facecolor(fig_facecolor)    
        ax = fig.add_subplot(111, projection='polar', 
                             axis_bgcolor=axis_bgcolor)
        ax.set_title(self.get_field_plot_title())
                        
        b = 1           # inner radius   
        a = b*self.c    # outer radius
        
        rho = linspace(b,a,n_rho)
        phi = linspace(0,2*pi,n_phi)
        # meshgrid form of rho and phi
        RHO, PHI = meshgrid(rho, phi)
        
        # plot the centre circle of the annulus
        circle_N = 100
        circle_phi = linspace(0,2*pi,circle_N)
        circle_inner_radius = circle_N*[b]
        circle_outer_radius = circle_N*[a]
        circle_centre = circle_N*[0]
        ax.fill_between(circle_phi, circle_centre, circle_inner_radius,
                        facecolor=fig_facecolor, alpha=1.0, linewidth=0)
        ax.plot(circle_phi, circle_inner_radius, 
                circle_phi, circle_outer_radius,
                linewidth=2, color='black')
        
        # Vector field in rho, phi basis
        H_rho = self.H_rho
        H_phi = self.H_phi
        E_rho = self.E_rho
        E_phi = self.E_phi

        # vector field in Cartesian x,y basis, calculated from rho, phi basis
        E_x = E_rho(RHO,PHI)*cos(PHI)-E_phi(RHO,PHI)*sin(PHI)
        E_y = E_rho(RHO,PHI)*sin(PHI)+E_phi(RHO,PHI)*cos(PHI)
        H_x = H_rho(RHO,PHI)*cos(PHI)-H_phi(RHO,PHI)*sin(PHI)
        H_y = H_rho(RHO,PHI)*sin(PHI)+H_phi(RHO,PHI)*cos(PHI)
        # make the field plots
        self.E_field = ax.quiver(PHI,RHO,E_x,E_y, color=E_color)
        self.H_field = ax.quiver(PHI,RHO,H_x,H_y, color=H_color)
        

        # get rid of the radial and polar ticks
        ax.set_thetagrids([]), ax.set_rticks([])

        
class TEmode(TMmode, object):
    '''Contain a single TE wave guide mode, and methods to calculate important 
        quantities'''
    
    def __init__(self,m,n,c):
        # Initialize the super class
        super(TEmode, self).__init__(m,n,c)
        self.mode = 'TE'
    
    def root_equation(self,m,c,x):
        '''Radial root equation of Phi for TE mode'''
        return yvp(m,x,1)*jvp(m,c*x,1)-jvp(m,x,1)*yvp(m,c*x,1)
    
    def guess_root(self,m,n,c):
        '''Guess the root chi_mn for TE mode'''
        if m==0:
            return pi*n/(c-1.)
        elif m!=0 and n==1:
            return 2*m/(c+1.)
        else:
            return pi*(n-1.)/(c-1.)
            
    def marcuvitz(self):
        '''returns a string label and value for the root form tabulated in Marcuvitz'''
        if self.n==1 and self.m!=0:
            label = '(c+1)*chi'
            root = (self.c+1.)*self.root
        else:
            label = '(c-1)*chi'
            root = (self.c-1.)*self.root
        return label, root
    
    def z(self,x):
        'Z(x) equation that keeps showing up in waveguide modes'
        m, n, chi = self.m, self.n, self.root
        return yvp(m,chi,1)*jn(m,x)-jvp(m,chi,1)*yn(m,x)
    
    def z_dash(self,x):
        ''' Z'(x) equation for waveguide mode '''
        m, n, chi = self.m, self.n, self.root
        # jvp(m,x,r) is the rth derivative of the bessel function of order m evaluated at x
        return yvp(m,chi,1)*jvp(m,x,1)-jvp(m,chi,1)*yvp(m,x,1)
    
    def E_rho(self, rho, phi):
        ''' radial component of electric field evaluated at (rho,phi) - polar coordinates '''
        m, chi, kz = self.m, self.root, self.kz
        return OMEGA*MU*m/rho*self.z(chi*rho)*sin(m*phi)
    
    def E_phi(self, rho, phi):
        ''' polar component of electric field evaluated at (rho,phi) - polar coordinates '''
        m, chi, kz = self.m, self.root, self.kz
        return OMEGA*MU*chi*self.z_dash(chi*rho)*cos(m*phi)
    
    def E_z(self, rho, phi):
        ''' z component of Electric field '''
        return zeros(rho.shape)
    
    def H_rho(self, rho, phi):
        ''' radial component of magnetic field '''
        m, chi, kz = self.m, self.root, self.kz
        return -1*kz*chi*self.z_dash(chi*rho)*cos(m*phi)
    
    def H_phi(self, rho, phi):
        ''' polar component of magnetic field '''
        m, chi, kz = self.m, self.root, self.kz
        return kz*m/rho*self.z(chi*rho)*sin(m*phi)
    
    def H_z(self, rho, phi):
        ''' z component of magnetic field '''
        m, chi, kz = self.m, self.root, self.kz
        return chi**2*self.z(chi*rho)*cos(m*phi)
    
class TEMmode(TMmode, object):
    ''' contain a single TEM mode information and methods to calculate important
        quantities '''
    
    def __init__(self,c):
        self.c = c
        self.mode = 'TEM'
        self.field_plot_title = '%s mode'%self.mode
    
    def __str__(self): 
        return '%s mode, c=%s'%(self.mode, self.c)
    
    def get_field_plot_title(self):
        ''' title to be used when plotting the vector fields '''
        return '%s mode' % self.mode
    def E_rho(self, rho, phi):
        ''' radial component of electric field '''
        return -1*K/rho
    
    def E_phi(self, rho, phi):
        ''' polar component of Electric field '''
        return 0
    
    def E_z(self, rho, phi):
        ''' z component of electric field '''
        return 0
    
    def H_rho(self, rho, phi):
        ''' radial component of magnetic field '''
        return 0
    
    def H_phi(self, rho, phi):
        ''' polar component of magnetic field '''
        return -OMEGA*EPSILON/rho
    
    def H_z(self, rho, phi):
        ''' z component of magnetic field '''
        return 0
    
    
if __name__ == '__main__':
    
    # set parameters
    Nx = 200 # number of x values to plot
    c = 3.2 # ratio of outer to inner radius
    n = 1
    m = 0
    
    z = TEmode(m, n, c)
    z.set_root()
    z.find_root()
    
#    z = TEMmode(c)
    
    fig = plt.figure()
    ax = fig.add_subplot(111)

    z.plot_field(ax, n_phi=100, n_rho=100)



    plt.show()