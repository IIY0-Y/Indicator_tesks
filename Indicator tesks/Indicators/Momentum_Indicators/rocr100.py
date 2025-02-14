import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Momentum Indicators",
    "indicator_name": "ROCR100",
    "indicator_payload": "'timeperiod': 10",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "11"
}

def rocr100(df, col, coin_symbol, interval, is_price, timeperiod=10):
    if is_price:
        rocr100_col_name = coin_symbol + "_" + interval + "_rocr100_" + str(timeperiod)
    else:
        rocr100_col_name = col + "_rocr100_" + str(timeperiod)
    rocr100 = ta.ROCR100(df[col], timeperiod=timeperiod)
    df[rocr100_col_name] = rocr100
    df=df.dropna()
    return df

