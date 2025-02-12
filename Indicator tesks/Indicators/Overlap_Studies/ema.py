import pandas as pd
import talib as ta

def ema(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        ema_col_name = coin_symbol + "_" + interval + "_ema_" + str(timeperiod)
    else:
        ema_col_name = col + "_ema_" + str(timeperiod)
    ema = ta.EMA(df[col], timeperiod=timeperiod)
    df[ema_col_name] = ema
    df=df.dropna()
    return df

