
def upsample(x,M):
    import numpy as np
    
    output = np.hstack((x.reshape(len(x),1),np.zeros((len(x),M-1))))
    return output.flatten()

def sinc_interp(x, s, u):
    """
    Taken from endolith's github
    
    Interpolates x, sampled at "s" instants
    Output y is sampled at "u" instants ("u" for "upsampled")
    
    from Matlab:
    http://phaseportrait.blogspot.com/2008/06/sinc-interpolation-in-matlab.html        
    """
    
    import numpy as np
    
    assert len(x) == len(s), 'x and s must be the same length'
    
    # Find the period    
    T = s[1] - s[0]
    
    sincM = np.tile(u, (len(s), 1)) - np.tile(s[:, np.newaxis], (1, len(u)))
    y = np.dot(x, np.sinc(sincM/T))
    return y


if __name__=='__main__':
    import numpy as np

    from matplotlib import pyplot as plt
    from scipy import signal
    from random import randint

    from filter_ir import *
    
    sample_rate=32e3
    samples_per_symbol=8
    m=4 #constelation size
    num_sym=64 #number of symbols

    symbol_map={0:(-1.0,-1.0),1:(-1.0,1.0),2:(1.0,-1.0),3:(1.0,1.0)}

    rrc_ir=root_raised_cos(samples_per_symbol,0.35,M=6)    
    
    data=np.array([randint(0,m-1) for tmp in range(num_sym)])
    IQ_n1=np.pad(np.array([symbol_map[x][0]+symbol_map[x][1]*1j for x in data]),10,mode='constant')
    
    IQ_n2=upsample(IQ_n1,samples_per_symbol)

    IQ_n3=signal.convolve(IQ_n2,rrc_ir,mode='same')
    IQ_n4=signal.convolve(IQ_n3,rrc_ir,mode='same')/samples_per_symbol

    Ns=np.arange(0,len(IQ_n4))
    
    u=np.linspace(0,len(Ns),num=len(Ns))
    Y=sinc_interp(IQ_n4,Ns-15.1,u)

    plt.plot(Ns,IQ_n4.real)
    plt.plot(u,Y.real)
    plt.show()
    
