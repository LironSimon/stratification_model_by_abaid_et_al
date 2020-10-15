
from scipy.integrate import odeint
from Imported_data_and_properties import *


# function that returns d2X_dt2, drhod_dt, deta_dt
def model(z,t,X):
    dX_dt=z[0]
    rhod=z[1]
    eta=z[2]

    d2X_dt2=g*(rhop-rho(X))/rhop+F_drg(Re(2*dX_dt-eta))
    drhod_dt=beta(dX_dt)*(rho(X)-rhod)
    deta_dt=g*(rho(X-omega)-rhod)/rhod+F_drg(Re(eta-dX_dt))

    return [d2X_dt2, drhod_dt, deta_dt]

#initial conditions
z0=[Vt1,rho(0),Vt1]

#defining the time steps for the solution
t_tot=np.linspace(0, t_e, 100)      #generate a solution at 101 evenly spaced samples in the interval 0 <= t <= t_e

z=odeint(model, z0, t_tot,args=(X,))