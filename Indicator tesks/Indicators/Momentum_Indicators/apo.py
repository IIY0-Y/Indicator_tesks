import pandas as pd
import talib as ta

def apo(df, col, coin_symbol, interval, is_price, fastperiod=12, slowperiod=26, matype=0):
    if is_price:
        apo_col_name = coin_symbol + "_" + interval + "_apo_" + str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(matype)
    else:
        apo_col_name = col + "_apo_" + str(fastperiod) + "_" + str(slowperiod) + "_" + str(matype)
    apo = ta.APO(df[col], fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
    df[apo_col_name] = apo
    df=df.dropna()
    return df

