import pandas as pd
import talib as ta

def cdlhangingman(df, coin_symbol, interval):
    cdlhangingman = ta.CDLHANGINGMAN(df['open'], df['high'], df['low'], df['close'])
    cdlhangingman_col_name = coin_symbol + "_" + interval + "_cdlhangingman"
    df[cdlhangingman_col_name] = cdlhangingman
    return df

