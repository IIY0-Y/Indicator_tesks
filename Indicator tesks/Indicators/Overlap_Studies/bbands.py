import talib as ta
import pandas as pd
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "BBANDS",
    "indicator_payload": {
        "timeperiod": 5,
        "nbdevup": 2,
        "nbdevdn": 2,
        "matype": 0
    },
    "indicator_input_col": "real",
    "indicator_return_col": {
        "0": "upperband",
        "1": "middleband",
        "2": "lowerband"
    },
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "nn"
}

class Bbands:
    def __init__(self):
        pass

    def run(self, df, col, coin_symbol, interval, is_price, timeperiod=14, nbdevup=2, nbdevdn=2, matype=0):
        if is_price:
            bbands_col_base = f"{coin_symbol}_{interval}_bbands_{timeperiod}"
        else:
            bbands_col_base = f"{col}_bbands_{timeperiod}"

        upper, middle, lower = ta.BBANDS(df[col], timeperiod=timeperiod, nbdevup=nbdevup, nbdevdn=nbdevdn, matype=matype)
        
        df[f"{bbands_col_base}_upper"] = upper
        df[f"{bbands_col_base}_middle"] = middle
        df[f"{bbands_col_base}_lower"] = lower
        df = df.dropna()
        
        return df

