import pandas as pd
import talib as ta

def cdl3starsinsouth(df, coin_symbol, interval):
    cdl3starsinsouth = ta.CDL3STARSINSOUTH(df['open'], df['high'], df['low'], df['close'])
    cdl3starsinsouth_col_name = coin_symbol + "_" + interval + "_cdl3starsinsouth"
    df[cdl3starsinsouth_col_name] = cdl3starsinsouth
    return df

