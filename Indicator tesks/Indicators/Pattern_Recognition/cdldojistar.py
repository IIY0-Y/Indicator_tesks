import pandas as pd
import talib as ta

def cdldojistar(df, coin_symbol, interval):
    cdldojistar = ta.CDLDOJISTAR(df['open'], df['high'], df['low'], df['close'])
    cdldojistar_col_name = coin_symbol + "_" + interval + "_cdldojistar"
    df[cdldojistar_col_name] = cdldojistar
    return df

