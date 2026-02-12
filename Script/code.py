import re

# פתיחת קבצים (הסרתי את ה- .txt הכפול בסיומת אם לא צריך)
file1 = open("Data/orf_trans_all.fa.txt", "r")
file2 = open("Result/yeast_zinc_finger_orf.txt", "w")

gene = ""
protein_name = ""
count = 0

def check_gene(sequence, name_to_print):
    global count
    if not sequence: return # הגנה מפני ריצה על רצף ריק בהתחלה
    
    # המוטיב שביקשת
    match = re.findall(r"C.H.[LIVMFY]C.{2}C[LIVMYA]", sequence)
    if match:
        count += 1
        file2.write(name_to_print + "\n")
        for m in match:
            file2.write(m + "\n")

for line in file1:
    line = line.rstrip("\n")
    if line.startswith(">"):
        # 1. קודם בודקים את החלבון שסיימנו לאסוף עם השם הישן שלו
        if gene !="": 
            check_gene(gene, protein_name)
        
        # 2. עכשיו מעדכנים לשם של החלבון החדש ומאפסים רצף
        protein_name = line.split()[0]
        gene = "" 
    else:
        gene += line

# 3. בדיקת החלבון האחרון בקובץ
check_gene(gene, protein_name)

file2.write(f"Number of proteins containing Zinc Finger Motif: {count}\n")

file1.close()
file2.close()