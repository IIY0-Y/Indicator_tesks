import pandas as pd
import talib as ta

def cdlmathold(df, coin_symbol, interval, penetration=0):
    cdlmathold = ta.CDLMATHOLD(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdlmathold_col_name = coin_symbol + "_" + interval + "_cdlmathold_" + str(penetration).replace(".", "dot")
    df[cdlmathold_col_name] = cdlmathold
    return df

