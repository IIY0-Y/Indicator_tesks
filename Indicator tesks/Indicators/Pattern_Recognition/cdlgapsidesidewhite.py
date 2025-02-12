import pandas as pd
import talib as ta

def cdlgapsidesidewhite(df, coin_symbol, interval):
    cdlgapsidesidewhite = ta.CDLGAPSIDESIDEWHITE(df['open'], df['high'], df['low'], df['close'])
    cdlgapsidesidewhite_col_name = coin_symbol + "_" + interval + "_cdlgapsidesidewhite"
    df[cdlgapsidesidewhite_col_name] = cdlgapsidesidewhite
    return df

