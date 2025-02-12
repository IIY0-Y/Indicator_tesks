import pandas as pd
import talib as ta

def cdltakuri(df, coin_symbol, interval):
    cdltakuri = ta.CDLTAKURI(df['open'], df['high'], df['low'], df['close'])
    cdltakuri_col_name = coin_symbol + "_" + interval + "_cdltakuri"
    df[cdltakuri_col_name] = cdltakuri
    return df

