import pandas as pd
import talib as ta

def ht_trendline(df, col, coin_symbol, interval, is_price):
    if is_price:
        ht_trendline_col_name = coin_symbol + "_" + interval + "_ht_trendline"
    else:
        ht_trendline_col_name = col + "_ht_trendline"
    ht_trendline = ta.HT_TRENDLINE(df[col])
    df[ht_trendline_col_name] = ht_trendline
    df=df.dropna()
    return df

