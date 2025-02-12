import talib as ta
import pandas as df

class Rsi:
    def __init__(self):
        pass

    @staticmethod
    def run(df, col, coin_symbol, interval, is_price, timeperiod=14):
        if is_price:
            rsi_col_name = f"{coin_symbol}_{interval}_rsi_{timeperiod}"
        else:
            rsi_col_name = f"{col}_rsi_{timeperiod}"

        df[rsi_col_name] = ta.RSI(df[col], timeperiod=timeperiod)
        df = df.dropna()
        
        return df
