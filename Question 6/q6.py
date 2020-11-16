import numpy as np
from astropy import units as u
from astropy import constants as const

Rs=const.R_sun
Re=const.R_earth
Ms=const.M_sun
Me=const.M_earth
G=const.G
c=const.c
day=24*60*60*u.second

for i in range(int(input())):
    re,rs=map(float,input().split())
    re,rs=re*u.meter,rs*u.meter
    t_d1=day*(np.sqrt(1-((3*G*Me)/((c**2)*(re-Re)))))
    td1=day-t_d1
    t_d2=day*(np.sqrt(1-((3*G*Ms)/((c**2)*(rs-Rs)))))
    td2=day-t_d2
    print("{0:0.05f}".format(abs(td1-td2)))
