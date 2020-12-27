import math
tooo = int(input())
for i in range(tooo):
    re , rs = map(float , input().split())
    t=86400
    g=6.673*math.pow(10,-11)
    me=5.972*math.pow(10,24)
    ms=1.989*math.pow(10,30)
    re1=g*me/re
    rs1=g*ms/rs
    ve=math.sqrt(re1)
    vs=math.sqrt(rs1)
    c=3*math.pow(10,8)
    re2=1-((ve*ve)/(c*c))
    rs2=1-((vs*vs)/(c*c))
    te1=t/(math.sqrt(re2))
    ts1=t/(math.sqrt(rs2))

    rsh=2*g*me/(c*c)
    y=1-(1.5*rsh/re)
    to=t*math.sqrt(y)

    rsh=2*g*ms/(c*c)
    y1=1-(1.5*rsh/rs)
    to1=t*math.sqrt(y1)

    print("{:.5e}".format(ts1-to1-(te1-to)))
