import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLMATHOLD",
    "indicator_payload": "'penetration': 0",
    "indicator_input_col": {
        "0": "open",
        "1": "high",
        "2": "low",
        "3": "close"
    },
    "indicator_return_col": "integer",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "11"
}

def cdlmathold(df, coin_symbol, interval, penetration=0):
    cdlmathold = ta.CDLMATHOLD(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdlmathold_col_name = coin_symbol + "_" + interval + "_cdlmathold_" + str(penetration).replace(".", "dot")
    df[cdlmathold_col_name] = cdlmathold
    return df

