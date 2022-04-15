# import packages required
import os
from os import listdir
import sys
import numpy as np
import pandas as pd
from tabulate import tabulate

#peak_beds="/Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks/results_3_calledpeaks/nuclei_BRD4_abcam_R1.relaxed.bed - Annotated peaks.txt"
peak_beds="/Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks/relaxed_beds/unfixedCells_BRD4_abcam_R1.relaxed.bed"
#peak_beds="/Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks/relaxed_beds/nuclei_BRD4_abcam_R1.relaxed.bed"
#print(peak_beds.split("/")[-1].split("_R1")[0])

def read_bed_file(file_path):
    df = pd.read_csv(file_path,sep=' ',header=None)
    df.to_csv(file_path, sep='\t',header=None,index=False)
    print(df.head(5))
    
#file_path="/Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks/relaxed_beds/unfixedCells_BRD4_abcam_R1.relaxed.bed"
read_bed_file(peak_beds)
