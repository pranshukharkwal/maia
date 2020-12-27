import math
tooo = int(input())
for i in range(tooo):
    r=float(input())
    t=86400
    g=6.673*math.pow(10,-11)
    m=5.972*math.pow(10,24)
    U=g*m/r
    v=math.sqrt(U)
    
    c=2.9979*math.pow(10,8)
    r2=1-((v*v)/(c*c))
    t1=t/(math.sqrt(r2))
    
    rsh=2*g*m/(c*c)
    y=1-(1.5*rsh/r)
    to=t*math.sqrt(y)
    
    ve=math.sqrt(2*U)
    be=ve/c
    b=v/c
    b11=460/c
    x=1-((b*b) + (be*be) + ((b11*b11*be*be)/(1-(be*be))))
    tf=t/(math.sqrt(x))
    print("{:.5e}".format(tf-t+t-to+t1-t))
