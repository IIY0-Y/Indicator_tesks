import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "KAMA",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def kama(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        kama_col_name = coin_symbol + "_" + interval + "_kama_" + str(timeperiod)
    else:
        kama_col_name = col + "_kama_" + str(timeperiod)
    kama = ta.KAMA(df[col], timeperiod=timeperiod)
    df[kama_col_name] = kama
    df=df.dropna()
    return df

