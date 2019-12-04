from Bio.Align.Applications import MuscleCommandline
from StringIO import StringIO
from Bio import AlignIO

#muscle_exe = r"C:\muscle3.8.31_i86win32.exe" #specify the location of your muscle exe file

input_sequences = "ermB_record.fasta"
output_alignment = "ermBsequence.txt"

def align_v1 (Fasta): 
    muscle_cline = MuscleCommandline(muscle_exe, input=Fasta, out=output_alignment)
    stdout, stderr = muscle_cline()
    MultipleSeqAlignment = AlignIO.read(output_alignment, "fasta") 
    print MultipleSeqAlignment

align_v1(input_sequences)
