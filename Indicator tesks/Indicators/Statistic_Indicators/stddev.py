import pandas as pd
import talib as ta

def stddev(df, col, coin_symbol, interval, is_price, timeperiod=5, nbdev=1):
    if is_price:
        stddev_col_name = coin_symbol + "_" + interval + "_stddev_" + str(timeperiod) + "_" + str(nbdev)
    else:
        stddev_col_name = col + "_stddev_" + str(timeperiod) + "_" + str(nbdev)
    stddev = ta.STDDEV(df[col], timeperiod=timeperiod, nbdev=nbdev)
    df[stddev_col_name] = stddev
    df=df.dropna()
    return df

