import pandas as pd
import talib as ta

def cdlxsidegap3methods(df, coin_symbol, interval):
    cdlxsidegap3methods = ta.CDLXSIDEGAP3METHODS(df['open'], df['high'], df['low'], df['close'])
    cdlxsidegap3methods_col_name = coin_symbol + "_" + interval + "_cdlxsidegap3methods"
    df[cdlxsidegap3methods_col_name] = cdlxsidegap3methods
    return df

