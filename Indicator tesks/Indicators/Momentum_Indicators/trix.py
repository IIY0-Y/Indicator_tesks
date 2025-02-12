import pandas as pd
import talib as ta

def trix(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        trix_col_name = coin_symbol + "_" + interval + "_trix_" + str(timeperiod)
    else:
        trix_col_name = col + "_trix_" + str(timeperiod)
    trix = ta.TRIX(df[col], timeperiod=timeperiod)
    df[trix_col_name] = trix
    df=df.dropna()
    return df

