import numpy as np

from matplotlib import pyplot as plt
from scipy import signal
from random import randint
from sampling import *
from filter_ir import *

if __name__=='__main__':

    """
    Generate Modulated Signal
    """
    sample_rate=32e3
    samples_per_symbol=8
    m=4 #constelation size
    num_sym=64 #number of symbols

    symbol_map={0:(-1.0,-1.0),1:(-1.0,1.0),2:(1.0,-1.0),3:(1.0,1.0)}
    
    data=np.array([randint(0,m-1) for tmp in range(num_sym)])
    rrc_ir=root_raised_cos(samples_per_symbol,0.35,M=6)    

    IQ_n1=np.pad(np.array([symbol_map[x][0]+symbol_map[x][1]*1j for x in data]),10,mode='constant')
    IQ_n2=upsample(IQ_n1,samples_per_symbol)

    #Apply Tx root-raised cosine
    IQ_n3=signal.convolve(IQ_n2,rrc_ir,mode='same')


    """
    Intentionally delay signal by random value
    """
    rand=10.1 #Not so random for now.
    Ns=np.arange(0,len(IQ_n3))
    IQ_n4=sinc_interp(IQ_n3,Ns-rand,Ns)
    
    #Apply Rx root-raised cosine
    IQ_n5a=signal.convolve(IQ_n4,rrc_ir,mode='same')/samples_per_symbol
    IQ_n5b=signal.convolve(IQ_n3,rrc_ir,mode='same')/samples_per_symbol

    plt.plot(Ns,IQ_n5a.real)
    plt.plot(Ns,IQ_n5b.real)

    plt.show()

    
