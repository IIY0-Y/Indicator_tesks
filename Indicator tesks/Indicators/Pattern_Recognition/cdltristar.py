import pandas as pd
import talib as ta

def cdltristar(df, coin_symbol, interval):
    cdltristar = ta.CDLTRISTAR(df['open'], df['high'], df['low'], df['close'])
    cdltristar_col_name = coin_symbol + "_" + interval + "_cdltristar"
    df[cdltristar_col_name] = cdltristar
    return df

