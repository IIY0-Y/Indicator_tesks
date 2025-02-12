import pandas as pd
import talib as ta

def linearreg_intercept(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        linearreg_intercept_col_name = coin_symbol + "_" + interval + "_linearreg_intercept_" + str(timeperiod)
    else:
        linearreg_intercept_col_name = col + "_linearreg_intercept_" + str(timeperiod)
    linearreg_intercept = ta.LINEARREG_INTERCEPT(df[col], timeperiod=timeperiod)
    df[linearreg_intercept_col_name] = linearreg_intercept
    df=df.dropna()
    return df

