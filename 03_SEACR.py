# Import Required Packages 
import os
from os import listdir
import sys
import numpy as np
import pandas as pd
from tabulate import tabulate

# read in input arguments that are required
seacr_location			= sys.argv[1] # where is seacr.py located? <path>/SEACR-1.1/SEACR_1.1.sh
bedgraphs_folder	= sys.argv[2] # where are the normalized bed_files <path>/02_bam_processing_v1
output_folder			= sys.argv[3] # where to put the called peaks? <path>/03_peak_calling_v1beds
#chrom_sizes_txt			= sys.argv[4] # path and anem of the chormosome sies text file needed for the bed converstion <path>/hg38.chrom.sizes

# Move to the folder with the saved bam and stats files
os.chdir(bedgraphs_folder)

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
cell_bedgraphs = []
for file_name in listdir():
	if file_name.startswith("unfixedCells"):
		cell_bedgraphs.append(bedgraphs_folder+ "/" +file_name)
# sort alphabetically
cell_bedgraphs.sort()

# Move to the output folder
os.chdir( output_folder )

# save commands to the output script
script_name = "03_cut_n_run_seacrCall_peakConvert.sh"
output_script = open( script_name, 'w' )

# move to the normalized beds directory to make the bw converage files for viewing
output_command = "cd " +bedgraphs_folder
output_script.write(output_command)
output_script.write("\n\n")

output_command = "echo \"Making bedgraph and bw coverage maps\""
output_script.write(output_command)
output_script.write("\n")

# convert normalized beds (bedgraph formats) to bw coverage files
for sample_counter in range(len(nuclei_bedgraphs)):
	# bedgraph to bw
	output_command = "bedGraphToBigWig " +nuclei_bedgraphs[sample_counter] +chrom_sizes_txt+ " " +nuclei_bedgraphs[sample_counter]
	output_script.write(output_command)
	output_script.write("\n")
		# remove bedgraph
	output_command = "rm " +nuclei_bedgraphs[sample_counter]
	output_script.write(output_command)
	output_script.write("\n")

for sample_counter in range(len(cell_bedgraphs)):
	# bedgraph to bw
	output_command = "bedGraphToBigWig " +cell_bedgraphs[sample_counter]+chrom_sizes_txt+ " " +cell_bedgraphs[sample_counter]
	output_script.write(output_command)
	output_script.write("\n")
	# remove bedgraph
	output_command = "rm " +cell_bedgraphs[sample_counter]
	output_script.write(output_command)
	output_script.write("\n")

output_script.write("\n\n")

# move to the output directory
output_command = "cd " +output_folder
output_script.write(output_command)
output_script.write("\n\n")

# for file - only need 2 and not 3 references!
for sample_counter in range(len(nuclei_bedgraphs)-1):
	# update the user on whats happening
	output_command = "echo \"Calling SEACR on Nuclear files  - Relaxed!\""
	output_script.write(output_command)
	output_script.write("\n")
	# pull out the name of the current data file so as to include it as the output prefix
	current_name = nuclei_bedgraphs[sample_counter].split("/")[8].split("_")[0:3]
	current_name.append("relaxed")
	current_name_string = "_".join(current_name)
	# call SEACR
	output_command = "bash " +seacr_location+ " " +nuclei_bedgraphs[sample_counter]+ " " +nuclei_bedgraphs[2]+ " non relaxed " +current_name_string
	output_script.write(output_command)
	output_script.write("\n")

output_script.write("\n\n")

# for file - only need 2 and not 3 references!
for sample_counter in range(len(nuclei_bedgraphs)-1):
	# update the user on whats happening
	output_command = "echo \"Calling SEACR on Nuclear files  - Stringent!\""
	output_script.write(output_command)
	output_script.write("\n")
	# pull out the name of the current data file so as to include it as the output prefix
	current_name = nuclei_bedgraphs[sample_counter].split("/")[8].split("_")[0:3]
	current_name.append("stringent")
	current_name_string = "_".join(current_name)
	# call SEACR
	output_command = "bash " +seacr_location+ " " +nuclei_bedgraphs[sample_counter]+ " " +nuclei_bedgraphs[2]+ " non stringent " +current_name_string
	output_script.write(output_command)
	output_script.write("\n")

output_script.write("\n\n")

# for file - only need 2 and not 3 references!
for sample_counter in range(len(cell_bedgraphs)-1):
	# update the user on whats happening
	output_command = "echo \"Calling SEACR on Regular files  - Relaxed!\""
	output_script.write(output_command)
	output_script.write("\n")
	# pull out the name of the current data file so as to include it as the output prefix
	current_name = cell_bedgraphs[sample_counter].split("/")[8].split("_")[0:3]
	current_name.append("relaxed")
	current_name_string = "_".join(current_name)
	# call SEACR
	output_command = "bash " +seacr_location+ " " +cell_bedgraphs[sample_counter]+ " " +cell_bedgraphs[2]+ " non relaxed " +current_name_string
	output_script.write(output_command)
	output_script.write("\n")

output_script.write("\n\n")

# for file - only need 2 and not 3 references!
for sample_counter in range(len(cell_bedgraphs)-1):
	# update the user on whats happening
	output_command = "echo \"Calling SEACR on Regular files  - Stringent!\""
	output_script.write(output_command)
	output_script.write("\n")
	# pull out the name of the current data file so as to include it as the output prefix
	current_name = cell_bedgraphs[sample_counter].split("/")[8].split("_")[0:3]
	current_name.append("stringent")
	current_name_string = "_".join(current_name)
	# call SEACR
	output_command = "bash " +seacr_location+ " " +cell_bedgraphs[sample_counter]+ " " +cell_bedgraphs[2]+ " non stringent " +current_name_string
	output_script.write(output_command)
	output_script.write("\n")

output_script.write("\n\n")

# pull out the called peak files
called_peak_beds = []
for file_name in listdir():
	if file_name.endswith("bed"):
		called_peak_beds.append(output_folder+ "/" +file_name)
# sort alphabetically
called_peak_beds.sort()

# for each file re-arrange to make in the same format as macs to allow annotation script to run
for sample_counter in range(len(called_peak_beds)):
	# call SEACR
	output_command = "awk \'{print $1\"\\t\"$2\"\\t\"$3\"\\t\"$6\"\\t\"$5\"\\t\"$4}\' " +called_peak_beds[sample_counter]+ " > " +called_peak_beds[sample_counter][:-3]+ "rearrangedCols.bed"
	output_script.write(output_command)
	output_script.write("\n")

output_script.write("\n\n\n")

# for each file re-arrange to make in the format for Homer to call peaks
for sample_counter in range(len(called_peak_beds)):
	# call SEACR
	output_command = "awk \'{print $4\"\\t\"$1\"\\t\"$2\"\\t\"$3\"\\t+\"}\' " +called_peak_beds[sample_counter]+ " > " +called_peak_beds[sample_counter][:-3]+ "homerMotif.bed"
	output_script.write(output_command)
	output_script.write("\n")

# close the script file
output_script.close()

# make script executable
os.system("chmod +x " +script_name)
