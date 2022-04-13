# CUTnRUN
## Bioinformatics Pipeline For CUT&RUN Analysis

This repo will contain the code needed to run the CUT&RUN pipeline. Currently in development.

For all of these steps, you will need to run the python script for the step, and then run the associated bash script that python script generates before moving onto the next step in the pipeline.

Usage example: 
python 03_SEACR.py "/Users/fkoback/software/SEACR/SEACR_1.3.sh" "/Users/fkoback/Documents/Projects/CUTnRUN/data"  "/Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks" "y"

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

Rest of pipeline in development 
     
