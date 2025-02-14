import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Statistic Functions",
    "indicator_name": "VAR",
    "indicator_payload": {
        "timeperiod": 5,
        "nbdev": 1
    },
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "n1"
}

def var(df, col, coin_symbol, interval, is_price, timeperiod=5, nbdev=1):
    if is_price:
        var_col_name = coin_symbol + "_" + interval + "_var_" + str(timeperiod) + "_" + str(nbdev)
    else:
        var_col_name = col + "_var_" + str(timeperiod) + "_" + str(nbdev)
    var = ta.VAR(df[col], timeperiod=timeperiod, nbdev=nbdev)
    df[var_col_name] = var
    df=df.dropna()
    return df

