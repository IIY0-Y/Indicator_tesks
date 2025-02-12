import pandas as pd
import talib as ta

def sinh(df, col, coin_symbol, interval, is_price):
    if is_price:
        sinh_col_name = coin_symbol + "_" + interval + "_sinh"
    else:
        sinh_col_name = col + "_sinh"
    sinh = ta.SINH(df[col])
    df[sinh_col_name] = sinh
    df=df.dropna()
    return df

