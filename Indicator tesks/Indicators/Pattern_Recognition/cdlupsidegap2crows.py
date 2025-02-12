import pandas as pd
import talib as ta

def cdlupsidegap2crows(df, coin_symbol, interval):
    cdlupsidegap2crows = ta.CDLUPSIDEGAP2CROWS(df['open'], df['high'], df['low'], df['close'])
    cdlupsidegap2crows_col_name = coin_symbol + "_" + interval + "_cdlupsidegap2crows"
    df[cdlupsidegap2crows_col_name] = cdlupsidegap2crows
    return df

