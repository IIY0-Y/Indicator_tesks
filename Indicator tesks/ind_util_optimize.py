# import pandas_ta as pta
import talib as ta
from indicators.real.SMA import Sma


class Ind:

    def get(self, df, ind, col, payloads, coin_symbol, is_price, interval):
        ind_name = ind
        col_name = col
        payload = payloads
        if 'RSI' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.rsi(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)
        if 'SMA' == ind_name:
            timeperiod = payload.get('timeperiod')
            return Sma.run(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)
        # if 'MACD' == ind_name:
        #     fastperiod = payload.get('fastperiod')
        #     slowperiod = payload.get('slowperiod')
        #     signalperiod = payload.get('signalperiod')
        #     return self.macd(df=df, col=col_name, fastperiod=fastperiod, slowperiod=slowperiod,
        #                      signalperiod=signalperiod, coin_symbol=coin_symbol)
        if 'EMA' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.ema(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)

        if 'DEMA' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.dema(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                             interval=interval)

        if 'HT_TRENDLINE' == ind_name:
            return self.ht_trendline(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'KAMA' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.kama(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                             interval=interval)

        if 'MA' == ind_name:
            timeperiod = payload.get('timeperiod')
            matype = payload.get('matype')
            return self.ma(df=df, col=col_name, timeperiod=timeperiod, matype=matype, coin_symbol=coin_symbol,
                           is_price=is_price, interval=interval)

        if 'MIDPOINT' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.midpoint(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                                 interval=interval)

        if 'T3' == ind_name:
            timeperiod = payload.get('timeperiod')
            vfactor = payload.get('vfactor')
            return self.t3(df=df, col=col_name, timeperiod=timeperiod, vfactor=vfactor, coin_symbol=coin_symbol,
                           is_price=is_price, interval=interval)

        if 'TEMA' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.tema(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                             interval=interval)

        if 'TRIMA' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.trima(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                              interval=interval)

        if 'WMA' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.wma(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)

        if 'APO' == ind_name:
            fastperiod = payload.get('fastperiod')
            slowperiod = payload.get('slowperiod')
            matype = payload.get('matype')
            return self.apo(df=df, col=col_name, fastperiod=fastperiod, slowperiod=slowperiod, matype=matype,
                            coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'CMO' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.cmo(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)

        if 'MOM' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.mom(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)

        if 'PPO' == ind_name:
            fastperiod = payload.get('fastperiod')
            slowperiod = payload.get('slowperiod')
            matype = payload.get('matype')
            return self.ppo(df=df, col=col_name, fastperiod=fastperiod, slowperiod=slowperiod, matype=matype,
                            coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'ROC' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.roc(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)

        if 'ROCP' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.rocp(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                             interval=interval)

        if 'ROCR' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.rocr(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                             interval=interval)

        if 'ROCR100' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.rocr100(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                                interval=interval)

        if 'TRIX' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.trix(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                             interval=interval)

        if 'HT_DCPERIOD' == ind_name:
            return self.ht_dcperiod(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'HT_DCPHASE' == ind_name:
            return self.ht_dcphase(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'LINEARREG' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.linearreg(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol,
                                  is_price=is_price, interval=interval)

        if 'LINEARREG_ANGLE' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.linearreg_angle(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol,
                                        is_price=is_price, interval=interval)

        if 'LINEARREG_INTERCEPT' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.linearreg_intercept(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol,
                                            is_price=is_price, interval=interval)

        if 'LINEARREG_SLOPE' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.linearreg_slope(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol,
                                        is_price=is_price, interval=interval)

        if 'STDDEV' == ind_name:
            timeperiod = payload.get('timeperiod')
            nbdev = payload.get('nbdev')
            return self.stddev(df=df, col=col_name, timeperiod=timeperiod, nbdev=nbdev, coin_symbol=coin_symbol,
                               is_price=is_price, interval=interval)

        if 'TSF' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.tsf(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)

        if 'VAR' == ind_name:
            timeperiod = payload.get('timeperiod')
            nbdev = payload.get('nbdev')
            return self.var(df=df, col=col_name, timeperiod=timeperiod, nbdev=nbdev, coin_symbol=coin_symbol,
                            is_price=is_price, interval=interval)

        if 'ACOS' == ind_name:
            return self.acos(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'ASIN' == ind_name:
            return self.asin(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'ATAN' == ind_name:
            return self.atan(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'CEIL' == ind_name:
            return self.ceil(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'COS' == ind_name:
            return self.cos(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'COSH' == ind_name:
            return self.cosh(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'EXP' == ind_name:
            return self.exp(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'FLOOR' == ind_name:
            return self.floor(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'LN' == ind_name:
            return self.ln(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'LOG10' == ind_name:
            return self.log10(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'SIN' == ind_name:
            return self.sin(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'SINH' == ind_name:
            return self.sinh(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'SQRT' == ind_name:
            return self.sqrt(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'TAN' == ind_name:
            return self.tan(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'TANH' == ind_name:
            return self.tanh(df=df, col=col_name, coin_symbol=coin_symbol, is_price=is_price, interval=interval)

        if 'MAX' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.max(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)

        if 'MIN' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.min(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)

        if 'SUM' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.sum(df=df, col=col_name, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price=is_price,
                            interval=interval)
        ################################################################################################################

        if 'BBANDS' == ind_name:
            timeperiod = payload.get('timeperiod')
            nbdevup = payload.get('nbdevup')
            nbdevdn = payload.get('nbdevdn')
            matype = payload.get('matype')
            return self.bbands(df=df, col=col_name, interval=interval, timeperiod=timeperiod,nbdevup=nbdevup,nbdevdn=nbdevdn,matype=matype, coin_symbol=coin_symbol, is_price = is_price)


        # if 'MAMA' == ind_name:
        #     fastlimit = payload.get('fastlimit')
        #     slowlimit = payload.get('slowlimit')
        #     return self.mama(df=df, col=col_name, fastlimit=fastlimit,slowlimit=slowlimit, coin_symbol=coin_symbol, is_price = is_price)


        if 'MACD' == ind_name:
            fastperiod = payload.get('fastperiod')
            slowperiod = payload.get('slowperiod')
            signalperiod = payload.get('signalperiod')
            return self.macd(df=df, col=col_name, interval=interval, fastperiod=fastperiod,slowperiod=slowperiod,signalperiod=signalperiod, coin_symbol=coin_symbol, is_price = is_price)


        if 'MACDEXT' == ind_name:
            fastperiod = payload.get('fastperiod')
            fastmatype = payload.get('fastmatype')
            slowperiod = payload.get('slowperiod')
            slowmatype = payload.get('slowmatype')
            signalperiod = payload.get('signalperiod')
            signalmatype = payload.get('signalmatype')
            return self.macdext(df=df, col=col_name, interval=interval, fastperiod=fastperiod,fastmatype=fastmatype,slowperiod=slowperiod,slowmatype=slowmatype,signalperiod=signalperiod,signalmatype=signalmatype, coin_symbol=coin_symbol, is_price = is_price)


        if 'MACDFIX' == ind_name:
            signalperiod = payload.get('signalperiod')
            return self.macdfix(df=df, col=col_name, interval=interval, signalperiod=signalperiod, coin_symbol=coin_symbol, is_price = is_price)


        if 'STOCHRSI' == ind_name:
            timeperiod = payload.get('timeperiod')
            fastk_period = payload.get('fastk_period')
            fastd_period = payload.get('fastd_period')
            fastd_matype = payload.get('fastd_matype')
            return self.stochrsi(df=df, col=col_name, interval=interval, timeperiod=timeperiod,fastk_period=fastk_period,fastd_period=fastd_period,fastd_matype=fastd_matype, coin_symbol=coin_symbol, is_price = is_price)


        if 'HT_PHASOR' == ind_name:

            return self.ht_phasor(df=df, col=col_name, interval=interval, coin_symbol=coin_symbol, is_price = is_price)

        if 'HT_SINE' == ind_name:
            return self.ht_sine(df=df, col=col_name, interval=interval, coin_symbol=coin_symbol, is_price = is_price)

        if 'MINMAX' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.minmax(df=df, col=col_name, interval=interval, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price = is_price)

        if 'MINMAXINDEX' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.minmaxindex(df=df, col=col_name, interval=interval, timeperiod=timeperiod, coin_symbol=coin_symbol, is_price = is_price)
        ################# Custom Indicators ###############################################################################################
        if 'rolling_thehold' == ind_name:
            thehold_rolling = payload.get('thehold_rolling')
            up_quantile = payload.get('up_quantile')
            down_quantile = payload.get('down_quantile')
            return self.rolling_thehold(df=df, col=col_name, coin_symbol=coin_symbol, interval=interval,
                                        is_price=is_price, thehold_rolling=thehold_rolling,
                                        up_quantile=up_quantile, down_quantile=down_quantile)

        if 'expanding_quantile' == ind_name:
            min_periods = payload.get('min_periods')
            up_quantile = payload.get('up_quantile')
            down_quantile = payload.get('down_quantile')
            return self.expanding_quantile(df=df, col=col_name, coin_symbol=coin_symbol, interval=interval,
                                           is_price=is_price, min_periods=min_periods,
                                           up_quantile=up_quantile, down_quantile=down_quantile)
        if 'lag' == ind_name:
            timeperiod = payload.get('timeperiod')
            return self.lag(df=df, col=col_name, coin_symbol=coin_symbol, interval=interval, is_price=is_price,
                            timeperiod=timeperiod)




    def dema(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            dema_col_name = coin_symbol + "_" + interval + "_dema_" + str(timeperiod)
        else:
            dema_col_name = col + "_dema_" + str(timeperiod)
        dema = ta.DEMA(df[col], timeperiod=timeperiod)
        df[dema_col_name] = dema
        df=df.dropna()
        return df

    def ema(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            ema_col_name = coin_symbol + "_" + interval + "_ema_" + str(timeperiod)
        else:
            ema_col_name = col + "_ema_" + str(timeperiod)
        ema = ta.EMA(df[col], timeperiod=timeperiod)
        df[ema_col_name] = ema
        df=df.dropna()
        return df

    def ht_trendline(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            ht_trendline_col_name = coin_symbol + "_" + interval + "_ht_trendline"
        else:
            ht_trendline_col_name = col + "_ht_trendline"
        ht_trendline = ta.HT_TRENDLINE(df[col])
        df[ht_trendline_col_name] = ht_trendline
        df=df.dropna()
        return df

    def kama(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            kama_col_name = coin_symbol + "_" + interval + "_kama_" + str(timeperiod)
        else:
            kama_col_name = col + "_kama_" + str(timeperiod)
        kama = ta.KAMA(df[col], timeperiod=timeperiod)
        df[kama_col_name] = kama
        df=df.dropna()
        return df

    def ma(self, df, col, coin_symbol, interval, is_price, timeperiod=30, matype=0):
        if is_price:
            ma_col_name = coin_symbol + "_" + interval + "_ma_" + str(timeperiod) + "_" + str(matype)
        else:
            ma_col_name = col + "_ma_" + str(timeperiod) + "_" + str(matype)
        ma = ta.MA(df[col], timeperiod=timeperiod, matype=matype)
        df[ma_col_name] = ma
        df=df.dropna()
        return df

    def midpoint(self, df, col, coin_symbol, interval, is_price, timeperiod=14):
        if is_price:
            midpoint_col_name = coin_symbol + "_" + interval + "_midpoint_" + str(timeperiod)
        else:
            midpoint_col_name = col + "_midpoint_" + str(timeperiod)
        midpoint = ta.MIDPOINT(df[col], timeperiod=timeperiod)
        df[midpoint_col_name] = midpoint
        df=df.dropna()
        return df

    def sma(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            sma_col_name = coin_symbol + "_" + interval + "_sma_" + str(timeperiod)
        else:
            sma_col_name = col + "_sma_" + str(timeperiod)
        sma = ta.SMA(df[col], timeperiod=timeperiod)
        df[sma_col_name] = sma
        df=df.dropna()
        # first_non_nan_value = df[sma_col_name].dropna().iloc[0]
        # df[sma_col_name] = df[sma_col_name].fillna(first_non_nan_value)
        return df

    def t3(self, df, col, coin_symbol, interval, is_price, timeperiod=5, vfactor=0):
        if is_price:
            t3_col_name = coin_symbol + "_" + interval + "_t3_" + str(timeperiod) + "_" + str(vfactor).replace(".","dot")
        else:
            t3_col_name = col + "_t3_" + str(timeperiod) + "_" + str(vfactor).replace(".","dot")
        t3 = ta.T3(df[col], timeperiod=timeperiod, vfactor=vfactor)
        df[t3_col_name] = t3
        df=df.dropna()
        return df

    def tema(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            tema_col_name = coin_symbol + "_" + interval + "_tema_" + str(timeperiod)
        else:
            tema_col_name = col + "_tema_" + str(timeperiod)
        tema = ta.TEMA(df[col], timeperiod=timeperiod)
        df[tema_col_name] = tema
        df=df.dropna()
        return df

    def trima(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            trima_col_name = coin_symbol + "_" + interval + "_trima_" + str(timeperiod)
        else:
            trima_col_name = col + "_trima_" + str(timeperiod)
        trima = ta.TRIMA(df[col], timeperiod=timeperiod)
        df[trima_col_name] = trima
        df=df.dropna()
        return df

    def wma(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            wma_col_name = coin_symbol + "_" + interval + "_wma_" + str(timeperiod)
        else:
            wma_col_name = col + "_wma_" + str(timeperiod)
        wma = ta.WMA(df[col], timeperiod=timeperiod)
        df[wma_col_name] = wma
        df=df.dropna()
        return df

    def apo(self, df, col, coin_symbol, interval, is_price, fastperiod=12, slowperiod=26, matype=0):
        if is_price:
            apo_col_name = coin_symbol + "_" + interval + "_apo_" + str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(matype)
        else:
            apo_col_name = col + "_apo_" + str(fastperiod) + "_" + str(slowperiod) + "_" + str(matype)
        apo = ta.APO(df[col], fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
        df[apo_col_name] = apo
        df=df.dropna()
        return df

    def cmo(self, df, col, coin_symbol, interval, is_price, timeperiod=14):
        if is_price:
            cmo_col_name = coin_symbol + "_" + interval + "_cmo_" + str(timeperiod)
        else:
            cmo_col_name = col + "_cmo_" + str(timeperiod)
        cmo = ta.CMO(df[col], timeperiod=timeperiod)
        df[cmo_col_name] = cmo
        df=df.dropna()
        return df

    def mom(self, df, col, coin_symbol, interval, is_price, timeperiod=10):
        if is_price:
            mom_col_name = coin_symbol + "_" + interval + "_mom_" + str(timeperiod)
        else:
            mom_col_name = col + "_mom_" + str(timeperiod)
        mom = ta.MOM(df[col], timeperiod=timeperiod)
        df[mom_col_name] = mom
        df=df.dropna()
        return df

    def ppo(self, df, col, coin_symbol, interval, is_price, fastperiod=12, slowperiod=26, matype=0):
        if is_price:
            ppo_col_name = coin_symbol + "_" + interval + "_ppo_" + str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(matype)
        else:
            ppo_col_name = col + "_ppo_" + str(fastperiod) + "_" + str(slowperiod) + "_" + str(matype)
        ppo = ta.PPO(df[col], fastperiod=fastperiod, slowperiod=slowperiod, matype=matype)
        df[ppo_col_name] = ppo
        df=df.dropna()
        return df

    def roc(self, df, col, coin_symbol, interval, is_price, timeperiod=10):
        if is_price:
            roc_col_name = coin_symbol + "_" + interval + "_roc_" + str(timeperiod)
        else:
            roc_col_name = col + "_roc_" + str(timeperiod)
        roc = ta.ROC(df[col], timeperiod=timeperiod)
        df[roc_col_name] = roc
        df=df.dropna()
        return df

    def rocp(self, df, col, coin_symbol, interval, is_price, timeperiod=10):
        if is_price:
            rocp_col_name = coin_symbol + "_" + interval + "_rocp_" + str(timeperiod)
        else:
            rocp_col_name = col + "_rocp_" + str(timeperiod)
        rocp = ta.ROCP(df[col], timeperiod=timeperiod)
        df[rocp_col_name] = rocp
        df=df.dropna()
        return df

    def rocr(self, df, col, coin_symbol, interval, is_price, timeperiod=10):
        if is_price:
            rocr_col_name = coin_symbol + "_" + interval + "_rocr_" + str(timeperiod)
        else:
            rocr_col_name = col + "_rocr_" + str(timeperiod)
        rocr = ta.ROCR(df[col], timeperiod=timeperiod)
        df[rocr_col_name] = rocr
        df=df.dropna()
        return df

    def rocr100(self, df, col, coin_symbol, interval, is_price, timeperiod=10):
        if is_price:
            rocr100_col_name = coin_symbol + "_" + interval + "_rocr100_" + str(timeperiod)
        else:
            rocr100_col_name = col + "_rocr100_" + str(timeperiod)
        rocr100 = ta.ROCR100(df[col], timeperiod=timeperiod)
        df[rocr100_col_name] = rocr100
        df=df.dropna()
        return df

    def rsi(self, df, col, coin_symbol, interval, is_price, timeperiod=14):
        if is_price:
            rsi_col_name = coin_symbol + "_" + interval + "_rsi_" + str(timeperiod).replace(".","dot")
        else:
            rsi_col_name = col + "_rsi_" + str(timeperiod)
        rsi = ta.RSI(df[col], timeperiod=timeperiod)
        df[rsi_col_name] = rsi
        df=df.dropna()
        return df

    def trix(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            trix_col_name = coin_symbol + "_" + interval + "_trix_" + str(timeperiod)
        else:
            trix_col_name = col + "_trix_" + str(timeperiod)
        trix = ta.TRIX(df[col], timeperiod=timeperiod)
        df[trix_col_name] = trix
        df=df.dropna()
        return df

    def ht_dcperiod(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            ht_dcperiod_col_name = coin_symbol + "_" + interval + "_ht_dcperiod"
        else:
            ht_dcperiod_col_name = col + "_ht_dcperiod"
        ht_dcperiod = ta.HT_DCPERIOD(df[col])
        df[ht_dcperiod_col_name] = ht_dcperiod
        df=df.dropna()
        return df

    def ht_dcphase(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            ht_dcphase_col_name = coin_symbol + "_" + interval + "_ht_dcphase"
        else:
            ht_dcphase_col_name = col + "_ht_dcphase"
        ht_dcphase = ta.HT_DCPHASE(df[col])
        df[ht_dcphase_col_name] = ht_dcphase
        df=df.dropna()
        return df

    def linearreg(self, df, col, coin_symbol, interval, is_price, timeperiod=14):
        if is_price:
            linearreg_col_name = coin_symbol + "_" + interval + "_linearreg_" + str(timeperiod)
        else:
            linearreg_col_name = col + "_linearreg_" + str(timeperiod)
        linearreg = ta.LINEARREG(df[col], timeperiod=timeperiod)
        df[linearreg_col_name] = linearreg
        df=df.dropna()
        return df

    def linearreg_angle(self, df, col, coin_symbol, interval, is_price, timeperiod=14):
        if is_price:
            linearreg_angle_col_name = coin_symbol + "_" + interval + "_linearreg_angle_" + str(timeperiod)
        else:
            linearreg_angle_col_name = col + "_linearreg_angle_" + str(timeperiod)
        linearreg_angle = ta.LINEARREG_ANGLE(df[col], timeperiod=timeperiod)
        df[linearreg_angle_col_name] = linearreg_angle
        df=df.dropna()
        return df

    def linearreg_intercept(self, df, col, coin_symbol, interval, is_price, timeperiod=14):
        if is_price:
            linearreg_intercept_col_name = coin_symbol + "_" + interval + "_linearreg_intercept_" + str(timeperiod)
        else:
            linearreg_intercept_col_name = col + "_linearreg_intercept_" + str(timeperiod)
        linearreg_intercept = ta.LINEARREG_INTERCEPT(df[col], timeperiod=timeperiod)
        df[linearreg_intercept_col_name] = linearreg_intercept
        df=df.dropna()
        return df

    def linearreg_slope(self, df, col, coin_symbol, interval, is_price, timeperiod=14):
        if is_price:
            linearreg_slope_col_name = coin_symbol + "_" + interval + "_linearreg_slope_" + str(timeperiod)
        else:
            linearreg_slope_col_name = col + "_linearreg_slope_" + str(timeperiod)
        linearreg_slope = ta.LINEARREG_SLOPE(df[col], timeperiod=timeperiod)
        df[linearreg_slope_col_name] = linearreg_slope
        df=df.dropna()
        return df

    def stddev(self, df, col, coin_symbol, interval, is_price, timeperiod=5, nbdev=1):
        if is_price:
            stddev_col_name = coin_symbol + "_" + interval + "_stddev_" + str(timeperiod)+ "_" +str(nbdev)
        else:
            stddev_col_name = col + "_stddev_" + str(timeperiod) + "_" + str(nbdev)
        stddev = ta.STDDEV(df[col], timeperiod=timeperiod, nbdev=nbdev)
        df[stddev_col_name] = stddev
        df=df.dropna()
        return df

    def tsf(self, df, col, coin_symbol, interval, is_price, timeperiod=14):
        if is_price:
            tsf_col_name = coin_symbol + "_" + interval + "_tsf_" + str(timeperiod)
        else:
            tsf_col_name = col + "_tsf_" + str(timeperiod)
        tsf = ta.TSF(df[col], timeperiod=timeperiod)
        df[tsf_col_name] = tsf
        df=df.dropna()
        return df

    def var(self, df, col, coin_symbol, interval, is_price, timeperiod=5, nbdev=1):
        if is_price:
            var_col_name = coin_symbol + "_" + interval + "_var_" + str(timeperiod) + "_" + str(nbdev)
        else:
            var_col_name = col + "_var_" + str(timeperiod) + "_" + str(nbdev)
        var = ta.VAR(df[col], timeperiod=timeperiod, nbdev=nbdev)
        df[var_col_name] = var
        df=df.dropna()
        return df

    def acos(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            acos_col_name = coin_symbol + "_" + interval + "_acos"
        else:
            acos_col_name = col + "_acos"
        acos = ta.ACOS(df[col])
        df[acos_col_name] = acos
        df=df.dropna()
        return df

    def asin(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            asin_col_name = coin_symbol + "_" + interval + "_asin"
        else:
            asin_col_name = col + "_asin"
        asin = ta.ASIN(df[col])
        df[asin_col_name] = asin
        df=df.dropna()
        return df

    def atan(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            atan_col_name = coin_symbol + "_" + interval + "_atan"
        else:
            atan_col_name = col + "_atan"
        atan = ta.ATAN(df[col])
        df[atan_col_name] = atan
        df=df.dropna()
        return df

    def ceil(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            ceil_col_name = coin_symbol + "_" + interval + "_ceil"
        else:
            ceil_col_name = col + "_ceil"
        ceil = ta.CEIL(df[col])
        df[ceil_col_name] = ceil
        df=df.dropna()
        return df

    def cos(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            cos_col_name = coin_symbol + "_" + interval + "_cos"
        else:
            cos_col_name = col + "_cos"
        cos = ta.COS(df[col])
        df[cos_col_name] = cos
        df=df.dropna()
        return df

    def cosh(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            cosh_col_name = coin_symbol + "_" + interval + "_cosh"
        else:
            cosh_col_name = col + "_cosh"
        cosh = ta.COSH(df[col])
        df[cosh_col_name] = cosh
        df=df.dropna()
        return df

    def exp(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            exp_col_name = coin_symbol + "_" + interval + "_exp"
        else:
            exp_col_name = col + "_exp"
        exp = ta.EXP(df[col])
        df[exp_col_name] = exp
        df=df.dropna()
        return df

    def floor(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            floor_col_name = coin_symbol + "_" + interval + "_floor"
        else:
            floor_col_name = col + "_floor"
        floor = ta.FLOOR(df[col])
        df[floor_col_name] = floor
        df=df.dropna()
        return df

    def ln(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            ln_col_name = coin_symbol + "_" + interval + "_ln"
        else:
            ln_col_name = col + "_ln"
        ln = ta.LN(df[col])
        df[ln_col_name] = ln
        df=df.dropna()
        return df

    def log10(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            log10_col_name = coin_symbol + "_" + interval + "_log10"
        else:
            log10_col_name = col + "_log10"
        log10 = ta.LOG10(df[col])
        df[log10_col_name] = log10
        df=df.dropna()
        return df

    def sin(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            sin_col_name = coin_symbol + "_" + interval + "_sin"
        else:
            sin_col_name = col + "_sin"
        sin = ta.SIN(df[col])
        df[sin_col_name] = sin
        df=df.dropna()
        return df

    def sinh(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            sinh_col_name = coin_symbol + "_" + interval + "_sinh"
        else:
            sinh_col_name = col + "_sinh"
        sinh = ta.SINH(df[col])
        df[sinh_col_name] = sinh
        df=df.dropna()
        return df

    def sqrt(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            sqrt_col_name = coin_symbol + "_" + interval + "_sqrt"
        else:
            sqrt_col_name = col + "_sqrt"
        sqrt = ta.SQRT(df[col])
        df[sqrt_col_name] = sqrt
        df=df.dropna()
        return df

    def tan(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            tan_col_name = coin_symbol + "_" + interval + "_tan"
        else:
            tan_col_name = col + "_tan"
        tan = ta.TAN(df[col])
        df[tan_col_name] = tan
        df=df.dropna()
        return df

    def tanh(self, df, col, coin_symbol, interval, is_price):
        if is_price:
            tanh_col_name = coin_symbol + "_" + interval + "_tanh"
        else:
            tanh_col_name = col + "_tanh"
        tanh = ta.TANH(df[col])
        df[tanh_col_name] = tanh
        df=df.dropna()
        return df

    def max(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            max_col_name = coin_symbol + "_" + interval + "_max_" + str(timeperiod)
        else:
            max_col_name = col + "_max_" + str(timeperiod)
        max = ta.MAX(df[col], timeperiod=timeperiod)
        df[max_col_name] = max
        df=df.dropna()
        return df

    def min(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            min_col_name = coin_symbol + "_" + interval + "_min_" + str(timeperiod)
        else:
            min_col_name = col + "_min_" + str(timeperiod)
        min = ta.MIN(df[col], timeperiod=timeperiod)
        df[min_col_name] = min
        df=df.dropna()
        return df

    def sum(self, df, col, coin_symbol, interval, is_price, timeperiod=30):
        if is_price:
            sum_col_name = coin_symbol + "_" + interval + "_sum_" + str(timeperiod)
        else:
            sum_col_name = col + "_sum_" + str(timeperiod)
        sum = ta.SUM(df[col], timeperiod=timeperiod)
        df[sum_col_name] = sum
        df=df.dropna()
        return df

    ################ Above are simple indicators #########################################################################
    ################ Below are complex indicators #########################################################################

    def bbands(self, df, col, coin_symbol, interval, is_price,timeperiod = 5,nbdevup = 2,nbdevdn = 2,matype = 0):
        bbands = ta.BBANDS(df[col],timeperiod=timeperiod,nbdevup=nbdevup,nbdevdn=nbdevdn,matype=matype)
        if is_price:
            upperband_col_name = coin_symbol + "_" + interval + "_upperband_" +str(timeperiod)+ "_" +str(nbdevup).replace(".","dot")+ "_" +str(nbdevdn).replace(".","dot")+ "_" +str(matype)
            middleband_col_name = coin_symbol + "_" + interval + "_middleband_" +str(timeperiod)+ "_" +str(nbdevup).replace(".","dot")+ "_" +str(nbdevdn).replace(".","dot")+ "_" +str(matype)
            lowerband_col_name = coin_symbol + "_" + interval + "_lowerband_" +str(timeperiod)+ "_" +str(nbdevup).replace(".","dot")+ "_" +str(nbdevdn).replace(".","dot")+ "_" +str(matype)
        else:
            upperband_col_name =  col + "_upperband_" +str(timeperiod)+ "_" +str(nbdevup).replace(".","dot")+ "_" +str(nbdevdn).replace(".","dot")+ "_" +str(matype)
            middleband_col_name =  col + "_middleband_" +str(timeperiod)+ "_" +str(nbdevup).replace(".","dot")+ "_" +str(nbdevdn).replace(".","dot")+ "_" +str(matype)
            lowerband_col_name =  col + "_lowerband_" +str(timeperiod)+ "_" +str(nbdevup).replace(".","dot")+ "_" +str(nbdevdn).replace(".","dot")+ "_" +str(matype)
        cols = [upperband_col_name,middleband_col_name,lowerband_col_name]
        for i, c in enumerate(cols):
            df[c] = bbands[i]
        df=df.dropna()
        return df


    # def mama(self, df, col, coin_symbol, is_price,fastlimit = 0,slowlimit = 0):
    #     mama = ta.MAMA(df[col],fastlimit=fastlimit,slowlimit=slowlimit)
    #     if is_price:
    #         mama_col_name = coin_symbol + "_mama_" +str(fastlimit).replace(".","dot")+ "_" +str(slowlimit).replace(".","dot")
    #         fama_col_name = coin_symbol + "_fama_" +str(fastlimit).replace(".","dot")+ "_" +str(slowlimit).replace(".","dot")
    #     else:
    #         mama_col_name =  col + "_mama_" +str(fastlimit).replace(".","dot")+ "_" +str(slowlimit).replace(".","dot")
    #         fama_col_name =  col + "_fama_" +str(fastlimit).replace(".","dot")+ "_" +str(slowlimit).replace(".","dot")
    #     cols = [mama_col_name,fama_col_name]
    #     for i, c in enumerate(cols):
    #         df[c] = mama[i]
    #         first_non_nan_value = df[c].dropna().iloc[0]
    #         df[c] = df[c].fillna(first_non_nan_value)
    #     return df


    def macd(self, df, col, coin_symbol, interval, is_price,fastperiod = 12,slowperiod = 26,signalperiod = 9):
        macd = ta.MACD(df[col],fastperiod=fastperiod,slowperiod=slowperiod,signalperiod=signalperiod)
        if is_price:
            macd_col_name = coin_symbol + "_" + interval + "_macd_" +str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(signalperiod)
            macdsignal_col_name = coin_symbol + "_" + interval + "_macdsignal_" +str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(signalperiod)
            macdhist_col_name = coin_symbol + "_" + interval + "_macdhist_" +str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(signalperiod)
        else:
            macd_col_name =  col + "_macd_" +str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(signalperiod)
            macdsignal_col_name =  col + "_macdsignal_" +str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(signalperiod)
            macdhist_col_name =  col + "_macdhist_" +str(fastperiod)+ "_" +str(slowperiod)+ "_" +str(signalperiod)
        cols = [macd_col_name,macdsignal_col_name,macdhist_col_name]
        for i, c in enumerate(cols):
            df[c] = macd[i]

        df=df.dropna()
        return df


    def macdext(self, df, col, coin_symbol, interval, is_price,fastperiod = 12,fastmatype = 0,slowperiod = 26,slowmatype = 0,signalperiod = 9,signalmatype = 0):
        macdext = ta.MACDEXT(df[col],fastperiod=fastperiod,fastmatype=fastmatype,slowperiod=slowperiod,slowmatype=slowmatype,signalperiod=signalperiod,signalmatype=signalmatype)
        if is_price:
            macd_col_name = coin_symbol + "_" + interval + "_macd_" +str(fastperiod)+ "_" +str(fastmatype)+ "_" +str(slowperiod)+ "_" +str(slowmatype)+ "_" +str(signalperiod)+ "_" +str(signalmatype)
            macdsignal_col_name = coin_symbol + "_" + interval + "_macdsignal_" +str(fastperiod)+ "_" +str(fastmatype)+ "_" +str(slowperiod)+ "_" +str(slowmatype)+ "_" +str(signalperiod)+ "_" +str(signalmatype)
            macdhist_col_name = coin_symbol + "_" + interval + "_macdhist_" +str(fastperiod)+ "_" +str(fastmatype)+ "_" +str(slowperiod)+ "_" +str(slowmatype)+ "_" +str(signalperiod)+ "_" +str(signalmatype)
        else:
            macd_col_name =  col + "_macd_" +str(fastperiod)+ "_" +str(fastmatype)+ "_" +str(slowperiod)+ "_" +str(slowmatype)+ "_" +str(signalperiod)+ "_" +str(signalmatype)
            macdsignal_col_name =  col + "_macdsignal_" +str(fastperiod)+ "_" +str(fastmatype)+ "_" +str(slowperiod)+ "_" +str(slowmatype)+ "_" +str(signalperiod)+ "_" +str(signalmatype)
            macdhist_col_name =  col + "_macdhist_" +str(fastperiod)+ "_" +str(fastmatype)+ "_" +str(slowperiod)+ "_" +str(slowmatype)+ "_" +str(signalperiod)+ "_" +str(signalmatype)
        cols = [macd_col_name,macdsignal_col_name,macdhist_col_name]
        for i, c in enumerate(cols):
            df[c] = macdext[i]

        df=df.dropna()
        return df


    def macdfix(self, df, col, coin_symbol, interval, is_price,signalperiod = 9):
        macdfix = ta.MACDFIX(df[col],signalperiod=signalperiod)
        if is_price:
            macd_col_name = coin_symbol + "_" + interval + "_macd_" +str(signalperiod)
            macdsignal_col_name = coin_symbol + "_" + interval + "_macdsignal_" +str(signalperiod)
            macdhist_col_name = coin_symbol + "_" + interval + "_macdhist_" +str(signalperiod)
        else:
            macd_col_name =  col + "_macd_" +str(signalperiod)
            macdsignal_col_name =  col + "_macdsignal_" +str(signalperiod)
            macdhist_col_name =  col + "_macdhist_" +str(signalperiod)
        cols = [macd_col_name,macdsignal_col_name,macdhist_col_name]
        for i, c in enumerate(cols):
            df[c] = macdfix[i]
        df=df.dropna()
        return df


    def stochrsi(self, df, col, coin_symbol, interval, is_price,timeperiod = 14,fastk_period = 5,fastd_period = 3,fastd_matype = 0):
        stochrsi = ta.STOCHRSI(df[col],timeperiod=timeperiod,fastk_period=fastk_period,fastd_period=fastd_period,fastd_matype=fastd_matype)
        if is_price:
            fastk_col_name = coin_symbol + "_" + interval + "_fastk_" +str(timeperiod)+ "_" +str(fastk_period)+ "_" +str(fastd_period)+ "_" +str(fastd_matype)
            fastd_col_name = coin_symbol + "_" + interval + "_fastd_" +str(timeperiod)+ "_" +str(fastk_period)+ "_" +str(fastd_period)+ "_" +str(fastd_matype)
        else:
            fastk_col_name =  col + "_fastk_" +str(timeperiod)+ "_" +str(fastk_period)+ "_" +str(fastd_period)+ "_" +str(fastd_matype)
            fastd_col_name =  col + "_fastd_" +str(timeperiod)+ "_" +str(fastk_period)+ "_" +str(fastd_period)+ "_" +str(fastd_matype)
        cols = [fastk_col_name,fastd_col_name]
        for i, c in enumerate(cols):
            df[c] = stochrsi[i]
        df=df.dropna()
        return df


    def ht_phasor(self, df, col, coin_symbol, interval, is_price):
        ht_phasor = ta.HT_PHASOR(df[col])
        if is_price:
            inphase_col_name = coin_symbol + "_" + interval + "_inphase"
            quadrature_col_name = coin_symbol + "_" + interval + "_quadrature"
        else:
            inphase_col_name =  col + "_inphase"
            quadrature_col_name =  col + "_quadrature"
        cols = [inphase_col_name,quadrature_col_name]
        for i, c in enumerate(cols):
            df[c] = ht_phasor[i]
        df=df.dropna()
        return df


    def ht_sine(self, df, col, coin_symbol, interval, is_price):
        ht_sine = ta.HT_SINE(df[col])
        if is_price:
            sine_col_name = coin_symbol + "_" + interval + "_sine"
            leadsine_col_name = coin_symbol + "_" + interval + "_leadsine"
        else:
            sine_col_name =  col + "_sine"
            leadsine_col_name =  col + "_leadsine"
        cols = [sine_col_name,leadsine_col_name]
        for i, c in enumerate(cols):
            df[c] = ht_sine[i]
        df=df.dropna()
        return df


    def minmax(self, df, col, coin_symbol, interval, is_price,timeperiod = 30):
        minmax = ta.MINMAX(df[col],timeperiod=timeperiod)
        if is_price:
            min_col_name = coin_symbol + "_" + interval + "_min_" +str(timeperiod)
            max_col_name = coin_symbol + "_" + interval + "_max_" +str(timeperiod)
        else:
            min_col_name =  col + "_min_" +str(timeperiod)
            max_col_name =  col + "_max_" +str(timeperiod)
        cols = [min_col_name,max_col_name]
        for i, c in enumerate(cols):
            df[c] = minmax[i]
        df=df.dropna()
        return df


    def minmaxindex(self, df, col, coin_symbol, interval, is_price,timeperiod = 30):
        minmaxindex = ta.MINMAXINDEX(df[col],timeperiod=timeperiod)
        if is_price:
            minidx_col_name = coin_symbol + "_" + interval + "_minidx_" +str(timeperiod)
            maxidx_col_name = coin_symbol + "_" + interval + "_maxidx_" +str(timeperiod)
        else:
            minidx_col_name =  col + "_minidx_" +str(timeperiod)
            maxidx_col_name =  col + "_maxidx_" +str(timeperiod)
        cols = [minidx_col_name,maxidx_col_name]
        for i, c in enumerate(cols):
            df[c] = minmaxindex[i]
        df=df.dropna()
        return df
    #############################    self add    ########################################################################
    def rolling_thehold(self, df, col, coin_symbol, interval, is_price, thehold_rolling=30, up_quantile=0.75, down_quantile=0.25):
        up_quantile_str=str(up_quantile).replace(".","dot")
        down_quantile_str=str(down_quantile).replace(".","dot")
        if is_price:
            up_col_name = f"{coin_symbol}_{interval}_up_rolling_thehold_{thehold_rolling}_{up_quantile_str}_{down_quantile_str}"
            down_col_name = f"{coin_symbol}_{interval}_down_rolling_thehold_{thehold_rolling}_{up_quantile_str}_{down_quantile_str}"
        else:
            up_col_name = f"{col}_up_rolling_thehold_{thehold_rolling}_{up_quantile_str}_{down_quantile_str}"
            down_col_name = f"{col}_down_rolling_thehold_{thehold_rolling}_{up_quantile_str}_{down_quantile_str}"

        df[up_col_name] = df[col].rolling(window=thehold_rolling).quantile(up_quantile)
        df[down_col_name] = df[col].rolling(window=thehold_rolling).quantile(down_quantile)

        # Filling NaN values
        # first_non_nan_value_up = df[up_col_name].dropna().iloc[0]
        # df[up_col_name] = df[up_col_name].fillna(first_non_nan_value_up)
        #
        # first_non_nan_value_down = df[down_col_name].dropna().iloc[0]
        # df[down_col_name] = df[down_col_name].fillna(first_non_nan_value_down)
        df=df.dropna()
        return df

    def expanding_quantile(self, df, col, coin_symbol, interval, is_price, min_periods=60, up_quantile=0.75, down_quantile=0.25):
        up_quantile_str=str(up_quantile).replace(".","dot")
        down_quantile_str=str(down_quantile).replace(".","dot")
        if is_price:
            up_col_name = f"{coin_symbol}_{interval}_expanding_up_quantile_{min_periods}_{up_quantile_str}_{down_quantile_str}"
            down_col_name = f"{coin_symbol}_{interval}_expanding_down_quantile_{min_periods}_{up_quantile_str}_{down_quantile_str}"
        else:
            up_col_name = f"{col}_expanding_up_quantile_{min_periods}_{up_quantile_str}_{down_quantile_str}"
            down_col_name = f"{col}_expanding_down_quantile_{min_periods}_{up_quantile_str}_{down_quantile_str}"

        df[up_col_name] = df[col].expanding(min_periods=min_periods).quantile(up_quantile)
        df[down_col_name] = df[col].expanding(min_periods=min_periods).quantile(down_quantile)

        # Filling NaN values
        # first_non_nan_value_up = df[up_col_name].dropna().iloc[0]
        # df[up_col_name] = df[up_col_name].fillna(first_non_nan_value_up)
        #
        # first_non_nan_value_down = df[down_col_name].dropna().iloc[0]
        # df[down_col_name] = df[down_col_name].fillna(first_non_nan_value_down)
        df=df.dropna()
        return df

    def lag(self, df, col, coin_symbol, interval, is_price, timeperiod=1):
        if is_price:
            lag_col_name = f"{coin_symbol}_{interval}_lag_{timeperiod}"
        else:
            lag_col_name = f"{col}_lag_{timeperiod}"

        df[lag_col_name] = df[col].shift(timeperiod)

        # Filling NaN values
        # first_non_nan_value = df[lag_col_name].dropna().iloc[0]
        # df[lag_col_name] = df[lag_col_name].fillna(first_non_nan_value)
        df=df.dropna()
        return df
    

#############################################################################

class KlineInd:
    def get(self, df, ind, payloads, coin_symbol, interval):
        ind_name = ind
        payload = payloads
        if 'BOP' == ind_name:

            return self.bop(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'AVGPRICE' == ind_name:

            return self.avgprice(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDL2CROWS' == ind_name:

            return self.cdl2crows(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDL3BLACKCROWS' == ind_name:

            return self.cdl3blackcrows(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDL3INSIDE' == ind_name:

            return self.cdl3inside(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDL3LINESTRIKE' == ind_name:

            return self.cdl3linestrike(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDL3OUTSIDE' == ind_name:

            return self.cdl3outside(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDL3STARSINSOUTH' == ind_name:

            return self.cdl3starsinsouth(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDL3WHITESOLDIERS' == ind_name:

            return self.cdl3whitesoldiers(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLABANDONEDBABY' == ind_name:
            penetration = payload.get('penetration')
            return self.cdlabandonedbaby(df=df, coin_symbol=coin_symbol, interval=interval, penetration=penetration)


        if 'CDLADVANCEBLOCK' == ind_name:

            return self.cdladvanceblock(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLBELTHOLD' == ind_name:

            return self.cdlbelthold(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLBREAKAWAY' == ind_name:

            return self.cdlbreakaway(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLCLOSINGMARUBOZU' == ind_name:

            return self.cdlclosingmarubozu(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLCONCEALBABYSWALL' == ind_name:

            return self.cdlconcealbabyswall(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLCOUNTERATTACK' == ind_name:

            return self.cdlcounterattack(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLDARKCLOUDCOVER' == ind_name:
            penetration = payload.get('penetration')
            return self.cdldarkcloudcover(df=df, coin_symbol=coin_symbol, interval=interval, penetration=penetration)


        if 'CDLDOJI' == ind_name:

            return self.cdldoji(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLDOJISTAR' == ind_name:

            return self.cdldojistar(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLDRAGONFLYDOJI' == ind_name:

            return self.cdldragonflydoji(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLENGULFING' == ind_name:

            return self.cdlengulfing(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLEVENINGDOJISTAR' == ind_name:
            penetration = payload.get('penetration')
            return self.cdleveningdojistar(df=df, coin_symbol=coin_symbol, interval=interval, penetration=penetration)


        if 'CDLEVENINGSTAR' == ind_name:
            penetration = payload.get('penetration')
            return self.cdleveningstar(df=df, coin_symbol=coin_symbol, interval=interval, penetration=penetration)


        if 'CDLGAPSIDESIDEWHITE' == ind_name:

            return self.cdlgapsidesidewhite(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLGRAVESTONEDOJI' == ind_name:

            return self.cdlgravestonedoji(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLHAMMER' == ind_name:

            return self.cdlhammer(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLHANGINGMAN' == ind_name:

            return self.cdlhangingman(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLHARAMI' == ind_name:

            return self.cdlharami(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLHARAMICROSS' == ind_name:

            return self.cdlharamicross(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLHIGHWAVE' == ind_name:

            return self.cdlhighwave(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLHIKKAKE' == ind_name:

            return self.cdlhikkake(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLHIKKAKEMOD' == ind_name:

            return self.cdlhikkakemod(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLHOMINGPIGEON' == ind_name:

            return self.cdlhomingpigeon(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLIDENTICAL3CROWS' == ind_name:

            return self.cdlidentical3crows(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLINNECK' == ind_name:

            return self.cdlinneck(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLINVERTEDHAMMER' == ind_name:

            return self.cdlinvertedhammer(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLKICKING' == ind_name:

            return self.cdlkicking(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLKICKINGBYLENGTH' == ind_name:

            return self.cdlkickingbylength(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLLADDERBOTTOM' == ind_name:

            return self.cdlladderbottom(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLLONGLEGGEDDOJI' == ind_name:

            return self.cdllongleggeddoji(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLLONGLINE' == ind_name:

            return self.cdllongline(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLMARUBOZU' == ind_name:

            return self.cdlmarubozu(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLMATCHINGLOW' == ind_name:

            return self.cdlmatchinglow(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLMATHOLD' == ind_name:
            penetration = payload.get('penetration')
            return self.cdlmathold(df=df, coin_symbol=coin_symbol, interval=interval, penetration=penetration)


        if 'CDLMORNINGDOJISTAR' == ind_name:
            penetration = payload.get('penetration')
            return self.cdlmorningdojistar(df=df, coin_symbol=coin_symbol, interval=interval, penetration=penetration)


        if 'CDLMORNINGSTAR' == ind_name:
            penetration = payload.get('penetration')
            return self.cdlmorningstar(df=df, coin_symbol=coin_symbol, interval=interval, penetration=penetration)


        if 'CDLONNECK' == ind_name:

            return self.cdlonneck(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLPIERCING' == ind_name:

            return self.cdlpiercing(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLRICKSHAWMAN' == ind_name:

            return self.cdlrickshawman(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLRISEFALL3METHODS' == ind_name:

            return self.cdlrisefall3methods(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLSEPARATINGLINES' == ind_name:

            return self.cdlseparatinglines(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLSHOOTINGSTAR' == ind_name:

            return self.cdlshootingstar(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLSHORTLINE' == ind_name:

            return self.cdlshortline(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLSPINNINGTOP' == ind_name:

            return self.cdlspinningtop(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLSTALLEDPATTERN' == ind_name:

            return self.cdlstalledpattern(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLSTICKSANDWICH' == ind_name:

            return self.cdlsticksandwich(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLTAKURI' == ind_name:

            return self.cdltakuri(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLTASUKIGAP' == ind_name:

            return self.cdltasukigap(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLTHRUSTING' == ind_name:

            return self.cdlthrusting(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLTRISTAR' == ind_name:

            return self.cdltristar(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLUNIQUE3RIVER' == ind_name:

            return self.cdlunique3river(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLUPSIDEGAP2CROWS' == ind_name:

            return self.cdlupsidegap2crows(df=df, coin_symbol=coin_symbol, interval=interval)


        if 'CDLXSIDEGAP3METHODS' == ind_name:

            return self.cdlxsidegap3methods(df=df, coin_symbol=coin_symbol, interval=interval)




    def bop(self, df, coin_symbol, interval):
        bop=ta.BOP(df['open'],df['high'],df['low'],df['close'])
        bop_col_name=coin_symbol+"_"+interval+"_bop"
        df[bop_col_name]=bop
        return df


    def avgprice(self, df, coin_symbol, interval):
        avgprice=ta.AVGPRICE(df['open'],df['high'],df['low'],df['close'])
        avgprice_col_name=coin_symbol+"_"+interval+"_avgprice"
        df[avgprice_col_name]=avgprice
        return df


    def cdl2crows(self, df, coin_symbol, interval):
        cdl2crows=ta.CDL2CROWS(df['open'],df['high'],df['low'],df['close'])
        cdl2crows_col_name=coin_symbol+"_"+interval+"_cdl2crows"
        df[cdl2crows_col_name]=cdl2crows
        return df


    def cdl3blackcrows(self, df, coin_symbol, interval):
        cdl3blackcrows=ta.CDL3BLACKCROWS(df['open'],df['high'],df['low'],df['close'])
        cdl3blackcrows_col_name=coin_symbol+"_"+interval+"_cdl3blackcrows"
        df[cdl3blackcrows_col_name]=cdl3blackcrows
        return df


    def cdl3inside(self, df, coin_symbol, interval):
        cdl3inside=ta.CDL3INSIDE(df['open'],df['high'],df['low'],df['close'])
        cdl3inside_col_name=coin_symbol+"_"+interval+"_cdl3inside"
        df[cdl3inside_col_name]=cdl3inside
        return df


    def cdl3linestrike(self, df, coin_symbol, interval):
        cdl3linestrike=ta.CDL3LINESTRIKE(df['open'],df['high'],df['low'],df['close'])
        cdl3linestrike_col_name=coin_symbol+"_"+interval+"_cdl3linestrike"
        df[cdl3linestrike_col_name]=cdl3linestrike
        return df


    def cdl3outside(self, df, coin_symbol, interval):
        cdl3outside=ta.CDL3OUTSIDE(df['open'],df['high'],df['low'],df['close'])
        cdl3outside_col_name=coin_symbol+"_"+interval+"_cdl3outside"
        df[cdl3outside_col_name]=cdl3outside
        return df


    def cdl3starsinsouth(self, df, coin_symbol, interval):
        cdl3starsinsouth=ta.CDL3STARSINSOUTH(df['open'],df['high'],df['low'],df['close'])
        cdl3starsinsouth_col_name=coin_symbol+"_"+interval+"_cdl3starsinsouth"
        df[cdl3starsinsouth_col_name]=cdl3starsinsouth
        return df


    def cdl3whitesoldiers(self, df, coin_symbol, interval):
        cdl3whitesoldiers=ta.CDL3WHITESOLDIERS(df['open'],df['high'],df['low'],df['close'])
        cdl3whitesoldiers_col_name=coin_symbol+"_"+interval+"_cdl3whitesoldiers"
        df[cdl3whitesoldiers_col_name]=cdl3whitesoldiers
        return df


    def cdlabandonedbaby(self, df, coin_symbol, interval, penetration=0):
        cdlabandonedbaby=ta.CDLABANDONEDBABY(df['open'],df['high'],df['low'],df['close'], penetration=penetration)
        cdlabandonedbaby_col_name=coin_symbol+"_"+interval+"_cdlabandonedbaby_" + str(penetration).replace(".", "dot")
        df[cdlabandonedbaby_col_name]=cdlabandonedbaby
        return df


    def cdladvanceblock(self, df, coin_symbol, interval):
        cdladvanceblock=ta.CDLADVANCEBLOCK(df['open'],df['high'],df['low'],df['close'])
        cdladvanceblock_col_name=coin_symbol+"_"+interval+"_cdladvanceblock"
        df[cdladvanceblock_col_name]=cdladvanceblock
        return df


    def cdlbelthold(self, df, coin_symbol, interval):
        cdlbelthold=ta.CDLBELTHOLD(df['open'],df['high'],df['low'],df['close'])
        cdlbelthold_col_name=coin_symbol+"_"+interval+"_cdlbelthold"
        df[cdlbelthold_col_name]=cdlbelthold
        return df


    def cdlbreakaway(self, df, coin_symbol, interval):
        cdlbreakaway=ta.CDLBREAKAWAY(df['open'],df['high'],df['low'],df['close'])
        cdlbreakaway_col_name=coin_symbol+"_"+interval+"_cdlbreakaway"
        df[cdlbreakaway_col_name]=cdlbreakaway
        return df


    def cdlclosingmarubozu(self, df, coin_symbol, interval):
        cdlclosingmarubozu=ta.CDLCLOSINGMARUBOZU(df['open'],df['high'],df['low'],df['close'])
        cdlclosingmarubozu_col_name=coin_symbol+"_"+interval+"_cdlclosingmarubozu"
        df[cdlclosingmarubozu_col_name]=cdlclosingmarubozu
        return df


    def cdlconcealbabyswall(self, df, coin_symbol, interval):
        cdlconcealbabyswall=ta.CDLCONCEALBABYSWALL(df['open'],df['high'],df['low'],df['close'])
        cdlconcealbabyswall_col_name=coin_symbol+"_"+interval+"_cdlconcealbabyswall"
        df[cdlconcealbabyswall_col_name]=cdlconcealbabyswall
        return df


    def cdlcounterattack(self, df, coin_symbol, interval):
        cdlcounterattack=ta.CDLCOUNTERATTACK(df['open'],df['high'],df['low'],df['close'])
        cdlcounterattack_col_name=coin_symbol+"_"+interval+"_cdlcounterattack"
        df[cdlcounterattack_col_name]=cdlcounterattack
        return df


    def cdldarkcloudcover(self, df, coin_symbol, interval, penetration=0):
        cdldarkcloudcover=ta.CDLDARKCLOUDCOVER(df['open'],df['high'],df['low'],df['close'], penetration=penetration)
        cdldarkcloudcover_col_name=coin_symbol+"_"+interval+"_cdldarkcloudcover_" + str(penetration).replace(".", "dot")
        df[cdldarkcloudcover_col_name]=cdldarkcloudcover
        return df


    def cdldoji(self, df, coin_symbol, interval):
        cdldoji=ta.CDLDOJI(df['open'],df['high'],df['low'],df['close'])
        cdldoji_col_name=coin_symbol+"_"+interval+"_cdldoji"
        df[cdldoji_col_name]=cdldoji
        return df


    def cdldojistar(self, df, coin_symbol, interval):
        cdldojistar=ta.CDLDOJISTAR(df['open'],df['high'],df['low'],df['close'])
        cdldojistar_col_name=coin_symbol+"_"+interval+"_cdldojistar"
        df[cdldojistar_col_name]=cdldojistar
        return df


    def cdldragonflydoji(self, df, coin_symbol, interval):
        cdldragonflydoji=ta.CDLDRAGONFLYDOJI(df['open'],df['high'],df['low'],df['close'])
        cdldragonflydoji_col_name=coin_symbol+"_"+interval+"_cdldragonflydoji"
        df[cdldragonflydoji_col_name]=cdldragonflydoji
        return df


    def cdlengulfing(self, df, coin_symbol, interval):
        cdlengulfing=ta.CDLENGULFING(df['open'],df['high'],df['low'],df['close'])
        cdlengulfing_col_name=coin_symbol+"_"+interval+"_cdlengulfing"
        df[cdlengulfing_col_name]=cdlengulfing
        return df


    def cdleveningdojistar(self, df, coin_symbol, interval, penetration=0):
        cdleveningdojistar=ta.CDLEVENINGDOJISTAR(df['open'],df['high'],df['low'],df['close'], penetration=penetration)
        cdleveningdojistar_col_name=coin_symbol+"_"+interval+"_cdleveningdojistar_" + str(penetration).replace(".", "dot")
        df[cdleveningdojistar_col_name]=cdleveningdojistar
        return df


    def cdleveningstar(self, df, coin_symbol, interval, penetration=0):
        cdleveningstar=ta.CDLEVENINGSTAR(df['open'],df['high'],df['low'],df['close'], penetration=penetration)
        cdleveningstar_col_name=coin_symbol+"_"+interval+"_cdleveningstar_" + str(penetration).replace(".", "dot")
        df[cdleveningstar_col_name]=cdleveningstar
        return df


    def cdlgapsidesidewhite(self, df, coin_symbol, interval):
        cdlgapsidesidewhite=ta.CDLGAPSIDESIDEWHITE(df['open'],df['high'],df['low'],df['close'])
        cdlgapsidesidewhite_col_name=coin_symbol+"_"+interval+"_cdlgapsidesidewhite"
        df[cdlgapsidesidewhite_col_name]=cdlgapsidesidewhite
        return df


    def cdlgravestonedoji(self, df, coin_symbol, interval):
        cdlgravestonedoji=ta.CDLGRAVESTONEDOJI(df['open'],df['high'],df['low'],df['close'])
        cdlgravestonedoji_col_name=coin_symbol+"_"+interval+"_cdlgravestonedoji"
        df[cdlgravestonedoji_col_name]=cdlgravestonedoji
        return df


    def cdlhammer(self, df, coin_symbol, interval):
        cdlhammer=ta.CDLHAMMER(df['open'],df['high'],df['low'],df['close'])
        cdlhammer_col_name=coin_symbol+"_"+interval+"_cdlhammer"
        df[cdlhammer_col_name]=cdlhammer
        return df


    def cdlhangingman(self, df, coin_symbol, interval):
        cdlhangingman=ta.CDLHANGINGMAN(df['open'],df['high'],df['low'],df['close'])
        cdlhangingman_col_name=coin_symbol+"_"+interval+"_cdlhangingman"
        df[cdlhangingman_col_name]=cdlhangingman
        return df


    def cdlharami(self, df, coin_symbol, interval):
        cdlharami=ta.CDLHARAMI(df['open'],df['high'],df['low'],df['close'])
        cdlharami_col_name=coin_symbol+"_"+interval+"_cdlharami"
        df[cdlharami_col_name]=cdlharami
        return df


    def cdlharamicross(self, df, coin_symbol, interval):
        cdlharamicross=ta.CDLHARAMICROSS(df['open'],df['high'],df['low'],df['close'])
        cdlharamicross_col_name=coin_symbol+"_"+interval+"_cdlharamicross"
        df[cdlharamicross_col_name]=cdlharamicross
        return df


    def cdlhighwave(self, df, coin_symbol, interval):
        cdlhighwave=ta.CDLHIGHWAVE(df['open'],df['high'],df['low'],df['close'])
        cdlhighwave_col_name=coin_symbol+"_"+interval+"_cdlhighwave"
        df[cdlhighwave_col_name]=cdlhighwave
        return df


    def cdlhikkake(self, df, coin_symbol, interval):
        cdlhikkake=ta.CDLHIKKAKE(df['open'],df['high'],df['low'],df['close'])
        cdlhikkake_col_name=coin_symbol+"_"+interval+"_cdlhikkake"
        df[cdlhikkake_col_name]=cdlhikkake
        return df


    def cdlhikkakemod(self, df, coin_symbol, interval):
        cdlhikkakemod=ta.CDLHIKKAKEMOD(df['open'],df['high'],df['low'],df['close'])
        cdlhikkakemod_col_name=coin_symbol+"_"+interval+"_cdlhikkakemod"
        df[cdlhikkakemod_col_name]=cdlhikkakemod
        return df


    def cdlhomingpigeon(self, df, coin_symbol, interval):
        cdlhomingpigeon=ta.CDLHOMINGPIGEON(df['open'],df['high'],df['low'],df['close'])
        cdlhomingpigeon_col_name=coin_symbol+"_"+interval+"_cdlhomingpigeon"
        df[cdlhomingpigeon_col_name]=cdlhomingpigeon
        return df


    def cdlidentical3crows(self, df, coin_symbol, interval):
        cdlidentical3crows=ta.CDLIDENTICAL3CROWS(df['open'],df['high'],df['low'],df['close'])
        cdlidentical3crows_col_name=coin_symbol+"_"+interval+"_cdlidentical3crows"
        df[cdlidentical3crows_col_name]=cdlidentical3crows
        return df


    def cdlinneck(self, df, coin_symbol, interval):
        cdlinneck=ta.CDLINNECK(df['open'],df['high'],df['low'],df['close'])
        cdlinneck_col_name=coin_symbol+"_"+interval+"_cdlinneck"
        df[cdlinneck_col_name]=cdlinneck
        return df


    def cdlinvertedhammer(self, df, coin_symbol, interval):
        cdlinvertedhammer=ta.CDLINVERTEDHAMMER(df['open'],df['high'],df['low'],df['close'])
        cdlinvertedhammer_col_name=coin_symbol+"_"+interval+"_cdlinvertedhammer"
        df[cdlinvertedhammer_col_name]=cdlinvertedhammer
        return df


    def cdlkicking(self, df, coin_symbol, interval):
        cdlkicking=ta.CDLKICKING(df['open'],df['high'],df['low'],df['close'])
        cdlkicking_col_name=coin_symbol+"_"+interval+"_cdlkicking"
        df[cdlkicking_col_name]=cdlkicking
        return df


    def cdlkickingbylength(self, df, coin_symbol, interval):
        cdlkickingbylength=ta.CDLKICKINGBYLENGTH(df['open'],df['high'],df['low'],df['close'])
        cdlkickingbylength_col_name=coin_symbol+"_"+interval+"_cdlkickingbylength"
        df[cdlkickingbylength_col_name]=cdlkickingbylength
        return df


    def cdlladderbottom(self, df, coin_symbol, interval):
        cdlladderbottom=ta.CDLLADDERBOTTOM(df['open'],df['high'],df['low'],df['close'])
        cdlladderbottom_col_name=coin_symbol+"_"+interval+"_cdlladderbottom"
        df[cdlladderbottom_col_name]=cdlladderbottom
        return df


    def cdllongleggeddoji(self, df, coin_symbol, interval):
        cdllongleggeddoji=ta.CDLLONGLEGGEDDOJI(df['open'],df['high'],df['low'],df['close'])
        cdllongleggeddoji_col_name=coin_symbol+"_"+interval+"_cdllongleggeddoji"
        df[cdllongleggeddoji_col_name]=cdllongleggeddoji
        return df


    def cdllongline(self, df, coin_symbol, interval):
        cdllongline=ta.CDLLONGLINE(df['open'],df['high'],df['low'],df['close'])
        cdllongline_col_name=coin_symbol+"_"+interval+"_cdllongline"
        df[cdllongline_col_name]=cdllongline
        return df


    def cdlmarubozu(self, df, coin_symbol, interval):
        cdlmarubozu=ta.CDLMARUBOZU(df['open'],df['high'],df['low'],df['close'])
        cdlmarubozu_col_name=coin_symbol+"_"+interval+"_cdlmarubozu"
        df[cdlmarubozu_col_name]=cdlmarubozu
        return df


    def cdlmatchinglow(self, df, coin_symbol, interval):
        cdlmatchinglow=ta.CDLMATCHINGLOW(df['open'],df['high'],df['low'],df['close'])
        cdlmatchinglow_col_name=coin_symbol+"_"+interval+"_cdlmatchinglow"
        df[cdlmatchinglow_col_name]=cdlmatchinglow
        return df


    def cdlmathold(self, df, coin_symbol, interval, penetration=0):
        cdlmathold=ta.CDLMATHOLD(df['open'],df['high'],df['low'],df['close'], penetration=penetration)
        cdlmathold_col_name=coin_symbol+"_"+interval+"_cdlmathold_" + str(penetration).replace(".", "dot")
        df[cdlmathold_col_name]=cdlmathold
        return df


    def cdlmorningdojistar(self, df, coin_symbol, interval, penetration=0):
        cdlmorningdojistar=ta.CDLMORNINGDOJISTAR(df['open'],df['high'],df['low'],df['close'], penetration=penetration)
        cdlmorningdojistar_col_name=coin_symbol+"_"+interval+"_cdlmorningdojistar_" + str(penetration).replace(".", "dot")
        df[cdlmorningdojistar_col_name]=cdlmorningdojistar
        return df


    def cdlmorningstar(self, df, coin_symbol, interval, penetration=0):
        cdlmorningstar=ta.CDLMORNINGSTAR(df['open'],df['high'],df['low'],df['close'], penetration=penetration)
        cdlmorningstar_col_name=coin_symbol+"_"+interval+"_cdlmorningstar_" + str(penetration).replace(".", "dot")
        df[cdlmorningstar_col_name]=cdlmorningstar
        return df


    def cdlonneck(self, df, coin_symbol, interval):
        cdlonneck=ta.CDLONNECK(df['open'],df['high'],df['low'],df['close'])
        cdlonneck_col_name=coin_symbol+"_"+interval+"_cdlonneck"
        df[cdlonneck_col_name]=cdlonneck
        return df


    def cdlpiercing(self, df, coin_symbol, interval):
        cdlpiercing=ta.CDLPIERCING(df['open'],df['high'],df['low'],df['close'])
        cdlpiercing_col_name=coin_symbol+"_"+interval+"_cdlpiercing"
        df[cdlpiercing_col_name]=cdlpiercing
        return df


    def cdlrickshawman(self, df, coin_symbol, interval):
        cdlrickshawman=ta.CDLRICKSHAWMAN(df['open'],df['high'],df['low'],df['close'])
        cdlrickshawman_col_name=coin_symbol+"_"+interval+"_cdlrickshawman"
        df[cdlrickshawman_col_name]=cdlrickshawman
        return df


    def cdlrisefall3methods(self, df, coin_symbol, interval):
        cdlrisefall3methods=ta.CDLRISEFALL3METHODS(df['open'],df['high'],df['low'],df['close'])
        cdlrisefall3methods_col_name=coin_symbol+"_"+interval+"_cdlrisefall3methods"
        df[cdlrisefall3methods_col_name]=cdlrisefall3methods
        return df


    def cdlseparatinglines(self, df, coin_symbol, interval):
        cdlseparatinglines=ta.CDLSEPARATINGLINES(df['open'],df['high'],df['low'],df['close'])
        cdlseparatinglines_col_name=coin_symbol+"_"+interval+"_cdlseparatinglines"
        df[cdlseparatinglines_col_name]=cdlseparatinglines
        return df


    def cdlshootingstar(self, df, coin_symbol, interval):
        cdlshootingstar=ta.CDLSHOOTINGSTAR(df['open'],df['high'],df['low'],df['close'])
        cdlshootingstar_col_name=coin_symbol+"_"+interval+"_cdlshootingstar"
        df[cdlshootingstar_col_name]=cdlshootingstar
        return df


    def cdlshortline(self, df, coin_symbol, interval):
        cdlshortline=ta.CDLSHORTLINE(df['open'],df['high'],df['low'],df['close'])
        cdlshortline_col_name=coin_symbol+"_"+interval+"_cdlshortline"
        df[cdlshortline_col_name]=cdlshortline
        return df


    def cdlspinningtop(self, df, coin_symbol, interval):
        cdlspinningtop=ta.CDLSPINNINGTOP(df['open'],df['high'],df['low'],df['close'])
        cdlspinningtop_col_name=coin_symbol+"_"+interval+"_cdlspinningtop"
        df[cdlspinningtop_col_name]=cdlspinningtop
        return df


    def cdlstalledpattern(self, df, coin_symbol, interval):
        cdlstalledpattern=ta.CDLSTALLEDPATTERN(df['open'],df['high'],df['low'],df['close'])
        cdlstalledpattern_col_name=coin_symbol+"_"+interval+"_cdlstalledpattern"
        df[cdlstalledpattern_col_name]=cdlstalledpattern
        return df


    def cdlsticksandwich(self, df, coin_symbol, interval):
        cdlsticksandwich=ta.CDLSTICKSANDWICH(df['open'],df['high'],df['low'],df['close'])
        cdlsticksandwich_col_name=coin_symbol+"_"+interval+"_cdlsticksandwich"
        df[cdlsticksandwich_col_name]=cdlsticksandwich
        return df


    def cdltakuri(self, df, coin_symbol, interval):
        cdltakuri=ta.CDLTAKURI(df['open'],df['high'],df['low'],df['close'])
        cdltakuri_col_name=coin_symbol+"_"+interval+"_cdltakuri"
        df[cdltakuri_col_name]=cdltakuri
        return df


    def cdltasukigap(self, df, coin_symbol, interval):
        cdltasukigap=ta.CDLTASUKIGAP(df['open'],df['high'],df['low'],df['close'])
        cdltasukigap_col_name=coin_symbol+"_"+interval+"_cdltasukigap"
        df[cdltasukigap_col_name]=cdltasukigap
        return df


    def cdlthrusting(self, df, coin_symbol, interval):
        cdlthrusting=ta.CDLTHRUSTING(df['open'],df['high'],df['low'],df['close'])
        cdlthrusting_col_name=coin_symbol+"_"+interval+"_cdlthrusting"
        df[cdlthrusting_col_name]=cdlthrusting
        return df


    def cdltristar(self, df, coin_symbol, interval):
        cdltristar=ta.CDLTRISTAR(df['open'],df['high'],df['low'],df['close'])
        cdltristar_col_name=coin_symbol+"_"+interval+"_cdltristar"
        df[cdltristar_col_name]=cdltristar
        return df


    def cdlunique3river(self, df, coin_symbol, interval):
        cdlunique3river=ta.CDLUNIQUE3RIVER(df['open'],df['high'],df['low'],df['close'])
        cdlunique3river_col_name=coin_symbol+"_"+interval+"_cdlunique3river"
        df[cdlunique3river_col_name]=cdlunique3river
        return df


    def cdlupsidegap2crows(self, df, coin_symbol, interval):
        cdlupsidegap2crows=ta.CDLUPSIDEGAP2CROWS(df['open'],df['high'],df['low'],df['close'])
        cdlupsidegap2crows_col_name=coin_symbol+"_"+interval+"_cdlupsidegap2crows"
        df[cdlupsidegap2crows_col_name]=cdlupsidegap2crows
        return df


    def cdlxsidegap3methods(self, df, coin_symbol, interval):
        cdlxsidegap3methods=ta.CDLXSIDEGAP3METHODS(df['open'],df['high'],df['low'],df['close'])
        cdlxsidegap3methods_col_name=coin_symbol+"_"+interval+"_cdlxsidegap3methods"
        df[cdlxsidegap3methods_col_name]=cdlxsidegap3methods
        return df

