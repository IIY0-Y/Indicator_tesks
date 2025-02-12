import pandas as pd
import talib as ta

def tan(df, col, coin_symbol, interval, is_price):
    if is_price:
        tan_col_name = coin_symbol + "_" + interval + "_tan"
    else:
        tan_col_name = col + "_tan"
    tan = ta.TAN(df[col])
    df[tan_col_name] = tan
    df=df.dropna()
    return df

