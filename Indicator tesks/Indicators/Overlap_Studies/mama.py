import pandas as pd
import talib as ta

def mama(df, col, coin_symbol, interval, is_price, fastlimit=0, slowlimit=0):
    mama = ta.MAMA(df[col], fastlimit=fastlimit, slowlimit=slowlimit)
    if is_price:
        mama_col_name = coin_symbol + "_" + interval + "_mama_" + str(fastlimit).replace(".", "dot") + "_" + str(slowlimit).replace(".", "dot")
        fama_col_name = coin_symbol + "_" + interval + "_fama_" + str(fastlimit).replace(".", "dot") + "_" + str(slowlimit).replace(".", "dot")
    else:
        mama_col_name = col + "_mama_" + str(fastlimit).replace(".", "dot") + "_" + str(slowlimit).replace(".", "dot")
        fama_col_name = col + "_fama_" + str(fastlimit).replace(".", "dot") + "_" + str(slowlimit).replace(".", "dot")
    
    cols = [mama_col_name, fama_col_name]
    for i, c in enumerate(cols):
        df[c] = mama[i]
        first_non_nan_value = df[c].dropna().iloc[0]
        df[c] = df[c].fillna(first_non_nan_value)
    return df

