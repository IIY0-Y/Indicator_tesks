import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Momentum Indicators",
    "indicator_name": "ROCR",
    "indicator_payload": "'timeperiod': 10",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "11"
}

def rocr(df, col, coin_symbol, interval, is_price, timeperiod=10):
    if is_price:
        rocr_col_name = coin_symbol + "_" + interval + "_rocr_" + str(timeperiod)
    else:
        rocr_col_name = col + "_rocr_" + str(timeperiod)
    rocr = ta.ROCR(df[col], timeperiod=timeperiod)
    df[rocr_col_name] = rocr
    df=df.dropna()
    return df

