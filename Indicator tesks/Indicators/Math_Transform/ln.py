import pandas as pd
import talib as ta

def ln(df, col, coin_symbol, interval, is_price):
    if is_price:
        ln_col_name = coin_symbol + "_" + interval + "_ln"
    else:
        ln_col_name = col + "_ln"
    ln = ta.LN(df[col])
    df[ln_col_name] = ln
    df=df.dropna()
    return df

