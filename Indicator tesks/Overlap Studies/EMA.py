import talib as ta
import pandas as pd

class Ema:
    def __init__(self):
        pass

    def run(self, df, col, coin_symbol, interval, is_price, timeperiod=14):
        if is_price:
            ema_col_name = f"{coin_symbol}_{interval}_ema_{timeperiod}"
        else:
            ema_col_name = f"{col}_ema_{timeperiod}"

        df[ema_col_name] = ta.EMA(df[col], timeperiod=timeperiod)
        df = df.dropna()
        
        return df
