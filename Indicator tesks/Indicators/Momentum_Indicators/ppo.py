import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Momentum Indicators",
    "indicator_name": "PPO",
    "indicator_payload": {
        "fastperiod": 12,
        "slowperiod": 26,
        "matype": 0
    },
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "Oscillators",
    "chart_type": "line",
    "ind_type": "n1"
}

def ppo(df, col, coin_symbol, interval, is_price, fastperiod=12, slowperiod=26, matype=0):
    if is_price:
        ppo_col_name = coin_symbol + "_" + interval + "_ppo_" + str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(matype)
    else:
        ppo_col_name = col + "_ppo_" + str(fastperiod) + "_" + str(slowperiod) + "_" + str(matype)
    ppo = ta.PPO(df[col], fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
    df[ppo_col_name] = ppo
    df=df.dropna()
    return df

