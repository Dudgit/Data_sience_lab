aggdict = {'adt':'first','ugos':"first","vgos":"first","sla":"first","ugosa":"first","vgosa":"first"}


def individual_eddy(Eddies):
    res = []

    lats = Eddies.index.get_level_values('latitude').unique()
    for lat in lats:
        longs = Eddies.loc[(Eddies.index.get_level_values('latitude') == lat)].index.get_level_values('longitude').unique()
        for longi in longs:
            res.append(Eddies.loc[(Eddies.index.get_level_values('latitude') == lat) & (Eddies.index.get_level_values('longitude') == longi)])
    return res

def format_Eddy(Eddy_df):
    Eddies = Eddy_df.loc[Eddy_df.ugos.notna()]
    ABT = Eddies.groupby(["longitude","latitude"]).agg(aggdict)
    return ABT