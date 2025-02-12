import pandas as pd
import talib as ta

def tsf(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        tsf_col_name = coin_symbol + "_" + interval + "_tsf_" + str(timeperiod)
    else:
        tsf_col_name = col + "_tsf_" + str(timeperiod)
    tsf = ta.TSF(df[col], timeperiod=timeperiod)
    df[tsf_col_name] = tsf
    df=df.dropna()
    return df

