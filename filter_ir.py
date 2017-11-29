def raised_cos(Ns,b,M=6):
    import numpy as np
    from numpy import pi,sinc,cos,sin

    s_arr=np.linspace(-M*Ns,M*Ns,num=2*Ns*M+1)
    ir=np.zeros(len(s_arr))
    
    for i,t in enumerate(s_arr):
        if (1-(2*b*t/Ns)**2)==0:
            ir[i]=pi/(4*Ns)*sinc(1/(2*b))
        else:
            ir[i]=1.0/Ns*sinc(pi*t/Ns)*cos(pi*b*t/Ns)/(1-(2*b*t/Ns)**2) 
            #ir[i]=sin(pi*t/Ns)/(pi*t/Ns)*cos(pi*b*t/Ns)/(1-(2*b*t/Ns)**2)

    return ir

def root_raised_cos(Ns,b,M=6):
    import numpy as np
    from numpy import pi,sinc,cos,sin,sqrt
    
    s_arr=np.linspace(-M*Ns,M*Ns,num=2*Ns*M+1)
    ir=np.zeros(len(s_arr))
    
    for i,t in enumerate(s_arr):
        if t==0:
            ir[i]=1/Ns*(1.0+b*(4/pi-1.0))
        elif (1-(2*b*t/Ns)**2)==0:
            ir[i]=b/(Ns*sqrt(2))*((1.0+2/pi)*sin(pi/(4*b))+(1.0-2.0/pi)*cos(pi/(4*b)))
        else:
            ir[i]=1.0/Ns*(sin(pi*t/Ns*(1.0-b))+4*b*t/Ns*cos(pi*t/Ns*(1.0+b)))/(pi*t/Ns*(1.0-(4*b*t/Ns)**2))

    return ir
