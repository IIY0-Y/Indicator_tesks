import pandas as pd
import talib as ta

def cdlhomingpigeon(df, coin_symbol, interval):
    cdlhomingpigeon = ta.CDLHOMINGPIGEON(df['open'], df['high'], df['low'], df['close'])
    cdlhomingpigeon_col_name = coin_symbol + "_" + interval + "_cdlhomingpigeon"
    df[cdlhomingpigeon_col_name] = cdlhomingpigeon
    return df

