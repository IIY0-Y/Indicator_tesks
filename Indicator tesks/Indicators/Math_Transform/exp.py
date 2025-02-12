import pandas as pd
import talib as ta

def exp(df, col, coin_symbol, interval, is_price):
    if is_price:
        exp_col_name = coin_symbol + "_" + interval + "_exp"
    else:
        exp_col_name = col + "_exp"
    exp = ta.EXP(df[col])
    df[exp_col_name] = exp
    df=df.dropna()
    return df

