import pandas as pd
import talib as ta

def bop(df, coin_symbol, interval):
    bop = ta.BOP(df['open'], df['high'], df['low'], df['close'])
    bop_col_name = coin_symbol + "_" + interval + "_bop"
    df[bop_col_name] = bop
    return df

