import talib as ta
import pandas as pd

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
