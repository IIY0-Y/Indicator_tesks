import pandas as pd
import talib as ta

def cdlonneck(df, coin_symbol, interval):
    cdlonneck = ta.CDLONNECK(df['open'], df['high'], df['low'], df['close'])
    cdlonneck_col_name = coin_symbol + "_" + interval + "_cdlonneck"
    df[cdlonneck_col_name] = cdlonneck
    return df

