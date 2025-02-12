import pandas as pd
import talib as ta

def cdlidentical3crows(df, coin_symbol, interval):
    cdlidentical3crows = ta.CDLIDENTICAL3CROWS(df['open'], df['high'], df['low'], df['close'])
    cdlidentical3crows_col_name = coin_symbol + "_" + interval + "_cdlidentical3crows"
    df[cdlidentical3crows_col_name] = cdlidentical3crows
    return df

