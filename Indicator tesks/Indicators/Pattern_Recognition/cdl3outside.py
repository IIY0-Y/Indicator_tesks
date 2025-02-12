import pandas as pd
import talib as ta

def cdl3outside(df, coin_symbol, interval):
    cdl3outside = ta.CDL3OUTSIDE(df['open'], df['high'], df['low'], df['close'])
    cdl3outside_col_name = coin_symbol + "_" + interval + "_cdl3outside"
    df[cdl3outside_col_name] = cdl3outside
    return df

