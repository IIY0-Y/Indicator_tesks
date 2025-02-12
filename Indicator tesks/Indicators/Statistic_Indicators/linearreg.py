import pandas as pd
import talib as ta

def linearreg(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        linearreg_col_name = coin_symbol + "_" + interval + "_linearreg_" + str(timeperiod)
    else:
        linearreg_col_name = col + "_linearreg_" + str(timeperiod)
    linearreg = ta.LINEARREG(df[col], timeperiod=timeperiod)
    df[linearreg_col_name] = linearreg
    df=df.dropna()
    return df

