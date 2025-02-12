import pandas as pd
import talib as ta

def roc(df, col, coin_symbol, interval, is_price, timeperiod=10):
    if is_price:
        roc_col_name = coin_symbol + "_" + interval + "_roc_" + str(timeperiod)
    else:
        roc_col_name = col + "_roc_" + str(timeperiod)
    roc = ta.ROC(df[col], timeperiod=timeperiod)
    df[roc_col_name] = roc
    df=df.dropna()
    return df

