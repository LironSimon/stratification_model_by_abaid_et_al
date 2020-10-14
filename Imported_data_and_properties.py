# Imported_data_and_eq uploads all relevet data entries from prior matlab files, to define the variables needed for later calculations
import numpy as np
import pandas as pd
import glob

#Arranging trajectory file folders to excerpt data from:
folders_directory_list = sorted(glob.glob('Data/*'))[1:]      #lst of all Traj file folders, without the index file

folders_dict={}
for folder in folders_directory_list:
    fldr_name=folder.rsplit("\\")[-1]
    folders_dict[fldr_name] = glob.glob(folder + '/*csv')


# Testing my readings on a single file
data=pd.read_csv(folders_dict["TrajP1"][0])
###info that's not in the Traj files
g = 9.81                # gravitational acceleration [m/s2]
Xs = 0.037              # upper limit of the interface (start) [m]
Xe = 0.05               # bottom limit of the interface (exit) [m]
h=Xe-Xs                 # interface thickness [m]
rho1= 976               # density top layer [kg/m3]
rho2 = 1025             # density bottom layer [kg/m3]
lam = 0.35              # hyperbolic function constructive param used to simulate density profile [-]
# func constructing the density profile of the whole tank [kg/m3]
def rho(X): return rho2 - 0.5 * (rho2 - rho1) * (1 - np.tanh(X - (Xe + Xs) / (2 * lam * h)))
nu1 = 1.43e-6           # kinematic viscosity of the top layer [m2/s]
nu2 = 1.012e-6          # kinematic viscosity of the bottom layer [m2/s]

#locing info acc to index file in Data (minus 2 lines from what's listed)
###general data:
X = data.iloc[1]        # the bead’s position as a func of t, initialized at the top of the tank. [m]
t = data.iloc[5]        # starts from 0 at the top of the tank [s]
rho = rho(X)
Vp_file = data.iloc[3]  # particle velocity as calculated in the mat files [m/s]
def F_drg(Re): return 0.00064 * Re ** 1.44  # drag force as a func. of Re, derived from direct measuring of Vterminal in constant density environment

###sphere properties:
d = data.iloc[7,0]                        # sphere's diameter [m]
rhop = data.iloc[8,0]                     # sphere's density [kg/m3]
def Vol_p(d): return np.pi * d ** 3 / 6   # sphere's volume [m3]
def m(d, rhop): return rhop * Vol_p(d)    # sphere's mass [kg]
m=m(d,rhop)

###drift volume properties:
omega = 0.15            # distance from the sphere [cm]
z = 4.792e-5            # entrained fluid’s mass [Kg]. Can be shifted to fit data
beta0 = 0.06            # diffusivity due to mass concentrations, set to same order as diffusivity of salt in water [1/s]
beta_trb = 0.94         # turbulent diffusivity [1/cm]
def beta(Vp): return beta0 + beta_trb * abs(Vp)  # total diffusivity coefficient
