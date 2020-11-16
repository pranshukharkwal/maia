import numpy as np
from astropy import units as u
from astropy import constants as const

M=const.M_earth
G=const.G
c=const.c
R=const.R_earth
day=24*60*60*u.second

for i in range(int(input())):
    r=float(input())*u.meter
    t_d=day*(np.sqrt(1-((3*G*M)/((c**2)*(r-R)))))
    td=day-t_d
    print("{0:0.05f}".format(td))
