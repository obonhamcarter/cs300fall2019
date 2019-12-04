notes for lab 04
Date: 23 Sept 2019
---
unused

Steps:
- Click again on the green line of ```NM_001005291.3``` in this graphical area to make the associated blue and red lines disappear.
- Move your mouse over the gene name (```NM_001005291.3```) to expand a menu in which you are able to download the DNA sequence of this gene.
- On this expanded menu for the gene, click on the download link for the gene (note, you are clicking on the link for "NM_001005291.3") and allow the download to complete.
- Move this file to a working bin and run  (```fastaReadWrite_MotifChecker.py```) to search





\subsubsection*{Research Steps and Questions}
\begin{enumerate}
	\item From the chapter reading, it is known that the SNP, \emph{rs11868035}, is located within the gene, \emph{SREBF1}. We would like to find the string of nucleotides of this gene to analyze it further.

	\item Perform a search for this SNP at using the online web database provided by the National Center for Biotechnology Information (NCBI) at \url{https://www.ncbi.nlm.nih.gov/}.
	\begin{itemize}
		\color{red}{\item Q1: According to NCBI, which particular database are you using to find this gene?}
	\end{itemize}

	%The sequence of this gene may be viewed by searching for ``SREBF1'' at NCBI's \emph{nucleotide} database \url{https://www.ncbi.nlm.nih.gov/}. %To download the sequence of this gene and/or the protein it encodes, go to the NCBI homepage and perform search for

	\item Determine your results from the Entrez database from this query.
%	Using Entrez interface do a simple search by typing SREBF1 into the search box and choose Nucleotide as the database to search. Look through your search results.
	\begin{itemize}
		\item \textcolor{red}{ Q2: What general observations can you make regarding the usefulness of your results (i.e., How easy is it to locate the gene of interest?}
		\item \textcolor{red}{ Q3: The data of several different organisms is mixed together in the result of your query. What are four (4) different organisms in which this same gene (\emph{SREBF1}) may be found?}
	\end{itemize}
	\item Now, reduce the number of results by limiting the search to only genes found in the genetics of humans (\emph{homo sapiens}). Make sure your search results eliminate results that are not actually for SREBF1 but for some nearby gene.
	\begin{itemize}
		\item \textcolor{red}{ Q4: What is the exact search query that you used to give you results which concerned only the human versions of the gene?}
	\end{itemize}

	\item Find the gene whose LOCUS number is \emph{NG\_029029}.
	\begin{itemize}
		\item \textcolor{red}{ Q5: What is the full title of this gene?}
	\end{itemize}


%	\item Find an entry that includes ``RefSeqGene'' in its title, it should have accession number NG\_029029.1. Click on this sequence and observe the GenBank record for this gene.

	\item  You are currently looking at the ``Genbank'' format of the gene. Now, click on the ``FASTA'' link on the top of the page. to change the view of the gene's information.

	\begin{itemize}
		\item \textcolor{red}{ Q6: What is the major difference between the ``Genbank'' and ``FASTA'' formats? }
	\end{itemize}

	\item Now, save the gene in a file using the FASTA format by clicking on the  ``Send to'' button. Place this FASTA format file in your lab4 directory. You may have to create that directory if you don't have one in your course repository (cs300f2017-bbill/labs/). Return to GenBank and navigate through the features list. You can click on the links associated with features to alter the sequence display to show only the desired feature. You can also choose Highlight Sequence Features from the \emph{Analyze this Sequence} list of links on the top right side of the page to visualize the locations of the features within the sequence. The list on the right also provides links to other additional information about this gene. Explore the various types of information available on this page.
	\begin{itemize}
		\item \textcolor{red}{ Q7: Through your exploration, what (exactly) are the highlighted regions?}
	\end{itemize}
\end{enumerate}
