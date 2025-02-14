import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Cycle Indicators",
    "indicator_name": "HT_DCPHASE",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "1"
}

def ht_dcphase(df, col, coin_symbol, interval, is_price):
    if is_price:
        ht_dcphase_col_name = coin_symbol + "_" + interval + "_ht_dcphase"
    else:
        ht_dcphase_col_name = col + "_ht_dcphase"
    ht_dcphase = ta.HT_DCPHASE(df[col])
    df[ht_dcphase_col_name] = ht_dcphase
    df=df.dropna()
    return df

