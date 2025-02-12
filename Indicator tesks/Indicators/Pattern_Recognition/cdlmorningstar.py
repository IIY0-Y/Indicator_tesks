import pandas as pd
import talib as ta

def cdlmorningstar(df, coin_symbol, interval, penetration=0):
    cdlmorningstar = ta.CDLMORNINGSTAR(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdlmorningstar_col_name = coin_symbol + "_" + interval + "_cdlmorningstar_" + str(penetration).replace(".", "dot")
    df[cdlmorningstar_col_name] = cdlmorningstar
    return df

