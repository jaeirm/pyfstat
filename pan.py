import pandas as pd
file = r"C:\Users\jai\Desktop\text_reg\x.xlsx"
c1 = pd.read_excel(file,usecols='a')
 
c2 = pd.read_excel(file,usecols='B')
 
print(c1)