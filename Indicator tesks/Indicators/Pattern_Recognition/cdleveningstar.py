import pandas as pd
import talib as ta

def cdleveningstar(df, coin_symbol, interval, penetration=0):
    cdleveningstar = ta.CDLEVENINGSTAR(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdleveningstar_col_name = coin_symbol + "_" + interval + "_cdleveningstar_" + str(penetration).replace(".", "dot")
    df[cdleveningstar_col_name] = cdleveningstar
    return df

