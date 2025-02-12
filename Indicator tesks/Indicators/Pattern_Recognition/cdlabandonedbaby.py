import pandas as pd
import talib as ta

def cdlabandonedbaby(df, coin_symbol, interval, penetration=0):
    cdlabandonedbaby = ta.CDLABANDONEDBABY(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdlabandonedbaby_col_name = coin_symbol + "_" + interval + "_cdlabandonedbaby_" + str(penetration).replace(".", "dot")
    df[cdlabandonedbaby_col_name] = cdlabandonedbaby
    return df

