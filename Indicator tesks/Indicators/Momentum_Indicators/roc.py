import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Momentum Indicators",
    "indicator_name": "ROC",
    "indicator_payload": "'timeperiod': 10",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "11"
}

def roc(df, col, coin_symbol, interval, is_price, timeperiod=10):
    if is_price:
        roc_col_name = coin_symbol + "_" + interval + "_roc_" + str(timeperiod)
    else:
        roc_col_name = col + "_roc_" + str(timeperiod)
    roc = ta.ROC(df[col], timeperiod=timeperiod)
    df[roc_col_name] = roc
    df=df.dropna()
    return df

