import pandas as pd
import talib as ta

def cdl3linestrike(df, coin_symbol, interval):
    cdl3linestrike = ta.CDL3LINESTRIKE(df['open'], df['high'], df['low'], df['close'])
    cdl3linestrike_col_name = coin_symbol + "_" + interval + "_cdl3linestrike"
    df[cdl3linestrike_col_name] = cdl3linestrike
    return df

