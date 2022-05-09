# CUTnRUN Pipeline
## Bioinformatics Pipeline For CUT&RUN Analysis

This repo will contain the code needed to run the CUT&RUN pipeline. 

For all of these steps, you will need to run the python script for the step, and then run the associated bash script that python script generates before moving onto the next step in the pipeline.
### Software Requirements: ###
1. [TrimGalore](https://github.com/FelixKrueger/TrimGalore) wrapper to apply adapter and quality trimming to fastq files -- wynton has this already 
2. [Bowtie2](http://bowtie-bio.sourceforge.net/bowtie2/manual.shtml) for aligning. Other pipelines use BWA, but Bowtie2 seems to perform better and does not require Stampy after alignment. 
3. [samtools](http://www.htslib.org/download/) - wynton has this already 
4. [bamtools](https://github.com/pezmaster31/bamtools) install with **conda install -c bioconda bamtools**  **for these, make sure your conda folder is in your path, ie export PATH="/your/path/to/miniconda3:$PATH"**
5. [deeptools](https://deeptools.readthedocs.io/en/develop/) **conda install -c conda-forge -c bioconda deeptools** 
6. [Bwa](https://github.com/lh3/bwa) follow the instructions in that link to download bwa and make your reference index by running the following command: **bwa index /path/to/genome.fa** 
7. Make sure you have all required packages installed in R (**ChIPseeker,TxDb.Mmusculus.UCSC.mm10.knownGene, clusterProfiler,ReactomePA,tidyverse,ggupset, ggimage**)
8. [Homer](http://homer.ucsd.edu/homer/) To download this, make a Homer folder in your software directory (or in whatever location you want to have Homer downloaded). Then navigate to that folder and type **wet http://homer.ucsd.edu/homer/configureHomer.pl** , **perl configureHomer.pl -install, PATH=$PATH:/your/path/to/Homer/.//bin/** ,then once you have Homer added to your path, install the relevant genome, ie  **perl /wynton/home/srivastava/franceskoback/software/Homer/.//configureHomer.pl -install mm10**
9. 

To start with fastqs, use scripts 1 and 2. If you already have sorted bedgraphs, skip to the "STARTING FROM SORTED BEDGRAPHS:" Portion below. Else 
### on FIRST GO: ### 
1. Git clone this repository 
2. make results and data directories within this folder (mkdir results, mkdir data)
3. copy your paired fastq data into this repository (..R1_001.fastq.gz and R2_001.fastq.gz or something similar) or cp -r /path/to/data ./data within this repo folder)
5. Run python script one following the format in the "Usage example" portion of the readme below. This will output a bash script that you will then run to do the first step in this pipeline, ie **bash one_cut_n_run_cells_BRD4_dia_trim_align.sh** **NOTE: Sometimes this alignment will output data that contains lines of the form: chr1_GL456221_random, chr4_JH584293_random, etc. In order to fix this issue, and get rid of any lines that did not align to  chromomes properly, in your results/one_aligned folder:  `samtools view -o out.bam in.bam `seq 1 21 | sed 's/^/chr/'``**  where 1 and 21 correspond to the mouse genome chromosome numbers. 
8. Run python script two following the format in the "Usage example" portion of the readme below. This will output a bash script that you will then run to do the first step in this pipeline, ie **bash two_cut_n_run_bamToBed_normalize.sh** 
9. **Repeat steps 1-8 for every set of paired fastq data you wish to run. Then, once you have a bunch of ** 
10. Run python script three following the format in the "Usage example" portion of the readme below. This will output a bash script that you will then run to do the first step in this pipeline, ie **bash three_SEACRcall.sh** or if submitting as a job, **qsub -cwd -pe smp 12 -l mem_free=12G -l scratch=1000G -l h_rt=50:00:00 -m bea -M frances.koback@gladstone.ucsf.edu three_SEACRcall.sh** 
11. Run four_Annotation.py as shown in the "Usage example" below-- **this will modify your bed files so be sure about this step before you run! Ie do not run this twice!!** SEACR output data structure has just numbers in the first column of the bed, corresponding to chromosome number. The resulting bed files from this will have "chr" appended in the chromosome column to match the format required for the subsequent analyses in R. This will also output a bash script that will move all plots generated in step 11 below into folders to clean up your directory. 
12. Change working directory in four_Annotation.R: setwd("/your/path/to/results/three_calledpeaks") four_Annotation.R 
13. Make sure you're using R> 4.0 module load r/4.1.3 then run 
14. Run bash script outputted in step 10, ie **bash 
15. Run 5th python script 
16. Run 6th R script 


These are run on each set of paired fastqs until you get a list of sorted bedgraphs, then proceed with the steps below.

### Steps to Install STARTING FROM 3: ##
1. Git clone this repository 
2. make results and data directories within this folder 
3. copy your data (.sorted.bedGraphs) into this repository or know where it is (cp -r /path/to/data ./data within this repo folder)
4. Run 3rd python script 
5. nano that bash script output and put #!/usr/bin/env bash on top of bash script if submitting as job 
6. Rename 03_SEACRcall.sh to three_SEACRcall.sh if submitting as a job-- DONE change this to be three, four, etc instead of starting with numbers
7. qsub -cwd -pe smp 12 -l mem_free=12G -l scratch=1000G -l h_rt=50:00:00 -m bea -M frances.koback@gladstone.ucsf.edu three_SEACRcall.sh
8. run four_Annotation.py as shown below 
9. make sure you have all packages downloaded in R (ChIPseeker,TxDb.Mmusculus.UCSC.mm10.knownGene, clusterProfiler,ReactomePA,tidyverse,ggupset, ggimage)
10. change working directory in four_Annotation.R : setwd("/wynton/group/gladstone/users/franceskoback/CUTnRUN/results/three_calledpeaks")
11. module load CBI r/4.1.3 , then run "Rscript 04_Annotation.R" this will generate plots in the directory above. 
12. To move them to a new folder called "four_ChIPSeeker", run bash script four_moveplots.sh 
13. On initial run, to make a Homer folder in your software directory (or wherever you want to have it downloaded), navigate to that software folder and type wet http://homer.ucsd.edu/homer/configureHomer.pl
14. perl configureHomer.pl -install 
15. PATH=$PATH:/wynton/home/srivastava/franceskoback/software/Homer/.//bin/
16. perl /wynton/home/srivastava/franceskoback/software/Homer/.//configureHomer.pl -install mm10
18. run 5th python script 
19. bash five_cut_n_run_homer_motifs_v1beds.sh
20. on wynton, do module load CBI bedops 
21. mkdir six_MemeMotifs in results folder 
22. go to three_calledpeaks and make relaxed and stringent folders then do mv *.relaxed.bed ./relaxed and mv *.stringent.bed ./stringent-- DONE make this automatically happen after running third step 
23. go to your data folder and do wget http://hgdownload.cse.ucsc.edu/goldenpath/mm10/bigZips/mm10.fa.gz to download the mm10.fa genome  
24. navigate to 6th script in src folder and nano to change the path names at the top of the Rscript to match your paths-- including the path to the mm10 genome above  
25. Make sure you're using R > 4.0 ( module load r/4.1.3 ) 
26. Rscript 06_MemeMotifs.R (DONE: make this six_MemeMotifs.R)




## Usage example: ##
- python **one_Align_wynton.py** "cells_BRD4_dia" "/wynton/group/gladstone/users/franceskoback/Projects/CUTnRUN/data/cells_BRD4_dia_S3_R1_001.fastq.gz" "/wynton/group/gladstone/users/franceskoback/Projects/CUTnRUN/data/cells_BRD4_dia_S3_R2_001.fastq.gz" 8 "/wynton/group/gladstone/users/franceskoback/Projects/CUTnRUN/results/one_aligned" mm10
- python **two_Normalize.py** "/wynton/group/gladstone/users/franceskoback/Projects/CUTnRUN/results/one_aligned" "/wynton/group/gladstone/users/franceskoback/Projects/CUTnRUN/results/two_normalize" 
- python **three_SEACR.py** "/wynton/home/srivastava/franceskoback/software/SEACR/SEACR_1.3.sh" "/wynton/group/gladstone/users/franceskoback/Projects/CUTnRUN/results/two_normalize" "/wynton/group/gladstone/users/franceskoback/Projects/CUTnRUN/results/three_calledpeaks" "n"
- python **four_Annotation.py** "/Users/fkoback/Documents/Projects/CUTnRUN/results/three_calledpeaks"
- or python **four_Annotation.py** "/wynton/group/gladstone/users/franceskoback/CUTnRUN/results/three_calledpeaks"

- run **four_Annotation.R**

- python **five_HomerMotifs.py** /Users/fkoback/Documents/Projects/CUTnRUN/results_3_calledpeaks/relaxed_beds relaxed.bed /Users/fkoback/Documents/Projects/CUTnRUN/05_homer_peak_motifs
- or **python five_HomerMotifs.py** /wynton/group/gladstone/users/franceskoback/CUTnRUN/results/three_calledpeaks "relaxed.bed" /wynton/group/gladstone/users/franceskoback/CUTnRUN/results/five_HomerMotifs

- Run **six_MemeMotifs.R**

## Steps of Analysis (and to-dos for development)
  
  - **Script 1**
      - Trimming with trimmomatic ([CnRAP](https://star-protocols.cell.com/protocols/944#key-resources-table)) or TrimGalore([nf-core](https://nf-co.re/cutandrun))-- TBD. Wynton has TrimGalore module available). Modifying this workflow to make it use TrimGalore. The original script uses kseq to trim, but that is unneccessary with TrimGalore (Trimmomatic fails to trim reads containing 6 bp or less, which is why Kseq is used in conjunction with Trimmomatic. 
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
      - **four_Annotation.py Argument 1**: path to data containing bed file outputs from SEACR (*relaxed.bed and *stringent.bed)
      - **four_Annotation.R** run in RStudio or R to generate plots 

  - **Script 5: Homer Motifs**
      - **five_Motifs.py** make sure you have genome downloaded (ie perl /opt/anaconda3/envs/python385/share/homer-4.10-0/.//configureHomer.pl -install mm10
      - **Note**: make sure beds are in correct Homer format. The script "check_bed_format.py" makes sure the bed files are tab-delimited and allows you to change them to be tab-delimited if they are space delimited instead

  - **Script 6: Meme Motifs**
      - **Download Bedops** https://bedops.readthedocs.io/en/latest/content/installation.html
      - **Note**: change path names in R script to match your environment 

Polishing in progress to make it reproducible in other compute environments!  

