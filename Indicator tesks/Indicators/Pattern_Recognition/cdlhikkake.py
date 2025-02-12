import pandas as pd
import talib as ta

def cdlhikkake(df, coin_symbol, interval):
    cdlhikkake = ta.CDLHIKKAKE(df['open'], df['high'], df['low'], df['close'])
    cdlhikkake_col_name = coin_symbol + "_" + interval + "_cdlhikkake"
    df[cdlhikkake_col_name] = cdlhikkake
    return df

