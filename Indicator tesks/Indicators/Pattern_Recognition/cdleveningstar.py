import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLEVENINGSTAR",
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

def cdleveningstar(df, coin_symbol, interval, penetration=0):
    cdleveningstar = ta.CDLEVENINGSTAR(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdleveningstar_col_name = coin_symbol + "_" + interval + "_cdleveningstar_" + str(penetration).replace(".", "dot")
    df[cdleveningstar_col_name] = cdleveningstar
    return df

