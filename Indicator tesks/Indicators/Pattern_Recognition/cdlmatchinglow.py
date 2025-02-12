import pandas as pd
import talib as ta

def cdlmatchinglow(df, coin_symbol, interval):
    cdlmatchinglow = ta.CDLMATCHINGLOW(df['open'], df['high'], df['low'], df['close'])
    cdlmatchinglow_col_name = coin_symbol + "_" + interval + "_cdlmatchinglow"
    df[cdlmatchinglow_col_name] = cdlmatchinglow
    return df

