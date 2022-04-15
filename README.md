# CUTnRUN
## Bioinformatics Pipeline For CUT&RUN Analysis

This repo will contain the code needed to run the CUT&RUN pipeline. Currently in development.

For all of these steps, you will need to run the python script for the step, and then run the associated bash script that python script generates before moving onto the next step in the pipeline.

## Usage example: ##
- python3 **01_cut_n_run_pairedReads_filter_align.py** "cells_FLAG_S4" "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/cutNrun_fastq_jan2022/cells_FLAG_S4_R1_001.fastq" "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/cutNrun_fastq_jan2022/cells_FLAG_S4_R2_001.fastq" 8 "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/results"
- python3 **02_cut_n_run_bamToBed_normalize_SEACRPrepv1.py** "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/results" "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/results_2_normalizedbeds" "/Users/fkoback/Documents/Projects/Arun/CUTnRUN/CnRAP/cutNrun_fastq_jan2022/mm10.chrom.sizes.txt"
- python **03_SEACR.py** "/Users/fkoback/software/SEACR/SEACR_1.3.sh" "/Users/fkoback/Documents/Projects/CUTnRUN/data"  "/Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks" "y"
- python **04_Annotation.py** "/Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks/results_3_calledpeaks"

- run **04_Annotation.R**

- python **05_Motifs.py** /Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks/relaxed_beds relaxed.bed /Users/fkoback/Documents/Projects/CUTnRUN/04_peak_motifs_v1beds

- Run **05_MemeMotifs.R**

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


Rest of pipeline in development 
