import pandas as pd
import talib as ta

def cdlbreakaway(df, coin_symbol, interval):
    cdlbreakaway = ta.CDLBREAKAWAY(df['open'], df['high'], df['low'], df['close'])
    cdlbreakaway_col_name = coin_symbol + "_" + interval + "_cdlbreakaway"
    df[cdlbreakaway_col_name] = cdlbreakaway
    return df

