import pandas as pd
import talib as ta

def cdl2crows(df, coin_symbol, interval):
    cdl2crows = ta.CDL2CROWS(df['open'], df['high'], df['low'], df['close'])
    cdl2crows_col_name = coin_symbol + "_" + interval + "_cdl2crows"
    df[cdl2crows_col_name] = cdl2crows
    return df

