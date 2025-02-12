import pandas as pd
import talib as ta

def cdlcounterattack(df, coin_symbol, interval):
    cdlcounterattack = ta.CDLCOUNTERATTACK(df['open'], df['high'], df['low'], df['close'])
    cdlcounterattack_col_name = coin_symbol + "_" + interval + "_cdlcounterattack"
    df[cdlcounterattack_col_name] = cdlcounterattack
    return df

