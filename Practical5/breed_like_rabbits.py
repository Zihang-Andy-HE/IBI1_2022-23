#start with 2 rabbits
r = 2
# g represent generation
g = 1
#stop breeding until more than 100 rabbits
while (r <= 100):
#g record generation
	g += 1
#r multiply 2 each generation
	r *=2

print('At '+str(g)+' generation over 100 rabbits have been born and the rabbits number is '+str(r))
