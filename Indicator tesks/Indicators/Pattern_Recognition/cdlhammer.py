import pandas as pd
import talib as ta

def cdlhammer(df, coin_symbol, interval):
    cdlhammer = ta.CDLHAMMER(df['open'], df['high'], df['low'], df['close'])
    cdlhammer_col_name = coin_symbol + "_" + interval + "_cdlhammer"
    df[cdlhammer_col_name] = cdlhammer
    return df

