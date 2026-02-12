import re
import os

# יצירת תיקיית תוצאות אם אינה קיימת (למניעת השגיאה הקודמת)
if not os.path.exists("Results"):
    os.makedirs("Results")

file1 = open("Data/orf_coding_all.fa.txt", "r")
file2 = open("Result/yeast_zinc_finger_orf.txt.txt", "w")

gene = ""
count = 0

def check_gene(sequence,protein_name):
    global count, TAA_count, TGA_count, TAG_count
    
    match = re.findall(r"C.H.[LIVMFY]C.{2}C[LIVMYA]", sequence)
    if match:
        count += 1
        file2.write(protein_name + "\n")
        for m in match:
            file2.write(m + "\n")


for line in file1:
    line = line.strip()
    if line.startswith(">"):
        protein_name = line.split()[0]
        # לפני שמתחילים גן חדש, בודקים את הגן הקודם שאספנו
        check_gene(gene,protein_name)
        gene = "" # איפוס לגן הבא
    else:
        gene += line

# חשוב: בדיקת הגן האחרון שנשאר בזיכרון אחרי שהלולאה נגמרה
check_gene(gene,protein_name)
file2.write(f"Number of proteins containing Zinc Finger Motif: {count}\n")