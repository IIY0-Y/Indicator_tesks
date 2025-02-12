import pandas as pd
import talib as ta

def cdlthrusting(df, coin_symbol, interval):
    cdlthrusting = ta.CDLTHRUSTING(df['open'], df['high'], df['low'], df['close'])
    cdlthrusting_col_name = coin_symbol + "_" + interval + "_cdlthrusting"
    df[cdlthrusting_col_name] = cdlthrusting
    return df

