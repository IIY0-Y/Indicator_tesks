# indicators/price/sma.py
import pandas as pd
import talib as ta



CONFIG = {
    "indicator_class": "Overlap Studies",      
    "indicator_name": "SMA",                   
    "indicator_payload": {                           
        "timeperiod": 30
    },
    "indicator_input_col": "real",                      
    "indicator_return_col": "real",                     
    "chart_area": "overlays",                  
    "chart_type": "line",                                  
    "indicator_type": "simple",                      
    "ind_type": 11     
    #  "ind_type": 01 , 0n , 11 , 1n , n1 , nn  The first one refers to the input parameter, and the second one refers to the output parameter. For example, if there is one input and one output, then it is 11.
                      
}

class Sma:
    def __init__(self):
        pass
    @staticmethod
    def run(df, col, coin_symbol, interval, is_price, timeperiod=30):
      

        if is_price:
            sma_col_name = f"{coin_symbol}_{interval}_sma_{timeperiod}"
        else:
            sma_col_name = f"{col}_sma_{timeperiod}"

     
        df[sma_col_name] = ta.SMA(df[col], timeperiod=timeperiod)


        df = df.dropna()

        return df
    
