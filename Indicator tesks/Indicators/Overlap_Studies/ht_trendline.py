import pandas as pd
import talib as ta
CONFIG = {
    "indicator_class": "Overlap Studies",
    "indicator_name": "HT_TRENDLINE",
    "indicator_payload": "",
    "indicator_input_col": "real",
    "indicator_return_col": "real",
    "chart_area": "overlays",
    "chart_type": "line",
    "ind_type": "1"
}

def ht_trendline(df, col, coin_symbol, interval, is_price):
    if is_price:
        ht_trendline_col_name = coin_symbol + "_" + interval + "_ht_trendline"
    else:
        ht_trendline_col_name = col + "_ht_trendline"
    ht_trendline = ta.HT_TRENDLINE(df[col])
    df[ht_trendline_col_name] = ht_trendline
    df=df.dropna()
    return df

