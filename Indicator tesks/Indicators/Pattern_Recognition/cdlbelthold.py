import pandas as pd
import talib as ta

def cdlbelthold(df, coin_symbol, interval):
    cdlbelthold = ta.CDLBELTHOLD(df['open'], df['high'], df['low'], df['close'])
    cdlbelthold_col_name = coin_symbol + "_" + interval + "_cdlbelthold"
    df[cdlbelthold_col_name] = cdlbelthold
    return df

