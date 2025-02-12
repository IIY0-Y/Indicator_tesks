import pandas as pd
import talib as ta

def cdlsticksandwich(df, coin_symbol, interval):
    cdlsticksandwich = ta.CDLSTICKSANDWICH(df['open'], df['high'], df['low'], df['close'])
    cdlsticksandwich_col_name = coin_symbol + "_" + interval + "_cdlsticksandwich"
    df[cdlsticksandwich_col_name] = cdlsticksandwich
    return df

