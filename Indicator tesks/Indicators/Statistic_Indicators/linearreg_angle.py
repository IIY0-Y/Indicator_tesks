import pandas as pd
import talib as ta

def linearreg_angle(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        linearreg_angle_col_name = coin_symbol + "_" + interval + "_linearreg_angle_" + str(timeperiod)
    else:
        linearreg_angle_col_name = col + "_linearreg_angle_" + str(timeperiod)
    linearreg_angle = ta.LINEARREG_ANGLE(df[col], timeperiod=timeperiod)
    df[linearreg_angle_col_name] = linearreg_angle
    df=df.dropna()
    return df

