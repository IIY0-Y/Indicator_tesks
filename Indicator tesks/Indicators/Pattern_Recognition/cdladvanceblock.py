import pandas as pd
import talib as ta

def cdladvanceblock(df, coin_symbol, interval):
    cdladvanceblock = ta.CDLADVANCEBLOCK(df['open'], df['high'], df['low'], df['close'])
    cdladvanceblock_col_name = coin_symbol + "_" + interval + "_cdladvanceblock"
    df[cdladvanceblock_col_name] = cdladvanceblock
    return df

