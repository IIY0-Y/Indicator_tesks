import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLEVENINGDOJISTAR",
    "indicator_payload": "'penetration': 0",
    "indicator_input_col": {
        "0": "open",
        "1": "high",
        "2": "low",
        "3": "close"
    },
    "indicator_return_col": "integer",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "11"
}

def cdleveningdojistar(df, coin_symbol, interval, penetration=0):
    cdleveningdojistar = ta.CDLEVENINGDOJISTAR(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdleveningdojistar_col_name = coin_symbol + "_" + interval + "_cdleveningdojistar_" + str(penetration).replace(".", "dot")
    df[cdleveningdojistar_col_name] = cdleveningdojistar
    return df

