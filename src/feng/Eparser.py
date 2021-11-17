import xarray as xr
aggdict = {'adt':'first','ugos':"mean","vgos":"mean","sla":"first","ugosa":"mean","vgosa":"mean"}


def individual_eddy(Eddies):
    res = []

    lats = Eddies.index.get_level_values('latitude').unique()
    for lat in lats:
        longs = Eddies.loc[(Eddies.index.get_level_values('latitude') == lat)].index.get_level_values('longitude').unique()
        for longi in longs:
            res.append(Eddies.loc[(Eddies.index.get_level_values('latitude') == lat) & (Eddies.index.get_level_values('longitude') == longi)])
    return res

    


def format_Eddy(Eddy_name):
    Eddy_df = xr.load_dataset(Eddy_name).to_dataframe()
    Eddies = Eddy_df.loc[Eddy_df.ugos.notna()]
    ABT = Eddies.groupby(["longitude","latitude"]).agg(aggdict)
    Current_time = Eddies.index.get_level_values("time").unique()[0]
    ABT["Born"] = Current_time
    ABT["Dead"] = 0
    ABT["Errcount"] = 0
    return ABT

def proceed(ABT,Eddie):
    new_eddies = list(set(Eddie.index)-set(ABT.index))
    dead_eddies = list(set(ABT.index)-set(Eddie.index))
    return new_eddies, dead_eddies

def update_ABT(current_ABT,newname,h = False):
    new_ABT = format_Eddy(newname)
    born,dead = proceed(current_ABT,new_ABT)
    #TODO: később csinálni ténylegesen hibahatárosdit
    #current_ABT.loc[dead,["Errcount"]] += 1
    dead_time = new_ABT.Born.iloc[0]
    
    current_ABT.loc[dead,"Dead"] =dead_time 
    current_ABT.loc[dead].to_csv("results/res.csv",mode='a',header = h)
    current_ABT.drop(current_ABT.loc[dead].index,inplace=True)
    
    current_ABT = current_ABT.append(new_ABT.loc[born])
    return current_ABT