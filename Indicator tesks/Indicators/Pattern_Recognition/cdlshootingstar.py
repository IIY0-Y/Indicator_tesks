import pandas as pd
import talib as ta

def cdlshootingstar(df, coin_symbol, interval):
    cdlshootingstar = ta.CDLSHOOTINGSTAR(df['open'], df['high'], df['low'], df['close'])
    cdlshootingstar_col_name = coin_symbol + "_" + interval + "_cdlshootingstar"
    df[cdlshootingstar_col_name] = cdlshootingstar
    return df

