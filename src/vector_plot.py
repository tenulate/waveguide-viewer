''' Plots a vector field inside an annulus with both vector points and 
    directions given in polar coordinates '''

# initial imports
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

# ratio of outter radius to inner radius
ratio = 3.
# radius        
inner_radius = 2        
outter_radius = inner_radius*ratio

# The meshgrid matrix used to plot arrows over RHO PHI
RHO, PHI = np.meshgrid(np.linspace(inner_radius,outter_radius,20), 
                       np.linspace(0,2*np.pi,30))

# Vector field in rho, phi basis
v_rho = lambda rho,phi: rho*np.cos(10*np.pi)
v_phi = lambda rho,phi: np.sin(phi)

# vector field in cartesian x,y basis, calculated from rho, phi basis
v_x = lambda rho,phi: v_rho(rho,phi)*np.cos(phi)-v_phi(rho,phi)*np.sin(phi)
v_y = lambda rho,phi: v_rho(rho,phi)*np.sin(phi)+v_phi(rho,phi)*np.cos(phi)

ax.quiver(PHI,RHO,v_x(RHO,PHI),v_y(RHO,PHI))

plt.show()