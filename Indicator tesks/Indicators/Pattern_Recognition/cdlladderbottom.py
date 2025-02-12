import pandas as pd
import talib as ta

def cdlladderbottom(df, coin_symbol, interval):
    cdlladderbottom = ta.CDLLADDERBOTTOM(df['open'], df['high'], df['low'], df['close'])
    cdlladderbottom_col_name = coin_symbol + "_" + interval + "_cdlladderbottom"
    df[cdlladderbottom_col_name] = cdlladderbottom
    return df

