#!/usr/bin/env python

import numpy as np
import h5py
from numpy.random import poisson

def populate_hod(halos, central_hod, satellite_hod):

	"""populate halos 'halos' with HOD given by functions 'central_hod' and 'satellite_hod'."""
	


if __name__ == '__main__':
	
	"""populate HOD for given parameters."""
	
	import argparse
	parser = argparse.ArgumentParser()
	parser.add_argument("halo_catalog")
	parser.add_argument("logMmin", type=float)
	parser.add_argument("siglogM", type=float)
	parser.add_argument("M1_over_Mmin", type=float)
	parser.add_argument("alpha", type=float)
	args = parser.parse_args()
	
	print(f"logMmin: {args.logMmin}")
	
	## read halos from HDF5 catalog
	
	halofile = h5py.File(args.halo_catalog)
	halos = halofile['halos']
	