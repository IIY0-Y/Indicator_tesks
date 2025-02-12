import pandas as pd
import talib as ta

def cdlmarubozu(df, coin_symbol, interval):
    cdlmarubozu = ta.CDLMARUBOZU(df['open'], df['high'], df['low'], df['close'])
    cdlmarubozu_col_name = coin_symbol + "_" + interval + "_cdlmarubozu"
    df[cdlmarubozu_col_name] = cdlmarubozu
    return df

