#read the sequences
fcat = open('ACE2_cat.fa','r')
fcat.readline()
seq_cat = fcat.readline()
frat = open('ACE2_mouse.fa','r')
frat.readline()
seq_rat = frat.readline()
fhomo = open('ACE2_human.fa','r')
fhomo.readline()
seq_homo = fhomo.readline()

# all the length of sequences are the same
#homo-rat
edit_distancehr=0
for i in range(len(seq_homo)):
    if seq_homo[i]!=seq_rat[i]:
        edit_distancehr += 1
percent=((len(seq_cat)-edit_distancehr)/len(seq_cat))
print('human-mouse' ,edit_distancehr,percent)

#homo-cat
edit_distancehc=0
for i in range(len(seq_homo)):
    if seq_homo[i]!=seq_cat[i]:
        edit_distancehc += 1
percent=((len(seq_cat)-edit_distancehc)/len(seq_cat))
print('human-cat',edit_distancehc,percent)

#cat-rat
edit_distancecr=0
for i in range(len(seq_cat)):
    if seq_cat[i]!=seq_rat[i]:
        edit_distancecr += 1
percent=((len(seq_cat)-edit_distancecr)/len(seq_cat))
print('cat-mouse',edit_distancecr,percent)
