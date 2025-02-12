import pandas as pd
import talib as ta

def cdlkickingbylength(df, coin_symbol, interval):
    cdlkickingbylength = ta.CDLKICKINGBYLENGTH(df['open'], df['high'], df['low'], df['close'])
    cdlkickingbylength_col_name = coin_symbol + "_" + interval + "_cdlkickingbylength"
    df[cdlkickingbylength_col_name] = cdlkickingbylength
    return df

