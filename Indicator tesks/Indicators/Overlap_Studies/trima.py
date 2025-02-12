import pandas as pd
import talib as ta

def trima(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        trima_col_name = coin_symbol + "_" + interval + "_trima_" + str(timeperiod)
    else:
        trima_col_name = col + "_trima_" + str(timeperiod)
    trima = ta.TRIMA(df[col], timeperiod=timeperiod)
    df[trima_col_name] = trima
    df=df.dropna()
    return df

