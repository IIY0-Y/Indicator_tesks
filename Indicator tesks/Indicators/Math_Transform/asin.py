import pandas as pd
import talib as ta

def asin(df, col, coin_symbol, interval, is_price):
    if is_price:
        asin_col_name = coin_symbol + "_" + interval + "_asin"
    else:
        asin_col_name = col + "_asin"
    asin = ta.ASIN(df[col])
    df[asin_col_name] = asin
    df=df.dropna()
    return df

