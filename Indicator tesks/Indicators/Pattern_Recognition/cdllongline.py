import pandas as pd
import talib as ta

def cdllongline(df, coin_symbol, interval):
    cdllongline = ta.CDLLONGLINE(df['open'], df['high'], df['low'], df['close'])
    cdllongline_col_name = coin_symbol + "_" + interval + "_cdllongline"
    df[cdllongline_col_name] = cdllongline
    return df

