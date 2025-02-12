import pandas as pd
import talib as ta

def avgprice(df, coin_symbol, interval):
    avgprice = ta.AVGPRICE(df['open'], df['high'], df['low'], df['close'])
    avgprice_col_name = coin_symbol + "_" + interval + "_avgprice"
    df[avgprice_col_name] = avgprice
    return df

