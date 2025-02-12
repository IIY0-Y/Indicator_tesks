import pandas as pd
import talib as ta

def var(df, col, coin_symbol, interval, is_price, timeperiod=5, nbdev=1):
    if is_price:
        var_col_name = coin_symbol + "_" + interval + "_var_" + str(timeperiod) + "_" + str(nbdev)
    else:
        var_col_name = col + "_var_" + str(timeperiod) + "_" + str(nbdev)
    var = ta.VAR(df[col], timeperiod=timeperiod, nbdev=nbdev)
    df[var_col_name] = var
    df=df.dropna()
    return df

