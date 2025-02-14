import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Pattern Recognition",
    "indicator_name": "CDLUPSIDEGAP2CROWS",
    "indicator_payload": "",
    "indicator_input_col": {
        "0": "open",
        "1": "high",
        "2": "low",
        "3": "close"
    },
    "indicator_return_col": "integer",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def cdlupsidegap2crows(df, coin_symbol, interval):
    cdlupsidegap2crows = ta.CDLUPSIDEGAP2CROWS(df['open'], df['high'], df['low'], df['close'])
    cdlupsidegap2crows_col_name = coin_symbol + "_" + interval + "_cdlupsidegap2crows"
    df[cdlupsidegap2crows_col_name] = cdlupsidegap2crows
    return df

