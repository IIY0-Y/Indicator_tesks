import pandas as pd
import talib as ta

def kama(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        kama_col_name = coin_symbol + "_" + interval + "_kama_" + str(timeperiod)
    else:
        kama_col_name = col + "_kama_" + str(timeperiod)
    kama = ta.KAMA(df[col], timeperiod=timeperiod)
    df[kama_col_name] = kama
    df=df.dropna()
    return df
