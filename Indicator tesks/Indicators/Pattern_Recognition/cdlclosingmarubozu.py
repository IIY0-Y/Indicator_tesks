import pandas as pd
import talib as ta

def cdlclosingmarubozu(df, coin_symbol, interval):
    cdlclosingmarubozu = ta.CDLCLOSINGMARUBOZU(df['open'], df['high'], df['low'], df['close'])
    cdlclosingmarubozu_col_name = coin_symbol + "_" + interval + "_cdlclosingmarubozu"
    df[cdlclosingmarubozu_col_name] = cdlclosingmarubozu
    return df

