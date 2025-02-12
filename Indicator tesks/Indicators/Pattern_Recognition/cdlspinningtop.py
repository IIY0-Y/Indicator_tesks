import pandas as pd
import talib as ta

def cdlspinningtop(df, coin_symbol, interval):
    cdlspinningtop = ta.CDLSPINNINGTOP(df['open'], df['high'], df['low'], df['close'])
    cdlspinningtop_col_name = coin_symbol + "_" + interval + "_cdlspinningtop"
    df[cdlspinningtop_col_name] = cdlspinningtop
    return df

