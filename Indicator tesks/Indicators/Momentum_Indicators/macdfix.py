import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Momentum Indicators",
    "indicator_name": "MACDFIX",
    "indicator_payload": "'signalperiod': 9",
    "indicator_input_col": "real",
    "indicator_return_col": {
        "0": "macd",
        "1": "macdsignal",
        "2": "macdhist"
    },
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "1n"
}

def macdfix(df, col, coin_symbol, interval, is_price, signalperiod=9):
    macdfix = ta.MACDFIX(df[col], signalperiod=signalperiod)
    if is_price:
        macd_col_name = coin_symbol + "_" + interval + "_macd_" + str(signalperiod)
        macdsignal_col_name = coin_symbol + "_" + interval + "_macdsignal_" + str(signalperiod)
        macdhist_col_name = coin_symbol + "_" + interval + "_macdhist_" + str(signalperiod)
    else:
        macd_col_name = col + "_macd_" + str(signalperiod)
        macdsignal_col_name = col + "_macdsignal_" + str(signalperiod)
        macdhist_col_name = col + "_macdhist_" + str(signalperiod)
    cols = [macd_col_name, macdsignal_col_name, macdhist_col_name]
    for i, c in enumerate(cols):
        df[c] = macdfix[i]
    df=df.dropna()
    return df

