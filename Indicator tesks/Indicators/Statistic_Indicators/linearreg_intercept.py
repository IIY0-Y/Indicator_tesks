import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Statistic Functions",
    "indicator_name": "LINEARREG_INTERCEPT",
    "indicator_payload": "'timeperiod': 14",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "11"
}

def linearreg_intercept(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        linearreg_intercept_col_name = coin_symbol + "_" + interval + "_linearreg_intercept_" + str(timeperiod)
    else:
        linearreg_intercept_col_name = col + "_linearreg_intercept_" + str(timeperiod)
    linearreg_intercept = ta.LINEARREG_INTERCEPT(df[col], timeperiod=timeperiod)
    df[linearreg_intercept_col_name] = linearreg_intercept
    df=df.dropna()
    return df

