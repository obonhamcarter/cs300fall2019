# uniprot exercises
# date: 20 November 2019
# ref: http://teaching.bioinformatics.dtu.dk/teaching/index.php/Exercise:_The_protein_database_UniProt

UniProt, http://www.uniprot.org/, consists of three parts:

UniProt Knowledge-base (UniProtKB)
protein sequences with annotation and references
UniProt Reference Clusters (UniRef)
homology-reduced database, where similar sequences (having a certain percentage identity) are merged into clusters, each with a representative sequence
UniProt Archive (UniParc)
an archive containing all versions of Uniprot without annotations


Simple text mining
First, we will find some UniProt entries using simple text mining. You are supposed to find the entry for human insulin.

Open the UniProt home-page http://www.uniprot.org/
Type human insulin in the search field in the top of the page. Leave the search menu on "UniProtKB", which is default. Press Enter or click the Search button.
Office-notes-line drawing.png
QUESTION 1:
How many hits do you find? (tip: See the number above the results list)
How many of these hits are from Swiss-Prot? (tip: See under "Reviewed" at the top left)
Can you identify the correct hit (i.e. see which one is actually human insulin and not something else)? If yes, write down is Accession code (found under Entry) and Entry name (also called ID).
In this case, it was relatively easy to spot the correct hit, but sometimes it is more difficult. If you do not identify the correct hit immediately, it will often help to narrow down the search, and that is exactly what we ask you to do in the next four questions.

The first step is searching for proteins that actually come from the organism "human" and are named something containing the word "insulin", as opposed to just containing the words "human" and "insulin" somewhere in the description. This can be done very easily: To the left of the results list under Search terms you find a list of links that allow you to restrict the search to specific fields.

Under Filter "human" as: click on: organism.
Office-notes-line drawing.png
QUESTION 2:
How many hits are now left? How many of these are from Swiss-Prot?
Under Filter "insulin" as: click on: protein name.
Office-notes-line drawing.png
QUESTION 3:
How many hits are now left? How many of these are from Swiss-Prot?
Note that all selections made with the mouse are shown in text format in the search field at the top of the page. It is possible to edit the search criteria manually in this field to make them broader or more narrow.

Try for instance to exclude proteins that are not insulin, but only insulin-like. You do this by adding the following text in the search field: NOT name:insulin-like and click on the Search button.
Office-notes-line drawing.png
QUESTION 4:
How many hits are now left?
Try now to exclude proteins that are insulin receptors (or described as substrates for insulin receptors).
Office-notes-line drawing.png
QUESTION 5:
How did you do this?
How many hits are now left?
The contents of UniProt
We shall now see what information is contained in a UniProt entry, and what further information is available as links in each entry.

Click on the accession-number for insulin (the blue code in the field Entry). This will take you to the insulin entry in the UniProtKB/Swiss-Prot database. Spend some time to get an overview of the page and the information it contains.

Note that you can click on the blue boxes in the left side of the page to scroll to different sections of the page. Try it!
Note also that every time there is a small "i" after a term on the page, you can click it to get information about the term. Try it!
Now click on Publications under Display in the upper left part of the window. Click on UniProtKB/Swiss-Prot under Source to show only those references that are part of the entry and exclude those that are "computationally mapped". Note that it is indicated what each reference has contributed ("Cited for"). You can get to the PubMed literature database at NCBI by clicking at the link "PubMed" for a reference — try this. The abstract of a publication can be read here (or directly at UniProt using the "Abstract"-link), if the work is an actual published article and not a "direct submission".

Office-notes-line drawing.png
QUESTION 6:
How many references are there in the insulin entry?
Why do you think insulin is such a highly investigated protein? (Hint: see other sections of the entry, e.g. Function and Pathol./Biotech, especially the subsections Involvement in disease and Pharmaceutical use)
Scroll back to Function and read the free-text description at the top of the section. Also have a look at the controlled vocabulary annotations: "Gene Ontology" (GO) and Keywords. Note that both of these are split into two different aspects: Molecular function and Biological process.
Now scroll to Subcell. location and read what is written there. Note that you find another set of "Gene Ontology" (GO) and Keywords annotations here; this time labelled Cellular component.
Office-notes-line drawing.png
QUESTION 7:
Where in the cell / outside the cell do you find insulin?
Why do you think is it found there? (Hint: consider the function)
Just like in GenBank, a UniProt entry has a Feature Table containing annotations that are coupled to specific parts of the sequence. In the default view, the Feature Table is not so easy to spot, since it is split up under different sections corresponding to the biological significance of the various annotations. However, you can click on Feature table under Display in the upper left part of the window to see those annotations only. Try it! Try also clicking on Feature viewer, which shows the same information in a graphical form.

Now switch back to the default (Entry) view. In the following, you will see some examples of Feature Table annotations.

Under Sequences, the subsection Natural variant lists the variants (mutations) of insulin that have been described in the literature. Under the heading Description, it is indicated which amino acid is changed into which other amino acid. If the variant is known to be associated with a disease, this is indicated with an abbreviation of the disease (e.g. "R → C in IDDM2").
Under Pathol./Biotech, the subsection Involvement in disease gives a description of each disease that is mentioned in the Feature Table, and repeats those variants that are associated with each disease.
Under PTM / Processing, the subsection Molecule processing shows that insulin has both a signal peptide and a pro-peptide. These are both cleaved off before secretion. The mature insulin (the A and B chains) is hence much smaller than what was shown under Sequences.
Office-notes-line drawing.png
QUESTION 8:
How long is the signal peptide and the propeptide, respectively?
Under Structure, the subsection Secondary structure shows a colour-coded representation of the sequence, showing the secondary structure elements "Helix" (α-helix), "Beta strand" (part of a β-pleated sheet) or "Turn" (the grey regions without specified secondary structure are often called "Loop" or "Coil"). Try to see what happens when you hover the mouse (without clicking) over the coloured bars. To see that this is really part of the feature table, try clicking on Show more details.
Office-notes-line drawing.png
QUESTION 9:
Which positions are in β-sheet conformation in insulin?
