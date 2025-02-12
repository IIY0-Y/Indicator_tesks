import pandas as pd
import talib as ta

def cdlgravestonedoji(df, coin_symbol, interval):
    cdlgravestonedoji = ta.CDLGRAVESTONEDOJI(df['open'], df['high'], df['low'], df['close'])
    cdlgravestonedoji_col_name = coin_symbol + "_" + interval + "_cdlgravestonedoji"
    df[cdlgravestonedoji_col_name] = cdlgravestonedoji
    return df

