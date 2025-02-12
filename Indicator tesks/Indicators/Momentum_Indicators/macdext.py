import pandas as pd
import talib as ta

def macdext(df, col, coin_symbol, interval, is_price, fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0):
    macdext = ta.MACDEXT(df[col], fastperiod=fastperiod, fastmatype=fastmatype, slowperiod=slowperiod, slowmatype=slowmatype, signalperiod=signalperiod, signalmatype=signalmatype)
    if is_price:
        macd_col_name = coin_symbol + "_" + interval + "_macd_" + str(fastperiod) + "_" + str(fastmatype) + "_" + str(slowperiod) + "_" + str(slowmatype) + "_" + str(signalperiod) + "_" + str(signalmatype)
        macdsignal_col_name = coin_symbol + "_" + interval + "_macdsignal_" + str(fastperiod) + "_" + str(fastmatype) + "_" + str(slowperiod) + "_" + str(slowmatype) + "_" + str(signalperiod) + "_" + str(signalmatype)
        macdhist_col_name = coin_symbol + "_" + interval + "_macdhist_" + str(fastperiod) + "_" + str(fastmatype) + "_" + str(slowperiod) + "_" + str(slowmatype) + "_" + str(signalperiod) + "_" + str(signalmatype)
    else:
        macd_col_name = col + "_macd_" + str(fastperiod) + "_" + str(fastmatype) + "_" + str(slowperiod) + "_" + str(slowmatype) + "_" + str(signalperiod) + "_" + str(signalmatype)
        macdsignal_col_name = col + "_macdsignal_" + str(fastperiod) + "_" + str(fastmatype) + "_" + str(slowperiod) + "_" + str(slowmatype) + "_" + str(signalperiod) + "_" + str(signalmatype)
        macdhist_col_name = col + "_macdhist_" + str(fastperiod) + "_" + str(fastmatype) + "_" + str(slowperiod) + "_" + str(slowmatype) + "_" + str(signalperiod) + "_" + str(signalmatype)
    cols = [macd_col_name, macdsignal_col_name, macdhist_col_name]
    for i, c in enumerate(cols):
        df[c] = macdext[i]
    df=df.dropna()
    return df

