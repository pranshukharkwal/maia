import ephem
from skyfield.api import position_of_radec, load_constellation_map
from skyfield import api
import datetime
from skyfield.api import load
import datetime
import pytz

year, month, date, hour, mins, lat, lon, azi, alt=map(float,input().split())

tz = pytz.timezone('Asia/Kolkata')
dt = datetime.datetime(int(year), int(month), int(date), int(hour), int(mins), tzinfo=tz)
t1 = dt.astimezone(pytz.utc)
ts = api.load.timescale()
y,m,d,h,mns=t1.year,t1.month,t1.date,t1.hour,t1.minute
t = ts.utc(y,m,h,mns)

topos = api.Topos(latitude_degrees=lat, longitude_degrees=lon)
observer = topos.at(t)
pos = observer.from_altaz(alt_degrees=alt, az_degrees=azi)
ra, dec, distance = pos.radec()
constellation_at = load_constellation_map()
coord = position_of_radec(ra.hours,dec.degrees)
print(constellation_at(coord))
print("RA = ",ra)
print("Dec = ",dec)

t2=(2020,11,14,22,00)
topos = api.Topos(latitude_degrees=31.77, longitude_degrees=76.98) #coordinates of iit mandi
observer = topos.at(t)
pos = observer.from_altaz(alt_degrees=90, az_degrees=0)
ra, dec, distance = pos.radec()
constellation_at = load_constellation_map()
coord = position_of_radec(ra.hours,dec.degrees)
print("Constellation right above Lucy: ",constellation_at(coord))

pos = observer.from_altaz(alt_degrees=270, az_degrees=0)
ra, dec, distance = pos.radec()
constellation_at = load_constellation_map()
coord = position_of_radec(ra.hours,dec.degrees)
print("Constellation on the other side of the planet: ",constellation_at(coord))

dirs=[0,90,270,315,45,135]
for i in range(6):
    alt=0
    azi=dirs[i]
    pos = observer.from_altaz(alt_degrees=alt, az_degrees=azi)
    ra, dec, distance = pos.radec()
    constellation_at = load_constellation_map()
    coord = position_of_radec(ra.hours,dec.degrees)
    print(constellation_at(coord))

