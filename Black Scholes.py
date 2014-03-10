#!/usr/bin/python
#-*- coding: utf-8 -*-
#author=moc
from math import *

#standard normal cdf
#alternative way of doing this: from scipy.stats import norm
#norm.cdf(x)


def cdf(X):
    (a1,a2,a3,a4,a5) = (0.31938153,-0.356563782,1.781477937,-1.821255978,1.330274429)
    L = abs(X)
    K = 1.0 / (1.0 + 0.2316419 * L)
    w = 1.0 - 1.0 / sqrt(2*pi)*exp(-L*L/2.) * (a1*K + a2*K*K + a3*pow(K,3) +
    a4*pow(K,4) + a5*pow(K,5))
    if X<0:
        w = 1.0-w
    return w

# Black Sholes Function


def BlackSholes(CallPutFlag,S,K,T,r,v):
#r=risk free rate, T=time to maturity, S=spot price of the asset, CallPutflag=call-put parity, v=volatility, K=strike price
    d1 = (log(S/K)+(r+v**2/2)*T)/(v*sqrt(T))
    d2 = d1-v*sqrt(T)
    if CallPutFlag=='c':
        return S*cdf(d1)-K*exp(-r*T)*cdf(d2)
    else:
        return K*exp(-r*T)*cdf(-d2)-S*cdf(-d1)
