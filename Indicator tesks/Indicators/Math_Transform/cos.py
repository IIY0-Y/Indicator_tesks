import pandas as pd
import talib as ta

def cos(df, col, coin_symbol, interval, is_price):
    if is_price:
        cos_col_name = coin_symbol + "_" + interval + "_cos"
    else:
        cos_col_name = col + "_cos"
    cos = ta.COS(df[col])
    df[cos_col_name] = cos
    df=df.dropna()
    return df

