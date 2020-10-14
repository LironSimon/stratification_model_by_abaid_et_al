# velocity_of_drift_volume formulates the changing velocity of the entrained fluid
# by solving a first order differential equation of velocity as a fuc. of t.
# the velocity of the sphere remains in the solution as a variable 

# inputs:
#     X: the bead’s position as a function of time, initialized at the top of the tank. [?]
#     t: starts from 0 at the top of the tank [s]
#     d: sphere's diameter [?]
#     rhop: sphere's density [?]
#     m(d,rhop): sphere's mass [?]
#     nu1: kinematic viscosity of the top layer
#     Re(Vp): particle's Reynolds number based on nu1
#     F_drg(Re): drag force as a func. of Re, derived from direct measuring of Vterminal in constant density enviroment
#	    z: entrained fluid’s mass
#     g: gravitational acceleration [cm/s2]
#     rho(X): the stratified density profile of the whole tank
#     omega: distance from the sphere [cm]
#     rhod(t): the density of the entrained fluid as a func. of t  

# outpust:
#	    eta(t): entrained fluid’s velocity.

from Imported_data_and_properties import *
from Drift_volume_density import *

# construct Re and velocity function
def Re(Vp): return vp*d/nu1     #momentery Re based on viscosity of the top layer 

def rhod(t): 
  pass

# I need it to somehoe solve:
#     m*d(eta(t))/dt-F_drg(Re(eta(t)-Vp))=z*g*(rho(X-omega)-rhod(t))/rhod(t)
#     eta(0)=-F_drg(Re(m*g*(rho(0)-rhop)/rhop) # In the begining the velocity equals the terminal velocity of the sphere
#     return eta(t)
