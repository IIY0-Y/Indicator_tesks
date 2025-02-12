import pandas as pd
import talib as ta

def cdlshortline(df, coin_symbol, interval):
    cdlshortline = ta.CDLSHORTLINE(df['open'], df['high'], df['low'], df['close'])
    cdlshortline_col_name = coin_symbol + "_" + interval + "_cdlshortline"
    df[cdlshortline_col_name] = cdlshortline
    return df

