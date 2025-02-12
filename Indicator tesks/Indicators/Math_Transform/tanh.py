import pandas as pd
import talib as ta

def tanh(df, col, coin_symbol, interval, is_price):
    if is_price:
        tanh_col_name = coin_symbol + "_" + interval + "_tanh"
    else:
        tanh_col_name = col + "_tanh"
    tanh = ta.TANH(df[col])
    df[tanh_col_name] = tanh
    df=df.dropna()
    return df

