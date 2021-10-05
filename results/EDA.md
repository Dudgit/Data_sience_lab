# Results of EDA
## Short description
As much as I understand, every .nc file contains information about 1 specific Eddy.  
These are multidimensional parameters with 3 indexes.  
- Longitude: position parameter  
- Lattitude: position parameter  
- Time: the specific time of the observation  
## Values
There are 3 value parameters, which I consider important at this stage.  
- sea_surface_height_above_sea_level: It is also a position parameter, for visualization it could be really usefull. For model training... We'll see.  
- surface_geostrophic_northward_sea_water_velocity: This is the velocity northward, esential to calculate radius.
- surface_geostrophic_eastward_sea_water_velocity: Eastwar velocity, similar to its pair.  

They contain nans. Handling plan: interpolation, for we assume that they don't jump too big in their values. Might be reasonable to create an interpolation limit, if there are too many missing values after each other. See that later.
