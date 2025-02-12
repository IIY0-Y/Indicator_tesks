import pandas as pd
import talib as ta

def cdldragonflydoji(df, coin_symbol, interval):
    cdldragonflydoji = ta.CDLDRAGONFLYDOJI(df['open'], df['high'], df['low'], df['close'])
    cdldragonflydoji_col_name = coin_symbol + "_" + interval + "_cdldragonflydoji"
    df[cdldragonflydoji_col_name] = cdldragonflydoji
    return df

