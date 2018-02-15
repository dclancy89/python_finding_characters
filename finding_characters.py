word_list = ['hello','world','my','name','is','Anna']
char = "o"

new_list = []

for x in word_list:
	if char in x:
		new_list.append(x)

# I only needed one loop for this. Thanks python!

print new_list