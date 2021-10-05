import pandas as pd

def get_longevity(df):
    """
    Description:  
    - - - - - - -  

    This function will calculate the longevity of the Eddy. The difference between it's smallest time value and its maximum. For we assume this is the longevity.  
    Version: 1.0  

    Args:  
    - - -   

    - df: pandas Dataframe, the data read from the given nc file, containing information about the given Eddy.  

    Returns:  
    - - - -  

    Timedelta, (days, hours, mins, sec)  
    """
    return df.index.get_level_values('time').max() - df.index.get_level_values('time').min()