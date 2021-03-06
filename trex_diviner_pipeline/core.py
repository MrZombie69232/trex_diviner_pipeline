# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

<<<<<<< HEAD
<<<<<<< HEAD
__all__ = []
=======
__all__ = ['read_image']
>>>>>>> current status
=======
__all__ = ['read_raster_image', 'slice_lat', 'read_cycle_image', 'read_ltime', 'read_images_into_stacked_array',
           'get_data_for_pixel']
>>>>>>> cleaned up

# Internal Cell
import math
from dataclasses import dataclass, field
from pathlib import Path, PosixPath
from typing import List

import heat1d
import planets
import xarray as xr
from heat1d.plotting import plot_last_surface_cooling
<<<<<<< HEAD
from scipy.spatial.distance import pdist, squareform
=======
from scipy.spatial.distance import pdist, squareform

import heat1d

# Cell
def read_raster_image(fpath, chunk_scale=2):
    fpath = Path(fpath)
    da = xr.open_rasterio(
        fpath, chunks={"x": chunk_scale * 2048, "y": chunk_scale * 1024}
    )
    return da

def slice_lat(data, lat_limit):
    return data.sel(lat=slice(lat_limit, -lat_limit))

# Cell
def read_cycle_image(fpath, chunk_scale=2):
    """Read an Diviner map cycle rasterio image into a dask.array.

    Using the `chunks` keyword in the open_rasterio method
    activates the return of an out-of-memory virtual array instead
    of the in-memory xarray.DataArray

    fpath: str, pathlib.Path
    chunk_scale: int
        Scaling the chunck
    """
    fpath = Path(fpath)
    da = read_raster_image(fpath)
    cycle = int(fpath.name.split("_")[4][:-1])
    da = da.assign_coords(band=[cycle])
    return da.rename({"band": "time"})
<<<<<<< HEAD
>>>>>>> current status
=======

# Cell
def read_ltime(fpath, chunk_scale=2):
    da = read_image(fpath, chunk_scale)
    return da.sel(y=slice(80, -80))


def read_images_into_stacked_array(image_paths, name, chunk_scale=2):
    arrays = [read_image(p, chunk_scale) for p in image_paths]
    stack = xr.concat(arrays, "time")
    stack.name = name
    return stack


def get_data_for_pixel(xoff, yoff, ReaderClass, image_paths, name, chunk_scale=1):
    stack = read_images_into_stacked_array(image_paths, name, chunk_scale)
    pix = stack.isel(x=xoff, y=yoff)
    pix = pix.where(pix != -32768)
    img = ReaderClass.from_fpath(image_paths[0])
    pix = pix * img.SCALING_FACTOR + img.OFFSET
    return pix.compute()
>>>>>>> cleaned up
