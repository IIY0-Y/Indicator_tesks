import pandas as pd
import talib as ta

def ppo(df, col, coin_symbol, interval, is_price, fastperiod=12, slowperiod=26, matype=0):
    if is_price:
        ppo_col_name = coin_symbol + "_" + interval + "_ppo_" + str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(matype)
    else:
        ppo_col_name = col + "_ppo_" + str(fastperiod) + "_" + str(slowperiod) + "_" + str(matype)
    ppo = ta.PPO(df[col], fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
    df[ppo_col_name] = ppo
    df=df.dropna()
    return df

