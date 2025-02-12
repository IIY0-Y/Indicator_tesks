import pandas as pd
import talib as ta

def rsi(df, col, coin_symbol, interval, is_price, timeperiod=14):
    if is_price:
        rsi_col_name = coin_symbol + "_" + interval + "_rsi_" + str(timeperiod).replace(".","dot")
    else:
        rsi_col_name = col + "_rsi_" + str(timeperiod)
    rsi = ta.RSI(df[col], timeperiod=timeperiod)
    df[rsi_col_name] = rsi
    df=df.dropna()
    return df

