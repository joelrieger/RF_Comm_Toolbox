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
    
    #s_arr=np.arange(-M*Ns,M*Ns+1)
    s_arr=np.linspace(-M*Ns,M*Ns,num=2*Ns*M+1)
    ir=np.zeros(len(s_arr))

    
    for i,t in enumerate(s_arr):
       if abs(1 - 16*b**2*(t/Ns)**2) == 0:
           ir[i] = 0.5*((1.0+b)*sin((1.0+b)*pi/(4.0*b))-(1.0-b)*cos((1.0-b)*pi/(4.0*b))+(4.0*b)/pi*sin((1.0-b)*pi/(4.0*b)))
       else:
           ir[i] = 4.0*b/(pi*(1.0-16.0*b**2*(t/Ns)**2))
           ir[i] = ir[i]*(np.cos((1.0+b)*pi*t/Ns)+sinc((1.0-b)*t/Ns)*(1.0-b)*pi/(4.0*b))
           
    return ir


if __name__=='__main__':
    from matplotlib import pyplot as plt
    from digital_comm import *
    
    ir_rc=root_raised_cos(6.0,0.35)
    plt.plot(ir_rc)

    rrc_ir=sqrt_rc_imp(6.0,0.35)
    plt.plot(rrc_ir)

    #diff=[abs(a-b) for a,b in zip(ir_rc,rrc_ir)]
    
    plt.plot(ir_rc)
    plt.plot(rrc_ir)
    plt.show()
