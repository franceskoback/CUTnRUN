# CUTnRUN
## Bioinformatics Pipeline For CUT&RUN Analysis

This repo will contain the code needed to run the CUT&RUN pipeline. Currently in development.

For all of these steps, you will need to run the python script for the step, and then run the associated bash script that python script generates before moving onto the next step in the pipeline.

### Steps to Install: ##
1. Git clone this repository 
2. copy your data into this repository or know where it is (cp -r /path/to/data ./data within this repo folder)
3. make results folder and folder for 3_calledpeaks within this folder 
4. Run 3rd python script 
5. nano that bash script output and put #!/usr/bin/env bash on top of bash script if submitting as job 
6. Rename 03_SEACRcall.sh to three_SEACRcall.sh if submitting as a job-- TODO change this to be three, four, etc instead of starting with numbers
7. qsub -cwd -pe smp 12 -l mem_free=12G -l scratch=1000G -l h_rt=50:00:00 -m bea -M frances.koback@gladstone.ucsf.edu three_SEACRcall.sh
8. run 04_Annotation.py as shown below 
9. make sure you have all packages downloaded in R (ChIPseeker,TxDb.Mmusculus.UCSC.mm10.knownGene, clusterProfiler,ReactomePA,tidyverse,ggupset, ggimage)
10. change working directory in 04_Annotation.R : setwd("/wynton/group/gladstone/users/franceskoback/CUTnRUN/results/3_calledpeaks")
11. run "Rscript 04_Annotation.R" this will generate plots in the directory above. To move them to a new folder called "four_ChIPSeeker", do mv *.txt ../four_ChIPSeeker and mv *.png ../four_ChIPSeeker TODO: make a bash script to run 04_Annotation.py, 04_Annotation.R, and the above commands to move the outputs to the correct folder 
12. TODO: change python script to connect to that specific Homer download if running on the server (if running in conda don't/ alternatively, run conda on server- look into this) 

## Usage example: ##
- python3 **01_cut_n_run_pairedReads_filter_align.py** "cells_FLAG_S4" "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/cutNrun_fastq_jan2022/cells_FLAG_S4_R1_001.fastq" "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/cutNrun_fastq_jan2022/cells_FLAG_S4_R2_001.fastq" 8 "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/results"
- python3 **02_cut_n_run_bamToBed_normalize_SEACRPrepv1.py** "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/results" "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/results_2_normalizedbeds" "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/cutNrun_fastq_jan2022/mm10.chrom.sizes.txt"
- python **03_SEACR.py** "/Users/fkoback/software/SEACR/SEACR_1.3.sh" "/Users/fkoback/Documents/Projects/CUTnRUN/data"  "/Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks" "y"
- **or** python **03_SEACR.py** "/wynton/home/srivastava/franceskoback/software/SEACR/SEACR_1.3.sh" "/wynton/group/gladstone/users/franceskoback/CUTnRUN/data"  "/wynton/group/gladstone/users/franceskoback/CUTnRUN/results/3_calledpeaks" "y"
- python **04_Annotation.py** "/Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks/results_3_calledpeaks"
- or python **04_Annotation.py** "/wynton/group/gladstone/users/franceskoback/CUTnRUN/results/3_calledpeaks"

- run **04_Annotation.R**

- python **05_HomerMotifs.py** /Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks/relaxed_beds relaxed.bed /Users/fkoback/Documents/Projects/CUTnRUN/05_homer_peak_motifs
- or **python 05_HomerMotifs.py** /wynton/group/gladstone/users/franceskoback/CUTnRUN/results/three_calledpeaks "relaxed.bed" /wynton/group/gladstone/users/franceskoback/CUTnRUN/results/five_HomerMotifs

- Run **06_MemeMotifs.R**

## Steps of Analysis (and to-dos for development)
  
  - **Script 1**
      - Trimming with trimmomatic ([CnRAP](https://star-protocols.cell.com/protocols/944#key-resources-table)) or TrimGalore([nf-core](https://nf-co.re/cutandrun))-- TBD)
      - Alignment with [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)
      - Filtering (removing unmapped reads and gathering sort, index, and alignment statistics): [samtools](http://www.htslib.org/)
    
  - **Script 2**
      - Bams to Bedgraphs 
      - Optional normalization to spike-in genome


  - **Script 3**
      - Call [SEACR](https://github.com/FredHutch/SEACR)
      - **Argument 1**: path to SEACR
      - **Argument 2**: path to data folder containing bedgraphs
      - **Argument 3**: path to folder where you want to store your results (and bash script this python script generates)
      - **Argument 4**: "y" or "n"-- "y" if there is an igg control 

  - **Script 4 Annotation**
      - **04_Annotation.py Argument 1**: path to data containing bed file outputs from SEACR (*relaxed.bed and *stringent.bed)
      - **04_Annotation.R** run in RStudio or R to generate plots 

  - **Script 5: Homer Motifs**
      - **05_Motifs.py** make sure you have genome downloaded (ie perl /opt/anaconda3/envs/python385/share/homer-4.10-0/.//configureHomer.pl -install mm10
      - **Note**: make sure beds are in correct Homer format. The script "check_bed_format.py" makes sure the bed files are tab-delimited and allows you to change them to be tab-delimited if they are space delimited instead

  - **Script 6: Meme Motifs**
      - **Download Bedops** https://bedops.readthedocs.io/en/latest/content/installation.html
      - **Note**: change path names in R script to match your environment 

Polishing in progress to make it reproducible in other compute environments!  
