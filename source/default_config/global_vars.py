# global_vars.py: Global variables used by MaSIF -- mainly pointing to environment variables of programs used by MaSIF.
# Pablo Gainza - LPDI STI EPFL 2018-2019
# Released under an Apache License 2.0

import os 
epsilon = 1.0e-6

msms_bin= ""
if 'MSMS_BIN' in os.environ:
   msms_bin = os.environ['MSMS_BIN']
else:
  print "ERROR: MSMS_BIN not set. Variable should point to MSMS program."
  sys.exit(1)

xyzrn_bin=""
if 'PDB2XYZRN' in os.environ:
   xyzrn_bin = os.environ['PDB2XYZRN']
else:
  print "ERROR: PDB2XYZRN not set. Variable should point to XYZRN program."
  sys.exit(1)

pdb2pqr_bin=""
if 'PDB2PQR_BIN' in os.environ:
   pdb2pqr_bin = os.environ['PDB2PQR_BIN']
else:
  print "ERROR: PDB2PQR_BIN not set. Variable should point to PDB2PQR_BIN program."
  sys.exit(1)

apbs_bin=""
if 'APBS_BIN' in os.environ:
   apbs_bin = os.environ['APBS_BIN']
else:
  print "ERROR: APBS_BIN not set. Variable should point to APBS program."
  sys.exit(1)
  
multivalue_bin=""
if 'MULTIVALUE_BIN' in os.environ:
   multivalue_bin = os.environ['MULTIVALUE_BIN']
else:
  print "ERROR: MULTIVALUE_BIN not set. Variable should point to MULTIVALUE program."
  sys.exit(1)


class NoSolutionError(Exception):
    pass
