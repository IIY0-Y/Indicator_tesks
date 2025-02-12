import pandas as pd
import talib as ta

def cdlkicking(df, coin_symbol, interval):
    cdlkicking = ta.CDLKICKING(df['open'], df['high'], df['low'], df['close'])
    cdlkicking_col_name = coin_symbol + "_" + interval + "_cdlkicking"
    df[cdlkicking_col_name] = cdlkicking
    return df

