# -*-coding:Latin-1 -*

import os 
from map import map_function
from reduce import reduce_function

table = []
k = 0
previous_key = ''
# table after shuffle and sort
table_after_ss = []
final_table = []
# input reader
# read the input file and store each line in a cell of a list
content = [line.rstrip('\r\n') for line in open('input.txt', 'r')]

print '1. INPUT READER', '\n'
print(content)
# call of the map function
mapper = map_function(content)

print('')
print '1. MAPPING', '\n'
print(mapper)
print("")

# shuffle and sort
# we put every element (key, value) of the input side by side in a list
for cell in mapper:
	for inner_cell in cell:
		table.append(inner_cell)

for key, value in table:
	# count of the number of occurencies of this key
	k = table.count((key,value))
	# if there is more than one occurency and the key is different from the previous one
	if k > 1 and key != previous_key:
		# append in a list of the a new tuple with the key and the values affected to this key
		table_after_ss.append((key, k*[value]))
	# else if there is only one occurence and the key is still different
	elif key != previous_key:
		# append in a list of the (key, value)
		table_after_ss.append((key, value))
	# at the end of the loop, set the previous_key to current one for next iteration
	previous_key = key
print '3. SHUFFLE AND SORT', '\n'
print(table_after_ss)

print('')
final_table = reduce_function(dict(table_after_ss))		
print '4. REDUCE', '\n'
print(final_table)

print('')
print '5. OUTPUT WRITER', '\n'
for key, value in final_table.items():
	print key, value