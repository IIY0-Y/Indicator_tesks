import pandas as pd
import talib as ta

def rocr100(df, col, coin_symbol, interval, is_price, timeperiod=10):
    if is_price:
        rocr100_col_name = coin_symbol + "_" + interval + "_rocr100_" + str(timeperiod)
    else:
        rocr100_col_name = col + "_rocr100_" + str(timeperiod)
    rocr100 = ta.ROCR100(df[col], timeperiod=timeperiod)
    df[rocr100_col_name] = rocr100
    df=df.dropna()
    return df

