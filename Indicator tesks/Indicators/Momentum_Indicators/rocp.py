import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Momentum Indicators",
    "indicator_name": "ROCP",
    "indicator_payload": "'timeperiod': 10",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "11"
}

def rocp(df, col, coin_symbol, interval, is_price, timeperiod=10):
    if is_price:
        rocp_col_name = coin_symbol + "_" + interval + "_rocp_" + str(timeperiod)
    else:
        rocp_col_name = col + "_rocp_" + str(timeperiod)
    rocp = ta.ROCP(df[col], timeperiod=timeperiod)
    df[rocp_col_name] = rocp
    df=df.dropna()
    return df

