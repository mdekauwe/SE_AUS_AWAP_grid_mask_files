#!/usr/bin/env python

"""
Generate a land-sea mask so we just run the code on SE Aus.

That's all folks.
"""
__author__ = "Martin De Kauwe"
__version__ = "1.0 (30.09.2019)"
__email__ = "mdekauwe@gmail.com"

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import glob
import xarray as xr
import netCDF4 as nc
import datetime
import os
import sys
import shutil
import netCDF4

def main():

    in_fname = "raw/MD_elev_orig_std_avg-sand_AWAP_AU_landmask.nc"
    out_fname = "SE_AUS_AWAP_landmask_debug_pixel.nc"
    ds = xr.open_dataset(in_fname)

    ds_out = ds.copy()

    landsea = ds.landsea.values
    landsea = np.where(np.logical_and(
                          ((ds_out.lat <= -28.0) & (ds_out.lat >= -40.0) &
                           (ds_out.lon >= 140.0) & (ds_out.lat <= 154.0)),
                          landsea == 0.0),
                          1.0, 1.0)

    row = 292
    col = 590
    landsea[row,col]=0.0
    row = 292
    col = 591
    landsea[row,col]=0.0
    



    ds_out['landsea'][:,:] = landsea

    ds_out.to_netcdf(out_fname)
    ds_out.close()

if __name__ == "__main__":

    main()
