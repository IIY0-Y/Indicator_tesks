import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "TRIMA",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def trima(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        trima_col_name = coin_symbol + "_" + interval + "_trima_" + str(timeperiod)
    else:
        trima_col_name = col + "_trima_" + str(timeperiod)
    trima = ta.TRIMA(df[col], timeperiod=timeperiod)
    df[trima_col_name] = trima
    df=df.dropna()
    return df

