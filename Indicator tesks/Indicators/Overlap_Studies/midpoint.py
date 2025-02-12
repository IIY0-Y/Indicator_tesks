import pandas as pd
import talib as ta

def midpoint(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        midpoint_col_name = coin_symbol + "_" + interval + "_midpoint_" + str(timeperiod)
    else:
        midpoint_col_name = col + "_midpoint_" + str(timeperiod)
    midpoint = ta.MIDPOINT(df[col], timeperiod=timeperiod)
    df[midpoint_col_name] = midpoint
    df=df.dropna()
    return df

