from sampling import *
from filter_ir import *

from random import randint
from scipy import signal
from matplotlib import pyplot as plt

import numpy as np

pad_symbols=5
sample_rate=32e3
samples_per_symbol=12
m=4 #constelation size
num_sym=16 #number of symbols

symbol_map={0:(-1.0,-1.0),1:(-1.0,1.0),2:(1.0,-1.0),3:(1.0,1.0)}

rrc_impulse=root_raised_cos(samples_per_symbol,0.35,M=6)
data=np.array([randint(0,m-1) for tmp in range(num_sym)])


IQ_n1=np.pad(np.array([symbol_map[x][0]+symbol_map[x][1]*1j for x in data]),pad_symbols,mode='constant')
IQ_n2=upsample(IQ_n1,samples_per_symbol)

IQ_n3=signal.convolve(IQ_n2,rrc_impulse,mode='same')
IQ_n4=signal.convolve(IQ_n3,rrc_impulse,mode='same')/samples_per_symbol

#plt.stem(IQ_n2.real)
plt.plot(IQ_n4.real)
plt.show()
