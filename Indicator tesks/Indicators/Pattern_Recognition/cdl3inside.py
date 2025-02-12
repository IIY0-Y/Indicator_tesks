import pandas as pd
import talib as ta

def cdl3inside(df, coin_symbol, interval):
    cdl3inside = ta.CDL3INSIDE(df['open'], df['high'], df['low'], df['close'])
    cdl3inside_col_name = coin_symbol + "_" + interval + "_cdl3inside"
    df[cdl3inside_col_name] = cdl3inside
    return df

