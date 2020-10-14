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
from scipy import integrate

# construct Re and deta_dt functions
def Re(Vp): return Vp*d/nu1     #momentery Re based on viscosity of the top layer 
def deta_dt(g,rho,X,omega,rhod,z,Vp): return g*(rho[X-omega]-rhod)/rhod + z*F_drg(Re(eta-Vp))

#defining the time steps for the solution
t_tot=np.linspace(0, 10, 101)      #generate a solution at 101 evenly spaced samples in the interval 0 <= t <= 10

eta0=-F_drg(Re((m*g*rho[0]-rhop)/rhop))

sol=odient(deta_dt, eta0, t_tot, arg=())    # [eta,t]
