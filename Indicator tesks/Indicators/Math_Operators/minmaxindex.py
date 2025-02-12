import pandas as pd
import talib as ta

def minmaxindex(df, col, coin_symbol, interval, is_price, timeperiod=30):
    minmaxindex = ta.MINMAXINDEX(df[col], timeperiod=timeperiod)
    if is_price:
        minidx_col_name = coin_symbol + "_" + interval + "_minidx_" + str(timeperiod)
        maxidx_col_name = coin_symbol + "_" + interval + "_maxidx_" + str(timeperiod)
    else:
        minidx_col_name = col + "_minidx_" + str(timeperiod)
        maxidx_col_name = col + "_maxidx_" + str(timeperiod)
    cols = [minidx_col_name, maxidx_col_name]
    for i, c in enumerate(cols):
        df[c] = minmaxindex[i]
    df=df.dropna()
    return df

