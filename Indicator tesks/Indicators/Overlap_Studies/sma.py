import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "SMA",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def sma(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        sma_col_name = coin_symbol + "_" + interval + "_sma_" + str(timeperiod)
    else:
        sma_col_name = col + "_sma_" + str(timeperiod)
    sma = ta.SMA(df[col], timeperiod=timeperiod)
    df[sma_col_name] = sma
    df=df.dropna()
    return df

