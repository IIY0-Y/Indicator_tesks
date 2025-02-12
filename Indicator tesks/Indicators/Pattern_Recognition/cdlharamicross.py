import pandas as pd
import talib as ta

def cdlharamicross(df, coin_symbol, interval):
    cdlharamicross = ta.CDLHARAMICROSS(df['open'], df['high'], df['low'], df['close'])
    cdlharamicross_col_name = coin_symbol + "_" + interval + "_cdlharamicross"
    df[cdlharamicross_col_name] = cdlharamicross
    return df

