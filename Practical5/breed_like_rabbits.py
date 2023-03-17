#start with 2 rabbits, r represent the number of rabbits
r = 2
# g represent generation
g = 1
#stop breeding until more than 100 rabbits
while (r <= 100):
#g record generation
	g += 1
#r multiply 2 each generation (Because the newborn number is the same as previous number)
	r *=2

print('At '+str(g)+' generation over 100 rabbits have been born and the rabbits number is '+str(r))
