import pandas as pd
import talib as ta

def cdleveningdojistar(df, coin_symbol, interval, penetration=0):
    cdleveningdojistar = ta.CDLEVENINGDOJISTAR(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdleveningdojistar_col_name = coin_symbol + "_" + interval + "_cdleveningdojistar_" + str(penetration).replace(".", "dot")
    df[cdleveningdojistar_col_name] = cdleveningdojistar
    return df

