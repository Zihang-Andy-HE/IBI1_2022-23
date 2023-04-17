fa=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
output_file=open('TGA_gene.fa','w')
dict={}
#search each line of fa
for line in fa:
    if line.startswith('>'):
        #if means it's a part of gene name
        # get line as a key,.split split into a list and get the first factor (divided by space)
        mRNA=''.join(line.split(" ")[0])        
#DEBUG for! dict[mRNA]='' should not be put under else, or it start from ''each time
        dict[mRNA]=''
    else:
    #else means it's gene and replace the /n to ''
        dict[mRNA] += line.replace('\n','')
#get the number of codon and store the information from dictionary to string
for genename in dict.keys():
    if dict[genename].endswith('TGA'):
        outcome = ''
        outcome += genename  + "\n" + dict[genename] + "\n"
#write it every time or it will start from '' each time 
# !define under for   outcome = ''
        output_file.write(outcome)
output_file.close()