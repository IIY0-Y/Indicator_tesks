import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "EMA",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def ema(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        ema_col_name = coin_symbol + "_" + interval + "_ema_" + str(timeperiod)
    else:
        ema_col_name = col + "_ema_" + str(timeperiod)
    ema = ta.EMA(df[col], timeperiod=timeperiod)
    df[ema_col_name] = ema
    df=df.dropna()
    return df

