import pandas as pd
import talib as ta

def cdlrisefall3methods(df, coin_symbol, interval):
    cdlrisefall3methods = ta.CDLRISEFALL3METHODS(df['open'], df['high'], df['low'], df['close'])
    cdlrisefall3methods_col_name = coin_symbol + "_" + interval + "_cdlrisefall3methods"
    df[cdlrisefall3methods_col_name] = cdlrisefall3methods
    return df

