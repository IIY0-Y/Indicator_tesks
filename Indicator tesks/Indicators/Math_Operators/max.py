import pandas as pd
import talib as ta

def max(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        max_col_name = coin_symbol + "_" + interval + "_max_" + str(timeperiod)
    else:
        max_col_name = col + "_max_" + str(timeperiod)
    max = ta.MAX(df[col], timeperiod=timeperiod)
    df[max_col_name] = max
    df=df.dropna()
    return df

