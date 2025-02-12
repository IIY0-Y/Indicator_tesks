import pandas as pd
import talib as ta

def tema(df, col, coin_symbol, interval, is_price, timeperiod=30):
    if is_price:
        tema_col_name = coin_symbol + "_" + interval + "_tema_" + str(timeperiod)
    else:
        tema_col_name = col + "_tema_" + str(timeperiod)
    tema = ta.TEMA(df[col], timeperiod=timeperiod)
    df[tema_col_name] = tema
    df=df.dropna()
    return df

