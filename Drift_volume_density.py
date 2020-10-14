# Drift_volume_density formulates the changing density of the entrained fluid,
# by solving a first order differential equation of densityy as a fundc of t.
# the velocity of the sphere (Vp) remains in the solution as a variable 
#
# INPUT ARGUMENTS
# ---------------
#   beta(Vp): total diffusivity coefficient
#   rho:  the stratified density profile of the whole tank
#
# OUTPUT ARGUMENTS
# ----------------
#   rhod: the density of the entrained fluid as a func. of t
#   t: time 
#
# SYNTAX
# ----------------
# [rhod,t]= odient(drhod_dt, rhod0, t_tot, arg=())
# ??


from Imported_data_and_properties import *
from scipy import integrate


# implementing a function that returns the right hand side of the density equation
def drhod_dt(beta(Vp), rho, rhod): return beta(Vp)*(rho-rhod)     #Change of density acc to Newtonian cooling equation

#defining the time steps for the solution
t_tot=np.linspace(0, 10, 101)      #generate a solution at 101 evenly spaced samples in the interval 0 <= t <= 10

rhod0=rho(0)

sol=odient(drhod_dt, rhod0, t_tot, arg=())    # [rhod,t]

