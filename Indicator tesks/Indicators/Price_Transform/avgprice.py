import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Price Transform",
    "indicator_name": "AVGPRICE",
    "indicator_payload": "",
    "indicator_input_col": {
        "0": "open",
        "1": "high",
        "2": "low",
        "3": "close"
    },
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def avgprice(df, coin_symbol, interval):
    avgprice = ta.AVGPRICE(df['open'], df['high'], df['low'], df['close'])
    avgprice_col_name = coin_symbol + "_" + interval + "_avgprice"
    df[avgprice_col_name] = avgprice
    return df

