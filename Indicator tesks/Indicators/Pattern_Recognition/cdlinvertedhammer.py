import pandas as pd
import talib as ta

def cdlinvertedhammer(df, coin_symbol, interval):
    cdlinvertedhammer = ta.CDLINVERTEDHAMMER(df['open'], df['high'], df['low'], df['close'])
    cdlinvertedhammer_col_name = coin_symbol + "_" + interval + "_cdlinvertedhammer"
    df[cdlinvertedhammer_col_name] = cdlinvertedhammer
    return df

