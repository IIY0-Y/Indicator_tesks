import pandas as pd
import talib as ta

def cdlunique3river(df, coin_symbol, interval):
    cdlunique3river = ta.CDLUNIQUE3RIVER(df['open'], df['high'], df['low'], df['close'])
    cdlunique3river_col_name = coin_symbol + "_" + interval + "_cdlunique3river"
    df[cdlunique3river_col_name] = cdlunique3river
    return df

