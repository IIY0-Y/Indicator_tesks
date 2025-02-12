import pandas as pd
import talib as ta

def ht_dcperiod(df, col, coin_symbol, interval, is_price):
    if is_price:
        ht_dcperiod_col_name = coin_symbol + "_" + interval + "_ht_dcperiod"
    else:
        ht_dcperiod_col_name = col + "_ht_dcperiod"
    ht_dcperiod = ta.HT_DCPERIOD(df[col])
    df[ht_dcperiod_col_name] = ht_dcperiod
    df=df.dropna()
    return df

