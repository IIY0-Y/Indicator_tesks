import pandas as pd
import talib as ta

def cosh(df, col, coin_symbol, interval, is_price):
    if is_price:
        cosh_col_name = coin_symbol + "_" + interval + "_cosh"
    else:
        cosh_col_name = col + "_cosh"
    cosh = ta.COSH(df[col])
    df[cosh_col_name] = cosh
    df=df.dropna()
    return df

