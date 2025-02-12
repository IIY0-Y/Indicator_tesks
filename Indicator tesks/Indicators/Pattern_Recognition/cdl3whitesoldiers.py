import pandas as pd
import talib as ta

def cdl3whitesoldiers(df, coin_symbol, interval):
    cdl3whitesoldiers = ta.CDL3WHITESOLDIERS(df['open'], df['high'], df['low'], df['close'])
    cdl3whitesoldiers_col_name = coin_symbol + "_" + interval + "_cdl3whitesoldiers"
    df[cdl3whitesoldiers_col_name] = cdl3whitesoldiers
    return df

