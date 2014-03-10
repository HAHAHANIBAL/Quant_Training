#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
from math import *
from scipy.stats import norm
#standard normal cdf
#alternative way of doing this: from scipy.stats import norm
#norm.cdf(x)


# Black Sholes Function


def BlackSholes(CallPutFlag,S,K,T,r,v):
#r=risk free rate, T=time to maturity, S=spot price of the asset, CallPutflag=call-put parity, v=volatility, K=strike price
    d1 = (log(S/K)+(r+v**2/2)*T)/(v*sqrt(T))
    d2 = d1-v*sqrt(T)
    if CallPutFlag=='c':
        return S*norm.cdf(d1)-K*exp(-r*T)*norm.cdf(d2)
    else:
        return K*exp(-r*T)*norm.cdf(-d2)-S*norm.cdf(-d1)
