import pandas as pd
import talib as ta

def floor(df, col, coin_symbol, interval, is_price):
    if is_price:
        floor_col_name = coin_symbol + "_" + interval + "_floor"
    else:
        floor_col_name = col + "_floor"
    floor = ta.FLOOR(df[col])
    df[floor_col_name] = floor
    df=df.dropna()
    return df

