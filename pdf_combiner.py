import PyPDF2
import sys
import os

merger = PyPDF2.PdfMerger()

for file in os.listdir(r"C:/Users/Christopher Turner/Documents/combinedpdfs"):
    if file.endswith(".pdf"):
        merger.append(file)
    merger.write("combined.pdf")
