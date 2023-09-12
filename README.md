# Format_Fasta
 Python Script that will format length of nucleotide bases in fasta file.

## How to use: 

This script will format nucleotide bases to be the same length of string. 

Example: 

\>Seq1
ATGGG
GGGGG
ATTGT
\>Seq2
ATGAGAGAGAAG
ATGAGAGAGAAG
ATGAGAGAGAAG

output will be: 
\>Seq1
ATGGGGGG
GGGGGGGG
ATTGTGAA
\>Seq2
ATGAGAGA
GAAGATGA
GAGAGAAG
ATGAGAGA
GAAG

## Python Command:
Run as follows:

python Format_Fasta.py <Path to Fasta> <Length of Sequence>

<Path to Fasta> is the path to the fasta file you want to format. (extension of the file should be .fa .fasta .FASTA)

<Length of Sequence> is an integer determining how many bases to have per squence.

*Exapmle:* 
python Format_Fasta.py /Users/Foo/Desktop/Fasta_file.fasta 35"
