import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Statistic Functions",
    "indicator_name": "LINEARREG",
    "indicator_payload": "'timeperiod': 14",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def linearreg(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        linearreg_col_name = coin_symbol + "_" + interval + "_linearreg_" + str(timeperiod)
    else:
        linearreg_col_name = col + "_linearreg_" + str(timeperiod)
    linearreg = ta.LINEARREG(df[col], timeperiod=timeperiod)
    df[linearreg_col_name] = linearreg
    df=df.dropna()
    return df

