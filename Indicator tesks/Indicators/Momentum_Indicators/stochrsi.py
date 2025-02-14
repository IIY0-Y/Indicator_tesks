import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Momentum Indicators",
    "indicator_name": "STOCHRSI",
    "indicator_payload": {
        "timeperiod": 14,
        "fastk_period": 5,
        "fastd_period": 3,
        "fastd_matype": 0
    },
    "indicator_input_col": "real",
    "indicator_return_col": {
        "0": "fastk",
        "1": "fastd"
    },
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "nn"
}

def stochrsi(df, col, coin_symbol, interval, is_price, timeperiod=14, fastk_period=5, fastd_period=3, fastd_matype=0):
    stochrsi = ta.STOCHRSI(df[col], timeperiod=timeperiod, fastk_period=fastk_period, fastd_period=fastd_period, fastd_matype=fastd_matype)
    if is_price:
        fastk_col_name = coin_symbol + "_" + interval + "_fastk_" + str(timeperiod) + "_" + str(fastk_period) + "_" + str(fastd_period) + "_" + str(fastd_matype)
        fastd_col_name = coin_symbol + "_" + interval + "_fastd_" + str(timeperiod) + "_" + str(fastk_period) + "_" + str(fastd_period) + "_" + str(fastd_matype)
    else:
        fastk_col_name = col + "_fastk_" + str(timeperiod) + "_" + str(fastk_period) + "_" + str(fastd_period) + "_" + str(fastd_matype)
        fastd_col_name = col + "_fastd_" + str(timeperiod) + "_" + str(fastk_period) + "_" + str(fastd_period) + "_" + str(fastd_matype)
    cols = [fastk_col_name, fastd_col_name]
    for i, c in enumerate(cols):
        df[c] = stochrsi[i]
    df=df.dropna()
    return df

