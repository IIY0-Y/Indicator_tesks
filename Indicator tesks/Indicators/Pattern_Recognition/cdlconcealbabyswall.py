import pandas as pd
import talib as ta

def cdlconcealbabyswall(df, coin_symbol, interval):
    cdlconcealbabyswall = ta.CDLCONCEALBABYSWALL(df['open'], df['high'], df['low'], df['close'])
    cdlconcealbabyswall_col_name = coin_symbol + "_" + interval + "_cdlconcealbabyswall"
    df[cdlconcealbabyswall_col_name] = cdlconcealbabyswall
    return df

