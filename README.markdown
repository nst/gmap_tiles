### Download Google Maps tiles

Edit `download_tiles.py` to specify the area and the zoom level you want.

    zoom = 15

    lat_start, lon_start = 46.53, 6.6
    lat_stop, lon_stop = 46.49, 6.7

    satellite = True    # roads if false

You can easily find coordinates with [http://itouchmap.com/latlong.html](http://itouchmap.com/latlong.html).

Then, run `$ python download_tiles.py` and get individual tiles:

    ...
    15_16989_11588_s.jpg
    15_16989_11589_s.jpg
    15_16989_11590_s.jpg
    ...

### Merge Google Maps tiles

Edit `merge_tiles.py` to specify the area and the zoom level you want, it's just the same as before.

    zoom = 15

    lat_start, lon_start = 46.53, 6.6
    lat_stop, lon_stop = 46.49, 6.7

    satellite = True    # roads if false

Then, run `$ python merge_tiles.py` and get `map_s.jpg` for satellite or `map_r.png` for roads.

![Google Maps Tiles](https://raw.github.com/nst/gmap_tiles/master/gmap.png)
