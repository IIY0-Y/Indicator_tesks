import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Statistic Functions",
    "indicator_name": "TSF",
    "indicator_payload": "'timeperiod': 14",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "11"
}

def tsf(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        tsf_col_name = coin_symbol + "_" + interval + "_tsf_" + str(timeperiod)
    else:
        tsf_col_name = col + "_tsf_" + str(timeperiod)
    tsf = ta.TSF(df[col], timeperiod=timeperiod)
    df[tsf_col_name] = tsf
    df=df.dropna()
    return df

