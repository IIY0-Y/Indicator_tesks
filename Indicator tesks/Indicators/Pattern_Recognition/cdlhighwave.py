import pandas as pd
import talib as ta

def cdlhighwave(df, coin_symbol, interval):
    cdlhighwave = ta.CDLHIGHWAVE(df['open'], df['high'], df['low'], df['close'])
    cdlhighwave_col_name = coin_symbol + "_" + interval + "_cdlhighwave"
    df[cdlhighwave_col_name] = cdlhighwave
    return df

