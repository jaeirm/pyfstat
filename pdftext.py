# importing required modules 
from PyPDF2 import PdfReader 
import pandas as pd
import re

# creating a pdf reader object 
reader = PdfReader(r"C:\Users\jai\Desktop\text_reg\3.pdf") 

# printing number of pages in pdf file 
#print(len(reader.pages)) 

# getting a specific page from the pdf file 
page = reader.pages[230] 

# extracting text from page 
text = page.extract_text() 
# print(text)

x = text.split()
# print(x)
# print(len(x))
s2 = []


y1 = "2023"
y2 = "2022"
ds  = {
    "part" :[],
    "shed":[],
    y1 : [],
    y2 :[],
}

it = ["capital","reserves & surplus","deposits","borrowings","other liabilities and provisions","total"]
for j in range(5):
    for i in range(len(x)):
        if x[i].lower() == it[j] and x[i+1] == str(j+1):
            ds["part"].append(x[i])
            ds["shed"].append(x[i+1])
            ds[y1].append(x[i+2])
            ds[y2].append(x[i+3])
        if x[i].lower() == "reserves" and x[i+3] == str(j+1):
            ds["part"].append("Reserves and Surplus")
            ds["shed"].append(x[i+3])
            ds[y1].append(x[i+4])
            ds[y2].append(x[i+5])
        if x[i].lower() == "other" and x[i+4] == str(j+1):
            ds["part"].append("Other Liabilities and Provisions")
            ds["shed"].append(x[i+4])
            ds[y1].append(x[i+5])
            ds[y2].append(x[i+6])
        if x[i].lower() == "total" and x[i-3] == str(5):
            ds["part"].append("Total Liabilities")
            ds["shed"].append(x[i+4])
            ds[y1].append(x[i+5])
            ds[y2].append(x[i+6])
            
        


print("dataset",ds)
        