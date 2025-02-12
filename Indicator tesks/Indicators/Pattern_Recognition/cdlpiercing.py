import pandas as pd
import talib as ta

def cdlpiercing(df, coin_symbol, interval):
    cdlpiercing = ta.CDLPIERCING(df['open'], df['high'], df['low'], df['close'])
    cdlpiercing_col_name = coin_symbol + "_" + interval + "_cdlpiercing"
    df[cdlpiercing_col_name] = cdlpiercing
    return df

