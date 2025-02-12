import pandas as pd
import talib as ta

def cdlstalledpattern(df, coin_symbol, interval):
    cdlstalledpattern = ta.CDLSTALLEDPATTERN(df['open'], df['high'], df['low'], df['close'])
    cdlstalledpattern_col_name = coin_symbol + "_" + interval + "_cdlstalledpattern"
    df[cdlstalledpattern_col_name] = cdlstalledpattern
    return df

