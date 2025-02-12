import pandas as pd
import talib as ta

def cdllongleggeddoji(df, coin_symbol, interval):
    cdllongleggeddoji = ta.CDLLONGLEGGEDDOJI(df['open'], df['high'], df['low'], df['close'])
    cdllongleggeddoji_col_name = coin_symbol + "_" + interval + "_cdllongleggeddoji"
    df[cdllongleggeddoji_col_name] = cdllongleggeddoji
    return df

