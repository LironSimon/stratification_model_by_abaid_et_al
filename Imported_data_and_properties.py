#!/usr/bin/env python
# coding: utf-8

# In[8]:


# Imported_data_and_eq uploads all relevet data entries from prior matlab files, to define the variables needed for later calculations

from scipy.io import loadmat
import numpy as np
import glob


# In[12]:


#Arranging files to excerpt data from
files_directory_list = glob.glob('../Mat_files/*.mat')
print(file_list)


# In[ ]:


#Asafi! do you understand why it doesn't load?


# In[ ]:


# Creating a lst of dictionaries, named after each file, storing rlvnt data

for file in file_directory_list:
    fname = file.rsplit('/')[-1].split('_')[0]
    data = loadmat(file)


# In[ ]:


#Asafi! do you have an idea of how to store all the info?
#I'd like to upload all the folowing info from the files 


# In[ ]:


#Defining variables

###sphere properties:
d= None                               # sphere's diameter [m] 
def Vol_p(d): return np.pi*d**3/6     # sphere's volume [m3]
rhop= None                            #	sphere's density [kg/m3]
def m(d,rhop): return rhop*Vol_p(d)   # sphere's mass [kg]

###general data:
X=np.aaray()                          # the bead’s position as a func of t, initialized at the top of the tank. [m]
t=np.aaray()                          # starts from 0 at the top of the tank [s]
g=9.81                                # gravitational acceleration [m/s2]
Xs= None                              # location of the start of the density interface [m]
Xe= None                              # location of the end of the density interface [m]
h= Xe - Xs                            # interface thickness [m]
rho1= None                            # density of the top layer [kg/m3]
rho2= None                            # density of the bottom layer [kg/m3]
lam=0.35                              # hyperbolic function constructive param used to simulate density profile [-]
def rho(X): return rho2 - 0.5*(rho2-rho1)*(1-np.tanh(X-(Xe + Xs)/(2*lam*h))   # rho: density profile of the whole tank [kg/m3]
def F_drg(Re)=0.00064*Re**1.44        #	drag force as a func. of Re, derived from direct measuring of Vterminal in constant density enviroment
nu1= None                             # kinematic viscosity of the top layer
nu2= None                             # kinematic viscosity of the bottom layer
Vp_measured=np.aaray()                # particle velocity as calculated in the mat files
      
###drift volume properties:
# drift volume is modeled as a point mass, draged by the sphere in with a constant distance
omega=0.15                            # distance from the sphere [cm]
beta0= 0.06                           #	diffusivity due to mass concentrations. Of same order as diffusivity of salt in water [1/s]
beta_trb= 0.94                        # turbulent diffusivity [1/cm]
def beta(Vp): return beta0+beta_trb*abs(Vp)     # total diffusivity coefficient	
z=0.04792                             # entrained fluid’s mass [g]. Can be shifted to fit data

