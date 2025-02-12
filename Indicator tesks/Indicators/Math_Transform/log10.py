import pandas as pd
import talib as ta

def log10(df, col, coin_symbol, interval, is_price):
    if is_price:
        log10_col_name = coin_symbol + "_" + interval + "_log10"
    else:
        log10_col_name = col + "_log10"
    log10 = ta.LOG10(df[col])
    df[log10_col_name] = log10
    df=df.dropna()
    return df

