# AUTOGENERATED! DO NOT EDIT! File to edit: 01_dems.ipynb (unless otherwise specified).

__all__ = ['LOLA_DEM']

# Cell
from dataclasses import dataclass
from pathlib import Path

import xarray as xr

from trex_diviner_pipeline import core


class LOLA_DEM:
    root = Path("/luna4/maye/dems")
    fnames = {
        "data": "ldem_128_jp2.tif",
        "slope": "ldem_128_slope_percent.tif",
        "aspect": "ldem_128_aspect.tif",
    }

    def __init__(self, lat_limit=None):
        self.lat_limit = lat_limit

        # assign name attributes data/slope/aspect:
        for key, fname in self.fnames.items():
            setattr(self, f"{key}_fpath", self.root / fname)
            setattr(self, key, core.read_raster_image(self.root/fname).squeeze(drop=True))

        lats = np.linspace(-90, 90, len(self.data.y))
        lons = np.linspace(-180, 180, len(self.data.x))
        for key in self.fnames.keys():
            o = getattr(self, key)
            o = o.assign_coords(lat=('y', lats))
            o = o.assign_coords(lon=('x', lons))
            o = o.swap_dims({'y':'lat', 'x':'lon'})
            setattr(self, key, o)

    def slice_lat(self, data, lat):
        s = slice(-lat, lat)
        return self.data.sel(lat=s, drop=True)