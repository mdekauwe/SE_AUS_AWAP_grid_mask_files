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

fname = "mask/SE_AUS_AWAP_csiro_soil_landmask.nc"
ds = xr.open_dataset(fname)
landsea_csiro = ds.landsea.values
ds.close()

fname = "mask/SE_AUS_AWAP_OpenLand_soil_landmask.nc"
ds = xr.open_dataset(fname)
landsea_open = ds.landsea.values
ds.close()

landsea_open = landsea_open[50:350,550:840]
landsea_csiro = landsea_csiro[50:350,550:840]
landsea_open = np.where(landsea_open == 1.0, np.nan, landsea_open)
landsea_csiro = np.where(landsea_csiro == 1.0, np.nan, landsea_csiro)

landsea_open = np.where(landsea_open == 0.0, 1.0, 0.0)
landsea_csiro = np.where(landsea_csiro == 0.0, 1.0, 0.0)

diff = landsea_open-landsea_csiro
diff = np.where(diff == 0.0, np.nan, diff)
#diff = np.where(diff == 0, np.nan, diff)
#diff = np.where(diff < 0, diff, np.nan)
plt.imshow(diff)
#plt.imshow(landsea_open)
plt.colorbar()
plt.show()
