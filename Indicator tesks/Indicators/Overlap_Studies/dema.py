import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "DEMA",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def dema(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        dema_col_name = coin_symbol + "_" + interval + "_dema_" + str(timeperiod)
    else:
        dema_col_name = col + "_dema_" + str(timeperiod)
    dema = ta.DEMA(df[col], timeperiod=timeperiod)
    df[dema_col_name] = dema
    df=df.dropna()
    return df

