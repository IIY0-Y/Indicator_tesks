import pandas as pd
import talib as ta

def cdltasukigap(df, coin_symbol, interval):
    cdltasukigap = ta.CDLTASUKIGAP(df['open'], df['high'], df['low'], df['close'])
    cdltasukigap_col_name = coin_symbol + "_" + interval + "_cdltasukigap"
    df[cdltasukigap_col_name] = cdltasukigap
    return df

