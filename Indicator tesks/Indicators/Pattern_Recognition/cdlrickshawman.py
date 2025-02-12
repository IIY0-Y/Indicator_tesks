import pandas as pd
import talib as ta

def cdlrickshawman(df, coin_symbol, interval):
    cdlrickshawman = ta.CDLRICKSHAWMAN(df['open'], df['high'], df['low'], df['close'])
    cdlrickshawman_col_name = coin_symbol + "_" + interval + "_cdlrickshawman"
    df[cdlrickshawman_col_name] = cdlrickshawman
    return df

