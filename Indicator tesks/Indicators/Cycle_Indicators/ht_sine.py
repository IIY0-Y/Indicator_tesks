import pandas as pd
import talib as ta

def ht_sine(df, col, coin_symbol, interval, is_price):
    ht_sine = ta.HT_SINE(df[col])
    if is_price:
        sine_col_name = coin_symbol + "_" + interval + "_sine"
        leadsine_col_name = coin_symbol + "_" + interval + "_leadsine"
    else:
        sine_col_name = col + "_sine"
        leadsine_col_name = col + "_leadsine"
    cols = [sine_col_name, leadsine_col_name]
    for i, c in enumerate(cols):
        df[c] = ht_sine[i]
    df=df.dropna()
    return df

