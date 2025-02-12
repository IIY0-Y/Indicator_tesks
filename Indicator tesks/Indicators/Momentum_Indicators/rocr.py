import pandas as pd
import talib as ta

def rocr(df, col, coin_symbol, interval, is_price, timeperiod=10):
    if is_price:
        rocr_col_name = coin_symbol + "_" + interval + "_rocr_" + str(timeperiod)
    else:
        rocr_col_name = col + "_rocr_" + str(timeperiod)
    rocr = ta.ROCR(df[col], timeperiod=timeperiod)
    df[rocr_col_name] = rocr
    df=df.dropna()
    return df

