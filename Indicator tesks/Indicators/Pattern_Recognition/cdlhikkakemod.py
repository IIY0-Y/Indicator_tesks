import pandas as pd
import talib as ta

def cdlhikkakemod(df, coin_symbol, interval):
    cdlhikkakemod = ta.CDLHIKKAKEMOD(df['open'], df['high'], df['low'], df['close'])
    cdlhikkakemod_col_name = coin_symbol + "_" + interval + "_cdlhikkakemod"
    df[cdlhikkakemod_col_name] = cdlhikkakemod
    return df

