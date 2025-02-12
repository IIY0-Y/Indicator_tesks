import pandas as pd
import talib as ta

def cdlengulfing(df, coin_symbol, interval):
    cdlengulfing = ta.CDLENGULFING(df['open'], df['high'], df['low'], df['close'])
    cdlengulfing_col_name = coin_symbol + "_" + interval + "_cdlengulfing"
    df[cdlengulfing_col_name] = cdlengulfing
    return df

