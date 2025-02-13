import pandas as pd
import talib as ta
from Cycle_Indicators import *
from Math_Operators import *
from Math_Transform import *
from Pattern_Recognition import *
from Price_Transform import *
from Statistic_Functions import *
from Volatility_Indicators import *
from Volume_Indicators import *
from Momentum_Indicators import *
from Overlap_Studies import *



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
