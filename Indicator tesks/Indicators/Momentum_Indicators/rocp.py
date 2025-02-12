import pandas as pd
import talib as ta

def rocp(df, col, coin_symbol, interval, is_price, timeperiod=10):
    if is_price:
        rocp_col_name = coin_symbol + "_" + interval + "_rocp_" + str(timeperiod)
    else:
        rocp_col_name = col + "_rocp_" + str(timeperiod)
    rocp = ta.ROCP(df[col], timeperiod=timeperiod)
    df[rocp_col_name] = rocp
    df=df.dropna()
    return df

