import pandas as pd
import talib as ta

def mom(df, col, coin_symbol, interval, is_price, timeperiod=10):
    if is_price:
        mom_col_name = coin_symbol + "_" + interval + "_mom_" + str(timeperiod)
    else:
        mom_col_name = col + "_mom_" + str(timeperiod)
    mom = ta.MOM(df[col], timeperiod=timeperiod)
    df[mom_col_name] = mom
    df=df.dropna()
    return df

