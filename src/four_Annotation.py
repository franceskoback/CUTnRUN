# import packages required
import os
from os import listdir
import sys
import numpy as np
import pandas as pd
from tabulate import tabulate

# Import Required Packages
normalized_beds_folder	= sys.argv[1]

os.chdir( normalized_beds_folder )


def add_chr_to_bed_file(file_path):
    df = pd.read_csv(file_path,sep='\t',header=None)
    df.iloc[:, 0] = 'chr' + df.iloc[:, 0].astype(str)
    df.to_csv(file_path, sep='\t',header=None,index=False)

# iterate through all file
for file in os.listdir():
    # Check whether file is in text format or not
    if file.endswith("relaxed.bed") | file.endswith("stringent.bed"):
        file_path = f"{normalized_beds_folder}/{file}"
  
        # call read text file function
        add_chr_to_bed_file(file_path)
        
