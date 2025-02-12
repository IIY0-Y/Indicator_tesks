import pandas as pd
import talib as ta

def cdlseparatinglines(df, coin_symbol, interval):
    cdlseparatinglines = ta.CDLSEPARATINGLINES(df['open'], df['high'], df['low'], df['close'])
    cdlseparatinglines_col_name = coin_symbol + "_" + interval + "_cdlseparatinglines"
    df[cdlseparatinglines_col_name] = cdlseparatinglines
    return df

