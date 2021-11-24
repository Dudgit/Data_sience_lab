import xarray as xr
import pandas as pd
from numpy import nan


aggdict = {'adt':'first','ugos':"mean","vgos":"mean","sla":"first","ugosa":"mean","vgosa":"mean"}

def format_Eddy(Eddy_name):
    """
    Description:  
    ------------  

    This fuction create a table in a format we later want to use, from the given dataset.  

    Args:  
    -----  

    Eddy_name: string, the name of the specific day-data, what we want to use  

    Returns:  
    --------  

    pandas DataFrame, an ABT like table, of one specific day  

    """
    Eddy_df = xr.load_dataset(Eddy_name).to_dataframe()
    Eddies = Eddy_df.loc[Eddy_df.ugos.notna()]
    ABT = Eddies.groupby(["longitude","latitude"]).agg(aggdict)
    Current_time = Eddies.index.get_level_values("time").unique()[0]
    ABT["Born"] = Current_time
    ABT["Dead"] = 0
    ABT["Errcount"] = 0
    return ABT

def proceed(ABT,Eddie):
    """
    Description:  
    ------------  

    Calculate the difference between 2 ABT like table  
    
    Args:  
    -----  

    - ABT: pandas DataFrame, the current ABT we have  

    - Eddie: pandas DataFrame, an ABT like table, describeing a specific day  

    Returns:  
    --------  

    Two list of multi indexes, which represent individual Eddies
    """
    
    new_eddies = list(set(Eddie.index)-set(ABT.index))
    dead_eddies = list(set(ABT.index)-set(Eddie.index))
    return new_eddies, dead_eddies


def update_ABT(current_ABT,newname,output_name="res",h = False):
    """
    Description:  
    ------------  

    Updates the current ABT with a new day, drops the dead eddies and write them out into the res.csv. May need a year-split update  

    Args:  
    ------  

    - current_ABT: pandas DataFrame, the current ABT  

    - newname: string, the name of the next day-data  

    - h(optional): bool, use header in the write out or not (use False, except in the first function call)  

    Returns:  
    --------  

    pandas DataFrame, the updated ABT
    """
    new_ABT = format_Eddy(newname)
    born,dead = proceed(current_ABT,new_ABT)
    #TODO: később csinálni ténylegesen hibahatárosdit
    #current_ABT.loc[dead,["Errcount"]] += 1
    dead_time = new_ABT.Born.iloc[0]

    current_ABT.loc[dead,"Dead"] =dead_time 
    current_ABT.loc[dead].to_csv(f"results/{output_name}.csv",mode='a',header = h)
    current_ABT.drop(current_ABT.loc[dead].index,inplace=True)

    current_ABT = current_ABT.append(new_ABT.loc[born])
    return current_ABT


    
def update_ABT_v2(current_ABT,newname,output_name="res",h = False):
    """
    Description:  
    ------------  

    Updates the current ABT with a new day, drops the dead eddies and write them out into the res.csv. May need a year-split update  

    Args:  
    ------  

    - current_ABT: pandas DataFrame, the current ABT  

    - newname: string, the name of the next day-data  

    - h(optional): bool, use header in the write out or not (use False, except in the first function call)  

    Returns:  
    --------  

    pandas DataFrame, the updated ABT
    """
    new_ABT = format_Eddy(newname)
    born,dead = proceed(current_ABT,new_ABT)
    possibly_dead = current_ABT[current_ABT.Errcount > 0]

    not_dead = pd.Series([p if p in new_ABT.index else nan  for p in possibly_dead.index]).dropna()
    if not not_dead.empty:
        current_ABT.loc[not_dead,"Errcount"] = 0
    current_ABT.loc[dead,"Errcount"] += 1 

    current_time = new_ABT.Born.iloc[0]

    die_condition = current_ABT.Errcount > 3
    current_ABT.loc[die_condition,"Dead"] = current_time - pd.to_timedelta(2,"D") 
    current_ABT.loc[die_condition].to_csv(f"results/{output_name}.csv",mode='a',header = h)
    current_ABT.drop(current_ABT.loc[dead].index,inplace=True)

    current_ABT = current_ABT.append(new_ABT.loc[born])
    return current_ABT