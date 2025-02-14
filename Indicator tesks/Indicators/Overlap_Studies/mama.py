import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "MAMA",
    "indicator_payload": {
        "fastlimit": 0,
        "slowlimit": 0
    },
    "indicator_input_col": "real",
    "indicator_return_col": {
        "0": "mama",
        "1": "fama"
    },
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "nn"
}

def mama(df, col, coin_symbol, interval, is_price, fastlimit=0, slowlimit=0):
    mama = ta.MAMA(df[col], fastlimit=fastlimit, slowlimit=slowlimit)
    if is_price:
        mama_col_name = coin_symbol + "_" + interval + "_mama_" + str(fastlimit).replace(".", "dot") + "_" + str(slowlimit).replace(".", "dot")
        fama_col_name = coin_symbol + "_" + interval + "_fama_" + str(fastlimit).replace(".", "dot") + "_" + str(slowlimit).replace(".", "dot")
    else:
        mama_col_name = col + "_mama_" + str(fastlimit).replace(".", "dot") + "_" + str(slowlimit).replace(".", "dot")
        fama_col_name = col + "_fama_" + str(fastlimit).replace(".", "dot") + "_" + str(slowlimit).replace(".", "dot")
    
    cols = [mama_col_name, fama_col_name]
    for i, c in enumerate(cols):
        df[c] = mama[i]
        first_non_nan_value = df[c].dropna().iloc[0]
        df[c] = df[c].fillna(first_non_nan_value)
    return df

