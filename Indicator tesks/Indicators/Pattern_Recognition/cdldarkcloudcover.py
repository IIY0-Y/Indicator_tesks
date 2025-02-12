import pandas as pd
import talib as ta

def cdldarkcloudcover(df, coin_symbol, interval, penetration=0):
    cdldarkcloudcover = ta.CDLDARKCLOUDCOVER(df['open'], df['high'], df['low'], df['close'], penetration=penetration)
    cdldarkcloudcover_col_name = coin_symbol + "_" + interval + "_cdldarkcloudcover_" + str(penetration).replace(".", "dot")
    df[cdldarkcloudcover_col_name] = cdldarkcloudcover
    return df

