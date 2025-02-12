import pandas as pd
import talib as ta

def cdlinneck(df, coin_symbol, interval):
    cdlinneck = ta.CDLINNECK(df['open'], df['high'], df['low'], df['close'])
    cdlinneck_col_name = coin_symbol + "_" + interval + "_cdlinneck"
    df[cdlinneck_col_name] = cdlinneck
    return df

