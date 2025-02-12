import pandas as pd
import talib as ta

def ma(df, col, coin_symbol, interval, is_price, timeperiod=30, matype=0):
    if is_price:
        ma_col_name = coin_symbol + "_" + interval + "_ma_" + str(timeperiod) + "_" + str(matype)
    else:
        ma_col_name = col + "_ma_" + str(timeperiod) + "_" + str(matype)
    ma = ta.MA(df[col], timeperiod=timeperiod, matype=matype)
    df[ma_col_name] = ma
    df=df.dropna()
    return df

