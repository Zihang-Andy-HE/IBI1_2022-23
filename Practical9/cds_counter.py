seq = 'ATGCAATCGACTACGATCTGAGAGGGCCTAA'
import re
if re.match('ATG', seq):
    l=len(seq)#length of the sequence
    n=seq.find('ATG')+3
    three=[]
    while n <= l-3:
        n=n+1
        if seq[n:n+3] == 'TAA' or seq[n:n+3] == 'TAG' or seq[n:n+3] == 'TGA':
            three.append(seq[n:n+3])
    counts = len(three)
    print('The sequence contains '+str(counts)+' possible coding sequences')
else:
    print('The sequence contains 0 possible coding sequences')
