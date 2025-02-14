import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Momentum Indicators",
    "indicator_name": "CMO",
    "indicator_payload": "'timeperiod': 14",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "11"
}

def cmo(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        cmo_col_name = coin_symbol + "_" + interval + "_cmo_" + str(timeperiod)
    else:
        cmo_col_name = col + "_cmo_" + str(timeperiod)
    cmo = ta.CMO(df[col], timeperiod=timeperiod)
    df[cmo_col_name] = cmo
    df=df.dropna()
    return df

