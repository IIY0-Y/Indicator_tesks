import pandas as pd
import talib as ta

def cdlmorningdojistar(df, coin_symbol, interval, penetration=0):
    cdlmorningdojistar = ta.CDLMORNINGDOJISTAR(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdlmorningdojistar_col_name = coin_symbol + "_" + interval + "_cdlmorningdojistar_" + str(penetration).replace(".", "dot")
    df[cdlmorningdojistar_col_name] = cdlmorningdojistar
    return df

