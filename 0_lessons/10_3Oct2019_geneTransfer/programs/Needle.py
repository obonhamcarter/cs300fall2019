from Bio.Emboss.Applications import NeedleCommandline
needle_cline = NeedleCommandline()
needle_cline.asequence="alpha.faa"
needle_cline.bsequence="beta.faa"
needle_cline.gapopen=10
needle_cline.gapextend=0.5
needle_cline.outfile="needle.txt"
print(needle_cline)
print(needle_cline.outfile)

stdout, stderr = needle_cline()
print(stdout + stderr)

