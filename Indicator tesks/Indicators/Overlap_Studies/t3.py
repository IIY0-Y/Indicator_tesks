import pandas as pd
import talib as ta

def t3(df, col, coin_symbol, interval, is_price, timeperiod=5, vfactor=0):
    if is_price:
        t3_col_name = coin_symbol + "_" + interval + "_t3_" + str(timeperiod) + "_" + str(vfactor).replace(".","dot")
    else:
        t3_col_name = col + "_t3_" + str(timeperiod) + "_" + str(vfactor).replace(".","dot")
    t3 = ta.T3(df[col], timeperiod=timeperiod, vfactor=vfactor)
    df[t3_col_name] = t3
    df=df.dropna()
    return df

