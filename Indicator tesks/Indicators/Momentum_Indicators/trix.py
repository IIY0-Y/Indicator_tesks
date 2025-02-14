import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Momentum Indicators",
    "indicator_name": "TRIX",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "11"
}

def trix(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        trix_col_name = coin_symbol + "_" + interval + "_trix_" + str(timeperiod)
    else:
        trix_col_name = col + "_trix_" + str(timeperiod)
    trix = ta.TRIX(df[col], timeperiod=timeperiod)
    df[trix_col_name] = trix
    df=df.dropna()
    return df

