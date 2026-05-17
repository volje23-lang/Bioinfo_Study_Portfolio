# Bioinfo Study Portfolio

Python 기반 바이오인포메틱스 및 면역 데이터 분석 학습 포트폴리오입니다.

면역 관련 유전자 데이터를 다루며
기초적인 데이터 처리, gene expression 분석, 
그리고 생물학적 해석 과정을 함께 익히는 것을 목표로 하였습니다.

Python과 pandas를 활용해
FASTA parsing, CSV 기반 데이터 처리 등을 직접 구현하며 학습하였습니다.


## Projects 

### 1. DNA GC Content Analyzer
- Calculate sequence length and GC content 
- Analyze nucleotide frequency using loops and conditions
- Save results to a txt report file

### 2. Interactive DNA Analysis Tool
- Analyze DNA sequences from user input
- Automatically convert lowercase input to uppercase
- Validate invalid DNA characters
- Classify sequence type based on GC content 
- Save analysis results to a log file 

### 3. FASTA File Parser
- Read biological sequence data from FASTA file
- Detect and parse FASTA headers (>)
- Extract DNA sequences
- Process biological sequence data from FASTA format

### 4. Immune Gene Expression Analysis
- Analyze immune gene expression data using pandas
- Compare expression patterns across immune-related marker genes
- Identify relatively highly expressed immune-associated genes
- Sort genes by expression level
- Observe simple immune gene expression trends
- Visualize expression distributions using matplotlib 
- Add average expression reference line 
- Save graph as PNG file

#### Biological Note

FOXP3 showed relatively high expression
compared to several other immune marker genes.

PDCD1 showed lower-than-average expression levels
compared to other immune marker genes.


### 5. Immune Gene Filtering Analysis
- Filter genes with above-average expression
- Extract selected immune-related marker genes from mixed datasets
- Practice filtering biologically relevant genes
- Organize filtered immune gene data for downstream analysis
- Save filtered results as CSV files

### 6. Simple Differential Expression Analysis
- Compare immune marker gene expression between control and treated conditions
- Calculate fold change and log2 fold change
- Classify genes as up-regulated, down-regulated, or no major change
- Visualize expression changes with a bar plot
- Save processed results as CSV files

#### Biological Note

Most immune-related genes were up-regulated in the treated condition, with TNF and FOXP3 showing relatively strong expression changes.

### 7. Cytokine Summary Analysis
- Summarize cytokine expression values
- Identify highly expressed cytokines using a simple threshold
- Sort cytokines by expression level
- Visualize cytokine expression with a bar plot

#### Biological Note

IL6, TNF, and IFNG were included as representative inflammatory cytokines.

Several cytokines showed expression values
above the dataset average.

### 8. Immune Heatmap Practice

- Visualize immune marker expression across multiple samples
- Practice converting tabular gene expression data into heatmap format
- Compare relative expression patterns between immune-related genes
- Use matplotlib to explore simple biological data visualization
- Save processed heatmap data and image outputs

#### Biological Note

IFNG, IL6, and TNF showed relatively high expression in Sample_C,
while IL10 expression remained more stable across samples.

Compared expression patterns between immune-related genes using heatmap visualization.


### 9. DNA Motif Pattern Finder

- Search repeated DNA motifs from sequence datasets
- Practice simple pattern matching using biological sequences
- Count motif frequency across multiple DNA samples
- Save motif search results as CSV files

#### Biological Note

Some sequences contained repeated ATG motifs,
while others showed little or no motif enrichment.

Counted ATG motifs and compared simple sequence pattern differences across samples.

### 10. GEO-style Immune Expression Analysis

- Practice analyzing public-dataset-like immune gene expression data
- Compare healthy and inflammatory conditions
- Calculate fold change and log2 fold change
- Classify genes based on expression change
- Visualize log2 fold change using matplotlib
- Save analyzed results as CSV files

#### Biological Note

IFNG, TNF, and IL6 showed increased expression
in the inflammatory condition.

Compared log2 fold change values between healthy and inflammatory conditions.

---

## Skills
- Python
- Pandas / NumPy
- Matplotlib
- FASTA sequence parsing
- CSV-based biological data processing
- Gene expression analysis
- Differential expression practice
- DNA motif pattern searching
- Basic immune-related data interpretation

## Future Roadmap
Currently exploring RNA-seq workflows and basic statistical methods for expression analysis. Next step is working with larger public datasets and digging into T-cell and immune checkpoint markers.

