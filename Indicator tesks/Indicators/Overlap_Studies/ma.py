import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "MA",
    "indicator_payload": {
        "timeperiod": 30,
        "matype": 0
    },
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "n1"
}

def ma(df, col, coin_symbol, interval, is_price, timeperiod=30, matype=0):
    if is_price:
        ma_col_name = coin_symbol + "_" + interval + "_ma_" + str(timeperiod) + "_" + str(matype)
    else:
        ma_col_name = col + "_ma_" + str(timeperiod) + "_" + str(matype)
    ma = ta.MA(df[col], timeperiod=timeperiod, matype=matype)
    df[ma_col_name] = ma
    df=df.dropna()
    return df

