import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Statistic Functions",
    "indicator_name": "LINEARREG_SLOPE",
    "indicator_payload": "'timeperiod': 14",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "11"
}

def linearreg_slope(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        linearreg_slope_col_name = coin_symbol + "_" + interval + "_linearreg_slope_" + str(timeperiod)
    else:
        linearreg_slope_col_name = col + "_linearreg_slope_" + str(timeperiod)
    linearreg_slope = ta.LINEARREG_SLOPE(df[col], timeperiod=timeperiod)
    df[linearreg_slope_col_name] = linearreg_slope
    df=df.dropna()
    return df

