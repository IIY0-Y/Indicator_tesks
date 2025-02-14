import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "WMA",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def wma(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        wma_col_name = coin_symbol + "_" + interval + "_wma_" + str(timeperiod)
    else:
        wma_col_name = col + "_wma_" + str(timeperiod)
    wma = ta.WMA(df[col], timeperiod=timeperiod)
    df[wma_col_name] = wma
    df=df.dropna()
    return df

