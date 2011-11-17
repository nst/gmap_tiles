# http://oregonarc.com/2011/02/command-line-tile-cutter-for-google-maps-improved/
# http://media.oregonarc.com/fish/tile.py

import math

def latlon2px(z,lat,lon):
    x = 2**z*(lon+180)/360*256
    y = -(.5*math.log((1+math.sin(math.radians(lat)))/(1-math.sin(math.radians(lat))))/math.pi-1)*256*2**(z-1)
    return x,y

def latlon2xy(z,lat,lon):
    x,y = latlon2px(z,lat,lon)
    x = int(x/256)#,int(x%256)
    y = int(y/256)#,int(y%256)
    return x,y
