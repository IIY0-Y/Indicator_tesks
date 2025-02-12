import pandas as pd
import talib as ta

def sum(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        sum_col_name = coin_symbol + "_" + interval + "_sum_" + str(timeperiod)
    else:
        sum_col_name = col + "_sum_" + str(timeperiod)
    sum = ta.SUM(df[col], timeperiod=timeperiod)
    df[sum_col_name] = sum
    df=df.dropna()
    return df

