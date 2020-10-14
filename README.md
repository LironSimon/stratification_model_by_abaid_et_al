# stratification_model_by_abaid_et_al
Equations of the model proposed by Abaid et al. 2004, of the stratification force exerted on a settling sphere

This resipatory compares mesured velocities of settling/rising spheres to the velocities precdicted by the proposed model.

- Mat_files: includes files used by Verso at Al, 2019, and a file of digitalized data from Fernnado 1999.
- Imported_data_and_properties: loads relevant information from the mat files, and defines pre-set parameters and formulas (acc. to the model)
### I still need to figure out how to store this data
### Maybe I should add some validation check to see if the Re,Fr and interface thickness are comparble to Abaid
- Drift_volume_density: solves a first order differential equation to formulate the changing density of the entrained fluid as a func of time. The velocity of the sphere remains in the solution as an unknown variable
- Velocity_of_drift_volume: solves a first order differential equation to formulate the changing velocity of the entrained fluid as a func of time, and uses the sol of Drift_volume_density for its calculations. The velocity of the sphere remains in the solution as an unknown variable
- Velocity_of_prtcl: solves a second order differential equation and formulates the changing velocity of the entrained fluid as a func of time. Uses both the sol of Drift_volume_density AND OF velocity_of_drift_volume for its calculations. plots the solution (the particle's velocity) and shows compatibilty to actual velocity
