from math import log10 as log10

class power(object):
    def __init__(self,pwr=0.0,sys='log'):
        if sys=='log':
            self.lin=1e-3*10**(pwr/10.0)
            self.log=pwr
        elif sys=='lin':
            self.lin=pwr
            self.log=10.0*log10(1000.0*pwr)
        else:
            print "Error: system not valid. Expected 'lin' or 'log'"
            return None

class mag(object):
    def __init__(self,xmag=0.0,sys='log'):
        if sys=='log':
            self.lin=10**(xmag/10.0)
            self.log=xmag
        elif sys=='lin':
            self.lin=xmag
            self.log=10.0*log10(xmag)
        else:
            print "Error: system not valid. Expected 'lin' or 'log'"
            return None

def logpwr(pwr):
    return power(pwr=float(pwr),sys='log')

def linpwr(pwr):
    return power(pwr=float(pwr),sys='lin')

def logmag(X):
    return mag(xmag=float(X),sys='log')

def linmag(X):
    return mag(xmag=float(X),sys='lin')

class RFGainBlock(object):
    def __init__(self,gain=0.0,NF=0.0,OIP=1000.0):
        self.gain=logmag(gain)
        self.NF=logmag(NF)
        self.OIP=logpwr(OIP)
        self.IIP=logpwr(self.OIP.log-self.gain.log)

    def __add__(a,b):
        #In the Rx Chain, A is before B. A+B != B+A
        
        newGain=logmag(a.gain.log+b.gain.log)
        newOIP=linpwr((1/(b.gain.lin*a.OIP.lin)+1/(b.OIP.lin))**(-1))
        newNF=linmag(a.NF.lin+(b.NF.lin-1.0)/(a.gain.lin))
        
        combined=RFGainBlock(gain=newGain.log,NF=newNF.log,OIP=newOIP.log)
        
        return combined

def LinearDynamicRange(RFChain):
    pass

def SpuriousFreeDynamicRange(RFChain):
    pass

def Atten(gain=-3.0,Tatt=25.0,T0=25.0):
    linGain=10**(gain/10.0)
    NF=linmag(1.0+(1.0/linGain-1)*Tatt/T0)
    
    return RFGainBlock(gain=gain,NF=NF.log)

if __name__=='__main__':
    A=RFGainBlock(gain=20.0,NF=1.3,OIP=22.0)
    B=RFGainBlock(gain=-6.0,NF=5.0,OIP=7.0)

    C=A+B
    
    print "Gain:", C.gain.log
    print "OIP:", C.OIP.log
    print "NF:", C.NF.log
    D=Atten(-3.0)
