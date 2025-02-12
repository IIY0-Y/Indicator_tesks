import pandas as pd
import talib as ta

def sin(df, col, coin_symbol, interval, is_price):
    if is_price:
        sin_col_name = coin_symbol + "_" + interval + "_sin"
    else:
        sin_col_name = col + "_sin"
    sin = ta.SIN(df[col])
    df[sin_col_name] = sin
    df=df.dropna()
    return df

