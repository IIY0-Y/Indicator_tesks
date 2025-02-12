import pandas as pd
import talib as ta

def cdldoji(df, coin_symbol, interval):
    cdldoji = ta.CDLDOJI(df['open'], df['high'], df['low'], df['close'])
    cdldoji_col_name = coin_symbol + "_" + interval + "_cdldoji"
    df[cdldoji_col_name] = cdldoji
    return df

