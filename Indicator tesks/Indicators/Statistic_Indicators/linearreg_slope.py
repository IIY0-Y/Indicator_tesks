import pandas as pd
import talib as ta

def linearreg_slope(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        linearreg_slope_col_name = coin_symbol + "_" + interval + "_linearreg_slope_" + str(timeperiod)
    else:
        linearreg_slope_col_name = col + "_linearreg_slope_" + str(timeperiod)
    linearreg_slope = ta.LINEARREG_SLOPE(df[col], timeperiod=timeperiod)
    df[linearreg_slope_col_name] = linearreg_slope
    df=df.dropna()
    return df

