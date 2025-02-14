import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLDARKCLOUDCOVER",
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

def cdldarkcloudcover(df, coin_symbol, interval, penetration=0):
    cdldarkcloudcover = ta.CDLDARKCLOUDCOVER(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdldarkcloudcover_col_name = coin_symbol + "_" + interval + "_cdldarkcloudcover_" + str(penetration).replace(".", "dot")
    df[cdldarkcloudcover_col_name] = cdldarkcloudcover
    return df

