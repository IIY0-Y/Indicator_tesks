import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "TEMA",
    "indicator_payload": "'timeperiod': 30",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def tema(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        tema_col_name = coin_symbol + "_" + interval + "_tema_" + str(timeperiod)
    else:
        tema_col_name = col + "_tema_" + str(timeperiod)
    tema = ta.TEMA(df[col], timeperiod=timeperiod)
    df[tema_col_name] = tema
    df=df.dropna()
    return df

