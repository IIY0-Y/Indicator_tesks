import pandas as pd
import talib as ta

def ceil(df, col, coin_symbol, interval, is_price):
    if is_price:
        ceil_col_name = coin_symbol + "_" + interval + "_ceil"
    else:
        ceil_col_name = col + "_ceil"
    ceil = ta.CEIL(df[col])
    df[ceil_col_name] = ceil
    df=df.dropna()
    return df

