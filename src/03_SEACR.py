# Import Required Packages 
import os
from os import listdir
import sys
import numpy as np
import pandas as pd
from tabulate import tabulate

# read in input arguments that are required
seacr_path			= sys.argv[1] # where is seacr.py located? <path>/SEACR-1.1/SEACR_1.1.sh
bedgraphs_folder	= sys.argv[2] # where are the normalized bed_files <path>/02_bam_processing_v1
output_folder			= sys.argv[3] # where to put the called peaks? <path>/03_peak_calling_v1beds
igg_control = sys.argv[4]
#chrom_sizes_txt			= sys.argv[4] # path and anem of the chormosome sies text file needed for the bed converstion <path>/hg38.chrom.sizes

# Move to the folder with the saved bam and stats files
os.chdir(bedgraphs_folder)

if igg_control=="y":
    igg_bedgraphs = []
    for file_name in listdir():
        if file_name.startswith("igg"):
            igg_bedgraphs.append(bedgraphs_folder+ "/" +file_name)
    igg_bedgraphs.sort()
    


# Grouping the Nuclei Data
nuclei_bedgraphs = []
for file_name in listdir():
	if file_name.startswith("nuclei"):
		nuclei_bedgraphs.append(bedgraphs_folder+ "/" +file_name)
# sort alphabetically
nuclei_bedgraphs.sort()

# Grouping the Cell Data
cell_bedgraphs = []
for file_name in listdir():
	if file_name.startswith("cells"):
		cell_bedgraphs.append(bedgraphs_folder+ "/" +file_name)
# sort alphabetically
cell_bedgraphs.sort()

# Grouping the Unfixed Cells Data
unfixed_bedgraphs = []
for file_name in listdir():
	if file_name.startswith("unfixedCells"):
		unfixed_bedgraphs.append(bedgraphs_folder+ "/" +file_name)
# sort alphabetically
unfixed_bedgraphs.sort()

# Move to the output folder
os.chdir( output_folder )

# save commands to the output script
script_name = "03_SEACRcall.sh"
output_script = open( script_name, 'w' )

# move to the output directory
output_command = "cd " +output_folder
output_script.write(output_command)
output_script.write("\n\n")

for count in range(len(nuclei_bedgraphs)):
    output_command = "echo \"Calling SEACR on Nuclei Data  - Non and Relaxed\""
    # Non is no normalization of control to target data
    output_script.write(output_command)
    output_script.write("\n")
    prefix = nuclei_bedgraphs[count].rsplit('/', 1)[-1].rsplit('.')[0]
    current_command= nuclei_bedgraphs[count]
    output_command = "bash " +seacr_path+ " " +str(nuclei_bedgraphs[count])+ " " +str(igg_bedgraphs[0])+ " non relaxed " + str(prefix)
    output_script.write(output_command)
    output_script.write("\n")

output_script.write("\n\n")

for count in range(len(cell_bedgraphs)):
    output_command = "echo \"Calling SEACR on Cell Data  - Non and Relaxed\""
    # Non is no normalization of control to target data
    output_script.write(output_command)
    output_script.write("\n")
    prefix = cell_bedgraphs[count].rsplit('/', 1)[-1].rsplit('.')[0]
    current_command= cell_bedgraphs[count]
    output_command = "bash " +seacr_path+ " " +str(cell_bedgraphs[count])+ " " +str(igg_bedgraphs[0])+ " non relaxed " + str(prefix)
    output_script.write(output_command)
    output_script.write("\n")
    
output_script.write("\n\n")

for count in range(len(unfixed_bedgraphs)):
    output_command = "echo \"Calling SEACR on Unfixed Data  - Non and Relaxed\""
    # Non is no normalization of control to target data
    output_script.write(output_command)
    output_script.write("\n")
    prefix = unfixed_bedgraphs[count].rsplit('/', 1)[-1].rsplit('.')[0]
    current_command= cell_bedgraphs[count]
    output_command = "bash " +seacr_path+ " " +str(unfixed_bedgraphs[count])+ " " +str(igg_bedgraphs[0])+ " non relaxed " + str(prefix)
    output_script.write(output_command)
    output_script.write("\n")
    
output_script.write("\n\n")    
    
for count in range(len(nuclei_bedgraphs)):
    output_command = "echo \"Calling SEACR on Nuclei Data  - Non and Stringent\""
    # Non is no normalization of control to target data
    output_script.write(output_command)
    output_script.write("\n")
    prefix = nuclei_bedgraphs[count].rsplit('/', 1)[-1].rsplit('.')[0]
    current_command= nuclei_bedgraphs[count]
    output_command = "bash " +seacr_path+ " " +str(nuclei_bedgraphs[count])+ " " +str(igg_bedgraphs[0])+ " non stringent " + str(prefix)
    output_script.write(output_command)
    output_script.write("\n")

output_script.write("\n\n")

for count in range(len(cell_bedgraphs)):
    output_command = "echo \"Calling SEACR on Cell Data  - Non and Stringent\""
    # Non is no normalization of control to target data
    output_script.write(output_command)
    output_script.write("\n")
    prefix = cell_bedgraphs[count].rsplit('/', 1)[-1].rsplit('.')[0]
    current_command= cell_bedgraphs[count]
    output_command = "bash " +seacr_path+ " " +str(cell_bedgraphs[count])+ " " +str(igg_bedgraphs[0])+ " non stringent " + str(prefix)
    output_script.write(output_command)
    output_script.write("\n")
    
output_script.write("\n\n")

for count in range(len(unfixed_bedgraphs)):
    output_command = "echo \"Calling SEACR on Unfixed Data  - Non and Stringent\""
    # Non is no normalization of control to target data
    output_script.write(output_command)
    output_script.write("\n")
    prefix = unfixed_bedgraphs[count].rsplit('/', 1)[-1].rsplit('.')[0]
    current_command= cell_bedgraphs[count]
    output_command = "bash " +seacr_path+ " " +str(unfixed_bedgraphs[count])+ " " +str(igg_bedgraphs[0])+ " non stringent " + str(prefix)
    output_script.write(output_command)
    output_script.write("\n")