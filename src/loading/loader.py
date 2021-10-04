# %%
import netCDF4 as nc

folder_name = "data/"
def loadnc(fname,deepness = 1):
    """
    Description:  
    - - - - - - -  

    This function will load the .nc format files from the data folder.  

    Args:  
    - - -  

    - fname: string, name of the file, we want to load  
    - deepnes: integer, how deep is the folder, where you call the function from 
    Returns:  
    - - - - -  

    netCDF4 dataset
    """
    folder = "../"*deepness + folder_name
    return nc.Dataset(f"{folder}{fname}.nc")

#loadnc(filepath)
# %%
