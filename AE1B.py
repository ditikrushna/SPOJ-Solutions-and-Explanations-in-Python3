inp2 = raw_input()

numBoxes, screwsPerTable, tables = inp1.split()
 
boxes = inp2.split()
 
numBoxes = int(numBoxes)
screwsPerTable = int(screwsPerTable)
tables = int(tables)
boxes = map(int, boxes)
 
boxes.sort()
boxes.reverse()
 
needed = tables * screwsPerTable
 
i = 0
while needed > 0:
    needed -= boxes[i]
    i += 1
 
print i
