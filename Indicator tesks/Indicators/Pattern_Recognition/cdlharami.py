import pandas as pd
import talib as ta

def cdlharami(df, coin_symbol, interval):
    cdlharami = ta.CDLHARAMI(df['open'], df['high'], df['low'], df['close'])
    cdlharami_col_name = coin_symbol + "_" + interval + "_cdlharami"
    df[cdlharami_col_name] = cdlharami
    return df

