#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 08:28:38 2023

@author: alumno
"""

from scipy import signal as sig
import matplotlib.pyplot as plt
import numpy as np

from pytc2.sistemas_lineales import plot_plantilla, group_delay

cant_coef = 661
fs = 1000

# plantilla
ripple = 0.5 # dB
attenuation = 40 # dB

frecs = [0.0,         0.4,     0.5, 0.6,     1.0]
gains = [-attenuation, -ripple, 0.0, -ripple, -attenuation]

den = 1

num_firls = sig.firls(cant_coef, frecs, gains, fs=fs)
_,  hh_firls = sig.freqz(num_firls, den)