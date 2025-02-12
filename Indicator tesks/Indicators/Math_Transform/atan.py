import pandas as pd
import talib as ta

def atan(df, col, coin_symbol, interval, is_price):
    if is_price:
        atan_col_name = coin_symbol + "_" + interval + "_atan"
    else:
        atan_col_name = col + "_atan"
    atan = ta.ATAN(df[col])
    df[atan_col_name] = atan
    df=df.dropna()
    return df

