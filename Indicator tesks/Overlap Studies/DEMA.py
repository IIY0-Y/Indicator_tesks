import talib as ta
import pandas as pd


def dema(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
      if is_price:
          dema_col_name = coin_symbol + "_" + interval + "_dema_" + str(timeperiod)
      else:
          dema_col_name = col + "_dema_" + str(timeperiod)
      dema = ta.DEMA(df[col], timeperiod=timeperiod)
      df[dema_col_name] = dema
      df=df.dropna()
      return df
