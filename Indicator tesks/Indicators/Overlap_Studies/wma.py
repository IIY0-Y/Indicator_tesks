import pandas as pd
import talib as ta

def wma(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        wma_col_name = coin_symbol + "_" + interval + "_wma_" + str(timeperiod)
    else:
        wma_col_name = col + "_wma_" + str(timeperiod)
    wma = ta.WMA(df[col], timeperiod=timeperiod)
    df[wma_col_name] = wma
    df=df.dropna()
    return df

