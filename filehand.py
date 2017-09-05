name = raw_input("Enter file:")
if len(name) < 1 : name = "fh2.txt"
book = dict()
lst = list()
count = 0
handle = open(name)
for line in handle:
    if line.startswith('From: '):    # any of the starting line
        line = line.split()
        line1 = str(line[1])
        lst.append(line1)
        
        
                
for adr in lst:
            if adr not in book:
                book[adr] = 1
            else:
                book[adr] = book[adr] + 1

maxval = None
maxkey = None
for key,val in book.items() :

  if val > maxval:
      maxval = val
      maxkey = key   

print maxkey, maxval
