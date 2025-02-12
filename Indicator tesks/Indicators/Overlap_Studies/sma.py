import pandas as pd
import talib as ta

def sma(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        sma_col_name = coin_symbol + "_" + interval + "_sma_" + str(timeperiod)
    else:
        sma_col_name = col + "_sma_" + str(timeperiod)
    sma = ta.SMA(df[col], timeperiod=timeperiod)
    df[sma_col_name] = sma
    df=df.dropna()
    return df

