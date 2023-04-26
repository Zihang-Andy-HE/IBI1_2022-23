#practical11
#read the sequences
fcat = open('ACE2_cat.fa','r')
fcat.readline()
seq_cat = fcat.readline().strip() #!!remove  '/'
fcat.close
frat = open('ACE2_mouse.fa','r')
frat.readline()
seq_rat = frat.readline().strip()
frat.close
fhomo = open('ACE2_human.fa','r')
fhomo.readline()
seq_homo = fhomo.readline().strip()
fhomo.close

#close the file is a good habit 
#use with open() as can close it automatic

import blosum as bl
blosum62=bl.BLOSUM(62)


# all the length of sequences are the same
#homo-rat
edit_distancehr=0
score=0
for i in range(len(seq_homo)):
    if seq_homo[i]!=seq_rat[i]:
        edit_distancehr += 1
    h=seq_homo[i]
    r=seq_rat[i]    
    score += blosum62[h][r]
percent=((len(seq_cat)-edit_distancehr)/len(seq_cat))
print('human-mouse' ,score,percent)

#homo-cat
edit_distancehc=0
score=0
for i in range(len(seq_homo)):
    if seq_homo[i]!=seq_cat[i]:
        edit_distancehc += 1
    h=seq_homo[i]
    c=seq_cat[i]    
    score += blosum62[h][c]
percent=((len(seq_cat)-edit_distancehc)/len(seq_cat))
print('human-cat',score,percent)

#cat-rat
edit_distancecr=0
score=0
for i in range(len(seq_cat)):
    if seq_cat[i]!=seq_rat[i]:
        edit_distancecr += 1
    r=seq_rat[i]
    c=seq_cat[i]    
    score += blosum62[r][c]
percent=((len(seq_cat)-edit_distancecr)/len(seq_cat))
print('cat-mouse',score,percent)

#findings and intepretations are in another file Findings.txt
