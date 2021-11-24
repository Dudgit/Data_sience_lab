features = ["vgos","ugos","vgosa","ugosa"]
import pandas as pd

def convert_types(Eddy):
    Eddy.loc[:,features] = Eddy.loc[:,features].astype(float)

def add_new_features(Eddy1):
    convert_types(Eddy1)
    Eddy1["Longevity"] = (pd.to_datetime(Eddy1.Dead) - pd.to_datetime(Eddy1.Born)).dt.days

    Eddy1["radius"] =  abs(Eddy1.ugos)+  abs(Eddy1.vgos) 
    Eddy1["radius_glob"] = abs(Eddy1.ugosa) + abs(Eddy1.vgosa)

    """
    Eddy1["multiplied"] =  abs(Eddy1.ugos )  * abs(Eddy1.vgos )
    Eddy1["multiplieda"] = abs(Eddy1.ugosa) *  abs(Eddy1.vgosa)

    Eddy1["substracted"] =  abs(Eddy1.ugos )  / abs(Eddy1.vgos )
    Eddy1["substracteda"] = abs(Eddy1.ugosa) /  abs(Eddy1.vgosa)

    Eddy1["deducted"] =  abs(Eddy1.ugos  ) - abs(Eddy1.vgos )
    Eddy1["deducteda"] = abs(Eddy1.ugosa )-  abs(Eddy1.vgosa)

    Eddy1["exp1a"] =  abs(Eddy1.ugos*Eddy1.ugosa  ) + abs(Eddy1.vgos*Eddy1.vgosa )
    Eddy1["exp2a"] =  abs(Eddy1.ugos+Eddy1.ugosa  ) + abs(Eddy1.vgos+Eddy1.vgosa )
    Eddy1["exp3a"] =  abs(Eddy1.ugos)+abs(Eddy1.ugosa  ) * abs(Eddy1.vgos)+abs(Eddy1.vgosa )
    Eddy1["exp4a"] =  abs(Eddy1.ugos)*abs(Eddy1.ugosa) * abs(Eddy1.vgos)*abs(Eddy1.vgosa )

    Eddy1["exp1"] =  Eddy1.ugos*Eddy1.ugosa   + Eddy1.vgos*Eddy1.vgosa 
    Eddy1["exp2"] =  Eddy1.ugos+Eddy1.ugosa   + Eddy1.vgos+Eddy1.vgosa 
    Eddy1["exp3"] =  (Eddy1.ugos+Eddy1.ugosa)   * (Eddy1.vgos+Eddy1.vgosa)
    Eddy1["exp4"] =  Eddy1.ugos*Eddy1.ugosa   * Eddy1.vgos*Eddy1.vgosa
    """