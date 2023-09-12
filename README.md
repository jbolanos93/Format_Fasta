# Format_Fasta
 Python Script that will format length of nucleotide bases in fasta file.
## Requirements 
* python 3.0 or greater
## Description: 

This script will format nucleotide bases to be the same length of string. 

**Example:**

\>Seq1<br>
ATGGG<br>
GGGGG<br>
ATTGT<br>
\>Seq2<br>
ATGAGAGAGAAG<br>
ATGAGAGAGAAG<br>
ATGAGAGAGAAG<br>

output will be: <br><br>
\>Seq1<br>
ATGGGGGG<br>
GGGGGGGG<br>
ATTGTGAA<br>
\>Seq2<br>
ATGAGAGA<br>
GAAGATGA<br>
GAGAGAAG<br>
ATGAGAGA<br>
GAAG<br>

New file will be written in the same directory as the provided fasta. 

*note: Package downloads a sample fasta to test code with.*
## How to use:
**Run as follows:**
```python
python Format_Fasta.py <Path to Fasta> <Length of Sequence>
```
**Path to Fasta:** is the path to the fasta file you want to format. (extension of the file should be .fa .fasta .FASTA)

**Length of Sequence:** is an integer determining how many bases to have per squence.

**Example:**
```python
python Format_Fasta.py /Users/Foo/Desktop/Fasta_file.fasta 35
```