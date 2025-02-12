import pandas as pd
import talib as ta

def ht_phasor(df, col, coin_symbol, interval, is_price):
    ht_phasor = ta.HT_PHASOR(df[col])
    if is_price:
        inphase_col_name = coin_symbol + "_" + interval + "_inphase"
        quadrature_col_name = coin_symbol + "_" + interval + "_quadrature"
    else:
        inphase_col_name = col + "_inphase"
        quadrature_col_name = col + "_quadrature"
    cols = [inphase_col_name, quadrature_col_name]
    for i, c in enumerate(cols):
        df[c] = ht_phasor[i]
    df=df.dropna()
    return df

